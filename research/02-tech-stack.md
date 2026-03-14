# Technical Stack Recommendations

> Research compiled for use by the building agent. All recommendations are for a static site hosted on GitHub Pages with no build tools.

## CSS Approach: Custom CSS (No Framework)

**Decision:** Write custom CSS from scratch. Tailwind Play CDN was evaluated but rejected — it loads ~300KB+ at runtime, causes FOUC, and is explicitly not recommended for production by the Tailwind team. Pico CSS is too opinionated for this custom botanical aesthetic.

Custom CSS gives total design control, zero overhead, and modern CSS features (Grid, Flexbox, `clamp()`, container queries) have excellent browser support.

### CSS Architecture

```
css/style.css structure:
1. Custom Properties (Design Tokens)
2. Reset/Base
3. Typography
4. Layout (sections, grid)
5. Components (nav, cards, countdown, etc.)
6. Botanical decorations
7. Animations
8. Responsive adjustments
```

### Design Tokens

```css
:root {
  /* Colors — extracted from invitation */
  --color-bg: #faf9f6;           /* warm off-white */
  --color-bg-alt: #f5f0eb;       /* slightly warmer for alternating sections */
  --color-text: #3a3a3a;         /* charcoal */
  --color-text-light: #6b6b6b;   /* secondary text */
  --color-sage: #8a9a7b;         /* sage/olive green */
  --color-sage-dark: #6b7d5e;    /* darker sage for hover */
  --color-sage-light: #c5d1bc;   /* light sage for backgrounds */
  --color-blue: #7b8fa8;         /* dusty/steel blue */
  --color-blue-light: #b8c5d4;   /* light blue accent */
  --color-gold: #b8a88a;         /* warm gold accent */
  --color-cream: #f0ebe3;        /* cream */

  /* Typography */
  --font-script: 'Alex Brush', cursive;
  --font-heading: 'Cormorant Garamond', serif;
  --font-small-caps: 'Cormorant SC', serif;
  --font-body: 'Montserrat', sans-serif;

  /* Spacing */
  --section-padding: clamp(3rem, 8vw, 6rem);
  --content-width: min(90%, 800px);
}
```

---

## Animation: AOS (Animate on Scroll) 2.3.4

**Decision:** Use AOS. ~6KB gzipped total. Declarative `data-aos` attributes are easy to work with.

### CDN Links

```html
<link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
```

### Initialization

```javascript
AOS.init({
  duration: 800,
  easing: 'ease-out-cubic',
  once: true,        // animate only once (don't re-trigger on scroll up)
  offset: 50,        // trigger 50px before element enters viewport
});
```

### Recommended Animations

| Animation | Use For |
|-----------|---------|
| `fade-up` | Primary content reveal (default) |
| `fade` | Subtle section reveals |
| `fade-right` / `fade-left` | Alternating content blocks |
| `zoom-in` | Sparingly — couple's names in hero |

### Usage

```html
<div data-aos="fade-up" data-aos-delay="100">Content here</div>
```

### Fallback: Pure CSS + IntersectionObserver

If AOS is deemed too heavy, this achieves 90% of the effect in ~20 lines:

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
```

```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}
.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}
```

---

## Typography

### Primary Recommendation: Alex Brush + Cormorant Garamond + Montserrat

| Role | Font | Weight(s) | Rationale |
|------|------|-----------|-----------|
| **Couple's names** | Alex Brush | 400 | Flowing connected script, closest match to invitation calligraphy. Romantic without being kitschy. |
| **Section headings** | Cormorant Garamond | 300, 400, 500, 600 + italics | Elegant high-contrast serif by Christian Thalmann. European, refined, not overused in wedding space. |
| **Small caps / "OCH"** | Cormorant SC | 300, 400, 500 | Small caps variant for decorative text and labels (matches invitation "OCH" styling) |
| **Body text** | Montserrat | 300, 400, 500 | Clean geometric sans-serif. Light weights feel modern and airy. Excellent mobile readability. |

### Google Fonts Link

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Cormorant+SC:wght@300;400;500&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
```

### Alternative Pairings (if primary doesn't feel right)

| Pairing | Feel | Notes |
|---------|------|-------|
| Playfair Display + Lato | Classic wedding | Bordering on overused |
| Cormorant + EB Garamond + Work Sans | More nuanced | 3-font complexity |
| Bodoni Moda + DM Sans | Fashion-forward modern | Less romantic, more contemporary |

### Script Font Comparison

| Font | Feel | Overused? | Invitation Match |
|------|------|-----------|-----------------|
| **Alex Brush** | Flowing, romantic | Medium | **Best match** |
| Great Vibes | Very ornate, thick | **Very overused** | Too heavy |
| Dancing Script | Casual, bouncy | High | Too informal |
| Tangerine | Ultra-thin, delicate | Low | Too thin, hard to read |
| Pinyon Script | Classic calligraphy | Low | Good, slightly more formal |
| Rouge Script | Elegant, slightly retro | Low | Fresh alternative |

