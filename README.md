# Laaiop website

Statische website voor Laaiop (opruim- en ontruimingsdienst, provincie Antwerpen). Gemaakt door NotchUp.

## Mappen

- `dist/`: de kant-en-klare site voor Vercel (nette URL's, `vercel.json`, sitemap, robots, llms.txt).
- `staging/`: dezelfde site met relatieve links, voor de preview op claude.ai.
- `content.py`: **alle instellingen, placeholders en dienstteksten**. Hier vul je in wat de klant aanlevert.
- `pages.py`: de opbouw en teksten van alle pagina's.
- `build.py`: bouwt de site. `assets/`: css, js, lettertypes, logo's en foto's.

## Wijzigen en opnieuw bouwen

```
python3 build.py            # bouwt dist/  (Vercel)
python3 build.py staging    # bouwt staging/
```

Geen extra pakketten nodig, alleen Python 3.

## Op Vercel zetten

**Optie A, via GitHub (aangeraden):** zet deze map in een GitHub-repository, kies in Vercel *Add New > Project*, importeer de repo en stel in:
- Framework preset: *Other*
- Build command: `python3 build.py`
- Output directory: `dist`

Elke push bouwt dan automatisch een nieuwe versie, met een preview-URL per branch.

**Optie B, zonder GitHub:** installeer de Vercel CLI (`npm i -g vercel`), ga naar de map `dist` en voer `vercel` uit (preview) of `vercel --prod`.

## Voor de lancering

1. Vul in `content.py` alle `PLACEHOLDERS` in (telefoon, prijzen, termijnen, score, adres, btw, verzekering...). Alles wat nog `None` is, staat geel gemarkeerd op de site.
2. Vul `SITE["telefoon_link"]` en `SITE["whatsapp_nummer"]` in, dan werken de bel- en WhatsApp-knoppen.
3. Formulier: zet een endpoint in `SITE["form_endpoint"]` (bv. Formspree, Make, Zapier of een GoHighLevel-webhook). Het formulier stuurt `multipart/form-data` met foto's. Zonder endpoint gaat het formulier gewoon naar `/bedankt/`.
4. Tracking: zet de GTM-container in `SITE["gtm_id"]`. Dat activeert ook de cookiebanner met Google Consent Mode v2. Events in de dataLayer: `klik_whatsapp`, `klik_telefoon`, `formulier_stap_2`, `formulier_stap_3`, `formulier_verzonden`.
5. Zet `SITE["noindex"]` op `False`. Zolang die op `True` staat, blokkeren `robots.txt`, de meta-tag en een `X-Robots-Tag`-header elke indexering (veilig voor een demo-URL).
6. Vervang de stockfoto's door eigen foto's (ploeg, camionette, voor-en-na) en vul de voor-en-na-blokken en de drie Google-reviews in. Gebruik nooit verzonnen reviews.
7. Laat privacybeleid, cookiebeleid en algemene voorwaarden juridisch nakijken.
8. Koppel laaiop.be in Vercel en dien `https://www.laaiop.be/sitemap.xml` in bij Google Search Console.

## SEO en GEO

- Unieke title en meta description per pagina, canonical, Open Graph, sitemap.
- Schema.org: LocalBusiness (met werkgebied en dienstencatalogus), Service per dienst, FAQPage, BreadcrumbList.
- Antwoord-eerst blokken ("In het kort") en FAQ's op elke dienstpagina, zodat AI-zoekmachines (ChatGPT, Perplexity, Google AI Overviews) Laaiop correct kunnen citeren.
- `llms.txt` met een samenvatting van het bedrijf en alle diensten; AI-crawlers zijn expliciet toegelaten in `robots.txt` (na lancering).
- Lettertypes lokaal (WOFF2), foto's in WebP met srcset, geen externe libraries: snel op gsm.
