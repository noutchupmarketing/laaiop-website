# -*- coding: utf-8 -*-
"""
Bouwt de Laaiop-website als statische HTML.

    python3 build.py            -> dist/     (productie / Vercel, nette URL's)
    python3 build.py staging    -> staging/  (relatieve links, voor de preview)

Teksten en placeholders staan in content.py.
"""
import json, os, re, shutil, sys, html, hashlib
# Zet op True zodra er echte voor-en-na-foto's zijn: dan komt het blok terug op de home.
VOOR_NA_KLAAR = False
REVIEWS_KLAAR = False  # True zodra er echte Google-reviews en een score zijn: toont de reviewsectie en de score
from content import SITE, PLACEHOLDERS, WERKGEBIED, DIENSTEN, FORM_DIENSTEN, SLUG_NAAR_FORM, FAQ_ALGEMEEN, INBEGREPEN

MODE = sys.argv[1] if len(sys.argv) > 1 else "prod"
OUT = "staging" if MODE == "staging" else "dist"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(ROOT, OUT)
D = {d["slug"]: d for d in DIENSTEN}

# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)

def ph(text):
    """Vervang {{SLEUTEL}} door de ingevulde waarde of een gemarkeerde placeholder."""
    def r(m):
        k = m.group(1)
        v = PLACEHOLDERS.get(k)
        if v:
            return esc(v)
        return '<mark class="ph">[%s]</mark>' % k.replace("_", " ")
    return re.sub(r"\{\{([A-Z_]+)\}\}", r, text)

def ph_plat(text):
    """Placeholders in attributen en JSON: waarde of [SLEUTEL] zonder opmaak."""
    return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: PLACEHOLDERS.get(m.group(1)) or "[%s]" % m.group(1).replace("_", " "), text)

def wa_link(tekst="Hallo Laaiop, ik wil graag een prijs."):
    from urllib.parse import quote
    nr = SITE.get("whatsapp_nummer")
    return ("https://wa.me/%s?text=%s" % (nr, quote(tekst))) if nr else ("https://wa.me/?text=%s" % quote(tekst))

def tel_link():
    return ("tel:" + SITE["telefoon_link"]) if SITE.get("telefoon_link") else "/richtprijs/#contact"

def tel_tekst():
    return ph("{{TELEFOON}}")

# ---------------------------------------------------------------- iconen (24px, lijn)
P = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
ICONEN = {
    "huis": '<path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
    "doos": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5"/><path d="M12 12v9"/><path d="m7.5 5.2 9 4.6"/>',
    "appartement": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h1.5M13.5 7H15M9 11h1.5M13.5 11H15M9 15h1.5M13.5 15H15"/><path d="M10.5 21v-3h3v3"/>',
    "garage": '<path d="M3 10 12 4l9 6v10H3z"/><path d="M7 20v-7h10v7"/><path d="M7 16h10"/>',
    "winkel": '<path d="M4 9h16l-1.5-5h-13z"/><path d="M5 9v11h14V9"/><path d="M10 20v-5h4v5"/><path d="M4 9a2.7 2.7 0 0 0 5.3 0 2.7 2.7 0 0 0 5.4 0 2.7 2.7 0 0 0 5.3 0"/>',
    "zetel": '<path d="M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3"/><path d="M3 13a2 2 0 0 1 4 0v2h10v-2a2 2 0 0 1 4 0v5H3z"/><path d="M5 18v2M19 18v2"/>',
    "blad": '<path d="M5 20c0-8.5 5.5-15 15-15 0 9.5-6.5 15-15 15z"/><path d="M5 20 13 12"/>',
    "bakstenen": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 9.7h18M3 14.3h18M9 5v4.7M15 5v4.7M6 9.7v4.6M12 9.7v4.6M18 9.7v4.6M9 14.3V19M15 14.3V19"/>',
    "koelkast": '<rect x="6" y="2.5" width="12" height="19" rx="2"/><path d="M6 10h12M9 5.5v2M9 13v3"/>',
    "dampkap": '<path d="M9.5 3h5v6l6 5h-17l6-5z"/><path d="M3.5 14v2h17v-2"/><path d="M8 19.5c.6-.8.6-1.7 0-2.5M12 19.5c.6-.8.6-1.7 0-2.5M16 19.5c.6-.8.6-1.7 0-2.5"/>',
    "camera": '<path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13.5" r="3.5"/>',
    "euro": '<path d="M17.5 6.5A7 7 0 1 0 17.5 17.5"/><path d="M4 10.5h9M4 13.5h9"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12.5 3 3 5-6"/>',
    "schild": '<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6z"/><path d="m9 12 2 2 4-4.5"/>',
    "bezem": '<path d="M14 3 9.5 12"/><path d="M6 12h7l2 9H4z"/><path d="M8 16v5M11 16v5"/>',
    "kringloop": '<path d="M4 12a8 8 0 0 1 13.66-5.66L20 8.5"/><path d="M20 3.5v5h-5"/><path d="M20 12a8 8 0 0 1-13.66 5.66L4 15.5"/><path d="M4 20.5v-5h5"/>',
    "hart": '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.3 4.3 4.3 0 0 1 19.5 10C19.5 15.4 12 20 12 20z"/>',
    "klok": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "telefoon": '<path d="M6.5 3h3l1.5 4.5-2 1.5a11 11 0 0 0 6 6l1.5-2L21 14.5v3A2.5 2.5 0 0 1 18.5 20C10.5 20 4 13.5 4 5.5A2.5 2.5 0 0 1 6.5 3z"/>',
    "chat": '<path d="M4 18.5 5.3 15A7.5 7.5 0 1 1 8.6 18z"/><path d="M8.5 9.5c.5 2.5 2.5 4.5 5 5l1-1.5 2 .8"/>',
    "pin": '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "ster": '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8-4.3-4.1 5.9-.9z" fill="currentColor" stroke="none"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "sluit": '<path d="M6 6l12 12M18 6 6 18"/>',
    "upload": '<path d="M12 16V4"/><path d="m7 9 5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
    "foto": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="m21 16-5-5-8 8"/>',
    "metaal": '<path d="M4 15h16l-2-6H6z"/><path d="M8 9V6h8v3"/><path d="M4 15v3h16v-3"/>',
    "stekker": '<path d="M9 3v5M15 3v5"/><path d="M6 8h12v3a6 6 0 0 1-12 0z"/><path d="M12 17v4"/>',
    "vuilzak": '<path d="M8 6c1-2 7-2 8 0"/><path d="M7 7h10l1.5 12a2 2 0 0 1-2 2h-9a2 2 0 0 1-2-2z"/>',
    "route": '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
    "winkelkar": '<path d="M3 4h2.5l2.2 10.5h10.6L20.5 7H7"/><circle cx="9.5" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
    "trap": '<path d="M3 20h5v-4h4v-4h4V8h5"/>',
    "afstand": '<path d="M3 12h18"/><path d="m7 8-4 4 4 4M17 8l4 4-4 4"/>',
    "gebouw": '<path d="M4 21V6l8-3v18"/><path d="M12 8h8v13"/><path d="M7 8h2M7 12h2M7 16h2M15 12h2M15 16h2"/>',
    "kalender": '<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    "document": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
}
def icoon(naam, cls=""):
    return '<svg viewBox="0 0 24 24" %s aria-hidden="true"%s>%s</svg>' % (P, (' class="%s"' % cls) if cls else "", ICONEN[naam])