---

## Botanical Assets

### Format: PNG (not SVG)

Watercolor texture cannot be represented in SVG. Use PNG with transparency for all botanical elements. SVG only for simple line-art dividers and icons.

### Free Sources

| Source | License | Best For |
|--------|---------|----------|
| **Freepik** | Free with attribution, Premium without | Best selection — search "watercolor eucalyptus corner", "botanical border sage green" |
| **Pixabay** | Free, no attribution needed | Fewer options but truly free |
| **rawpixel.com** | Free tier + CC0 section | Excellent botanical collection |
| **Vecteezy** | Free with attribution | Good watercolor floral borders |

### CSS Integration for Corner Botanicals

```css
.section-botanical {
  position: relative;
  overflow: hidden;
}

/* Top-right corner (matching invitation layout) */
.section-botanical::before {
  content: '';
  position: absolute;
  top: -20px;
  right: -20px;
  width: clamp(200px, 40vw, 400px);
  height: clamp(200px, 40vw, 400px);
  background: url('../assets/images/botanical-corner-top.png') no-repeat;
  background-size: contain;
  opacity: 0.85;
  pointer-events: none;
  z-index: 0;
}

/* Bottom-left corner (mirrored) */
.section-botanical::after {
  content: '';
  position: absolute;
  bottom: -20px;
  left: -20px;
  width: clamp(200px, 40vw, 400px);
  height: clamp(200px, 40vw, 400px);
  background: url('../assets/images/botanical-corner-bottom.png') no-repeat;
  background-size: contain;
  opacity: 0.85;
  pointer-events: none;
  z-index: 0;
  transform: scaleX(-1) scaleY(-1);
}

.section-botanical > * {
  position: relative;
  z-index: 1;
}
```

### Image Optimization Strategy

1. Crop tightly — remove excess transparent area
2. Limit dimensions — corner decorations rarely need >600px wide
3. Compress with TinyPNG or Squoosh (60-80% reduction)
4. Convert to WebP with transparency (50% smaller than optimized PNG)
5. Use CSS `background-image` for decorative botanicals (not `<img>`)
6. Target: 50-100KB per botanical piece after optimization
7. **Total botanical asset budget: <500KB across all decorative images**

---

## Countdown Timer

### JavaScript (Vanilla, ~30 lines)

```javascript
function initCountdown() {
  const weddingDate = new Date('2026-05-23T16:00:00+02:00');  // CEST

  function updateCountdown() {
    const now = new Date();
    const diff = weddingDate - now;

    if (diff <= 0) {
      document.querySelector('.countdown').innerHTML =
        '<p class="countdown-message">Idag är dagen!</p>';
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    updateUnit('days', days);
    updateUnit('hours', hours);
    updateUnit('minutes', minutes);
    updateUnit('seconds', seconds);
  }

  function updateUnit(id, value) {
    const el = document.getElementById(`countdown-${id}`);
    if (el) el.textContent = String(value).padStart(2, '0');
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);
}

document.addEventListener('DOMContentLoaded', initCountdown);
```

### HTML

```html
<div class="countdown" aria-label="Nedräkning till bröllopet">
  <div class="countdown-unit">
    <span class="countdown-number" id="countdown-days">00</span>
    <span class="countdown-label">dagar</span>
  </div>
  <div class="countdown-separator">:</div>
  <div class="countdown-unit">
    <span class="countdown-number" id="countdown-hours">00</span>
    <span class="countdown-label">timmar</span>
  </div>
  <div class="countdown-separator">:</div>
  <div class="countdown-unit">
    <span class="countdown-number" id="countdown-minutes">00</span>
    <span class="countdown-label">minuter</span>
  </div>
  <div class="countdown-separator">:</div>
  <div class="countdown-unit">
    <span class="countdown-number" id="countdown-seconds">00</span>
    <span class="countdown-label">sekunder</span>
  </div>
</div>
```

### CSS

```css
.countdown {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.5rem);
  padding: 2rem 0;
}

.countdown-unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 60px;
}

.countdown-number {
  font-family: var(--font-heading);
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 300;
  color: var(--color-sage-dark);
  line-height: 1;
}

.countdown-label {
  font-family: var(--font-body);
  font-size: clamp(0.65rem, 1.5vw, 0.8rem);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-text-light);
  margin-top: 0.25rem;
}

.countdown-separator {
  font-family: var(--font-heading);
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  color: var(--color-sage-light);
  align-self: flex-start;
  margin-top: 0.2em;
}
```

---

## Navigation: Sticky Header + Mobile Hamburger

### HTML Structure

