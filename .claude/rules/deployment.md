# Deployment Guide

## Hosting

- **Platform:** GitHub Pages (project site)
- **Repo:** `jonatan-ekstrom/cajsaswedding` (public)
- **Branch:** `master` (deploy from root)
- **Review URL:** https://jonatan-ekstrom.github.io/cajsaswedding/
- **Custom domain:** `bringe2026.se` (domain via Loopia, DNS via Cloudflare)
- **Domain expiry:** 2027-03-16 (Loopia)
- **Cloudflare nameservers:** `decker.ns.cloudflare.com`, `stella.ns.cloudflare.com`

### DNS Records (Cloudflare — all DNS only, proxy OFF)

| Type | Name | Content |
|------|------|---------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `jonatan-ekstrom.github.io` |

## Deploying Updates

```bash
git add -A && git commit -m "Update site" && git push origin master
```

> **Path note:** All asset refs are relative (e.g. `assets/images/...`, `css/style.css`) so they resolve correctly under the `/cajsaswedding/` prefix.
