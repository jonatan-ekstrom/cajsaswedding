---
globs: ["assets/**", "index.html"]
---

# Botanical Asset Reference

## Deployed Asset Inventory

All assets are in `assets/images/florals/`. 14 PNG files with transparent backgrounds.

| Filename | Section Placement | Description |
|----------|-------------------|-------------|
| `corner-roses-blue.png` | Hero TR | Large corner cluster with white roses and blue accent flower |
| `corner-blue-fern.png` | Hero BL | Complementary corner with blue rose and fern leaves |
| `sprig-berries.png` | Bröllopsdag BR | Small accent sprig with berries |
| `wreath-eucalyptus.png` | Hero (frames countdown) | Open eucalyptus wreath |
| `roses-cream-cluster.png` | Boende TL | White/cream rose cluster |
| `eucalyptus-silver.png` | Plats BL | Single eucalyptus branch |
| `anemone-blue.png` | Plats TR | Small blue anemone accent |
| `olive-branch.png` | Gåvor TR | Small olive/greenery accent |
| `buds-blue.png` | FAQ TR | Small dusty blue bud sprig |
| `eucalyptus-populus.png` | FAQ BL | Heart-shaped eucalyptus leaf branch |
| `bouquet-blue-rose.png` | Gåvor BL | Blue rose bouquet (centered, soft fadeout) |
| `rosebuds-accent.png` | Boende BR | White rosebuds with eucalyptus (centered, soft fadeout) |
| `bouquet-blue-anemone.png` | Bröllopsdag TL | Blue anemone cluster (centered, soft fadeout) |
| `garland-eucalyptus.png` | Boende (inline below card) | Horizontal eucalyptus garland |

## Style Reference for Regeneration

If any asset needs to be regenerated (e.g., via Copilot Creator or similar tools):

- **Technique:** Wet-on-wet watercolor blending with soft, feathered edges — NOT hard outlines, NOT digital illustration
- **Leaves:** Elongated eucalyptus (silver dollar + willow varieties), heart-shaped eucalyptus populus, small oval filler foliage
- **Flowers:** White/cream garden roses (dominant), dusty steel-blue anemones or roses (accent), tiny white gypsophila sprigs
- **Feel:** Delicate, translucent, hand-painted — visible paper texture through washes

### Color Reference

| Element | Color Description | Hex |
|---------|------------------|-----|
| Darkest leaves | Dark olive green | `#5C6B4F` |
| Standard leaves | Sage green | `#8FA07C` |
| Light leaf wash | Pale sage | `#B5C4A5` |
| Blue flowers | Dusty steel blue | `#6B8BA4` |
| White roses | Warm ivory/cream | `#F5F0E8` |
| Stems/branches | Warm brown-green | `#7A7A5A` |
| Baby's breath | Very pale cream | `#FAF8F5` |

## Post-Processing Notes

- All assets should be **centered with soft fadeout** — no hard edges at canvas boundaries
- Remove white background to transparent PNG before deploying
- Target resolution: at least 1000px on longest side for large elements, 500px for small accents
- Generous transparent padding on all sides (at least 20-25% of canvas width)

## Image Optimization Rules

- **Total floral budget:** <500KB combined (after compression)
- **Lazy loading:** All botanical images use `loading="lazy"` except hero images (use `loading="eager"`)
- **CSS placement:** All botanicals are `position: absolute` with `pointer-events: none` and `z-index: 1`
- **Responsive:** Scale down + reduce opacity on mobile, NEVER hide entirely (botanicals are core to the design identity)
