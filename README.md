# Secure Vendor™ site

Static site for Secure Vendor™ (securevendor.org), the vendor certification in the Secure Broker / Secure Funder family. Same layout system as those sites, with a a purple palette (light purple only in the badge and logo) and the family lime banner. (The repo keeps its original `secure-software-site` name.)

- `site.css`: shared styles; colors are the tokens at the top.
- Pages: `/`, `/how-it-works/`, `/join/`, `/contact/`, `/directory/`. Links are relative, so the site works on github.io and on a custom domain.
- `src/badge.svg`, `src/rings.svg`: sources for the badge and logo. Re-render the PNGs with `node src/render.js '[["src/badge.svg","secure-vendor-badge-2026.png",1254],["src/badge.svg","family-of-brands/secure-vendor-badge.png",240],["src/rings.svg","vendor-rings.png",500]]'`.
- `src/badge-white.svg`: the one-color white badge used in the footer's Family of Brands row. Re-render with `node src/render.js '[["src/badge-white.svg","family-of-brands/secure-vendor-badge.png",240]]'`.