def sterren():
    return '<div class="sterren" aria-hidden="true">' + "".join(icoon("ster") for _ in range(5)) + "</div>"

# ---------------------------------------------------------------- foto's
def img(naam, alt, breed=False, eager=False, cls="", sizes="(min-width: 900px) 50vw, 100vw"):
    if breed:
        return ('<img src="/assets/foto/%s-breed.webp" width="1440" height="737" alt="%s" %s decoding="async"%s>'
                % (naam, esc(alt), 'fetchpriority="high"' if eager else 'loading="lazy"', (' class="%s"' % cls) if cls else ""))
    return ('<img src="/assets/foto/%s.webp" srcset="/assets/foto/%s-640.webp 640w, /assets/foto/%s.webp 1040w" sizes="%s" width="1040" height="780" alt="%s" %s decoding="async"%s>'
            % (naam, naam, naam, sizes, esc(alt), 'fetchpriority="high"' if eager else 'loading="lazy"', (' class="%s"' % cls) if cls else ""))

def foto(naam, alt, caption, cls=""):
    return '<figure class="foto %s"><div class="fotokader">%s</div><figcaption>%s</figcaption></figure>' % (cls, img(naam, alt), caption)

def foto_placeholder(tekst, caption, cls=""):
    return ('<figure class="foto"><div class="foto__kader %s"><span>%s%s</span></div><figcaption>%s</figcaption></figure>'
            % (cls, icoon("foto"), tekst, caption))

def voor_na(titel, caption):
    return ('<figure class="foto"><div class="voorna">'
            '<div class="foto__kader" style="position:relative"><span class="voorna__tag">Voor</span><span>%s Eigen foto: voor</span></div>'
            '<div class="foto__kader" style="position:relative"><span class="voorna__tag voorna__tag--na">Na</span><span>%s Eigen foto: na</span></div>'
            '</div><figcaption><strong>%s</strong> %s</figcaption></figure>') % (icoon("foto"), icoon("foto"), titel, caption)

# ---------------------------------------------------------------- vaste blokken
# Realisaties komt terug in het menu zodra VOOR_NA_KLAAR op True staat
NAV = [("Diensten", "/diensten/"), ("Prijs en offerte", "/prijzen/"), ("Werkwijze", "/werkwijze/")] + ([("Realisaties", "/realisaties/")] if VOOR_NA_KLAAR else []) + [("Over ons", "/over-ons/"), ("Contact", "/richtprijs/")]
DIENST_GROEPEN = [("Ontruimen", ["huis-leegmaken-na-overlijden", "inboedel-opruimen", "appartement-leegmaken", "garage-zolder-kelder-opruimen", "kantoor-winkelpand-leegmaken"]),
                  ("Ophalen", ["grofvuil-ophalen", "groenafval-ophalen", "bouwafval-ophalen"]),
                  ("Leveren en extra", ["meubels-toestellen-leveren", "dampkap-afbreken-reinigen"])]

# Context per paginatype: header-CTA en de twee knoppen van de mobiele actiebalk
CONTEXT = {
    "standaard":    {"cta": ("Vraag je prijs aan", "/richtprijs/"), "balk": [("wa", "WhatsApp een foto"), ("tel", "Bellen")]},
    "plaatsbezoek": {"cta": ("Plan een plaatsbezoek", "#prijs-aanvragen"), "balk": [("tel", "Bellen"), ("anker", "Plaatsbezoek")]},
    "offerte":      {"cta": ("Vraag een offerte", "#prijs-aanvragen"), "balk": [("tel", "Bellen"), ("anker", "Offerte aanvragen")]},
    "richtprijs":   {"cta": ("Naar het formulier", "#formulier"), "balk": [("wa", "WhatsApp een foto"), ("tel", "Bellen")]},
    "bedankt":      {"cta": ("Terug naar home", "/"), "balk": [("wa", "Extra foto's via WhatsApp"), ("tel", "Bellen")]},
}

