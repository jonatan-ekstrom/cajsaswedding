# Scandinavian Wedding Website Design Trends

> Research compiled for use by the building agent. Focused on Nordic/European aesthetics matching the physical invitation design.

## Invitation Design Analysis

The four reference photos (`tmp/`) reveal a specific design language:

- **Botanical arrangement style**: Watercolor clusters in corners (top-right, bottom-left). Asymmetric, organic — not a full border or frame.
- **Foliage**: Sage/olive eucalyptus in multiple green tones (gray-green to warm olive). Semi-transparent watercolor with visible brushstrokes.
- **Flowers**: Dusty blue roses/peonies as primary accent (2-3 per cluster). White/cream roses and small white blossoms fill out arrangements.
- **Script font**: Flowing modern calligraphy for names. Connected letterforms with moderate thick-thin contrast. Romantic but legible.
- **Body font**: Clean transitional serif. Bold weight for labels ("Toastmaster/Toastmadame", "Klädkod").
- **Background**: Pure white or very light cream paper.
- **Text color**: Dark charcoal/near-black (not pure black).
- **Layout**: Centered text, generous line spacing, lots of whitespace. Botanicals bleed to edges.

---

## Core Nordic Design Principles

### Lagom ("just the right amount")
Every element earns its place. Decorative botanicals used sparingly but deliberately. Contrast with American wedding sites that layer textures, backgrounds, and ornamentation.

### Minimalist layout
- Single-page scrolling is dominant in Nordic wedding sites
- Generous vertical spacing (80-120px between sections)
- Content blocks narrow (max-width 700-800px for text), centered
- Full-width images or subtle backgrounds break up text
- No sidebars

### Nature-inspired palette
- Muted, desaturated earth tones
- White/off-white backgrounds (never pure `#FFFFFF` — always slightly warm)
- Greens lean sage/olive/eucalyptus (gray-greens, not kelly/emerald)
- Blues are dusty/steel, never bright
- High contrast avoided

### Typography restraint
- Script fonts only for names/key headings
- Body text in clean serif or geometric sans-serif
- Font sizes larger than typical (18-20px body)
- Letter-spacing expanded for all-caps subheadings
- Generous line-height (1.6-1.8)

### Photography integration
- Soft, natural-light photos, desaturated or slightly faded
- Single hero photo rather than slideshow
- Some sites skip photos entirely, relying on illustrations/botanicals

---

## Swedish-Specific Wedding Site Elements

### What Swedish sites include (that others may not):
- **Toastmaster section**: Very common; dedicated section with contact info
- **Swish integration**: QR codes for mobile payments
- **"Barnpolicy"**: Children policy explicitly stated
- **Boende**: Prominent accommodation section (Swedish weddings often involve travel)
- **Klädkod**: Dress code always clearly stated

### What Swedish sites typically omit:
- RSVP forms (email/phone preferred)
- Registry links to specific stores (cash gifts via Swish are the norm)
- Elaborate "our story" timelines
- Bridal party introductions

### Mobile-first imperative
70-80% of Swedish wedding website traffic comes from mobile. Guests receive the link via text/Swish/email and open immediately on phone. Design must prioritize mobile as primary, desktop as enhancement.

---

## Information Architecture

### Recommended: Single-Page Scrolling Layout

Why: 5-8 content sections fit well, guests want to scan quickly, mobile users prefer scrolling over tapping, simpler to build with plain HTML/CSS/JS, feels like unfolding a digital invitation.

### Section Order

```
1. Hero / Landing        — Names, date, countdown
2. Bröllopsdag           — Timeline/schedule
3. Plats & Hitta hit     — Venues, maps, directions
4. Boende                — Accommodation
5. Bröllopsgåva          — Gift section (primary CTA)
6. Vanliga frågor        — FAQ
7. Footer                — Contact, toastmasters
```

**Rationale:** Follows the guest's mental model — "What, When, Where, How, What else?" Gift section positioned after logistics so the guest is engaged before encountering it. Photo gallery better integrated as ambient imagery throughout sections rather than standalone.

---

## Section-by-Section Design Patterns

### Hero Section: Botanical Frame Hero

- Full viewport height (`min-height: 100vh`, flexbox centered)
- Botanical PNG decorations in corners (top-right large, bottom-left smaller) matching invitation placement
- Names in script font, large; "och" in small caps serif; date below in regular serif
- Countdown timer below date: numbers in serif, labels ("dagar", "timmar", "minuter") in small sans-serif
- Subtle scroll indicator at bottom (animated chevron)
- After wedding date: replace countdown with "Vi har gift oss!"

### Schedule/Timeline: Centered Vertical Timeline

- Vertical line connecting event dots (thin sage line, centered)
- Time at each node, event name and location beside it
- Small dots or botanical leaf icons at each node
- Mobile: same centered layout, reduced padding
- Alternative (more minimal): simple time + event rows with horizontal dividers

### Venue: Two-Card Layout

- Two equal cards side by side: Ceremony (Gårdsby kyrka) | Reception (Teleborgs Slott)
- Each with address and "Visa på karta" link to Google Maps
- Stack vertically on mobile
- Subtle card shadow: `box-shadow: 0 2px 12px rgba(0,0,0,0.06)`
- For embedded maps: apply `filter: grayscale(50%) contrast(0.9)` to match palette

### Accommodation: Featured Card

- Single prominent card for Teleborgs Slott
- Booking details: email, phone, website
- Note to mention wedding when booking
- Small sage-colored SVG icons for contact methods

### Gift Section (PRIMARY FEATURE)

- Optional slight sage tint background (`#EFF2EB`) to highlight importance
- Lead with personal message in italic serif (gratitude first, not the ask)
- Explain the Swish-to-toastmaster anonymity system
- Two QR code cards side by side (Christian Boman, Elin Bexell) with phone numbers as `tel:` links
- Swish logo for recognition
- **Tone: warm, no-pressure, appreciative. No suggested amounts.**

Sample text (Swedish):
> "Det bästa ni kan ge oss är er närvaro på vår stora dag. Om ni ändå önskar ge en gåva uppskattar vi ett bidrag till vår bröllopsresa. Swisha valfritt belopp till någon av våra toastmasters — de samlar ihop alla bidrag och ger dem till oss efter bröllopet, så vi aldrig vet vem som gett vad."

### FAQ: Accordion Pattern

- Use `<details>`/`<summary>` HTML elements for no-JS accordion
- Style with CSS transitions
- Items: Klädkod, Barn, OSA, Specialkost, Tal/spex, Parkering (placeholder), Transport (placeholder)
- Question in semi-bold serif, answer in regular weight

### Navigation

- **Desktop**: Sticky horizontal bar appearing after scrolling past hero. Small caps sans-serif labels. Scroll-spy active section indicator. Transparent-to-cream background transition.
- **Mobile**: Hamburger icon (top-right), slide-in drawer from right, large touch targets, close on link tap.
- Nav items: "Bröllopsdag" | "Plats" | "Boende" | "Gåva" | "Frågor"

### Section Dividers

- Most Scandinavian approach: generous whitespace only (100-150px padding)
- Optional: small centered SVG botanical element (single leaf sprig, 80-120px, sage at 40-60% opacity)
- Subtle background color alternation provides additional visual separation

---

## Deployment Notes (GitHub Pages)

- Serve from `main` branch root
- Add `.nojekyll` file
- Custom domain via CNAME file when ready
- Ensure `tmp/` and `research/` are in `.gitignore`
