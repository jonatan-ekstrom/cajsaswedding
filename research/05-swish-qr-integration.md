# Swish QR Code Integration — Research & Implementation Guide

> **Date:** 2026-03-14
> **Status:** Research complete, implementation pending
> **Decision:** Single QR code to Elin Bexell, pre-filled message, with mobile deep-link button

---

## 1. Background

The gift section should let guests contribute money toward the couple's honeymoon via Swish. To preserve anonymity (Cajsa & Filip won't know who gave what), payments go to toastmadame **Elin Bexell (070 392 96 70)** who pools contributions and transfers a lump sum after the wedding.

**Requirements:**
- Single Swish QR code pointing to Elin Bexell
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

### Example: Generate QR for Elin Bexell

```bash
curl -X POST https://mpc.getswish.net/qrg-swish/api/v1/prefilled \
  -H "Content-Type: application/json" \
  -d '{
    "format": "png",
    "size": 600,
    "payee": {
      "value": "0703929670",
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

**Example string for our use case:**
```
C0703929670;1;Bröllopsgåva Cajsa & Filip;6
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

### JSON Payload

```json
{
  "version": 1,
  "payee": {
    "value": "0703929670",
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

### Full URL-Encoded Link

```
swish://payment?data=%7B%22version%22%3A1%2C%22payee%22%3A%7B%22value%22%3A%220703929670%22%2C%22editable%22%3Afalse%7D%2C%22amount%22%3A%7B%22value%22%3A1%2C%22editable%22%3Atrue%7D%2C%22message%22%3A%7B%22value%22%3A%22Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip%22%2C%22editable%22%3Atrue%7D%7D
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
swish://payment?payee=0703929670&message=Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip
```

**Important:** Test on both iOS and Android with the latest Swish app before deploying.

---

## 4. Implementation Plan

### Step 1: Generate the QR Code Image

Run the curl command from Section 2. Save to `assets/icons/swish-qr-elin.png`. Verify the image opens correctly and scans with the Swish app.

### Step 2: Update HTML (`index.html`)

**Current state** (lines 222–247): Two swish cards in a `.swish-contacts` grid, each with a `.swish-qr-placeholder`.

**Target state:** Single centered card with real QR image and deep-link button.

- Remove Christian Boman's card
- Remove the `.swish-contacts` grid wrapper
- Replace `.swish-qr-placeholder` with `<img>` in a `.swish-qr` wrapper
- Add `<a class="swish-button">Öppna Swish</a>` with the deep link href
- Add a `.swish-hint` paragraph: "Skanna QR-koden eller tryck på knappen för att öppna Swish direkt."
- Update `.gift-instruction` text from "någon av våra toastmasters" → "vår toastmadame"

**Target HTML:**
```html
<div class="gift-card" data-aos="fade-up" data-aos-delay="100">
  <p class="gift-message">Den största gåvan ni kan ge oss är er närvaro på vår stora dag.
    Om ni ändå önskar ge en bröllopsgåva uppskattar vi ett bidrag till vår bröllopsresa.</p>

  <p class="gift-instruction">Swisha valfritt belopp till vår toastmadame nedan —
    hon samlar ihop alla bidrag och ger dem till oss efter bröllopet,
    så vi aldrig vet vem som gett vad.</p>

  <p class="gift-note">Helt frivilligt — er närvaro är det viktigaste!</p>

  <div class="swish-card" data-aos="fade-up" data-aos-delay="200">
    <div class="swish-qr">
      <img src="assets/icons/swish-qr-elin.png"
           alt="Swish QR-kod till Elin Bexell"
           width="200" height="200" loading="lazy" />
    </div>
    <p class="swish-role">Toastmadame</p>
    <p class="swish-name">Elin Bexell</p>
    <p class="swish-number">070 392 96 70</p>
    <a href="swish://payment?data=..." class="swish-button">Öppna Swish</a>
    <p class="swish-hint">Skanna QR-koden eller tryck på knappen för att öppna Swish direkt.</p>
  </div>
</div>
```

### Step 3: Update CSS (`css/style.css`)

**Remove:**
- `.swish-qr-placeholder` rule
- `.swish-contacts` grid rule

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

**Modify:** `.swish-card` — center as a standalone block (remove grid assumptions).

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

- [ ] QR image file is valid PNG and displays correctly
- [ ] Scan QR with Swish on iOS → payee "Elin Bexell" and message pre-filled
- [ ] Scan QR with Swish on Android → same verification
- [ ] Tap "Öppna Swish" on iOS → Swish app opens with correct data
- [ ] Tap "Öppna Swish" on Android → same verification
- [ ] Desktop: deep link does nothing gracefully (no error popup)
- [ ] Responsive: card centered on mobile (320px–480px)
- [ ] Responsive: card centered on tablet/desktop
- [ ] QR sharp on retina displays
- [ ] Text tone is warm and no-pressure

---

## 6. Files Summary

| File | Action |
|------|--------|
| `assets/icons/swish-qr-elin.png` | **Create** — generated via Swish API |
| `index.html` | **Edit** — gift section (lines 222–247) |
| `css/style.css` | **Edit** — gift section styles (lines 690–776) |

---

## 7. References

- [Swish QR Code API (developer.swish.nu)](https://developer.swish.nu/api/qr-codes/v1)
- [Swish QR code design specification v1.7.2 (PDF)](https://assets.ctfassets.net/zrqoyh8r449h/12uwjDy5xcCArc2ZeY5zbU/ce02e0321687bbb2aa5dbf5a50354ced/Guide-Swish-QR-code-design-specification_v1.7.2.pdf)
- [Swish QR format (GitHub)](https://github.com/lindskogen/swish-qr-format)
- [swish-qr Node.js library (GitHub)](https://github.com/gillstrom/swish-qr)