def dienst_dropdown():
    kol = "".join('<div><p class="dropdown__kop">%s</p><ul>%s</ul></div>' % (g, "".join(
        '<li><a href="/%s/">%s<span>%s</span></a></li>' % (s, icoon(D[s]["icoon"]), D[s]["naam"]) for s in slugs)) for g, slugs in DIENST_GROEPEN)
    return f"""<div class="dropdown" id="dienstenmenu" hidden>
  <div class="dropdown__in">{kol}</div>
  <div class="dropdown__voet"><a class="tekstlink" href="/diensten/">Alle diensten bekijken</a><a class="knop knop--primair knop--klein" href="/richtprijs/">Vraag je prijs aan</a></div>
</div>"""

def header(actief, ctx="standaard"):
    c = CONTEXT[ctx]
    items = ""
    for t, u in NAV:
        huidig = ' aria-current="page"' if actief == u else ""
        if t == "Diensten":
            items += f'<li class="nav__diensten"><button class="nav__knop" type="button" aria-expanded="false" aria-controls="dienstenmenu" data-dropdown{huidig}>Diensten<svg viewBox="0 0 24 24" {P} aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></button>{dienst_dropdown()}</li>'
        else:
            items += f'<li><a href="{u}"{huidig}>{t}</a></li>'
    mob_diensten = "".join('<li><a href="/%s/">%s</a></li>' % (d["slug"], d["naam"]) for d in DIENSTEN)
    mob = (f'<li><details class="mobielmenu__groep"><summary>Diensten</summary><ul>{mob_diensten}<li><a href="/diensten/">Alle diensten</a></li></ul></details></li>'
           + "".join('<li><a href="%s">%s</a></li>' % (u, t) for t, u in NAV[1:] + [("Voor professionals", "/voor-professionals/"), ("Werkgebied", "/werkgebied/"), ("Veelgestelde vragen", "/veelgestelde-vragen/")]))
    return f"""<a class="skiplink" href="#inhoud">Naar de inhoud</a>
<header class="header">
  <div class="wrap header__in">
    <a class="header__logo" href="/" aria-label="Laaiop, naar de homepagina"><img src="/assets/img/logo-positief.webp" width="400" height="118" alt="Laaiop"></a>
    <nav class="nav" aria-label="Hoofdmenu"><ul>{items}</ul></nav>
    <div class="header__acties">
      <a class="header__tel" href="{tel_link()}" data-track="klik_telefoon" data-locatie="header">{icoon("telefoon")}{tel_tekst()}</a>
      <a class="knop knop--primair knop--klein header__cta" href="{c["cta"][1]}">{c["cta"][0]}</a>
      <button class="menuknop" type="button" data-menu-open aria-controls="mobielmenu" aria-expanded="false">{icoon("menu")}Menu</button>
    </div>
  </div>
</header>
<div class="mobielmenu" id="mobielmenu" hidden role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobielmenu__top"><a href="/" aria-label="Laaiop, naar de homepagina"><img src="/assets/img/logo-negatief.webp" width="400" height="118" alt="Laaiop"></a><button class="menuknop" type="button" data-menu-sluit>{icoon("sluit")}Sluit</button></div>
  <nav aria-label="Mobiel menu"><ul>{mob}</ul></nav>
  <div class="knoppen"><a class="knop knop--primair" href="/richtprijs/">Vraag je prijs aan</a><a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="menu" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a><a class="knop knop--rand" href="{tel_link()}" data-track="klik_telefoon" data-locatie="menu">{icoon("telefoon")}Bel {tel_tekst()}</a></div>
</div>"""

def actiebalk(ctx="standaard"):
    knoppen = []
    for i, (soort, label) in enumerate(CONTEXT[ctx]["balk"]):
        stijl = "knop--primair" if i == 0 else "knop--donker"
        if soort == "wa":
            knoppen.append(f'<a class="knop {stijl}" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="actiebalk" target="_blank" rel="noopener">{icoon("chat")}{label}</a>')
        elif soort == "tel":
            knoppen.append(f'<a class="knop {stijl}" href="{tel_link()}" data-track="klik_telefoon" data-locatie="actiebalk">{icoon("telefoon")}{label}</a>')
        else:
            knoppen.append(f'<a class="knop {stijl}" href="#prijs-aanvragen">{icoon("kalender")}{label}</a>')
    return '<div class="actiebalk" aria-label="Snel contact">' + "".join(knoppen) + "</div>"