```html
<header class="site-header" id="site-header">
  <nav class="nav" aria-label="Huvudnavigation">
    <a href="#hem" class="nav-logo">C & F</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Öppna meny">
      <span class="nav-toggle-line"></span>
      <span class="nav-toggle-line"></span>
      <span class="nav-toggle-line"></span>
    </button>
    <ul class="nav-menu" id="nav-menu">
      <li><a href="#program">Bröllopsdagen</a></li>
      <li><a href="#plats">Plats</a></li>
      <li><a href="#boende">Boende</a></li>
      <li><a href="#gavor">Gåvor</a></li>
      <li><a href="#galleri">Galleri</a></li>
      <li><a href="#faq">FAQ</a></li>
    </ul>
  </nav>
</header>
```

### Key CSS

```css
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  background-color: transparent;
}

.site-header.scrolled {
  background-color: rgba(250, 249, 246, 0.95);
  backdrop-filter: blur(10px);
  box-shadow: 0 1px 10px rgba(0, 0, 0, 0.05);
}
```

### JavaScript (scroll detection + mobile toggle)

```javascript
function initNavScroll() {
  const header = document.getElementById('site-header');
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 50);
  }, { passive: true });
}

function initMobileNav() {
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.getElementById('nav-menu');

  toggle.addEventListener('click', () => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !isOpen);
    menu.classList.toggle('open');
  });

  // Close menu when clicking a link
  menu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', 'false');
      menu.classList.remove('open');
    });
  });
}
```

### Smooth Scrolling

```css
html {
  scroll-behavior: smooth;
  scroll-padding-top: 70px; /* Account for fixed nav height */
}
```

**CSS scroll-snap: Not recommended.** Feels rigid and interrupts natural browsing.

---

## Image Optimization

### Lazy Loading

```html
<!-- Hero: eager load -->
<img src="assets/images/hero.jpg" alt="Cajsa och Filip" loading="eager" fetchpriority="high">
<!-- Below fold: lazy load -->
<img src="assets/images/venue.jpg" alt="Teleborgs Slott" loading="lazy">
```

### Format Strategy

| Use Case | Format | Notes |
|----------|--------|-------|
| Photos | WebP with `<picture>` fallback to JPEG | 25-35% smaller |
| Botanical decorations | WebP with PNG fallback | Transparency + smaller |
| Icons, logos | SVG | Infinitely scalable |
| QR codes | PNG or SVG | Must be crisp |

### Responsive Images

```html
<picture>
  <source
    srcset="assets/images/hero-400.webp 400w,
            assets/images/hero-800.webp 800w,
            assets/images/hero-1200.webp 1200w"
    sizes="100vw" type="image/webp">
  <img
    src="assets/images/hero-800.jpg"
    srcset="assets/images/hero-400.jpg 400w,
            assets/images/hero-800.jpg 800w,
            assets/images/hero-1200.jpg 1200w"
    sizes="100vw" alt="Cajsa och Filip" loading="eager">
</picture>
```

---

## Maps: Hybrid Approach

Use **Google Maps links** (opens native map app on mobile) + optional lazy-loaded **OpenStreetMap embed** for visual display.

```html
<div class="venue-card">
  <h3>Vigsel — Gårdsby kyrka</h3>
  <p class="venue-address">Gårdsby kyrka, 355 92 Växjö</p>
  <div class="venue-actions">
    <a href="https://maps.google.com/?q=Gårdsby+kyrka,+355+92+Växjö"
       target="_blank" rel="noopener" class="btn btn-primary">
      Vägbeskrivning
    </a>
    <button class="btn btn-outline"
            onclick="this.nextElementSibling.style.display='block'; this.style.display='none';">
      Visa karta
    </button>
    <iframe
      src="https://www.openstreetmap.org/export/embed.html?bbox=14.75,56.85,14.85,56.90&layer=mapnik&marker=56.875,14.80"
      width="100%" height="300"
      style="display:none; border:0; border-radius:8px; margin-top:1rem;"
      loading="lazy" title="Karta till Gårdsby kyrka">
    </iframe>
  </div>
</div>
```

**Rationale:** Zero performance cost for the link. OpenStreetMap is free, no API key, GDPR-friendly. Hidden behind button click to avoid loading iframe by default.

---

## Full `<head>` Resource List

```html
<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cajsa & Filip — 23 maj 2026</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Cormorant+SC:wght@300;400;500&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">

  <!-- AOS -->
  <link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">

  <!-- Custom Styles -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- ... content ... -->

  <!-- Before closing </body> -->
  <script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
```

## Performance Budget

| Resource | Size (gzipped) |
|----------|---------------|
| Google Fonts (4 families) | ~40-60KB |
| AOS CSS | ~2KB |
| AOS JS | ~4KB |
| Custom CSS | ~10-15KB |
| Custom JS | ~5KB |
| **Total non-image payload** | **~65-85KB** |
| Botanical assets target | <500KB |
| **Total page weight target** | **<600KB** (excluding gallery photos) |
