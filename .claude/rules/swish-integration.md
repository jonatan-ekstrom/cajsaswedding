---
globs: ["index.html", "js/**"]
---

# Swish Integration Reference

## Swish Deep Link Format

```
swish://payment?data=<URL-encoded JSON>
```

### JSON Payload

```json
{
  "version": 1,
  "payee": { "value": "<phone_no_spaces>", "editable": false },
  "amount": { "value": 1, "editable": true },
  "message": { "value": "Bröllopsgåva Cajsa & Filip", "editable": true }
}
```

### Full Encoded URLs

**Christian Boman (0702259108):**
```
swish://payment?data=%7B%22version%22%3A%201%2C%20%22payee%22%3A%20%7B%22value%22%3A%20%220702259108%22%2C%20%22editable%22%3A%20false%7D%2C%20%22amount%22%3A%20%7B%22value%22%3A%201%2C%20%22editable%22%3A%20true%7D%2C%20%22message%22%3A%20%7B%22value%22%3A%20%22Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip%22%2C%20%22editable%22%3A%20true%7D%7D
```

**Elin Bexell (0703929670):**
```
swish://payment?data=%7B%22version%22%3A%201%2C%20%22payee%22%3A%20%7B%22value%22%3A%20%220703929670%22%2C%20%22editable%22%3A%20false%7D%2C%20%22amount%22%3A%20%7B%22value%22%3A%201%2C%20%22editable%22%3A%20true%7D%2C%20%22message%22%3A%20%7B%22value%22%3A%20%22Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip%22%2C%20%22editable%22%3A%20true%7D%7D
```

### Alternative Simpler Format (if JSON deep link doesn't work)

```
swish://payment?payee=0702259108&message=Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip
swish://payment?payee=0703929670&message=Br%C3%B6llopsg%C3%A5va%20Cajsa%20%26%20Filip
```

## Deep Link Behavior

| Platform | Result |
|----------|--------|
| iOS with Swish installed | Opens Swish app with fields pre-filled |
| Android with Swish installed | Opens Swish app with fields pre-filled |
| Desktop browser | Link does nothing (no handler) — QR code is the primary path |
| Mobile without Swish | May show "can't open" prompt — acceptable edge case |

## QR Code API (for regeneration)

```
POST https://mpc.getswish.net/qrg-swish/api/v1/prefilled
Content-Type: application/json
```

No authentication required. Returns binary image.

```json
{
  "format": "png",
  "size": 600,
  "payee": { "value": "0702259108", "editable": false },
  "amount": { "value": 1, "editable": true },
  "message": { "value": "Bröllopsgåva Cajsa & Filip", "editable": true }
}
```

Phone number format: `07XXXXXXXX` (national, no spaces, no country code).

## QR Format String (client-side fallback)

```
C<number>;<amount>;<message>;<editable_flags>
```

Editable flags: 0=all locked, 1=phone, 2=amount, 4=message (sum for combinations).

```
C0702259108;1;Bröllopsgåva Cajsa & Filip;6   # Christian (amount+message editable)
C0703929670;1;Bröllopsgåva Cajsa & Filip;6   # Elin (amount+message editable)
```
