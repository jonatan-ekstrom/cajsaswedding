# Swish QR Code Integration — Research & Implementation Guide

> **Date:** 2026-03-14
> **Status:** Research complete, implementation pending
> **Decision:** Two QR codes (one per toastmaster), pre-filled message, with mobile deep-link buttons

---

## 1. Background

The gift section should let guests contribute money toward the couple's honeymoon via Swish. To preserve anonymity (Cajsa & Filip won't know who gave what), payments go to the toastmasters who pool contributions and transfer a lump sum after the wedding.

**Recipients:**
| Role | Name | Phone / Swish |
|------|------|---------------|
| Toastmaster | Christian Boman | 070 225 91 08 |
| Toastmadame | Elin Bexell | 070 392 96 70 |

**Requirements:**
- One QR code per toastmaster — guests choose who to Swish
- Pre-filled message: "Bröllopsgåva Cajsa & Filip" (editable by guest)
- No pre-filled amount (guests choose freely)
- Mobile-friendly: deep-link button to open Swish app directly (guests can't scan their own screen)
- No backend — static site on GitHub Pages

---

## 2. Swish QR Code API

### Endpoint

```
POST https://mpc.getswish.net/qrg-swish/api/v1/prefilled
Content-Type: application/json
```

**No authentication required.** This is a public API.

### Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `format` | string | Output format: `"png"`, `"jpg"`, or `"svg"` |
| `size` | integer | Image size in pixels (minimum 300) |
| `payee.value` | string | Recipient's Swish number (phone number, no spaces) |
| `payee.editable` | boolean | Whether the payer can change the recipient |
| `amount.value` | number | Payment amount in SEK (use `1` as minimum placeholder if required) |
| `amount.editable` | boolean | Whether the payer can change the amount |
| `message.value` | string | Transaction message/reference |
| `message.editable` | boolean | Whether the payer can change the message |

### Response

Returns a **binary image file** in the requested format (PNG/JPG/SVG).

### Example: Generate QR Codes for Both Toastmasters

```bash
# Christian Boman
curl -X POST https://mpc.getswish.net/qrg-swish/api/v1/prefilled \
  -H "Content-Type: application/json" \
  -d '{
    "format": "png",
    "size": 600,
    "payee": { "value": "0702259108", "editable": false },
    "amount": { "value": 1, "editable": true },
    "message": { "value": "Bröllopsgåva Cajsa & Filip", "editable": true }
  }' \
  --output assets/icons/swish-qr-christian.png

# Elin Bexell
curl -X POST https://mpc.getswish.net/qrg-swish/api/v1/prefilled \
  -H "Content-Type: application/json" \
  -d '{
    "format": "png",
    "size": 600,
    "payee": { "value": "0703929670", "editable": false },
    "amount": { "value": 1, "editable": true },
    "message": { "value": "Bröllopsgåva Cajsa & Filip", "editable": true }
  }' \
  --output assets/icons/swish-qr-elin.png
```

**Notes:**
- Phone number format: `07XXXXXXXX` (no spaces, no country code)
- `size: 600` produces a high-res image that stays crisp when displayed at 200px CSS (3× for retina)
- `amount.value: 1` is a placeholder minimum — the guest can change it since `editable: true`
- If the API requires the amount field but you want it blank, try `"value": ""` or omit the `amount` object entirely

### Phone Number Format Uncertainty

The API may accept different formats. Try in this order:
1. `"0703929670"` (national, no spaces)
2. `"46703929670"` (international with country code, no +)
3. `"+46703929670"` (international with +)

### Fallback: Client-Side QR Generation

If the Swish API is unavailable, QR codes can be generated client-side using the **Swish QR format string**:

```
C<number>;<amount>;<message>;<editable_flags>
```

**Editable flags** (bitmask):
| Flag | Meaning |
|------|---------|
| `0` | All fields locked |
| `1` | Phone number editable |
| `2` | Amount editable |
| `4` | Message editable |

Sum the flags: e.g., `6` = amount (2) + message (4) editable.

**Example strings for our use case:**
```
C0702259108;1;Bröllopsgåva Cajsa & Filip;6   # Christian
C0703929670;1;Bröllopsgåva Cajsa & Filip;6   # Elin
```

This string can be encoded into a QR code using any standard JS library (e.g., [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) via CDN). No Swish API call needed.

**References:**
- [Swish QR format spec (GitHub)](https://github.com/lindskogen/swish-qr-format)
- [swish-qr Node.js library](https://github.com/gillstrom/swish-qr)

---

## 3. Swish Deep Links (Mobile)

Guests viewing the site on their phone can't scan a QR code on the same screen. The solution is a **Swish deep link** that opens the Swish app directly.

### URL Format

```
swish://payment?data=<URL-encoded JSON>
```

### JSON Payload Template

```json
{
  "version": 1,
  "payee": {
    "value": "<phone_no_spaces>",
    "editable": false
  },
  "amount": {
    "value": 1,
    "editable": true
  },
  "message": {
    "value": "Bröllopsgåva Cajsa & Filip",
    "editable": true
  }
}
```

### Full URL-Encoded Links

**Christian Boman:**
```
swish://payment?data=%7B%22version%22%3A%201%2C%20%22payee%22%3A%20%7B%22value%22%3A%20%220702259108%22%2C%20%22editable%22%3A%20false%7D%2C%20%22amount%22%3A%20%7B%22value%22%3A%201%2C%20%22editable%22%3A%20true%7D%2C%20%22message%22%3A%20%7B%22value%22%3A%20%22Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip%22%2C%20%22editable%22%3A%20true%7D%7D
```

**Elin Bexell:**
```
swish://payment?data=%7B%22version%22%3A%201%2C%20%22payee%22%3A%20%7B%22value%22%3A%20%220703929670%22%2C%20%22editable%22%3A%20false%7D%2C%20%22amount%22%3A%20%7B%22value%22%3A%201%2C%20%22editable%22%3A%20true%7D%2C%20%22message%22%3A%20%7B%22value%22%3A%20%22Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip%22%2C%20%22editable%22%3A%20true%7D%7D
```

### Behavior

| Platform | Result |
|----------|--------|
| iOS with Swish installed | Opens Swish app with fields pre-filled |
| Android with Swish installed | Opens Swish app with fields pre-filled |
| Desktop browser | Link does nothing (no handler) — QR code is the primary path |
| Mobile without Swish | May show "can't open" prompt — acceptable edge case |

### Alternative Simpler Format

If the JSON deep link doesn't work, try the simpler query-parameter format:
```
swish://payment?payee=0702259108&message=Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip
swish://payment?payee=0703929670&message=Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip
```

**Important:** Test on both iOS and Android with the latest Swish app before deploying.

---

## 4. Implementation Plan

### Step 1: Generate QR Code Images

Run the curl commands from Section 2. Saves to:
- `assets/icons/swish-qr-christian.png` (600×600px, ~147KB) — **done**
- `assets/icons/swish-qr-elin.png` (600×600px, ~143KB) — **done**

### Step 2: Update HTML (`index.html`)

**Current state:** Two swish cards in a `.swish-contacts` grid, each with a `.swish-qr-placeholder`.

**Target state:** Keep both cards, replace placeholders with real QR images and add deep-link buttons.

- Replace each `.swish-qr-placeholder` with `<img>` in a `.swish-qr` wrapper
- Add an "Öppna Swish" deep-link button below each card
- Add a `.swish-hint` paragraph below the cards

**Target HTML for each card:**
```html
<div class="swish-card" data-aos="fade-up" data-aos-delay="200">
  <div class="swish-qr">
    <img src="assets/icons/swish-qr-christian.png"
         alt="Swish QR-kod till Christian Boman"
         width="200" height="200" loading="lazy" />
  </div>
  <p class="swish-role">Toastmaster</p>
  <p class="swish-name">Christian Boman</p>
  <p class="swish-number">070 225 91 08</p>
  <a href="swish://payment?data=..." class="swish-button">Öppna Swish</a>
</div>
```

### Step 3: Update CSS (`css/style.css`)

**Remove:**
- `.swish-qr-placeholder` rule

**Add:**
```css
.swish-qr {
  width: 200px;
  height: 200px;
  margin: 0 auto 1rem;
  background: var(--white);
  border-radius: 8px;
  padding: 0.5rem;
  box-shadow: var(--shadow-soft);
}

.swish-qr img {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 4px;
}

.swish-button {
  display: inline-block;
  margin-top: 0.75rem;
  padding: 0.5rem 1.5rem;
  background: var(--sage);
  color: var(--white);
  font-family: var(--font-body);
  font-size: var(--text-sm);
  font-weight: 500;
  border-radius: 24px;
  text-decoration: none;
  transition: background 0.2s ease;
}

.swish-button:hover {
  background: var(--sage-dark);
}

.swish-hint {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  margin-top: 0.5rem;
  font-style: italic;
}
```

**Keep:** `.swish-contacts` grid (still needed for two cards side by side).

**Mobile breakpoint** (`@media max-width: 480px`):
```css
.swish-qr {
  width: 160px;
  height: 160px;
}
```

### Step 4: No JavaScript changes needed

Static image + native `<a>` deep link require zero JavaScript.

---

## 5. Testing Checklist

- [ ] Both QR image files are valid PNGs and display correctly
- [ ] Scan Christian's QR with Swish on iOS → payee and message pre-filled
- [ ] Scan Elin's QR with Swish on iOS → payee and message pre-filled
- [ ] Repeat both on Android
- [ ] Tap "Öppna Swish" for each toastmaster on iOS → Swish app opens with correct data
- [ ] Repeat on Android
- [ ] Desktop: deep link does nothing gracefully (no error popup)
- [ ] Responsive: cards side by side on desktop, stacked on mobile
- [ ] QR sharp on retina displays
- [ ] Text tone is warm and no-pressure

---

## 6. Files Summary

| File | Action | Status |
|------|--------|--------|
| `assets/icons/swish-qr-christian.png` | **Create** — generated via Swish API | Done |
| `assets/icons/swish-qr-elin.png` | **Create** — generated via Swish API | Done |
| `index.html` | **Edit** — gift section (lines 227–263) | Pending |
| `css/style.css` | **Edit** — gift section styles (lines 698–783) | Pending |

---

## 7. References

- [Swish QR Code API (developer.swish.nu)](https://developer.swish.nu/api/qr-codes/v1)
- [Swish QR code design specification v1.7.2 (PDF)](https://assets.ctfassets.net/zrqoyh8r449h/12uwjDy5xcCArc2ZeY5zbU/ce02e0321687bbb2aa5dbf5a50354ced/Guide-Swish-QR-code-design-specification_v1.7.2.pdf)
- [Swish QR format (GitHub)](https://github.com/lindskogen/swish-qr-format)
- [swish-qr Node.js library (GitHub)](https://github.com/gillstrom/swish-qr)
