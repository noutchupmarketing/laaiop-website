# Laaiop-website publiceren op Vercel met Claude Code

Kopieer alles onder "Opdracht voor Claude Code" en plak het in Claude Code, in de map waar je `laaiop-website.zip` hebt uitgepakt (de map `laaiop-site`).

---

## Opdracht voor Claude Code

Publiceer deze statische website op Vercel als demo voor de klant.

**Over het project**
- Map `laaiop-site`: statische HTML-site voor Laaiop (opruimdienst, provincie Antwerpen). Geen framework, geen npm-afhankelijkheden.
- `python3 build.py` bouwt de site in `dist/`. Alleen Python 3 nodig, geen extra pakketten.
- `dist/` is de map die online moet. Daarin staat al een `vercel.json` (cleanUrls, trailingSlash, cache-headers en een `X-Robots-Tag: noindex` zolang het een demo is).
- De map `staging/` en `__pycache__/` horen niet online.

**Stappen**
1. Controleer of `python3` en `node`/`npm` beschikbaar zijn. Installeer de Vercel CLI als die ontbreekt: `npm i -g vercel`.
2. Bouw de site opnieuw: `cd laaiop-site && python3 build.py`. Controleer dat `dist/index.html`, `dist/vercel.json`, `dist/sitemap.xml` en 25 pagina's bestaan.
3. Log in bij Vercel als dat nog niet zo is: `vercel login` (laat mij de login in de browser bevestigen).
4. Ga naar `laaiop-site/dist` en koppel een nieuw project: `vercel link --yes --project laaiop`. Kies mijn eigen account of team als daarom gevraagd wordt; vraag het mij als er meerdere teams zijn.
5. Publiceer: `vercel deploy --prod --yes` vanuit `laaiop-site/dist`.
6. Test de live URL:
   - `/`, `/diensten/`, `/garage-zolder-kelder-opruimen/`, `/prijzen/`, `/richtprijs/`, `/bedankt/` geven status 200;
   - een onbestaande URL toont de eigen 404-pagina;
   - `/assets/css/site.css` en `/assets/js/site.js` laden;
   - de response bevat de header `X-Robots-Tag: noindex, nofollow`.
7. Geef mij de productie-URL (bv. `laaiop.vercel.app`) en een korte samenvatting.

**Belangrijk**
- Verander niets aan de inhoud van de site. Alleen bouwen en publiceren.
- Zet `SITE["noindex"]` in `content.py` NIET op `False`; de site blijft een demo tot de klant alles heeft aangeleverd.
- Koppel nog geen eigen domein.

---

## Later: automatisch publiceren via GitHub (optioneel)

Wil je dat elke wijziging automatisch online komt, vraag Claude Code dan:

> Zet de map `laaiop-site` in een nieuwe private GitHub-repository `laaiop-website` (zonder `staging/` en `__pycache__/`, voeg een `.gitignore` toe). Koppel die repo aan het Vercel-project `laaiop` met Root Directory leeg, Framework Preset "Other", Build Command `python3 build.py` en Output Directory `dist`. Controleer na de eerste automatische build dat de site werkt.

## Bij lancering (pas als de klant alles heeft aangeleverd)

1. Placeholders invullen in `content.py` (zie README.md, "Voor de lancering").
2. `SITE["noindex"] = False` en `SITE["form_endpoint"]` en `SITE["gtm_id"]` invullen.
3. Opnieuw bouwen en publiceren, daarna in Vercel het domein `laaiop.be` en `www.laaiop.be` koppelen en de DNS-records instellen die Vercel toont.
4. `https://www.laaiop.be/sitemap.xml` indienen bij Google Search Console.
