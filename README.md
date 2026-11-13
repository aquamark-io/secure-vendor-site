# Secure Vendor™ site

Static site for Secure Vendor™ (securevendor.org), the vendor certification in the Secure Broker / Secure Funder family. Same layout system as those sites, with a purple palette matched to the badge.

- `site.css`: shared styles; colors are the tokens at the top.
- Pages: `/`, `/program-guidelines/` (Program Requirements), `/join/`, `/contact/`, `/directory/`. `/how-it-works/` redirects to Program Requirements. Links are relative, so the site works on github.io and on a custom domain.
- `vendor-badge.png`: the official full-color badge (shown in the hero).
- `family-of-brands/secure-vendor-badge.png`: white version for the footer, generated from it with `python3 src/make-white-badge.py vendor-badge.png family-of-brands/secure-vendor-badge.png`.
- `src/rings.svg`: source for the logo rings. Re-render with `node src/render.js '[["src/rings.svg","vendor-rings.png",500]]'`.