def footer(formeel=False, ctx="standaard"):
    diensten = "".join('<li><a href="/%s/">%s</a></li>' % (d["slug"], d["naam"]) for d in DIENSTEN)
    belofte = ('<p class="footer__belofte">Wij maken uw pand leeg en laten het proper achter.</p>' if formeel
               else '<p class="footer__belofte">Wij laden op. <span>Jij ademt op.</span></p>')
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__in">
      <div class="footer__merk">
        <img src="/assets/img/logo-negatief.webp" width="400" height="118" alt="Laaiop" loading="lazy">
        {belofte}
        <p>Laaiop is een opruim- en ontruimingsdienst uit de provincie Antwerpen. We maken woningen, appartementen, garages, zolders, kantoren en winkelpanden leeg. We halen groen- en bouwafval op. We leveren ook nieuwe meubels en toestellen. Altijd met een prijs vooraf en netjes opgeleverd.</p>
      </div>
      <div class="footer__contact" id="contact-footer"><h2>Contact</h2><ul>
        <li><a href="{tel_link()}" data-track="klik_telefoon" data-locatie="footer">{icoon("telefoon")}{tel_tekst()}</a></li>
        <li><a href="{wa_link()}" data-track="klik_whatsapp" data-locatie="footer" target="_blank" rel="noopener">{icoon("chat")}WhatsApp: stuur een foto</a></li>
        <li><a href="mailto:{SITE["email"]}">{icoon("document")}{SITE["email"]}</a></li>
        <li>Btw {ph("{{BTW}}")}</li>
      </ul><a class="knop knop--primair knop--klein" href="{(CONTEXT[ctx]["cta"][1] if ctx in ("plaatsbezoek", "offerte") else "/richtprijs/")}">{(CONTEXT[ctx]["cta"][0] if ctx in ("plaatsbezoek", "offerte") else "Vraag je prijs aan")}</a></div>
      <details class="footer__groep" open><summary><h2>Diensten</h2></summary><ul>{diensten}</ul></details>
      <details class="footer__groep" open><summary><h2>Laaiop</h2></summary><ul>
        <li><a href="/prijzen/">Prijs en offerte</a></li><li><a href="/werkwijze/">Werkwijze</a></li>{'<li><a href="/realisaties/">Realisaties</a></li>' if VOOR_NA_KLAAR else ""}
        <li><a href="/over-ons/">Over ons</a></li><li><a href="/voor-professionals/">Voor professionals</a></li><li><a href="/werkgebied/">Werkgebied</a></li>
        <li><a href="/veelgestelde-vragen/">Veelgestelde vragen</a></li></ul></details>
    </div>
    <div class="footer__onder">
      <p>&copy; 2026 Laaiop. Werkgebied: provincie Antwerpen.</p>
      <ul><li><a href="/privacybeleid/">Privacybeleid</a></li><li><a href="/cookiebeleid/">Cookiebeleid</a></li><li><a href="/algemene-voorwaarden/">Algemene voorwaarden</a></li></ul>
    </div>
    <p class="voet__woord" aria-hidden="true">{"".join('<span%s style="--l:%d">%s</span>' % (' class="voet__op"' if i > 3 else "", i, c) for i, c in enumerate("Laaiop"))}</p>
  </div>
</footer>
{actiebalk(ctx)}
<div class="cookie" id="cookie" hidden role="dialog" aria-label="Cookies">
  <p><strong>Cookies op laaiop.be.</strong> We gebruiken analytische cookies en advertentiecookies om te meten welke advertenties werken. Meer in ons <a href="/cookiebeleid/">cookiebeleid</a>.</p>
  <div class="knoppen"><button class="knop knop--primair knop--klein" type="button" data-cookie="ja">Alles aanvaarden</button><button class="knop knop--rand knop--klein" type="button" data-cookie="nee">Enkel noodzakelijke</button></div>
</div>"""

def vertrouwen(donker=True):
    google = f'<li>{icoon("ster")}<span><strong>{ph("{{SCORE}}")}</strong> op Google</span></li>' if REVIEWS_KLAAR else ""
    return f"""<ul class="vertrouwen">
  {google}
  <li>{icoon("euro")}<span>Offerte vooraf bevestigd</span></li>
  <li>{icoon("schild")}<span>Verzekerd</span></li>
  <li>{icoon("bezem")}<span>Proper achtergelaten</span></li>
</ul>"""

def regio_label():
    return f'<span class="eyebrow eyebrow--regio">{icoon("pin")}Provincie Antwerpen</span>'

def keuzes_diensten(vooraf=None):
    return "".join('<label class="keuze"><input type="radio" name="dienst" value="%s" required%s><span>%s</span></label>' % (v, " checked" if v == vooraf else "", l) for v, l in FORM_DIENSTEN)

def datalist():
    gem = sorted({g for _, lijst in WERKGEBIED for g in lijst})
    return '<datalist id="gemeenten">' + "".join('<option value="%s"></option>' % g for g in gem) + "</datalist>"

def upload_veld(id_):
    return f"""<div class="veld"><label for="{id_}">Foto's <span class="hint">(niet verplicht, met duidelijke foto's krijg je een betere offerte)</span></label>
  <div class="upload">{icoon("camera")}<strong><span class="alleen-mobiel">Kies foto's of neem er een</span><span class="alleen-desktop">Kies of sleep foto's hierheen</span></strong><span data-teller>Tot 10 foto's</span>
  <input id="{id_}" name="fotos" type="file" accept="image/*" multiple></div>
  <div class="voorbeelden" aria-live="polite"></div>
  <button class="upload__wis" type="button" data-wis-fotos hidden>Foto's wissen</button></div>"""

FORM_ICOON = {"woning": "huis", "inboedel": "doos", "garage": "garage", "kantoor": "winkel", "losse-stukken": "zetel",
              "groenafval": "blad", "bouwafval": "bakstenen", "levering": "koelkast", "dampkap": "dampkap", "anders": "chat"}

