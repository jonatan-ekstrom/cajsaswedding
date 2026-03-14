# Botanical Web Design Techniques

> Research compiled for translating Cajsa & Filip's watercolor botanical invitation design into a responsive wedding website.

## 1. Invitation Botanical Patterns (from reference photos)

**Top-right corner cluster** (main invitation): Large arrangement flowing from top-right, white/cream roses as dominant flower, sage/olive eucalyptus leaves extending outward, smaller filler foliage.

**Diagonal opposing corners** (Save the Date): Two mirrored botanical clusters at top-right and bottom-left, creating a frame. Each contains dusty steel-blue flowers (anemones or garden roses), sage green eucalyptus leaves, small white filler flowers (baby's breath / gypsophila).

**Bottom-left corner** (additional cards): Single cluster anchored to bottom-left.

### Key Visual Notes
- Botanicals are **asymmetric** — never perfectly mirrored, giving a natural hand-painted feel
- Watercolor uses visible **wet-on-wet blending** with soft edges, not hard outlines
- Leaves vary from dark olive (saturated) to light sage (translucent wash)
- Dusty blue flowers are a strong accent — used sparingly (1-2 per cluster)
- White/cream roses blend into background, creating depth through subtle value changes
- Small heart-shaped eucalyptus leaves (eucalyptus populus) are a recurring motif

---

## 2. Complete Color Palette

```css
:root {
  /* === PRIMARY: Sage/Olive Green (Eucalyptus) === */
  --sage-darkest: #5C6B4F;      /* Darkest leaf shadows */
  --sage-dark: #7A8B6A;          /* Standard eucalyptus leaf */
  --sage: #8FA07C;               /* Primary sage green */
  --sage-medium: #9DAE8B;        /* Mid-tone leaves */
  --sage-light: #B5C4A5;         /* Light eucalyptus wash */
  --sage-lightest: #D4DEC9;      /* Very light botanical bg */
  --sage-tint: #EBF0E5;          /* Barely-there sage tint */

  /* === SECONDARY: Dusty/Steel Blue (Blue flowers) === */
  --blue-dark: #4A6178;          /* Deep steel blue */
  --blue: #6B8BA4;               /* Primary dusty blue */
  --blue-medium: #8BA4B8;        /* Medium dusty blue */
  --blue-light: #A8BFD0;         /* Light blue accent */
  --blue-lightest: #D0DEE8;      /* Very light blue wash */
  --blue-tint: #E8EFF4;          /* Barely-there blue tint */

  /* === ACCENT: Warm Gold / Dark Olive === */
  --gold: #B8A06A;               /* Warm gold accent */
  --gold-dark: #97834D;          /* Dark gold for text */
  --gold-light: #D4C494;         /* Light gold highlight */
  --olive-accent: #6B6B3E;       /* Dark olive for accent text */

  /* === NEUTRALS: Cream / Ivory / White === */
  --white: #FFFFFF;
  --cream: #FAF8F5;              /* Primary background */
  --cream-warm: #F5F0E8;         /* Warmer cream for sections */
  --ivory: #F0EBE1;              /* Ivory for card backgrounds */
  --linen: #E8E2D8;              /* Linen/paper feel */

  /* === TEXT === */
  --text-primary: #2C2C2C;       /* Main body text (charcoal) */
  --text-secondary: #4A4A4A;     /* Secondary text */
  --text-muted: #7A7A7A;         /* Muted/caption text */
  --text-light: #A0A0A0;         /* Very light text */
  --text-on-dark: #FAF8F5;       /* Text on dark backgrounds */

  /* === UI STATES === */
  --hover-sage: #7A8B6A;
  --hover-blue: #5A7B94;
  --hover-gold: #A8903A;
  --focus-ring: rgba(107, 139, 164, 0.5);

  /* === OVERLAYS & SHADOWS === */
  --overlay-light: rgba(250, 248, 245, 0.85);
  --overlay-sage: rgba(143, 160, 124, 0.08);
  --overlay-blue: rgba(107, 139, 164, 0.06);
  --shadow-soft: 0 2px 20px rgba(44, 44, 44, 0.06);
  --shadow-medium: 0 4px 30px rgba(44, 44, 44, 0.10);
  --shadow-botanical: 0 2px 15px rgba(92, 107, 79, 0.08);

  /* === BORDERS === */
  --border-light: rgba(44, 44, 44, 0.08);
  --border-sage: rgba(143, 160, 124, 0.3);
  --border-gold: rgba(184, 160, 106, 0.3);

  /* === GRADIENTS (section transitions) === */
  --gradient-cream-to-sage: linear-gradient(180deg, var(--cream) 0%, var(--sage-tint) 100%);
  --gradient-sage-to-cream: linear-gradient(180deg, var(--sage-tint) 0%, var(--cream) 100%);
  --gradient-cream-to-blue: linear-gradient(180deg, var(--cream) 0%, var(--blue-tint) 100%);
}
```

### Contrast Ratios (Accessibility)

| Text Color | Background | Ratio | WCAG AA |
|---|---|---|---|
| `--text-primary` (#2C2C2C) | `--cream` (#FAF8F5) | ~14.5:1 | **Pass** |
| `--text-secondary` (#4A4A4A) | `--cream` (#FAF8F5) | ~8.8:1 | **Pass** |
| `--sage-dark` (#7A8B6A) | `--cream` (#FAF8F5) | ~3.8:1 | **Fail small text** |
| `--sage-darkest` (#5C6B4F) | `--cream` (#FAF8F5) | ~5.5:1 | **Pass** |
| `--blue-dark` (#4A6178) | `--cream` (#FAF8F5) | ~5.3:1 | **Pass** |
| `--blue` (#6B8BA4) | `--cream` (#FAF8F5) | ~3.7:1 | **Fail small text** |

**Rule:** Use `--sage-darkest` and `--blue-dark` for any text that must meet WCAG AA. Reserve lighter variants for large decorative headings (18pt+) or purely decorative elements.

---

## 3. Botanical Asset Strategy

### Format: PNG/WebP (not SVG)

Watercolor texture cannot be represented in SVG. Use PNG with transparency for all watercolor elements. SVG only for simple line-art dividers and icons.

### Suggested Asset Files

```
assets/images/
  botanical-corner-top-right.webp       (hero section, ~80KB)
  botanical-corner-bottom-left.webp     (mirrored arrangement, ~80KB)
  botanical-cluster-small.webp          (smaller accent, ~40KB)
  botanical-divider-horizontal.webp     (section divider, ~30KB)
  single-eucalyptus-leaf.svg            (small accent, <2KB)
  eucalyptus-branch.svg                 (divider branch, <3KB)
```

### Free Sources

| Source | License | Notes |
|--------|---------|-------|
| **Freepik** | Free with attribution | Best selection. Search: "watercolor eucalyptus corner", "botanical border sage green" |
| **Pixabay** | Free, no attribution | Fewer options but truly free |
| **rawpixel.com** | Free tier + CC0 | Excellent botanical collection |
| **Vecteezy** | Free with attribution | Good watercolor borders |

### Search terms
"watercolor eucalyptus clipart PNG transparent", "dusty blue flower watercolor", "botanical wedding frame PNG", "sage green botanical corner"

---

## 4. CSS Implementation: Corner Botanicals

### Basic Placement

```css
.botanical-section {
  position: relative;
  overflow: hidden;
}

.botanical-corner-tr {
  position: absolute;
  top: -20px;
  right: -30px;
  width: clamp(180px, 30vw, 400px);
  height: auto;
  pointer-events: none;
  z-index: 1;
  opacity: 0.9;
}

.botanical-corner-bl {
  position: absolute;
  bottom: -20px;
  left: -30px;
  width: clamp(150px, 25vw, 350px);
  height: auto;
  pointer-events: none;
  z-index: 1;
  opacity: 0.85;
  transform: scaleX(-1);  /* Mirror horizontally */
}

.botanical-section .section-content {
  position: relative;
  z-index: 2;
}
```

### Responsive Behavior: Scale Down + Reduce Opacity (Never Hide)

```css
@media (max-width: 768px) {
  .botanical-corner-tr {
    width: clamp(120px, 40vw, 200px);
    top: -10px;
    right: -20px;
    opacity: 0.7;
  }
  .botanical-corner-bl {
    width: clamp(100px, 35vw, 180px);
    bottom: -10px;
    left: -15px;
    opacity: 0.65;
  }
}

@media (max-width: 480px) {
  .botanical-corner-tr { width: 130px; opacity: 0.5; }
  .botanical-corner-bl { width: 100px; opacity: 0.45; }
}
```

**Strategy:** Scale down + reduce opacity, do NOT hide entirely. The botanical corners are core to the design identity. Hiding them on mobile would break the invitation connection.

### No Parallax

- Parallax on mobile is unreliable (iOS Safari disables it, Android varies)
- Watercolor botanicals look best when stable and frame-like
- The invitation is static — the web version should match

---

## 5. Section Dividers

### SVG Wavy/Organic Divider

```html
<div class="section-divider" role="presentation" aria-hidden="true">
  <svg viewBox="0 0 1440 60" preserveAspectRatio="none">
    <path d="M0,30 C240,50 480,10 720,30 C960,50 1200,10 1440,30 L1440,60 L0,60 Z"
          fill="var(--sage-tint)" />
  </svg>
</div>
```

```css
.section-divider {
  width: 100%;
  line-height: 0;
  margin: -1px 0;
}
.section-divider svg {
  width: 100%;
  height: 40px;
  display: block;
}
```

### Botanical Branch Divider

```html
<div class="botanical-divider" role="presentation" aria-hidden="true">
  <div class="divider-line"></div>
  <img src="assets/images/eucalyptus-branch.svg" alt="" class="divider-branch" loading="lazy" />
  <div class="divider-line"></div>
</div>
```

```css
.botanical-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 2rem 1rem;
  max-width: 600px;
  margin: 0 auto;
}
.divider-line {
  flex: 1;
  height: 1px;
  background: var(--border-sage);
}
.divider-branch {
  width: clamp(60px, 10vw, 120px);
  height: auto;
  opacity: 0.7;
}
```

### Inline SVG Leaf Divider (No External Assets)

```html
<svg class="leaf-divider" viewBox="0 0 400 30" role="presentation" aria-hidden="true">
  <line x1="20" y1="15" x2="175" y2="15" stroke="#B5C4A5" stroke-width="0.5"/>
  <ellipse cx="200" cy="15" rx="12" ry="6" fill="#8FA07C" opacity="0.6"
           transform="rotate(-30 200 15)"/>
  <ellipse cx="200" cy="15" rx="12" ry="6" fill="#8FA07C" opacity="0.4"
           transform="rotate(30 200 15)"/>
  <circle cx="200" cy="15" r="2" fill="#6B8BA4" opacity="0.5"/>
  <line x1="225" y1="15" x2="380" y2="15" stroke="#B5C4A5" stroke-width="0.5"/>
</svg>
```

---

## 6. Hero Section Design

### HTML Structure

```html
<section class="hero" id="hero">
  <img src="assets/images/botanical-corner-top-right.webp"
       alt="" role="presentation" aria-hidden="true"
       class="hero-botanical hero-botanical-tr" loading="eager" />
  <img src="assets/images/botanical-corner-bottom-left.webp"
       alt="" role="presentation" aria-hidden="true"
       class="hero-botanical hero-botanical-bl" loading="eager" />
  <div class="hero-content">
    <p class="hero-pretext">Vi gifter oss!</p>
    <h1 class="hero-names">
      <span class="name">Cajsa</span>
      <span class="ampersand">&amp;</span>
      <span class="name">Filip</span>
    </h1>
    <p class="hero-date">Lördag 23 maj 2026</p>
    <div class="countdown" aria-label="Nedräkning till bröllopet">
      <!-- countdown units -->
    </div>
  </div>
</section>
```

### Hero CSS

```css
.hero {
  position: relative;
  min-height: 100vh;
  min-height: 100dvh;  /* dynamic viewport height for mobile */
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background-color: var(--cream);
  padding: 2rem;
}

.hero-botanical {
  position: absolute;
  pointer-events: none;
  z-index: 1;
}
.hero-botanical-tr {
  top: -30px;
  right: -40px;
  width: clamp(200px, 35vw, 500px);
}
.hero-botanical-bl {
  bottom: -30px;
  left: -40px;
  width: clamp(180px, 30vw, 450px);
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 700px;
}

.hero-names .name {
  font-family: var(--font-script);
  font-size: var(--text-hero);
  color: var(--text-primary);
  display: block;
  line-height: 1.1;
}

.hero-names .ampersand {
  font-family: var(--font-heading);
  font-size: var(--text-xl);
  font-style: italic;
  color: var(--sage-dark);
  display: block;
  margin: 0.25rem 0;
}
```

### Hero Entrance Animations

```css
@media (prefers-reduced-motion: no-preference) {
  .hero-botanical-tr { animation: fadeSlideIn 1.2s ease-out 0.3s both; }
  .hero-botanical-bl { animation: fadeSlideIn 1.2s ease-out 0.6s both; }
  .hero-pretext { animation: fadeUp 0.8s ease-out 0.8s both; }
  .hero-names .name:first-child { animation: fadeUp 0.8s ease-out 1.0s both; }
  .hero-names .ampersand { animation: fadeUp 0.6s ease-out 1.2s both; }
  .hero-names .name:last-child { animation: fadeUp 0.8s ease-out 1.3s both; }
  .hero-date { animation: fadeUp 0.8s ease-out 1.6s both; }
  .countdown { animation: fadeUp 0.8s ease-out 1.9s both; }
}

@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(-15px) scale(0.97); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## 7. Paper/Texture Background

### CSS-Only Subtle Noise (no extra HTTP request)

```css
body {
  background-color: var(--cream);
  background-image:
    radial-gradient(ellipse at 20% 50%, var(--cream-warm) 0%, transparent 70%),
    radial-gradient(ellipse at 80% 50%, var(--blue-tint) 0%, transparent 70%);
}

/* SVG noise filter for paper feel */
.paper-texture::before {
  content: '';
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0.03;
  pointer-events: none;
  z-index: 9999;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
}
```

### Handmade Feel Techniques
1. **Soft shadows** instead of hard borders
2. **Warm whites** — never pure `#FFFFFF` for content areas
3. **Organic shapes** — `border-radius` with uneven values (e.g., `40% 60% 55% 45%`)
4. **Opacity variation** — botanicals at 0.5-0.9 for depth
5. **Letter-spacing on serif fonts** — mimics printed typography breathing room
6. **Generous whitespace** — the invitation has lots; the website should too

---

## 8. Section Layout Plan

| Section | Background | Botanical Elements | Divider Above |
|---|---|---|---|
| Hero | `--cream` | TR + BL corner clusters (large) | None |
| Bröllopsdag | `--cream` | Small branch accent near heading | Leaf divider |
| Plats & Hitta hit | `--sage-tint` | BL corner cluster (small) | SVG wave (cream → sage-tint) |
| Boende | `--cream` | None (keep clean for info density) | SVG wave (sage-tint → cream) |
| Gåvor | `--cream-warm` | TR corner cluster (medium) | Leaf divider |
| Bildgalleri | `--cream` | Small leaf accents on edges | Botanical branch divider |
| FAQ | `--sage-tint` | BL corner cluster (small, faded) | SVG wave |
| Footer | `--sage-darkest` or `--text-primary` | None (solid dark) | Hard transition |

### Section Spacing

```css
.section {
  padding: clamp(3rem, 8vw, 6rem) clamp(1.25rem, 5vw, 3rem);
}
.section--spacious {
  padding: clamp(4rem, 10vw, 8rem) clamp(1.25rem, 5vw, 3rem);
}
```

---

## 9. Gift Section — Special Design Treatment

```css
.gift-card {
  max-width: 600px;
  margin: 0 auto;
  padding: 2.5rem clamp(1.5rem, 5vw, 3rem);
  background-color: var(--white);
  border-radius: 8px;
  box-shadow: var(--shadow-botanical);
  border: 1px solid var(--border-light);
}
.gift-message {
  font-family: var(--font-heading);
  font-size: var(--text-lg);
  font-style: italic;
  font-weight: 300;
  color: var(--text-secondary);
  line-height: 1.7;
}
.swish-contacts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}
.swish-contact {
  padding: 1.5rem;
  background: var(--sage-tint);
  border-radius: 8px;
  text-align: center;
}
```

---

## 10. Responsive Typography Scale

```css
:root {
  --text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem);
  --text-sm: clamp(0.875rem, 0.8rem + 0.35vw, 1rem);
  --text-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --text-lg: clamp(1.125rem, 1rem + 0.6vw, 1.375rem);
  --text-xl: clamp(1.375rem, 1.1rem + 1.2vw, 1.875rem);
  --text-2xl: clamp(1.75rem, 1.3rem + 2vw, 2.75rem);
  --text-3xl: clamp(2.25rem, 1.5rem + 3.5vw, 4rem);
  --text-hero: clamp(2.75rem, 1.8rem + 4.5vw, 5.5rem);
}
```

### Script Font on Small Screens

```css
.script-text {
  font-family: var(--font-script);
  font-size: max(1.5rem, var(--text-xl)); /* Floor of 24px */
}

/* On very small screens, fall back to elegant serif italic */
@media (max-width: 360px) {
  .section-heading-script {
    font-family: var(--font-heading);
    font-style: italic;
    font-weight: 300;
  }
}
```

---

## 11. Accessibility

### Decorative Images

```html
<img src="botanical.webp" alt="" role="presentation" aria-hidden="true" />
<svg class="divider" role="presentation" aria-hidden="true">...</svg>
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### High Contrast Mode

```css
@media (prefers-contrast: high) {
  :root {
    --text-primary: #000000;
    --text-secondary: #1a1a1a;
    --cream: #FFFFFF;
  }
  .botanical-corner-tr, .botanical-corner-bl, .hero-botanical {
    opacity: 0.3;
  }
}
```

### Focus & Skip Link

```css
a:focus-visible, button:focus-visible {
  outline: 2px solid var(--blue-dark);
  outline-offset: 3px;
}
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  padding: 0.5rem 1rem;
  background: var(--cream);
  z-index: 200;
}
.skip-link:focus { top: 0; }
```

---

## 12. Placeholder for Missing Botanical Assets

Until real watercolor PNGs are sourced, use CSS-generated placeholders:

```css
.botanical-placeholder {
  position: absolute;
  width: clamp(180px, 30vw, 400px);
  aspect-ratio: 1;
  background: radial-gradient(
    ellipse at 70% 30%,
    var(--sage-light) 0%, var(--sage-tint) 40%, transparent 70%
  );
  border-radius: 30% 70% 60% 40%;
  opacity: 0.5;
  pointer-events: none;
}
```
