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
1. Hero            — Names, date, countdown, botanical frame
2. Couple Quote    — Short personal message from Cajsa & Filip (not a full section, styled quote element)
3. Bröllopsdag     — Day's timeline/schedule
4. Plats           — Ceremony + reception venues, maps, richer descriptions
5. Boende          — Teleborgs Slott accommodation
6. Gåvor           — Gift section (Swish to toastmasters) ★ PRIMARY FEATURE
7. Dela era bilder — Photo sharing section with QR code to shared Google Photos album
8. FAQ             — Dress code, children, contact, mobilfri vigsel, other hotels, +1 policy, etc.
9. Footer          — Toastmasters, email, credits
```

**Notes:**
- The couple quote (item 2) is a styled element between sections, not a full section with heading. Centered italic Cormorant Garamond, subtle botanical garland. Placeholder text for Cajsa & Filip to personalize.
- Photo sharing (item 7) is a NEW standalone section added after the March 2025 content review. Includes a QR code linking to a shared Google Photos album so guests can upload their photos. Pairs naturally with an "unplugged ceremony" note.
- Photo gallery as ambient imagery within sections remains the approach for *couple/venue photos*. The photo sharing section is for *guest-contributed photos*.

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
- [x] Bröllopsdag — centered vertical timeline
- [x] Plats — two-card layout (ceremony + reception) with map links
- [x] Boende — featured card with booking details
- [x] Gåvor — warm message + Swish QR/contact cards (★ showcase section)
- [x] FAQ — `<details>`/`<summary>` accordion
- [x] Footer — contact info, toastmasters

### Phase 7: Content Enhancements (March 2025)
- [ ] Couple quote — styled personal message between hero and Bröllopsdagen
- [ ] Plats — richer venue descriptions (atmosphere, couple's connection to venues)
- [ ] Dela era bilder — new photo sharing section with Google Photos album QR code + unplugged ceremony note
- [ ] FAQ additions: mobilfri vigsel, andra hotell i Växjö, +1 policy
- [ ] Nav update — add "Bilder" link for the new photo sharing section

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

- [x] Day's schedule/program details — filled in with timeline
- [x] Swish QR codes for toastmasters — implemented with QR images + deep links
- [ ] Couple quote text — draft provided, needs Cajsa & Filip's personalization
- [ ] Google Photos album link + QR code for photo sharing section
- [ ] Couple photos for ambient imagery
- [ ] Custom domain configuration
- [ ] Alternative hotel details for Växjö (verify recommendations)
- [ ] Gårdsby kyrka — couple's connection to the church (for richer venue description)

## Decisions Log (March 2025 Content Review)

Decisions made during content review with site owner (Jonatan Ekström):

| Item | Decision | Rationale |
|------|----------|-----------|
| OSA reminder banner | **Skip** | Site launches after OSA deadline (March 31) has passed |
| Transport between venues | **Skip** | Venues are close; guests expected to drive themselves |
| Parking info | **Skip** | Available at both venues; no need to state explicitly |
| Personal couple quote | **Add** | Short styled quote between hero and Bröllopsdagen |
| Photo sharing section | **Add** | New section with QR code to Google Photos album |
| Day-after brunch | **Skip** | Unknown if planned; skip for now |
| Richer venue descriptions | **Add** | Add atmosphere/character to Plats venue cards |
| Mobilfri vigsel FAQ | **Add** | Unplugged ceremony note in FAQ |
| Other hotels FAQ | **Add** | Alternative accommodation options in Växjö |
| +1 / plus-one FAQ | **Add** | No plus-ones; invitation is per named guest |
| Song requests | **Skip** | Not needed |
| Memorial section | **Skip** | Not needed |
