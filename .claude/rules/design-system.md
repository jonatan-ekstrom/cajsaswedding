---
globs: ["css/**", "index.html"]
---

# Design System Reference

## CSS Color Palette

The full `:root` variable set, extracted from the implemented design:

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

## WCAG Contrast Ratios

| Text Color | Background | Ratio | WCAG AA |
|---|---|---|---|
| `--text-primary` (#2C2C2C) | `--cream` (#FAF8F5) | ~14.5:1 | **Pass** |
| `--text-secondary` (#4A4A4A) | `--cream` (#FAF8F5) | ~8.8:1 | **Pass** |
| `--sage-dark` (#7A8B6A) | `--cream` (#FAF8F5) | ~3.8:1 | **Fail small text** |
| `--sage-darkest` (#5C6B4F) | `--cream` (#FAF8F5) | ~5.5:1 | **Pass** |
| `--blue-dark` (#4A6178) | `--cream` (#FAF8F5) | ~5.3:1 | **Pass** |
| `--blue` (#6B8BA4) | `--cream` (#FAF8F5) | ~3.7:1 | **Fail small text** |

**Rule:** Use `--sage-darkest` and `--blue-dark` for any text that must meet WCAG AA. Reserve lighter variants for large decorative headings (18pt+) or purely decorative elements.

## Responsive Typography Scale

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

## Section Layout Plan

| Section | Background | Botanical Elements | Divider Above |
|---|---|---|---|
| Hero | `--cream` | TR + BL corner clusters (large) | None |
| Bröllopsdag | `--cream` | Small branch accent near heading | Leaf divider |
| Plats & Hitta hit | `--sage-tint` | BL corner cluster (small) | SVG wave (cream -> sage-tint) |
| Boende | `--cream` | None (keep clean for info density) | SVG wave (sage-tint -> cream) |
| Gåvor | `--cream-warm` | TR corner cluster (medium) | Leaf divider |
| Dela era bilder | `--cream` | Small leaf accents on edges | Botanical branch divider |
| FAQ | `--sage-tint` | BL corner cluster (small, faded) | SVG wave |
| Footer | `--sage-darkest` or `--text-primary` | None (solid dark) | Hard transition |

## Nordic Design Principles

- **Lagom:** Every element earns its place. Decorative botanicals used sparingly but deliberately.
- **Minimalist layout:** Single-page scroll, generous vertical spacing (80-120px between sections), narrow content blocks (max-width 700-800px), no sidebars.
- **Nature palette:** Muted, desaturated earth tones. Never pure `#FFFFFF` for content areas — always slightly warm. Greens lean sage/olive (gray-greens). Blues are dusty/steel, never bright.
- **Typography restraint:** Script fonts only for names/key headings. Body in clean serif or sans-serif. Larger than typical (18-20px body). Generous line-height (1.6-1.8).
- **Whitespace:** The invitation has lots; the website should too.

## Accessibility Patterns

- **Reduced motion:** Wrap all animations in `@media (prefers-reduced-motion: no-preference)`.
- **High contrast:** Override text colors to `#000000`/`#1a1a1a` and reduce botanical opacity to 0.3.
- **Decorative images:** Always use `alt="" role="presentation" aria-hidden="true"`.
- **Focus/skip-link:** `outline: 2px solid var(--blue-dark)` with `outline-offset: 3px`. Skip link at top of page.
