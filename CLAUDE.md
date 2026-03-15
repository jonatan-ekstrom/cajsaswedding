# Cajsa & Filip's Wedding Website

## Project Overview

Static wedding website for **Cajsa Ekström & Filip Bringe**, hosted on GitHub Pages. Built by Jonatan Ekström (brother of the bride) as a gift/favor.

- **Tech stack:** Plain HTML, CSS, and JavaScript — no build tools or frameworks
- **Language:** Swedish
- **Hosting:** GitHub Pages with custom domain (TBD)
- **Repository:** `main` branch for deployment

## Wedding Details

| Detail | Value |
|---|---|
| **Couple** | Cajsa Ekström & Filip Bringe |
| **Date** | Lördag 23 maj 2026, kl. 16:00 |
| **Ceremony** | Gårdsby kyrka, 355 92 Växjö |
| **Reception** | Teleborgs Slott, Slottsallén 33, 352 56 Växjö |
| **Dress code** | Uppklädd klädsel |
| **Contact email** | filipcajsa2026@gmail.com |
| **RSVP deadline** | 31 mars 2026 (via email, NOT on the website) |
| **Children policy** | Welcome at the ceremony; dinner/party is adults only (except nursing babies) |

### Toastmasters

| Name | Phone |
|---|---|
| Christian Boman | 070 225 91 08 |
| Elin Bexell | 070 392 96 70 |

### Accommodation

Rooms available at Teleborgs Slott. Guests book directly:
- Email: info@teleborgsslott.com
- Phone: 0470-348980
- Website: teleborgsslott.com
- Mention the wedding when booking ("Cajsa & Filip")

## Website Sections

The site is a single-page layout with the following sections:

1. **Hero / Landing** — Names, date, countdown timer
2. **Couple Quote** — Short personal message from Cajsa & Filip (styled element, not a full section)
3. **Bröllopsdag (Schedule/Program)** — Timeline of the day
4. **Plats & Hitta hit (Venue & Getting there)** — Ceremony and reception locations with richer descriptions, map links
5. **Boende (Accommodation)** — Info about Teleborgs Slott rooms
6. **Gåvor / Bröllopsgåva (Gifts)** — **This is the primary reason for the website** (see below)
7. **Dela era bilder (Photo Sharing)** — QR code / link to shared Google Photos album for guest photos + unplugged ceremony note
8. **Vanliga frågor (FAQ)** — Dress code, children policy, mobilfri vigsel, +1 policy, other hotels, contact info
9. **Footer** — Toastmasters, email

## Gift Section — Key Feature

The couple does **not** want traditional gifts. Instead, they want guests to contribute money toward their honeymoon. The system works as follows:

- Guests send money via **Swish** to the **toastmasters** (Christian Boman & Elin Bexell), NOT directly to Cajsa & Filip
- The toastmasters pool all contributions and give a lump sum to the couple after the wedding
- This way Cajsa & Filip never know who gave what (or if someone chose not to give)
- **No suggested amount** — completely voluntary and open
- The page should display Swish QR codes and/or phone numbers for the toastmasters (placeholder for now — assets to be provided)
- Tone: warm, no-pressure, appreciative — emphasize that presence is the greatest gift

## Design Direction

The design should match the physical invitations (photos in `scratchpad/reference_photos/`):

- **Style:** Elegant, botanical, romantic
- **Color palette:**
  - White/cream background
  - Sage/olive green (leaves, eucalyptus)
  - Dusty/steel blue accent (flowers)
  - Dark gray or charcoal for body text
  - Warm gold or dark olive for accent text
- **Typography:**
  - Elegant script/cursive font for the couple's names and headings (similar to invitation)
  - Clean serif or sans-serif for body text
- **Decorative elements:** Watercolor-style botanical illustrations (leaves, roses, eucalyptus) — matching the invitation aesthetic
- **Mood:** Light, airy, refined — lots of whitespace