def contactformulier(id_="kort", vooraf=None):
    """Het enige contactformulier van de site, in drie stappen. Overal identiek; op een dienstpagina staat de dienst al aangeduid."""
    tegels = "".join('<label class="keuze keuze--tegel"><input type="radio" name="dienst" value="%s" required%s><span>%s%s</span></label>'
                     % (v, " checked" if v == vooraf else "", icoon(FORM_ICOON[v]), l) for v, l in FORM_DIENSTEN + [("anders", "Iets anders")])
    return f"""<form class="formulier formulier--stappen" data-richtprijs="contact" data-bedankt="/bedankt/" novalidate enctype="multipart/form-data">
  <input type="hidden" name="formulier" value="contact">
  <div class="formulier__kop">
    <div class="voortgang" aria-hidden="true"><span data-voortgang></span></div>
    <p class="formulier__status" data-stap-tekst aria-live="polite">Stap 1 van 3</p>
  </div>
  <div data-stap>
    <fieldset class="veld"><legend class="formulier__vraag">Waarmee kunnen we helpen?</legend><div class="keuzes keuzes--tegels">{tegels}</div></fieldset>
    <div class="formulier__voet"><button class="knop knop--primair" type="button" data-volgende>Volgende</button></div>
  </div>
  <div data-stap hidden>
    <p class="formulier__vraag">Vertel ons iets meer</p>
    <div class="veld"><label for="{id_}-gemeente">Gemeente</label><input id="{id_}-gemeente" name="gemeente" list="gemeenten" autocomplete="address-level2" required></div>
    <div class="veld"><label for="{id_}-bericht">Bericht <span class="hint">(niet verplicht)</span></label><textarea id="{id_}-bericht" name="bericht" rows="3" placeholder="Bv. wat er weg moet, verdieping en lift, gewenste periode"></textarea></div>
    {upload_veld(id_ + "-fotos")}
    <div class="formulier__voet"><button class="knop knop--tekst" type="button" data-vorige>Terug</button><button class="knop knop--primair" type="button" data-volgende>Volgende</button></div>
  </div>
  <div data-stap hidden>
    <p class="formulier__vraag">Hoe kunnen we je bereiken?</p>
    <div class="veld"><label for="{id_}-naam">Naam</label><input id="{id_}-naam" name="naam" autocomplete="name" required></div>
    <div class="veld"><label for="{id_}-tel">Telefoon</label><input id="{id_}-tel" name="telefoon" type="tel" autocomplete="tel" inputmode="tel" required></div>
    <div class="veld"><label for="{id_}-email">E-mail <span class="hint">(niet verplicht)</span></label><input id="{id_}-email" name="email" type="email" autocomplete="email"></div>
    <div class="formulier__voet"><button class="knop knop--tekst" type="button" data-vorige>Terug</button><button class="knop knop--primair" type="submit">Verstuur aanvraag</button></div>
    <p class="privacy">Deze gegevens gebruiken we alleen om je aanvraag te beantwoorden. Zie ons <a href="/privacybeleid/">privacybeleid</a>.</p>
  </div>
</form>"""

def prijsblok(titel="Wat kost het?", tekst="Stuur ons een paar duidelijke foto's. Je krijgt snel een voorlopige offerte. Die bevestigen we nadat we langs zijn geweest, zonder verrassingen achteraf.", vooraf=None, u=False, variant="standaard"):
    bel = "Bel ons" if u else "Bel"
    return f"""<section class="sectie" id="prijs-aanvragen" aria-labelledby="prijsblok-titel">
  <div class="wrap"><div class="prijsblok donker">
    <div class="prijsblok__tekst">
      <span class="eyebrow">Contact</span>
      <h2 id="prijsblok-titel">{titel}</h2>
      <p>{tekst}</p>
      <ul class="vinkjes">
        <li><span>Voorlopige offerte, meestal binnen {ph("{{TERMIJN}}")}</span></li>
        <li><span>Laden, transport, afvoer en opkuis inbegrepen</span></li>
        <li><span>Bevestigd nadat we langs zijn geweest</span></li>
      </ul>
      <div class="prijsblok__contact">
        <p class="of">Liever meteen contact?</p>
        <div class="knoppen"><a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="prijsblok" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a><a class="knop knop--rand" href="{tel_link()}" data-track="klik_telefoon" data-locatie="prijsblok">{icoon("telefoon")}{bel} {tel_tekst()}</a></div>
      </div>
    </div>
    {contactformulier("kort", vooraf)}
  </div></div>
</section>"""

def stappen(u=False, soort="standaard"):
    if soort == "levering":
        s = [("Stuur je vraag", "Wat moet er geleverd worden, en waar halen we het op?"),
             ("Je krijgt een voorlopige offerte", "Meestal binnen {{TERMIJN}}, ophalen en leveren inbegrepen."),
             ("Ter plaatse bevestigd", "De offerte bevestigen we wanneer we langskomen."),
             ("Geleverd, het oude gaat mee", "Op zijn plaats gezet, het oude correct afgevoerd.")]
    elif soort == "dampkap":
        s = [("Stuur duidelijke foto's", "Van de dampkap, met het merk erbij."),
             ("Je krijgt een voorlopige offerte", "Meestal binnen {{TERMIJN}}, voor reinigen of afbreken."),
             ("Bevestigd na ons bezoek", "We bekijken de kap en bevestigen de offerte."),
             ("Gereinigd of gedemonteerd", "Je keuken laten we proper achter.")]
    elif u:
        s = [("Neem contact op", "Bel ons of stuur duidelijke foto's."),
             ("U krijgt een voorlopige offerte", "Meestal binnen {{TERMIJN}}, op basis van uw foto's."),
             ("Bevestigd na ons bezoek", "Wij komen langs op een moment dat voor u past."),
             ("Wij maken leeg", "Persoonlijke spullen apart, netjes opgeleverd.")]
    else:
        s = [("Stuur duidelijke foto's", "Via WhatsApp of het formulier, met gemeente en verdieping."),
             ("Je krijgt een voorlopige offerte", "Meestal binnen {{TERMIJN}}, op basis van je foto's."),
             ("Bevestigd na ons bezoek", "We komen langs en bevestigen de offerte."),
             ("Wij laden op", "Op de afgesproken dag. Leeg en geveegd achtergelaten.")]
    return '<ol class="stappen">' + "".join('<li class="stap"><div><h3>%s</h3><p>%s</p></div></li>' % (t, ph(p)) for t, p in s) + "</ol>"

