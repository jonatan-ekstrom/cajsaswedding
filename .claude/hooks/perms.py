#!/usr/bin/env python
"""PreToolUse permission hook for Bash commands.

Adapted from the PM repository's permission system for the wedding website project.

Classification tiers (checked in order):
  1. Convention violations   -> DENY
  2. Dangerous commands      -> DENY   (global scan + per-stage)
  3. Git subcommands         -> DENY/ASK/ALLOW  (comprehensive)
  4. Safe-dir file ops       -> ALLOW  (cp/mv/mkdir/touch/tee/rm/rmdir in safe dirs)
  5. Non-safe-dir file ops   -> ALLOW if acceptEdits, ASK otherwise
  6. Global redirect check   -> ASK    (redirects outside safe dirs)
  7. Known safe commands      -> ALLOW  (_BASH_ALLOW set)
  8. Default                 -> ASK    (unrecognized command)

Reads tool-use JSON from stdin, writes permission JSON to stdout.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import sys


# ── Output helpers ──────────────────────────────────────────────────────────


def _out(obj: dict) -> None:
    json.dump(obj, sys.stdout)
    sys.stdout.flush()
    sys.exit(0)


def deny(reason: str) -> None:
    _out({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }})


def allow() -> None:
    _out({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
    }})


def ask(context: str) -> None:
    _out({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": context,
    }})


# ── Constants ───────────────────────────────────────────────────────────────


# Directories where file operations are always auto-allowed (gitignored scratch space)
SAFE_DIRS = ("scratchpad/",)


# ── Compiled patterns ──────────────────────────────────────────────────────


# Convention violations (anchored to stage start)
_CONVENTION_DENY: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^cd(\s|$)"),   "Never cd — run from project root"),
    (re.compile(r"^pushd\b"),    "Never pushd — run from project root"),
    (re.compile(r"^popd\b"),     "Never popd — run from project root"),
    (re.compile(r"^git\s+-C\b"), "Never git -C — breaks permission patterns"),
]


# Dangerous commands (anchored to stage start)
_STAGE_DENY: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^sudo\b"),                            "sudo is blocked"),
    (re.compile(r"^shutdown\b"),                        "shutdown is blocked"),
    (re.compile(r"^chmod\b"),                           "chmod is blocked"),
    (re.compile(r"^chown\b"),                           "chown is blocked"),
    (re.compile(r"^dd\b"),                              "dd is blocked"),
    (re.compile(r"^curl\b"),                            "curl is blocked — use the WebFetch tool for HTTP requests"),
    (re.compile(r"^wget\b"),                            "wget is blocked — use the WebFetch tool for HTTP requests"),
    (re.compile(r"^ssh(?!-)"),                          "ssh is blocked (network)"),
    (re.compile(r"^rm\s+-\w*f"),                        "Use 'rm' or 'rm -r' instead of 'rm -f' (force flag blocked)"),
    (re.compile(r"^rm\s+--force\b"),                    "Use 'rm' or 'rm -r' instead of 'rm -f' (force flag blocked)"),
    (re.compile(r"^git\s+push\b.*--force(?![a-z-])"),   "git push --force is blocked"),
    (re.compile(r"^git\s+push\b.*\s-[a-z]*f"),          "git push -f is blocked"),
    (re.compile(r"^git\s+reset\s+--hard\b"),            "git reset --hard is blocked"),
    (re.compile(r"^git\s+clean\b"),                     "git clean is blocked"),
    (re.compile(r"^git\s+filter-branch\b"),             "git filter-branch is blocked"),
    (re.compile(r"^eval\b"),                            "eval is blocked"),
    (re.compile(r"^exec\b"),                            "exec is blocked"),
    # Process / system-level — dangerous or irreversible
    (re.compile(r"^kill\b"),                            "kill is blocked"),
    (re.compile(r"^gkill\b"),                           "gkill is blocked"),
    (re.compile(r"^chroot\b"),                          "chroot is blocked"),
    (re.compile(r"^shred\b"),                           "shred is blocked"),
    (re.compile(r"^mknod\b"),                           "mknod is blocked"),
    (re.compile(r"^mount\b"),                           "mount is blocked"),
    (re.compile(r"^umount\b"),                          "umount is blocked"),
    (re.compile(r"^passwd\b"),                          "passwd is blocked"),
    (re.compile(r"^reboot\b"),                          "reboot is blocked"),
    (re.compile(r"^su\b"),                              "su is blocked"),
    (re.compile(r"^mkgroup\b"),                         "mkgroup is blocked"),
    (re.compile(r"^rebase\b"),                          "rebase (MSYS2 DLL rebase) is blocked"),
    (re.compile(r"^regtool\b"),                         "regtool (registry) is blocked"),
]


# Git subcommands that always need user approval (any form mutates state).
# Dual-mode commands (branch, config, remote, etc.) are handled separately.
_GIT_ASK: set[str] = {
    # History modification
    "am", "apply", "bisect", "cherry-pick", "citool", "commit",
    "merge", "mergetool", "rebase", "reset", "revert",
    # Remote interaction
    "clone", "pull", "push",
    # Working-tree / index modification
    "checkout", "mv", "restore", "rm", "sparse-checkout", "switch",
    # Repository setup / maintenance
    "gc", "init", "maintenance", "pack-refs", "prune",
    "repack", "replace", "submodule",
    # Bundle / archive operations that modify state
    "bundle",
    # Email (sends messages — side effect)
    "imap-send", "send-email",
    # External system bridges
    "fast-import", "p4", "svn",
    # Scalar (repo management)
    "scalar",
}


# Known safe commands — auto-allowed (read-only, info, text processing, builds)
_BASH_ALLOW: set[str] = {
    # File reading / text processing
    "awk", "base32", "base64", "basename", "cat", "column", "comm",
    "csplit", "cut", "diff", "dirname", "echo", "expand", "expr",
    "factor", "fmt", "fold", "grep", "head", "hexdump", "iconv",
    "join", "less", "look", "more", "nl", "numfmt", "od", "paste",
    "pr", "printf", "rev", "sed", "seq", "shuf", "sort", "strings",
    "tail", "tr", "tsort", "unexpand", "uniq", "wc", "xxd",
    # File system inspection (read-only)
    "df", "dir", "du", "file", "find", "ls", "lsof",
    "md5sum", "readlink", "realpath", "sha1sum", "sha256sum",
    "sha512sum", "stat", "test", "tree", "vdir",
    # Search tools
    "ag", "fd", "fzf", "jq", "rg", "yq",
    # System / process info
    "date", "env", "free", "getconf", "hostname", "id",
    "locale", "nproc", "printenv", "ps", "pwd", "top",
    "tty", "uname", "uptime", "which", "who", "whoami",
    # Shell builtins / harmless
    "alias", "builtin", "command", "compgen", "complete",
    # Shell control-flow terminators (standalone after ; splitting)
    "fi", "done", "esac",
    # Test / comparison builtins
    "[", "[[",
    "declare", "dirs", "export", "false", "hash", "help",
    "let", "local", "mapfile", "read", "readarray",
    "set", "shift", "shopt", "source", "trap", "true",
    "type", "typeset", "ulimit", "umask", "unset",
    # Build / dev tools
    "node", "npm", "npx", "python",
    # Document conversion
    "markitdown", "pandoc",
    # Clipboard
    "clip", "clip.exe",
}


# ── Helpers ─────────────────────────────────────────────────────────────────


def _first_word(cmd: str) -> str:
    """First word after stripping leading VAR=val assignments."""
    stripped = re.sub(r"^(\w+=\S*\s+)*", "", cmd)
    parts = stripped.split()
    return parts[0] if parts else ""


_MSYS_DRIVE_RE = re.compile(r"^/([a-zA-Z])/")


def _is_safe_dir(path: str) -> bool:
    """Check whether *path* falls inside a safe directory.

    Handles both relative paths (``css/foo``) and absolute paths
    (``/c/dev/wedding/css/foo`` or ``C:\\dev\\wedding\\css\\foo``) by
    resolving absolute paths relative to the repo root (CWD).
    MSYS-style paths (``/c/...``) are converted to Windows form first.
    """
    path = path.strip("'\"").replace("\\", "/")
    # Convert MSYS /c/... → C:/...
    m = _MSYS_DRIVE_RE.match(path)
    if m:
        path = m.group(1).upper() + ":/" + path[3:]
    # Resolve absolute paths to repo-relative
    if len(path) >= 3 and path[1] == ":":
        try:
            rel = os.path.relpath(path, os.getcwd()).replace("\\", "/")
            if not rel.startswith(".."):
                path = rel
        except ValueError:
            pass  # different drive on Windows — not safe
    elif path.startswith("/"):
        # Unix absolute path (not MSYS) — can't resolve on Windows
        pass
    path = path.lstrip("./")
    return any(path == d.rstrip("/") or path.startswith(d) for d in SAFE_DIRS)


def _redirect_targets(cmd: str) -> list[str]:
    """Extract output-redirect targets (> file, >> file), skip fd redirects."""
    return re.findall(r"(?<![&\d])>{1,2}\s*([^\s;&|]+)", cmd)


def _quote_aware_split(cmd: str, separators: list[str]) -> list[str]:
    """Split *cmd* on *separators* while respecting single/double quotes."""
    seps = sorted(separators, key=len, reverse=True)
    parts: list[str] = []
    buf: list[str] = []
    i = 0
    n = len(cmd)
    in_sq = False
    in_dq = False

    while i < n:
        c = cmd[i]

        if c == "\\" and in_dq and i + 1 < n:
            buf.append(c)
            buf.append(cmd[i + 1])
            i += 2
            continue

        if c == "'" and not in_dq:
            in_sq = not in_sq
            buf.append(c)
            i += 1
            continue
        if c == '"' and not in_sq:
            in_dq = not in_dq
            buf.append(c)
            i += 1
            continue

        if not in_sq and not in_dq:
            matched = False
            for sep in seps:
                if cmd[i : i + len(sep)] == sep:
                    parts.append("".join(buf).strip())
                    buf = []
                    i += len(sep)
                    matched = True
                    break
            if matched:
                continue

        buf.append(c)
        i += 1

    tail = "".join(buf).strip()
    if tail:
        parts.append(tail)
    return [p for p in parts if p]


def _split_compound(cmd: str) -> list[str]:
    """Split on ``&&``, ``||``, ``;`` respecting quotes."""
    return _quote_aware_split(cmd, ["&&", "||", ";"])


def _split_pipeline(cmd: str) -> list[str]:
    """Split on ``|`` (but not ``||``) respecting quotes."""
    return _quote_aware_split(cmd, ["|"])


# ── Write-target analysis ──────────────────────────────────────────────────


def _analyze_write(cmd: str, word: str) -> tuple[str, str]:
    """Classify file-write commands by their destination paths."""
    try:
        parts = shlex.split(cmd)
    except ValueError:
        parts = cmd.split()

    if word in ("cp", "mv"):
        if len(parts) >= 3:
            dest = parts[-1]
            if _is_safe_dir(dest):
                return "allow", ""
            return "ask", f"{word} targets '{dest}' (outside safe dirs)"
        return "ask", f"{word}: cannot determine target"

    if word == "mkdir":
        targets = [p for p in parts[1:] if not p.startswith("-")]
        if targets and all(_is_safe_dir(t) for t in targets):
            return "allow", ""
        return "ask", "mkdir outside safe dirs"

    if word in ("touch", "tee"):
        targets = [p for p in parts[1:] if not p.startswith("-")]
        if targets and all(_is_safe_dir(t) for t in targets):
            return "allow", ""
        return "ask", f"{word} outside safe dirs"

    if word == "rm":
        targets = [p for p in parts[1:] if not p.startswith("-")]
        if targets and all(_is_safe_dir(t) for t in targets):
            return "allow", ""
        return "ask", "rm outside safe dirs"

    if word == "rmdir":
        targets = [p for p in parts[1:] if not p.startswith("-")]
        if targets and all(_is_safe_dir(t) for t in targets):
            return "allow", ""
        return "ask", "rmdir outside safe dirs"

    return "ask", f"{word} requires approval"


# ── Dual-mode git classifiers ─────────────────────────────────────────────


def _classify_git_branch(parts: list[str]) -> tuple[str, str]:
    args = parts[2:]
    _MUT = {
        "-d", "-D", "-m", "-M", "-c", "-C", "-f", "--force",
        "--delete", "--move", "--copy", "--unset-upstream",
        "--edit-description",
    }
    if any(a in _MUT or a.startswith("--set-upstream-to") for a in args):
        return "ask", "git branch mutation requires approval"
    if not args:
        return "allow", ""
    _LIST = {
        "-l", "--list", "-a", "--all", "-r", "--remotes",
        "-v", "-vv", "--merged", "--no-merged",
        "--contains", "--no-contains", "--points-at",
    }
    if any(a in _LIST or a.startswith(("--sort", "--format")) for a in args):
        return "allow", ""
    if any(not a.startswith("-") for a in args):
        return "ask", "git branch creation requires approval"
    return "allow", ""


def _classify_git_config(parts: list[str]) -> tuple[str, str]:
    args = parts[2:]
    _WRITE = {
        "--global", "--system", "--unset", "--unset-all",
        "--remove-section", "--rename-section", "--replace-all", "--add",
    }
    if any(a in _WRITE for a in args):
        return "ask", "git config modification requires approval"
    non_flag = [a for a in args if not a.startswith("-")]
    if len(non_flag) >= 2:
        return "ask", "git config set requires approval"
    return "allow", ""


def _classify_git_notes(parts: list[str]) -> tuple[str, str]:
    action = parts[2] if len(parts) > 2 else "list"
    if action in ("add", "append", "edit", "copy", "remove", "merge", "prune"):
        return "ask", f"git notes {action} requires approval"
    return "allow", ""


def _classify_git_reflog(parts: list[str]) -> tuple[str, str]:
    action = parts[2] if len(parts) > 2 else "show"
    if action in ("expire", "delete"):
        return "ask", f"git reflog {action} requires approval"
    return "allow", ""


def _classify_git_remote(parts: list[str]) -> tuple[str, str]:
    action = parts[2] if len(parts) > 2 else ""
    if action in ("add", "remove", "rm", "rename", "set-url", "prune",
                   "set-head", "set-branches"):
        return "ask", f"git remote {action} requires approval"
    return "allow", ""


def _classify_git_stash(parts: list[str]) -> tuple[str, str]:
    action = parts[2] if len(parts) > 2 else "push"
    if action in ("list", "show"):
        return "allow", ""
    return "ask", f"git stash {action} requires approval"


def _classify_git_tag(parts: list[str]) -> tuple[str, str]:
    args = parts[2:]
    if any(a in ("-d", "--delete") for a in args):
        return "ask", "git tag deletion requires approval"
    if any(a in ("-l", "--list") for a in args):
        return "allow", ""
    if not args:
        return "allow", ""
    if all(a.startswith("-") for a in args):
        return "allow", ""
    return "ask", "git tag creation requires approval"


def _classify_git_worktree(parts: list[str]) -> tuple[str, str]:
    action = parts[2] if len(parts) > 2 else ""
    if action in ("add", "remove", "move", "prune", "repair", "lock", "unlock"):
        return "ask", f"git worktree {action} requires approval"
    return "allow", ""


# ── Per-stage classifier ───────────────────────────────────────────────────


_SHELL_PREFIX_KW = re.compile(
    r"^(?:then|else|elif|do|if|while|until|for|case)\s+"
)


def _unwrap_shell_syntax(stage: str) -> str:
    """Strip shell grouping chars and control-flow keywords from a stage."""
    s = stage.lstrip("({").strip()
    s = s.rstrip(")}").strip()
    m = _SHELL_PREFIX_KW.match(s)
    if m:
        s = s[m.end():]
    return s


def _classify_stage(stage: str, permission_mode: str = "default") -> tuple[str, str]:
    """Classify a single pipeline stage. Returns ``(decision, reason)``."""
    stage = stage.strip()
    if not stage:
        return "allow", ""

    stage = _unwrap_shell_syntax(stage)
    if not stage:
        return "allow", ""

    word = _first_word(stage)

    # Tier 1 — Convention violations
    for pat, reason in _CONVENTION_DENY:
        if pat.search(stage):
            return "deny", reason

    # Tier 2 — Dangerous commands
    for pat, reason in _STAGE_DENY:
        if pat.search(stage):
            return "deny", reason

    # Tier 3 — Git subcommands
    if word == "git":
        parts = stage.split()
        sub = parts[1] if len(parts) > 1 else ""

        if not sub:
            return "allow", ""

        if sub in _GIT_ASK:
            return "ask", f"git {sub} requires approval"

        if sub == "branch":
            return _classify_git_branch(parts)
        if sub == "config":
            return _classify_git_config(parts)
        if sub == "notes":
            return _classify_git_notes(parts)
        if sub == "reflog":
            return _classify_git_reflog(parts)
        if sub == "remote":
            return _classify_git_remote(parts)
        if sub == "stash":
            return _classify_git_stash(parts)
        if sub == "tag":
            return _classify_git_tag(parts)
        if sub == "worktree":
            return _classify_git_worktree(parts)

        return "allow", ""

    # Tier 4 — File-write commands (cp, mv, mkdir, touch, tee, rm, rmdir)
    if word in {"cp", "mv", "mkdir", "touch", "tee", "rm", "rmdir"}:
        decision, reason = _analyze_write(stage, word)
        if decision == "allow":
            return "allow", ""
        if permission_mode == "acceptEdits":
            return "allow", ""
        return "ask", reason

    # Tier 5 — Global redirect check
    redir = _redirect_targets(stage)
    if redir and not all(_is_safe_dir(r) for r in redir):
        return "ask", f"Redirect outside safe dirs: {redir}"

    # Tier 6 — Known safe commands
    if word in _BASH_ALLOW:
        return "allow", ""

    # Tier 7 — Default: ask
    return "ask", f"Unrecognized command: {word}"


# ── Top-level classifier ───────────────────────────────────────────────────


_PRIORITY = {"deny": 0, "ask": 1, "allow": 2}


def _most_restrictive(decisions: list[tuple[str, str]]) -> tuple[str, str]:
    return min(decisions, key=lambda d: _PRIORITY.get(d[0], 1))


def classify(command: str, permission_mode: str = "default") -> tuple[str, str]:
    """Classify a full Bash command string."""
    if re.search(r"curl\b.*\|\s*(?:ba)?sh\b", command):
        return "deny", "Piped remote execution is blocked"
    if re.search(r"wget\b.*\|\s*(?:ba)?sh\b", command):
        return "deny", "Piped remote execution is blocked"

    sub_cmds = _split_compound(command)
    if not sub_cmds:
        return "allow", ""

    results: list[tuple[str, str]] = []
    for sub in sub_cmds:
        stages = _split_pipeline(sub)
        stage_results = [_classify_stage(s, permission_mode) for s in stages]
        results.append(_most_restrictive(stage_results))

    return _most_restrictive(results)


# ── Entry point ─────────────────────────────────────────────────────────────


def main() -> None:
    if sys.platform == "win32":
        import io
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        print("perms.py: invalid or missing JSON on stdin", file=sys.stderr)
        sys.exit(2)

    if data.get("tool_name") != "Bash":
        print("perms.py: tool_name is not 'Bash'", file=sys.stderr)
        sys.exit(2)

    command = data.get("tool_input", {}).get("command", "")
    if not command:
        print("perms.py: empty or missing command", file=sys.stderr)
        sys.exit(2)

    permission_mode = data.get("permission_mode", "default")
    decision, reason = classify(command, permission_mode)

    if decision == "deny":
        deny(reason)
    elif decision == "allow":
        allow()
    else:
        ask(reason)


if __name__ == "__main__":
    main()
