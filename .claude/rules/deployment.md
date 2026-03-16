# Deployment Guide

## Hosting

- **Platform:** GitHub Pages (project site)
- **Repo:** `jonatan-ekstrom/cajsaswedding` (public)
- **Branch:** `master` (deploy from root)
- **Review URL:** https://jonatan-ekstrom.github.io/cajsaswedding/
- **Custom domain:** `bringe2026.se` (domain via Loopia, DNS via Cloudflare)

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

### Step 1: Register domain at Loopia ✅ DONE (2026-03-16)

- ~~Register `bringe2026.se` at Loopia (9 SEK, domain only, no DNS add-on)~~
- Domain expires 2027-03-16

### Step 2: Create Cloudflare account and add the domain ✅ DONE (2026-03-16)

- ~~Sign up at cloudflare.com (free tier)~~
- ~~Add site `bringe2026.se` → Free plan~~
- Assigned nameservers: `decker.ns.cloudflare.com`, `stella.ns.cloudflare.com`

### Step 3: Point Loopia nameservers to Cloudflare ✅ DONE (2026-03-16)

- ~~Replace Loopia defaults (`ns1.loopia.se`, `ns2.loopia.se`) with Cloudflare nameservers~~
- ~~Used "Tvinga ändring" (force change) to push through~~
### Step 4: Verify domain in GitHub (account-level) ✅ DONE (2026-03-16)

- ~~GitHub → Settings (account) → Pages → "Add a domain" → entered `bringe2026.se`~~
- ~~Added TXT record in Cloudflare for `_github-pages-challenge-jonatan-ekstrom`~~
- ~~Verified successfully~~

### Step 5: Add custom domain in GitHub repo settings ✅ DONE (2026-03-16)

- ~~Repo → Settings → Pages → Custom domain → `bringe2026.se` → Save~~
- ~~CNAME file auto-created and pulled locally~~

### Step 6: Configure DNS records in Cloudflare ✅ DONE (2026-03-16)

All records set to **DNS only** (gray cloud, proxy OFF):

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | `@` | `185.199.108.153` | DNS only |
| A | `@` | `185.199.109.153` | DNS only |
| A | `@` | `185.199.110.153` | DNS only |
| A | `@` | `185.199.111.153` | DNS only |
| CNAME | `www` | `jonatan-ekstrom.github.io` | DNS only |

### Step 7: Wait for SSL and enable HTTPS ✅ DONE (2026-03-16)

- ~~Let's Encrypt certificate provisioned (3/3 steps)~~
- ~~"Enforce HTTPS" enabled~~

### Step 8: Cloudflare SSL settings ✅ DONE (2026-03-16)

- ~~SSL/TLS encryption mode set to "Full"~~

## Verification Checklist

**After Phase 1:** ✅ (2026-03-15)
- [x] Site loads at `https://jonatan-ekstrom.github.io/cajsaswedding/`
- [x] All images/fonts/CSS load (check browser devtools Network tab)
- [x] Countdown timer works
- [x] Swish deep links work on mobile
- [x] Navigation and smooth scroll work
- [x] Site is responsive on mobile

**After Phase 2:** ✅ (2026-03-16)
- [x] Cloudflare dashboard shows domain as "Active" (nameservers propagated)
- [x] GitHub domain verification shows green checkmark (TXT record works)
- [x] `CNAME` file exists in repo (auto-created by GitHub, pulled locally)
- [x] `dig bringe2026.se` returns GitHub's A record IPs (`185.199.10x.153`)
- [x] `dig www.bringe2026.se` returns `jonatan-ekstrom.github.io`
- [x] `https://bringe2026.se` loads with valid SSL (Let's Encrypt cert)
- [x] `https://www.bringe2026.se` redirects correctly
- [x] Old GitHub Pages URL redirects to custom domain
- [x] Cloudflare SSL mode set to "Full"
- [x] All Cloudflare DNS records set to "DNS only" (gray cloud)