def faq_html(items, eerste_open=False):
    return '<div class="faq">' + "".join('<details%s><summary>%s</summary><div class="faq__antwoord"><p>%s</p></div></details>' % (" open" if (eerste_open and i == 0) else "", esc(v), ph(a)) for i, (v, a) in enumerate(items)) + "</div>"

def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": ph_plat(a)}} for v, a in items]}

def kruimel(paden):
    li = "".join(('<li><a href="%s">%s</a></li>' % (u, t)) if u else ('<li aria-current="page">%s</li>' % t) for t, u in paden)
    return '<nav class="kruimel" aria-label="Kruimelpad"><ol>%s</ol></nav>' % li

def kruimel_schema(paden, pad):
    items = []
    for i, (t, u) in enumerate(paden):
        items.append({"@type": "ListItem", "position": i + 1, "name": t, "item": SITE["url"] + (u if u else "/" + pad)})
    return {"@type": "BreadcrumbList", "itemListElement": items}

def gemeenten_html(kort=False):
    if kort:
        g = ["Antwerpen", "Mechelen", "Lier", "Turnhout", "Geel", "Mol", "Herentals", "Brasschaat", "Schoten", "Mortsel", "Boom", "Kontich"]
        return '<p class="gemeenten-kort">' + ", ".join(g) + ' <a class="tekstlink" href="/werkgebied/">en alle gemeenten daartussen</a></p>'
    return '<div class="gemeenten">' + "".join('<div><h3>%s</h3><ul>%s</ul></div>' % (r, "".join("<li>%s</li>" % x for x in lijst)) for r, lijst in WERKGEBIED) + "</div>"

def review_kaart(compact=True):
    return f"""<figure class="review review--compact">
  <div class="review__kop">{sterren()}<span class="review__bron">{ph("{{SCORE}}")} op Google, {ph("{{AANTAL_REVIEWS}}")} reviews</span></div>
  <blockquote><p><mark class="ph">[ECHTE GOOGLE-REVIEW]</mark> Hier komt een korte, echte review van een klant.</p></blockquote>
  <figcaption><cite><strong>[Voornaam]</strong>, [gemeente]</cite></figcaption>
</figure>"""

def tegels(diensten=DIENSTEN, kol=None):
    stijl = (' style="--kol:%d"' % kol) if kol else ""
    return f'<div class="tegels"{stijl}>' + "".join(
        '<a class="tegel" href="/%s/"><span class="tegel__icoon">%s</span><span class="tegel__tekst"><h3>%s</h3><p>%s</p></span><span class="tegel__pijl" aria-hidden="true">→</span></a>'
        % (d["slug"], icoon(d["icoon"]), d["naam"], d["tegel"]) for d in diensten) + "</div>"

# ---------------------------------------------------------------- schema.org
def org_schema():
    o = {
        "@type": "LocalBusiness", "@id": SITE["url"] + "/#organisatie", "name": "Laaiop", "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/icon-512.png", "image": SITE["url"] + "/assets/img/og-laaiop.jpg",
        "slogan": "Wij laden op. Jij ademt op.",
        "description": "Opruim- en ontruimingsdienst in de provincie Antwerpen: woningen, appartementen, garages, zolders, kantoren en winkelpanden leegmaken, groen- en bouwafval ophalen en meubels en toestellen leveren. Offerte vooraf bevestigd, leeg en geveegd opgeleverd.",
        "email": SITE["email"], "currenciesAccepted": "EUR", "knowsLanguage": "nl-BE",
        "areaServed": [{"@type": "AdministrativeArea", "name": "Provincie Antwerpen"}] + [{"@type": "City", "name": g} for g in ["Antwerpen", "Mechelen", "Lier", "Turnhout", "Geel", "Mol", "Herentals", "Brasschaat", "Schoten", "Mortsel", "Boom", "Kontich"]],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Diensten van Laaiop", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": d["naam"], "url": SITE["url"] + "/" + d["slug"] + "/"}} for d in DIENSTEN]},
    }
    if SITE.get("telefoon_link"): o["telephone"] = SITE["telefoon_link"]
    if PLACEHOLDERS.get("BTW"): o["vatID"] = PLACEHOLDERS["BTW"]
    if REVIEWS_KLAAR and PLACEHOLDERS.get("SCORE") and PLACEHOLDERS.get("AANTAL_REVIEWS"):
        o["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": PLACEHOLDERS["SCORE"].replace(",", "."), "reviewCount": PLACEHOLDERS["AANTAL_REVIEWS"]}
    return o

def website_schema():
    return {"@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/", "name": "Laaiop", "inLanguage": "nl-BE", "publisher": {"@id": SITE["url"] + "/#organisatie"}}

