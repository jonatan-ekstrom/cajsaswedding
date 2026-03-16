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
- **Status:** Waiting for Cloudflare to show "Active" (propagation in progress)

### Step 4: Verify domain in GitHub (account-level)

- Go to GitHub → **Settings** (account, not repo) → **Pages** → **"Add a domain"**
- Enter your domain — GitHub gives you a TXT record value
- Add the TXT record **in Cloudflare** (not Loopia):

| Type | Name | Content |
|------|------|---------|
| TXT | `_github-pages-challenge-jonatan-ekstrom` | *(value from GitHub)* |

- Wait for DNS propagation (usually a few minutes via Cloudflare), then click **Verify** in GitHub

### Step 5: Add custom domain in GitHub repo settings

Do this **before** configuring A/CNAME records to prevent domain takeover.

- Repo → **Settings → Pages → Custom domain** → enter domain → **Save**
- This auto-creates a `CNAME` file in the repo — pull it locally: `git pull origin master`

### Step 6: Configure DNS records in Cloudflare

Go to Cloudflare → your domain → **DNS → Records**. Add the following records.

> **Important:** Set all records to **"DNS only"** (gray cloud icon, proxy OFF). GitHub Pages needs direct DNS to issue its Let's Encrypt SSL certificate.

**A records** (apex `@`):

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | `@` | `185.199.108.153` | DNS only |
| A | `@` | `185.199.109.153` | DNS only |
| A | `@` | `185.199.110.153` | DNS only |
| A | `@` | `185.199.111.153` | DNS only |

**CNAME record** (www subdomain):

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| CNAME | `www` | `jonatan-ekstrom.github.io` | DNS only |

### Step 7: Wait for SSL and enable HTTPS

- GitHub Pages will automatically provision a Let's Encrypt certificate once DNS resolves
- Check status at: Repo → **Settings → Pages** — wait for green checkmark (can take 5 min – 1h)
- Once green, tick **"Enforce HTTPS"**

### Step 8: Cloudflare SSL settings

- Go to Cloudflare → your domain → **SSL/TLS**
- Set encryption mode to **"Full"** (not "Full (Strict)" and not "Flexible")
- This ensures Cloudflare connects to GitHub's cert properly if you ever enable the proxy later

## Verification Checklist

**After Phase 1:** ✅ (2026-03-15)
- [x] Site loads at `https://jonatan-ekstrom.github.io/cajsaswedding/`
- [x] All images/fonts/CSS load (check browser devtools Network tab)
- [x] Countdown timer works
- [x] Swish deep links work on mobile
- [x] Navigation and smooth scroll work
- [x] Site is responsive on mobile

**After Phase 2:**
- [ ] Cloudflare dashboard shows domain as "Active" (nameservers propagated)
- [ ] GitHub domain verification shows green checkmark (TXT record works)
- [ ] `CNAME` file exists in repo (auto-created by GitHub, pulled locally)
- [ ] `dig bringe2026.se` returns GitHub's A record IPs (`185.199.10x.153`)
- [ ] `dig www.bringe2026.se` returns `jonatan-ekstrom.github.io`
- [ ] `https://bringe2026.se` loads with valid SSL (Let's Encrypt cert)
- [ ] `https://www.bringe2026.se` redirects correctly
- [ ] Old GitHub Pages URL redirects to custom domain
- [ ] Cloudflare SSL mode set to "Full"
- [ ] All Cloudflare DNS records set to "DNS only" (gray cloud)
