# secure-software-site

Static site for Secure Software™ (securesoftware.org), the software certification in the Secure Broker / Secure Funder family. Same layout system as those sites, with an orange palette.

- `site.css`: shared styles; colors are the tokens at the top.
- Pages: `/`, `/how-it-works/`, `/join/`, `/contact/`, `/directory/`.
- `src/badge.svg`, `src/rings.svg`: sources for the badge and logo. Re-render the PNGs with `node src/render.js '[["src/badge.svg","secure-software-badge-2026.png",1254],["src/badge.svg","family-of-brands/secure-software-badge.png",240],["src/rings.svg","orange-rings.png",500]]'`.