# ---------------------------------------------------------------- pagina-sjabloon
def laadscherm():
    return """<div class="laden" id="laden" aria-hidden="true">
  <svg class="laden__dozen" viewBox="0 0 64 64"><rect x="3" y="35" width="27" height="26" rx="5"/><rect x="34" y="35" width="27" height="26" rx="5"/><rect x="18.5" y="5" width="27" height="26" rx="5"/></svg>
  <p class="laden__getal"><span>0</span>%</p>
  <span class="laden__balk"><i></i></span>
</div>
<script>
(function(){
  var d = document.documentElement, el = document.getElementById('laden');
  if(!el) return;
  if(!d.classList.contains('intro')){ el.parentNode.removeChild(el); return; }
  var getal = el.querySelector('.laden__getal span'), balk = el.querySelector('.laden__balk i');
  var doel = 6, toon = 0, begin = null, vorige = null, klaar = false;
  function af(){
    if(klaar) return;
    klaar = true;
    setTimeout(function(){
      d.classList.add('intro--klaar');
      document.dispatchEvent(new CustomEvent('laaiop:klaar'));
      setTimeout(function(){ el.parentNode && el.parentNode.removeChild(el); }, 1400);
    }, 200);
  }
  function zet(v){ if(v > doel) doel = v; }
  document.addEventListener('DOMContentLoaded', function(){
    zet(35);
    var beelden = Array.prototype.slice.call(document.images), n = beelden.length, k = 0;
    function een(){ k++; zet(35 + 50 * k / Math.max(1, n)); }
    if(!n) zet(85);
    beelden.forEach(function(b){ if(b.complete) een(); else { b.addEventListener('load', een); b.addEventListener('error', een); } });
    if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ zet(92); });
  });
  window.addEventListener('load', function(){ zet(100); });
  setTimeout(function(){ zet(100); }, 5000);
  setTimeout(af, 6500);  /* vangnet: ook als de tab op de achtergrond staat, nooit langer dan 6,5 seconden */
  function stap(t){
    if(klaar) return;
    if(begin === null) begin = vorige = t;
    /* Minstens 1,3 seconden, zodat de dozen een keer kunnen stapelen; tijdsgebaseerd, dus even snel bij elke beeldfrequentie */
    var mik = Math.min(doel, 100 * Math.min(1, (t - begin) / 1300));
    toon += (mik - toon) * (1 - Math.pow(0.88, (t - vorige) / 16.7));
    vorige = t;
    if(mik - toon < 0.4) toon = mik;
    getal.textContent = Math.round(toon);
    balk.style.transform = 'scaleX(' + (toon / 100).toFixed(3) + ')';
    if(toon >= 100){ af(); return; }
    requestAnimationFrame(stap);
  }
  requestAnimationFrame(stap);
})();
</script>
"""

def pagina(pad, titel, meta, body, actief=None, schema=None, noindex=False, og_beeld="/assets/img/og-laaiop.jpg", preload=None, formeel=False, ctx="standaard"):
    canon = SITE["url"] + "/" + pad
    graph = [org_schema(), website_schema(), {"@type": "WebPage", "@id": canon + "#webpagina", "url": canon, "name": titel, "description": meta, "inLanguage": "nl-BE", "isPartOf": {"@id": SITE["url"] + "/#website"}, "about": {"@id": SITE["url"] + "/#organisatie"}, "dateModified": SITE["bijgewerkt"]}] + (schema or [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    robots = "noindex, nofollow" if (noindex or SITE.get("noindex")) else "index, follow, max-image-preview:large"
    gtm_head = gtm_body = ""
    if SITE.get("gtm_id"):
        g = SITE["gtm_id"]
        gtm_head = ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
                    "gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500});</script>"
                    "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','%s');</script>" % g)
        gtm_body = '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%s" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>' % g
    cfg = json.dumps({"formEndpoint": SITE.get("form_endpoint"), "gtmId": SITE.get("gtm_id"), "rustig": formeel})
    intro = "true" if SITE.get("intro") else "false"
    beweeg = ("<script>try{if(!matchMedia('(prefers-reduced-motion: reduce)').matches){var d=document.documentElement;d.classList.add('beweeg');"
              "if(%s&&!sessionStorage.getItem('laaiop-intro')){d.classList.add('intro');sessionStorage.setItem('laaiop-intro','1')}}}catch(e){}</script>" % intro)
    pre = ""
    if preload:
        pre = '<link rel="preload" as="image" href="%s" fetchpriority="high">' % preload
    head = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(titel)}</title>
<meta name="description" content="{esc(meta)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#14213D">
<meta name="color-scheme" content="only light">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_BE">
<meta property="og:site_name" content="Laaiop">
<meta property="og:title" content="{esc(titel)}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE["url"]}{og_beeld}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/dm-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
{pre}
{beweeg}
<link rel="stylesheet" href="/assets/css/site.css?v={versie('css/site.css')}">
<script>window.LAAIOP={cfg};</script>
{gtm_head}
<script type="application/ld+json">{ld}</script>"""
    inhoud = f"""{gtm_body}{laadscherm() if SITE.get("intro") else ""}{header(actief, ctx)}