## File Structure

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
│   │   ├── florals/    # Botanical PNG decorations
│   │   └── photos/     # Wedding & venue photos (JPG)
│   └── icons/
│       └── swish/      # Swish QR codes
└── scratchpad/              # Reference material (not deployed, gitignored)
    └── reference_photos/    # Invitation photos for design reference
```

## Agent Guidelines

- **Always run sub-agents in the foreground** (never set `run_in_background: true`). Background agents cannot inherit the session's permission mode and will silently fail on Write/Edit operations. Foreground agents launched in the same message still run in parallel, so there is no concurrency penalty.

## Development Guidelines

- Mobile-first responsive design — most guests will view on phones
- Smooth scroll between sections
- Keep JavaScript minimal — countdown timer, smooth scroll, maybe a simple lightbox for photos
- Optimize images for web (compress, lazy-load)
- Ensure accessibility (semantic HTML, alt text, sufficient contrast)
- Test in Chrome, Safari, Firefox (mobile & desktop)
- Use Google Fonts or similar for web fonts (find close matches to the invitation style)
- All text content in Swedish

## Content Placeholders

The following content is TBD and should use clear placeholders:
- [x] Day's schedule/program details — implemented
- [x] Swish QR codes and numbers for toastmasters — implemented
- [ ] Couple quote text — draft provided, needs Cajsa & Filip's personalization
- [ ] Google Photos album link + QR code for photo sharing section
- [ ] Couple photos for ambient imagery
- [x] Gårdsby kyrka — couple's connection to the church (for venue description)
- [ ] Alternative hotel names for Växjö FAQ (verify recommendations)
- [ ] Custom domain configuration

## Design Research

Detailed design research is in the `research/` folder (not deployed):

- `research/00-index.md` — Summary, reconciled decisions, implementation checklist
- `research/01-scandinavian-trends.md` — Nordic design patterns, section layout guidance
- `research/02-tech-stack.md` — CSS, animations, fonts, assets, components
- `research/03-botanical-web-design.md` — Color palette, botanical CSS, hero design, accessibility

### Key Decisions (from research)

| Decision | Choice |
|----------|--------|
| CSS | Custom (no framework) |
| Animations | AOS 2.3.4 via CDN, subtle fade-up |
| Script font | Alex Brush (Google Fonts) |
| Heading font | Cormorant Garamond + Cormorant SC |
| Body font | Montserrat (300, 400, 500) |
| Botanical assets | PNG/WebP from free sources (Freepik, Pixabay, rawpixel) |
| Maps | Google Maps links + optional OpenStreetMap embed |
| FAQ | `<details>`/`<summary>` (no JS) |
| Couple/venue photos | Integrated as ambient imagery, not standalone section |
| Guest photo sharing | Standalone "Dela era bilder" section with Google Photos QR code |
| CSS approach | Mobile-first (`min-width` queries only) |
| Breakpoints | 480px (medium mobile), 768px (tablet layout + botanicals), 1024px (desktop nav + full botanicals) |
| Desktop nav | Horizontal links at 1024px+; hamburger menu below (6 Swedish labels don't fit at 768px) |

## Logistics Decisions (March 2025)

The following were explicitly decided during content review:
- **No OSA reminder** — site launches after the March 31 deadline
- **No transport info** — venues are close; guests drive themselves
- **No explicit parking info** — available at both venues, self-evident
- **No plus-ones** — invitation is per named guest only
- **Unplugged ceremony** — guests asked to put phones away during vigsel
- **Site launches post-OSA** — this was a late ask by the bride

## Notes

- The `scratchpad/` folder is gitignored; `scratchpad/reference_photos/` contains photos of the physical invitations
- The `research/` folder contains design research — do NOT deploy
- RSVP is handled via email (filipcajsa2026@gmail.com), not on the website
- The toastmasters are the contact for speeches/entertainment (tal/spex)
