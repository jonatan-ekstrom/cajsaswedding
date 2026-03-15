# Deployment Guide

## Hosting

- **Platform:** GitHub Pages (project site)
- **Repo:** `jonatan-ekstrom/cajsaswedding` (public)
- **Branch:** `master` (deploy from root)
- **Review URL:** https://jonatan-ekstrom.github.io/cajsaswedding/
- **Custom domain:** TBD (will be configured via Loopia after review)

## Phase 1: GitHub Pages Setup ✅ DONE (2026-03-15)

1. ~~Create repo on GitHub: `jonatan-ekstrom/cajsaswedding` (public)~~
2. ~~Add remote: `git remote set-url origin git@github.com:jonatan-ekstrom/cajsaswedding.git` (SSH)~~
3. ~~Push: `git push -u origin master`~~
4. ~~Enable Pages: Settings → Pages → Source: Deploy from branch → `master` / root → Save~~
5. ~~Verify at: `https://jonatan-ekstrom.github.io/cajsaswedding/`~~

**Push updates:**
```bash
git add -A && git commit -m "Update site" && git push origin master
```

> **Path note:** All asset refs are relative (e.g. `assets/images/...`, `css/style.css`) so they resolve correctly under the `/cajsaswedding/` prefix.

## Phase 2: Custom Domain (after review)

### 1. Register domain
- Register `.se` domain at [Loopia](https://loopia.se) (~150–200 SEK/year)

### 2. Verify domain in GitHub (account-level, not repo-level)
- Go to GitHub → **Settings → Pages → "Add a domain"**
- GitHub provides a TXT record value
- Add TXT record in Loopia DNS editor: `_github-pages-challenge-jonatan-ekstrom.yourdomain.se`
- Wait for DNS propagation, then click **Verify** in GitHub

### 3. Add domain in GitHub repo settings
Do this **before** configuring DNS to prevent domain takeover.
- Repo → Settings → Pages → Custom domain → enter domain → Save
- This auto-creates a `CNAME` file in the repo — pull it locally after: `git pull origin master`

### 4. Configure DNS in Loopia

**A records** (apex `@`):

| Type | Host | Value |
|------|------|-------|
| A | @ | `185.199.108.153` |
| A | @ | `185.199.109.153` |
| A | @ | `185.199.110.153` |
| A | @ | `185.199.111.153` |

**AAAA records** (IPv6, recommended — see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)):

Add the four IPv6 addresses listed in the GitHub documentation.

**CNAME record** (www subdomain):

| Type | Host | Value |
|------|------|-------|
| CNAME | www | `jonatan-ekstrom.github.io` |

### 5. Enable HTTPS
- Wait for DNS propagation (5 min – 24h)
- Once green checkmark appears in Pages settings, enable **"Enforce HTTPS"**

## Verification Checklist

**After Phase 1:** ✅ (2026-03-15)
- [x] Site loads at `https://jonatan-ekstrom.github.io/cajsaswedding/`
- [x] All images/fonts/CSS load (check browser devtools Network tab)
- [x] Countdown timer works
- [x] Swish deep links work on mobile
- [x] Navigation and smooth scroll work
- [x] Site is responsive on mobile

**After Phase 2:**
- [ ] `dig yourdomain.se` returns GitHub's A record IPs
- [ ] `https://yourdomain.se` loads with valid SSL
- [ ] `https://www.yourdomain.se` redirects correctly
- [ ] Old GitHub Pages URL redirects to custom domain