<main id="inhoud">
{body}
</main>
{footer(formeel, ctx)}
{datalist()}
<script src="/assets/js/site.js?v={versie('js/site.js')}" defer></script>"""
    return head, inhoud

# Versienummer op basis van de inhoud: assets worden een jaar gecachet, dus elke wijziging krijgt een nieuwe URL
def versie(pad):
    with open(os.path.join(ROOT, "assets", pad), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]

# ---------------------------------------------------------------- relatieve links voor staging
def maak_relatief(htmltekst, pad):
    diepte = pad.count("/")
    prefix = "../" * diepte
    def fix(url):
        if not url.startswith("/") or url.startswith("//"):
            return url
        u = url[1:]
        anker = ""
        if "#" in u:
            u, anker = u.split("#", 1); anker = "#" + anker
        if u == "" or u.endswith("/"):
            u = u + "index.html"
        return (prefix + u + anker) if (prefix or u) else ("./" + anker)
    htmltekst = re.sub(r'(href|src)="(/[^"]*)"', lambda m: '%s="%s"' % (m.group(1), fix(m.group(2))), htmltekst)
    htmltekst = re.sub(r'srcset="([^"]*)"', lambda m: 'srcset="%s"' % re.sub(r'(^|, )(/[^ ]+)', lambda n: n.group(1) + fix(n.group(2)), m.group(1)), htmltekst)
    htmltekst = re.sub(r'data-bedankt="(/[^"]*)"', lambda m: 'data-bedankt="%s"' % fix(m.group(1)), htmltekst)
    htmltekst = htmltekst.replace('url("../fonts/', 'url("../fonts/')
    return htmltekst

PAGINAS = []
def voeg_toe(pad, *args, **kw):
    PAGINAS.append((pad, pagina(pad, *args, **kw), kw.get("noindex", False)))

# ====================================================================== PAGINA'S
from pages import bouw_paginas
bouw_paginas(globals())

# ====================================================================== SCHRIJVEN
if os.path.exists(OUTDIR):
    shutil.rmtree(OUTDIR)
os.makedirs(OUTDIR)
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUTDIR, "assets"))
shutil.copy(os.path.join(ROOT, "favicon.ico"), OUTDIR)

for pad, (head, inhoud), _ in PAGINAS:
    doel = os.path.join(OUTDIR, pad, "index.html") if pad and not pad.endswith(".html") else os.path.join(OUTDIR, pad or "index.html")
    if pad == "404.html":
        doel = os.path.join(OUTDIR, "404.html")
    os.makedirs(os.path.dirname(doel), exist_ok=True)
    if MODE == "staging":
        head_r = maak_relatief(head, pad if pad != "404.html" else "")
        inhoud_r = maak_relatief(inhoud, pad if pad != "404.html" else "")
        if pad == "":
            # Artifact-hoofdpagina: wordt in een skelet verpakt, dus zonder doctype/html/head/body.
            tekst = head_r.replace('<meta charset="utf-8">\n', "").replace('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n', "") + "\n" + inhoud_r
        else:
            tekst = '<!doctype html>\n<html lang="nl-BE">\n<head>\n%s\n</head>\n<body>\n%s\n</body>\n</html>\n' % (head_r, inhoud_r)
    else:
        tekst = '<!doctype html>\n<html lang="nl-BE">\n<head>\n%s\n</head>\n<body>\n%s\n</body>\n</html>\n' % (head, inhoud)
    with open(doel, "w", encoding="utf-8") as f:
        f.write(tekst)

# sitemap, robots, llms.txt, manifest, vercel.json
urls = [p for p, _, ni in PAGINAS if not ni and p not in ("404.html",)]
with open(os.path.join(OUTDIR, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in urls:
        f.write("  <url><loc>%s/%s</loc><lastmod>%s</lastmod></url>\n" % (SITE["url"], p, SITE["bijgewerkt"]))
    f.write("</urlset>\n")
with open(os.path.join(OUTDIR, "robots.txt"), "w") as f:
    if SITE.get("noindex"):
        f.write("# Demo-omgeving: niet indexeren. Zet SITE['noindex'] op False bij lancering.\nUser-agent: *\nDisallow: /\n")
    else:
        f.write("User-agent: *\nAllow: /\nDisallow: /bedankt/\n\n# AI-zoekmachines expliciet toegelaten (GEO)\n")
        for bot in ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "Bingbot"]:
            f.write("User-agent: %s\nAllow: /\n\n" % bot)
        f.write("Sitemap: %s/sitemap.xml\n" % SITE["url"])
with open(os.path.join(OUTDIR, "site.webmanifest"), "w") as f:
    json.dump({"name": "Laaiop", "short_name": "Laaiop", "start_url": "/", "display": "standalone", "background_color": "#FFFFFF", "theme_color": "#14213D",
               "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, f)
from pages import llms_txt
with open(os.path.join(OUTDIR, "llms.txt"), "w") as f:
    f.write(llms_txt(globals()))
vercel = {"cleanUrls": True, "trailingSlash": True,
          "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                      {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}, {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"}]}]}
if SITE.get("noindex"):
    vercel["headers"].append({"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]})
with open(os.path.join(OUTDIR, "vercel.json"), "w") as f:
    json.dump(vercel, f, indent=2)
# Vercel leest bij een build vanuit GitHub de vercel.json in de hoofdmap: die houden we gelijk.
# Na een wijziging aan noindex: opnieuw bouwen en vercel.json mee committen.
if MODE != "staging":
    with open(os.path.join(ROOT, "vercel.json"), "w") as f:
        json.dump(dict({"framework": None, "buildCommand": "python3 build.py", "outputDirectory": "dist", "installCommand": ""}, **vercel), f, indent=2)
print("Gebouwd:", OUT, "-", len(PAGINAS), "pagina's")
