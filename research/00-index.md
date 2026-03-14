# Wedding Website Research Index

> This folder contains design research for Cajsa & Filip's wedding website. These files are optimized for use by a building agent to construct the site.

## Files

| File | Contents |
|------|----------|
| `00-index.md` | This file — summary, reconciled decisions, implementation checklist |
| `01-scandinavian-trends.md` | Nordic wedding website design patterns, section-by-section layout guidance, Swedish-specific elements |
| `02-tech-stack.md` | CSS architecture, animation library, fonts, asset sourcing, countdown timer, navigation, images, maps |
| `03-botanical-web-design.md` | Color palette, botanical CSS techniques, section dividers, hero design, accessibility, responsive botanicals |
| `04-copilot-image-prompts.md` | Copilot Creator prompts for generating botanical assets |
| `05-swish-qr-integration.md` | Swish QR code API research, deep-link format, implementation plan for gift section |

---

## Reconciled Design Decisions

The three research tracks produced slightly different recommendations in some areas. Here are the final reconciled decisions:

### Typography — Final Choice

| Role | Font | Source |
|------|------|--------|
| **Couple's names (script)** | Alex Brush | Google Fonts |
| **Section headings** | Cormorant Garamond (300, 400, 500, 600 + italics) | Google Fonts |
| **Small caps / decorative labels** | Cormorant SC (300, 400, 500) | Google Fonts |
| **Body text / UI** | Montserrat (300, 400, 500) | Google Fonts |

**Rationale:** Alex Brush is the closest free match to the invitation script. Cormorant Garamond is distinctly European and refined. Montserrat provides clean mobile readability. This pairing was recommended by the tech stack research and confirmed as appropriate by the trends research.

### Color Palette — Final Values

Use the comprehensive palette from `03-botanical-web-design.md` as the canonical reference. Key values:

| Token | Hex | Usage |
|-------|-----|-------|
| `--cream` | `#FAF8F5` | Primary background |
| `--sage` | `#8FA07C` | Primary accent |
| `--sage-darkest` | `#5C6B4F` | Text-safe green (WCAG AA) |
| `--blue` | `#6B8BA4` | Secondary accent |
| `--blue-dark` | `#4A6178` | Text-safe blue (WCAG AA) |
| `--text-primary` | `#2C2C2C` | Body text |
| `--gold` | `#B8A06A` | Warm accent (dividers, subtle highlights) |

### Animation Approach — AOS

Use AOS 2.3.4 via CDN. Subtle `fade-up` as default, `once: true`. Hero section gets CSS keyframe entrance animations (staggered fade-up). All animations wrapped in `prefers-reduced-motion` guard.

### CSS — Custom (no framework)

Write custom CSS from scratch. Use CSS custom properties for all design tokens. Mobile-first with breakpoints at 480px, 768px, 1024px.

### Botanicals — PNG/WebP assets

Source watercolor PNG assets from Freepik/Pixabay/rawpixel. Optimize to WebP. Use CSS `position: absolute` for corner placement. Scale down + reduce opacity on mobile (never hide). Use CSS gradient placeholders until real assets are sourced.

### Maps — Hybrid

Google Maps links (best mobile UX) + optional lazy-loaded OpenStreetMap embed behind a button click.

### FAQ — Native HTML

Use `<details>`/`<summary>` for zero-JS accordion behavior.

---

## Section Order (Final)

```
1. Hero          — Names, date, countdown, botanical frame
2. Bröllopsdag   — Day's timeline/schedule
3. Plats         — Ceremony + reception venues, maps
4. Boende        — Teleborgs Slott accommodation
5. Gåvor         — Gift section (Swish to toastmasters) ★ PRIMARY FEATURE
6. FAQ           — Dress code, children, contact, etc.
7. Footer        — Toastmasters, email, credits
```

**Note:** Photo gallery is NOT a standalone section. Instead, integrate photos as ambient imagery within other sections (hero, venue, etc.) as they become available.

---

## File Structure (Final)

```
wedding/
├── CLAUDE.md
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── assets/
│   ├── images/
│   │   ├── botanical-corner-top-right.webp
│   │   ├── botanical-corner-bottom-left.webp
│   │   ├── botanical-cluster-small.webp
│   │   ├── botanical-divider.webp
│   │   └── (couple photos, venue photos as available)
│   └── icons/
│       ├── swish-logo.svg
│       └── (QR codes when available)
├── research/            # Design research (do not deploy)
│   ├── 00-index.md
│   ├── 01-scandinavian-trends.md
│   ├── 02-tech-stack.md
│   └── 03-botanical-web-design.md
└── tmp/                 # Reference photos (do not deploy)
```

---

## Implementation Checklist

### Phase 1: Foundation
- [ ] HTML skeleton with all semantic sections
- [ ] CSS custom properties (full palette from `03-botanical-web-design.md`)
- [ ] Google Fonts import (Alex Brush, Cormorant Garamond, Cormorant SC, Montserrat)
- [ ] Mobile-first base styles, CSS reset, skip-link
- [ ] AOS library loaded via CDN

### Phase 2: Hero Section
- [ ] Hero layout (names, date, countdown)
- [ ] Botanical corner placeholders (CSS gradients until real PNG assets)
- [ ] Countdown timer (vanilla JS, Swedish labels)
- [ ] Entrance animations with `prefers-reduced-motion` guard

### Phase 3: Content Sections
- [ ] Bröllopsdag — centered vertical timeline
- [ ] Plats — two-card layout (ceremony + reception) with map links
- [ ] Boende — featured card with booking details
- [ ] Gåvor — warm message + Swish QR/contact cards (★ showcase section)
- [ ] FAQ — `<details>`/`<summary>` accordion
- [ ] Footer — contact info, toastmasters

### Phase 4: Navigation
- [ ] Sticky nav (transparent → solid on scroll)
- [ ] Mobile hamburger menu
- [ ] Smooth scroll to anchors (`scroll-behavior: smooth`)
- [ ] Close menu on link tap

### Phase 5: Visual Polish
- [ ] Section dividers (SVG waves + botanical branch)
- [ ] Alternating section backgrounds
- [ ] Subtle paper texture (CSS noise)
- [ ] Scroll-reveal animations (AOS `fade-up`)
- [ ] Botanical corner scaling per breakpoint

### Phase 6: Production
- [ ] Source and optimize real botanical PNG/WebP assets
- [ ] Image lazy loading (native `loading="lazy"`)
- [ ] WebP with fallback via `<picture>`
- [ ] Accessibility audit (contrast, keyboard nav, screen reader, reduced motion)
- [ ] Test: Chrome, Safari, Firefox — mobile + desktop
- [ ] Add `.nojekyll` for GitHub Pages
- [ ] Add `research/` and `tmp/` to `.gitignore`

---

## Key Content Placeholders (TBD from couple)

- [ ] Day's schedule/program details
- [ ] Parking and transport information
- [ ] Swish QR codes for toastmasters
- [ ] Couple photos
- [ ] Additional FAQ items
- [ ] Custom domain
