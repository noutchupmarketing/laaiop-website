# -*- coding: utf-8 -*-
"""Alle pagina's van laaiop.be. Wordt aangeroepen vanuit build.py."""


def _laad(g):
    for k, v in g.items():
        if not k.startswith("__"):
            globals()[k] = v


# ------------------------------------------------------------------ HOME
def home():
    chat = f"""<div class="chatkaart" role="img" aria-label="Voorbeeldgesprek: een klant stuurt via WhatsApp een foto van een volle garage, krijgt een voorlopige offerte en spreekt een bezoek af om die te bevestigen.">
  <div class="gsm__balk"><span class="gsm__avatar"><img src="/assets/img/icon-192.png" width="22" height="22" alt=""></span><span><span class="gsm__naam">Laaiop</span><span class="gsm__status">WhatsApp</span></span><span class="chatkaart__label">Voorbeeldgesprek</span></div>
  <div class="gsm__chat">
    <div class="bel bel--ik"><div class="bel__foto"><img src="/assets/foto/volle-garage-640.webp" width="640" height="480" alt="" fetchpriority="high"></div>Dit mag allemaal weg. Garage in Mortsel, gelijkvloers.<span class="bel__tijd">09:12</span></div>
    <div class="bel bel--zij">Dank je! Je voorlopige offerte zit in je mailbox: laden, afvoer en vegen inbegrepen.<span class="bel__tijd">09:31</span></div>
    <div class="bel bel--ik bel--extra">Top. Komen jullie donderdag langs om ze te bevestigen?<span class="bel__tijd">09:33</span></div>
  </div>
</div>"""

    hero = f"""<section class="hero" aria-labelledby="hero-titel">
  <div class="wrap hero__in">
    <div class="hero__tekst">
      <span class="eyebrow">Opruimen, ontruimen en leveren in de provincie Antwerpen</span>
      <h1 id="hero-titel">Laaiop maakt je woning, garage of zolder leeg. <em>Zonder verrassingen.</em></h1>
      <p class="lead">Stuur ons een paar duidelijke foto's via WhatsApp. We proberen je binnen {ph("{{TERMIJN}}")} te antwoorden met een <strong>voorlopige offerte</strong>. Die bevestigen we nadat we langs zijn geweest, met laden, afvoer en opkuis erin.</p>
      <div class="knoppen">
        <a class="knop knop--primair" href="/richtprijs/">Vraag je prijs aan</a>
        <a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="hero" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a>
      </div>
      {vertrouwen()}
    </div>
    <div class="heldbeeld">
      {chat}
    </div>
  </div>
</section>"""

    strook = f"""<section class="strook" aria-label="Waarom Laaiop">
  <div class="wrap"><ul>
    <li>{icoon("camera")}<div><strong>Voorlopige offerte via foto's</strong><span>Meestal binnen {ph("{{TERMIJN}}")}</span></div></li>
    <li>{icoon("euro")}<div><strong>Bevestigd na ons bezoek</strong><span>Vast, voor we beginnen</span></div></li>
    <li>{icoon("bezem")}<div><strong>Alles in één keer</strong><span>Laden, afvoeren, vegen</span></div></li>
    <li>{icoon("kringloop")}<div><strong>Tweede leven</strong><span>Bruikbaar gerief naar de kringwinkel</span></div></li>
  </ul></div>
</section>"""

    diensten = f"""<section class="sectie" aria-labelledby="diensten-titel">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Tien diensten, één laadploeg</span><h2 id="diensten-titel">Wat moet er weg, of wat moet er komen?</h2>
    <p>Je hoeft niet te weten welke dienst je nodig hebt. Zeg wat er weg moet of wat er moet komen, en Laaiop regelt de rest.</p></div>
    {tegels(kol=5)}
    <div class="ingangen">
      <a class="ingang ingang--staal" href="/voor-professionals/">{icoon("gebouw")}<span><strong>Notaris, makelaar, syndicus of bedrijf?</strong><span>Eén aanspreekpunt en oplevering op de afgesproken datum.</span></span><span class="tegel__pijl" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>"""

    prijskaart = f"""<div class="prijskaart" role="img" aria-label="Voorbeeld van een voorlopige offerte van Laaiop">
  <div class="prijskaart__kop"><img src="/assets/img/logo-positief.webp" width="400" height="118" alt=""><span class="label label--groen">Voorlopige offerte</span></div>
  <dl>
    <div><dt>Opdracht</dt><dd>Garage leegmaken</dd></div>
    <div><dt>Gemeente</dt><dd>Mortsel, gelijkvloers</dd></div>
    <div><dt>Laden en dragen</dt><dd>Inbegrepen</dd></div>
    <div><dt>Transport en afvoer</dt><dd>Inbegrepen</dd></div>
    <div><dt>Vegen na afloop</dt><dd>Inbegrepen</dd></div>
  </dl>
  <div class="prijskaart__totaal"><span>Prijs op maat<small>bevestigd na ons bezoek</small></span></div>
</div>"""

    route = f"""<div class="route">
  <div class="route__stap"><span class="route__punt">{icoon("winkelkar")}</span><div class="route__tekst"><strong>Ophalen in de winkel</strong><span>Of bij de verkoper op 2dehands</span></div></div>
  <div class="route__stap"><span class="route__punt">{icoon("koelkast")}</span><div class="route__tekst"><strong>Op zijn plaats gezet</strong><span>Ook op de derde verdieping</span></div></div>
  <div class="route__stap"><span class="route__punt">{icoon("kringloop")}</span><div class="route__tekst"><strong>Het oude gaat mee</strong><span>In dezelfde rit, correct afgevoerd</span></div></div>
</div>"""

    werkwijze = f"""<section class="sectie sectie--mist" aria-labelledby="werkwijze-titel">
  <div class="wrap">
    <div class="werkwijze-home">
      <div class="stapel stapel--groot">
        <div class="kop" style="margin-bottom:0"><span class="eyebrow">Zo werkt het</span><h2 id="werkwijze-titel">Van foto tot lege ruimte, in vier stappen</h2>
        <p>Je stuurt duidelijke foto's en krijgt snel een voorlopige offerte. Die bevestigen we nadat we langs zijn geweest. Zo weet je precies wat het kost, voor we beginnen.</p></div>
        {stappen()}
        <div class="knoppen"><a class="knop knop--primair" href="#prijs-aanvragen">Vraag je prijs aan</a><a class="tekstlink" href="/werkwijze/">Meer over onze werkwijze</a></div>
      </div>
      <div class="werkwijze-home__beeld">{prijskaart}</div>
    </div>
  </div>
</section>"""

    features = f"""<section class="sectie" aria-labelledby="leveren-titel">
  <div class="wrap">
      <div class="feature">
        <div class="feature__tekst">
          <span class="eyebrow">Ook leveren</span>
          <h2 id="leveren-titel" class="h3">Ophalen én leveren. Dat doen weinig opruimers.</h2>
          <p>Nieuwe koelkast gekocht? Laaiop haalt hem op in de winkel, zet hem op zijn plaats en neemt de oude meteen mee. Ook een zetel van 2dehands halen we bij de verkoper op. <strong>Eén rit, één prijs.</strong></p>
          <a class="tekstlink" href="/meubels-toestellen-leveren/">Meubels en toestellen leveren</a>
        </div>
        <div class="feature__beeld"><div class="paneel paneel--staal">{route}</div></div>
      </div>
  </div>
</section>"""

    reviews = f"""<section class="sectie sectie--perzik" aria-labelledby="reviews-titel">
  <div class="wrap">
    <div class="kop kop--midden"><span class="eyebrow">Reviews</span><h2 id="reviews-titel">Wat klanten over Laaiop zeggen</h2>
    <span class="googlescore">{sterren()}<span>{ph("{{SCORE}}")} op Google</span><span>{ph("{{AANTAL_REVIEWS}}")} reviews</span></span></div>
    <div class="reviews">
      {''.join(f'<figure class="review">{sterren()}<blockquote><p><mark class="ph">[ECHTE GOOGLE-REVIEW {i}]</mark> Hier komt een echte review van een klant, letterlijk overgenomen van Google.</p></blockquote><figcaption><cite><strong>[Voornaam]</strong>, [gemeente]</cite></figcaption></figure>' for i in (1, 2, 3))}
    </div>
    <p class="veeg-hint">Veeg opzij voor meer reviews</p>
  </div>
</section>"""

    voorna = f"""<section class="sectie" aria-labelledby="voorna-titel">
  <div class="wrap">
    <div class="kop"><span class="eyebrow">Realisaties</span><h2 id="voorna-titel">Voor en na. Zo laat Laaiop het achter.</h2></div>
    <div class="realisaties realisaties--rij">
      {voor_na("Garage in [GEMEENTE].", "[Korte beschrijving: wat stond er, hoe lang duurde het]")}
      {voor_na("Woning na overlijden in [GEMEENTE].", "[Korte beschrijving]")}
      {voor_na("Zolder in [GEMEENTE].", "[Korte beschrijving]")}
    </div>
      </div>
</section>"""

    lokaal = f"""<section class="sectie sectie--mist sectie--compact" aria-labelledby="lokaal-titel">
  <div class="wrap"><div class="lokaal">
    {img("woonstraat-camionette", "Witte camionette in een rustige straat met bakstenen woningen", sizes="(min-width: 900px) 30vw, 100vw", cls="lokaal__beeld")}
    <div class="stapel">
      <span class="eyebrow">Lokaal</span>
      <h2 id="lokaal-titel">Je laadploeg uit de provincie Antwerpen</h2>
      <p class="zacht">Laaiop kent de smalle straten in Antwerpen, de trappen in Mechelse herenhuizen en de opritten in de Kempen. We zijn snel ter plaatse en weten waar we parkeren.</p>
      {gemeenten_html(kort=True)}
    </div>
  </div></div>
</section>"""

    faq = f"""<section class="sectie" aria-labelledby="faq-titel">
  <div class="wrap wrap--smal">
    <div class="kop"><span class="eyebrow">Veelgestelde vragen</span><h2 id="faq-titel">Wat mensen ons het vaakst vragen</h2></div>
    {faq_html(FAQ_ALGEMEEN[:4])}
    <div class="cta-rij"><a class="tekstlink" href="/veelgestelde-vragen/">Alle veelgestelde vragen</a></div>
  </div>
</section>"""

    slot = f"""<section class="slotcta" aria-label="Contact">
  <div class="wrap slotcta__in">
    <p class="slotcta__titel">Oud gerief weg? Wij laden op.</p>
    <div class="knoppen"><a class="knop knop--primair" href="#prijs-aanvragen">Vraag je prijs aan</a><a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="slotcta" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a></div>
  </div>
</section>"""

    # Looptekst: twee gekantelde stroken die met je scrollbeweging meelopen (decoratief, de info staat ook elders)
    doos = '<svg class="band__teken" viewBox="0 0 64 64"><rect x="3" y="35" width="27" height="26" rx="5"/><rect x="34" y="35" width="27" height="26" rx="5"/><rect x="18.5" y="5" width="27" height="26" rx="5" class="band__accent"/></svg>'
    def bandset(woorden):
        return '<div class="band__set">' + "".join("<span>%s</span>%s" % (w, doos) for w in woorden) + "</div>"
    oranje = ["Prijs vooraf", "Laden, afvoeren, vegen", "Ook leveren", "Tweede leven via de kringwinkel", "Provincie Antwerpen"]
    nacht = ["Garage", "Zolder", "Kelder", "Woning", "Appartement", "Kantoor", "Groenafval", "Bouwafval", "Grofvuil"]
    band = f"""<div class="band" aria-hidden="true">
  <div class="band__strook band__strook--nacht"><div class="band__spoor" data-richting="-1">{bandset(nacht) * 2}</div></div>
  <div class="band__strook band__strook--oranje"><div class="band__spoor" data-richting="1">{bandset(oranje) * 2}</div></div>
</div>"""

    statement = """<section class="statement" aria-label="Onze belofte">
  <div class="wrap"><p class="statement__tekst">Jij wijst aan wat weg mag. Wij laden op, voeren af en vegen na. <em>Jij ademt op.</em></p></div>
</section>"""

    # Voor-en-na en het lokaal-blok komen pas terug met echte foto's; prijsblok sluit de pagina af.
    body = hero + strook + diensten + band + werkwijze + statement + features + (reviews if REVIEWS_KLAAR else "") + (voorna if VOOR_NA_KLAAR else "") + faq + prijsblok()
    voeg_toe("", "Ontruiming en opruimdienst provincie Antwerpen | Laaiop",
             "Woning, garage of zolder leegmaken in de provincie Antwerpen? Laaiop ruimt op, voert af en levert. Voorlopige offerte via foto's, bevestigd na ons bezoek.",
             body, actief="/", schema=[faq_schema(FAQ_ALGEMEEN[:4])], preload="/assets/foto/volle-garage-640.webp")


# ------------------------------------------------------------------ DIENSTPAGINA'S
def prijs_kaart_dienst(d, u):
    # Geen bedragen: een prijs krijg je alleen na foto's, als voorlopige offerte die we na ons bezoek bevestigen.
    stap1 = "U stuurt foto's" if u else "Je stuurt foto's"
    return f"""<div class="dienstprijs">
  <p class="dienstprijs__kop">Zo {"krijgt u uw" if u else "krijg je je"} prijs</p>
  <dl>
    <div><dt>Stap 1</dt><dd>{stap1}</dd></div>
    <div><dt>Stap 2, meestal binnen {ph("{{TERMIJN}}")}</dt><dd>Een voorlopige offerte</dd></div>
    <div><dt>Stap 3</dt><dd>Bevestigd na ons bezoek</dd></div>
  </dl>
  <p class="dienstprijs__incl">{icoon("check")}<span>{INBEGREPEN[d["slug"]]}</span></p>
  <a class="knop knop--primair" href="#prijs-aanvragen">{d["cta"]}</a>
</div>"""

def dienstpagina(d):
    u = d["toon"] == "u"
    vooraf = SLUG_NAAR_FORM.get(d["slug"])
    pad = d["slug"] + "/"
    paden = [("Home", "/"), ("Diensten", "/diensten/"), (d["naam"], None)]
    feiten = "".join('<li><strong>%s</strong><span>%s</span></li>' % (k, ph(v)) for k, v in d["kort_feiten"])
    wat = "".join("<li><span>%s</span></li>" % ph(x) for x in d["wat"])
    bestand, alt, cap = d["foto"]
    zakelijk = d["slug"] == "kantoor-winkelpand-leegmaken"
    variant = "offerte" if zakelijk else ("plaatsbezoek" if u else "standaard")
    ctx = variant
    knop2 = (f'<a class="knop knop--rand" href="{tel_link()}" data-track="klik_telefoon" data-locatie="dienst-hero">{icoon("telefoon")}Bel {tel_tekst()}</a>' if u
             else f'<a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="dienst-hero" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a>')
    hero = f"""<section class="paginahero">
  <div class="wrap paginahero__in paginahero__in--met-beeld">
    <div class="paginahero__tekst">
      {kruimel(paden)}
      {regio_label()}
      <h1>{d["h1"]}</h1>
      <p class="lead">{ph(d["intro"])}</p>
      <div class="knoppen"><a class="knop knop--primair" href="#prijs-aanvragen">{d["cta"]}</a>{knop2}</div>
      {vertrouwen()}
    </div>
    <figure class="foto foto--hero"><div class="fotokader">{img(bestand, alt, eager=True, sizes="(min-width: 980px) 40vw, 100vw")}</div><figcaption>{cap}</figcaption></figure>
  </div>
</section>"""
    kort = f"""<section class="sectie sectie--kort"><div class="wrap">
  <div class="kortblok">
    <div class="inhetkort"><h2>In het kort</h2><ul>{feiten}</ul></div>
    {prijs_kaart_dienst(d, u)}
  </div>
</div></section>"""
    soort = "levering" if d["slug"] == "meubels-toestellen-leveren" else ("dampkap" if d["slug"] == "dampkap-afbreken-reinigen" else "standaard")
    stapkop = 'Zo verloopt de ontruiming' if zakelijk else ('Zo gaat het, op uw tempo' if u else 'Zo gaat het')
    watblok = f"""<section class="sectie sectie--mist"><div class="wrap">
  <div class="twee" style="align-items:start">
    <div class="stapel"><span class="eyebrow">Wat Laaiop doet</span><h2 class="h3">Dit zit erin</h2><ul class="vinkjes{' vinkjes--rustig' if u else ''}">{wat}</ul></div>
    <div class="stapel"><span class="eyebrow">Zo werkt het</span><h2 class="h3">{stapkop}</h2><div class="stappen--lijst">{stappen(u, soort)}</div></div>
  </div>
</div></section>"""
    faq = f"""<section class="sectie sectie--mist"><div class="wrap wrap--smal">
  <div class="kop"><span class="eyebrow">Veelgestelde vragen</span><h2>Vragen over {d["naam"].lower()}</h2></div>
  {faq_html(d["faq"])}
</div></section>"""
    verwant = {
        "huis-leegmaken-na-overlijden": ["appartement-leegmaken", "inboedel-opruimen", "garage-zolder-kelder-opruimen"],
        "inboedel-opruimen": ["appartement-leegmaken", "garage-zolder-kelder-opruimen", "grofvuil-ophalen"],
        "appartement-leegmaken": ["inboedel-opruimen", "huis-leegmaken-na-overlijden", "grofvuil-ophalen"],
        "garage-zolder-kelder-opruimen": ["grofvuil-ophalen", "inboedel-opruimen", "groenafval-ophalen"],
        "kantoor-winkelpand-leegmaken": ["bouwafval-ophalen", "grofvuil-ophalen", "meubels-toestellen-leveren"],
        "grofvuil-ophalen": ["garage-zolder-kelder-opruimen", "meubels-toestellen-leveren", "inboedel-opruimen"],
        "groenafval-ophalen": ["bouwafval-ophalen", "garage-zolder-kelder-opruimen", "grofvuil-ophalen"],
        "bouwafval-ophalen": ["groenafval-ophalen", "dampkap-afbreken-reinigen", "grofvuil-ophalen"],
        "meubels-toestellen-leveren": ["grofvuil-ophalen", "inboedel-opruimen", "dampkap-afbreken-reinigen"],
        "dampkap-afbreken-reinigen": ["bouwafval-ophalen", "meubels-toestellen-leveren", "grofvuil-ophalen"],
    }[d["slug"]]
    gerel = "".join('<a href="/%s/">%s%s</a>' % (s, icoon(D[s]["icoon"]), D[s]["naam"]) for s in verwant)
    gebied = f"""<section class="sectie sectie--compact"><div class="wrap">
  <div class="stapel"><span class="eyebrow">Ook nodig?</span><h2 class="h3">Verwante diensten</h2><div class="gerelateerd">{gerel}</div>
  <p class="klein zacht">Laaiop werkt in de hele provincie Antwerpen. <a href="/werkgebied/">Bekijk het werkgebied</a>.</p></div>
</div></section>"""
    if zakelijk:
        pb = prijsblok("Vraag een offerte op maat", "Beschrijf het pand en geef aan wanneer het leeg moet zijn. U krijgt een voorlopige offerte, die we na een plaatsbezoek bevestigen, en een vast aanspreekpunt.", vooraf, True, "offerte")
    elif u:
        pb = prijsblok("Plan een gratis plaatsbezoek", "Op basis van uw foto's krijgt u een voorlopige offerte. Wij komen langs op een moment dat voor u past en bevestigen ze ter plaatse.", vooraf, True, "plaatsbezoek")
    else:
        pb = prijsblok("Wat kost het bij jou?", "Stuur ons een paar duidelijke foto's. Je krijgt snel een voorlopige offerte, die we bevestigen nadat we langs zijn geweest.", vooraf, False)
    body = hero + kort + watblok + faq + pb + gebied
    service = {"@type": "Service", "name": d["naam"], "serviceType": d["naam"], "description": d["meta"], "url": SITE["url"] + "/" + pad,
               "provider": {"@id": SITE["url"] + "/#organisatie"}, "areaServed": {"@type": "AdministrativeArea", "name": "Provincie Antwerpen"},
               "image": SITE["url"] + "/assets/foto/" + bestand + ".webp"}
    voeg_toe(pad, d["seo_titel"], d["meta"], body, actief="/diensten/",
             schema=[service, faq_schema(d["faq"]), kruimel_schema([("Home", "/"), ("Diensten", "/diensten/"), (d["naam"], None)], pad)],
             preload="/assets/foto/%s-640.webp" % bestand, formeel=u, ctx=ctx)


def diensten_overzicht():
    groepen = [("Ontruimen", ["huis-leegmaken-na-overlijden", "inboedel-opruimen", "appartement-leegmaken", "garage-zolder-kelder-opruimen", "kantoor-winkelpand-leegmaken"]),
               ("Ophalen", ["grofvuil-ophalen", "groenafval-ophalen", "bouwafval-ophalen"]),
               ("Leveren en extra", ["meubels-toestellen-leveren", "dampkap-afbreken-reinigen"])]
    blokken = "".join(f'<div class="stapel" style="margin-bottom:48px"><h2 style="font-size:1.6rem">{t}</h2>{tegels([D[s] for s in slugs], kol=len(slugs))}</div>' for t, slugs in groepen)
    body = f"""<section class="paginahero"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Diensten", None)])}
  <h1>Alle diensten van Laaiop</h1>
  <p class="lead">Leegmaken, ophalen en leveren in de provincie Antwerpen. Voor elke opdracht krijg je eerst een voorlopige offerte op basis van foto's, die we bevestigen nadat we langs zijn geweest. Laden, afvoer en opkuis zitten erin.</p>
  <div class="knoppen"><a class="knop knop--primair" href="/richtprijs/">Vraag je prijs aan</a></div>
</div></div></section>
<section class="sectie"><div class="wrap">{blokken}</div></section>""" + prijsblok()
    voeg_toe("diensten/", "Diensten: ontruimen, ophalen en leveren | Laaiop",
             "Alle diensten van Laaiop: woning leegmaken na overlijden, inboedel, appartement, garage, kantoor, grofvuil, groen- en bouwafval, leveringen en dampkappen.",
             body, actief="/diensten/", schema=[kruimel_schema([("Home", "/"), ("Diensten", None)], "diensten/")])


# ------------------------------------------------------------------ PRIJS EN OFFERTE
def prijzen():
    # Bewust geen bedragen: een prijs krijg je alleen na foto's, als voorlopige offerte die we na ons bezoek bevestigen.
    factoren = "".join(f'<div class="factor">{icoon(i)}<h3>{t}</h3><p>{s}</p></div>' for i, t, s in [
        ("doos", "Het volume", "Hoeveel er weg moet, in kubieke meter of laadbeurten. Dat is de grootste factor."),
        ("trap", "Verdieping en lift", "Gelijkvloers gaat sneller dan de vierde verdieping zonder lift."),
        ("afstand", "Afstand tot de camionette", "Kunnen we voor de deur staan, of moeten we vijftig meter dragen?"),
        ("vuilzak", "Soort afval", "Puin weegt zwaarder dan meubels. Gemengd afval kost meer dan gesorteerd."),
        ("bezem", "Demontage en opkuis", "Wandkasten, keukens of vaste rekken uitbreken vraagt meer tijd."),
        ("kringloop", "Wat nog bruikbaar is", "Spullen die naar de kringwinkel kunnen, verlagen de afvoerkosten."),
    ])
    faq = [("Waarom staan er geen prijzen op de site?", "Omdat geen twee opdrachten hetzelfde zijn. Een volle zolder op de derde verdieping is iets anders dan een garage op de begane grond. Met een paar foto's krijg je snel een voorlopige offerte die past bij jouw opdracht."),
           ("Hoe snel krijg ik een voorlopige offerte?", "We proberen iedereen binnen {{TERMIJN}} te antwoorden. Hoe duidelijker je foto's, hoe juister de voorlopige offerte."),
           ("Is de prijs echt vast?", "De prijs in de offerte die we bevestigen nadat we langs zijn geweest, is de prijs die je betaalt. De voorlopige offerte op basis van foto's is een eerste inschatting. Staat er op de dag zelf duidelijk meer dan afgesproken, dan bespreken we dat met je voor we het meenemen."),
           ("Wat zit er in de prijs?", "Laden, dragen, demonteren, transport, de afvoerkosten bij de verwerker en vegen na afloop. Geen verborgen kosten."),
           ("Is het plaatsbezoek gratis?", "Ja. Voor een volledige woning of een groot pand komen we gratis en vrijblijvend langs om je voorlopige offerte te bevestigen."),
           ("Hoe betaal ik?", "Je krijgt een factuur na de opdracht. Bedrijven krijgen een factuur met btw op naam van het bedrijf.")]
    body = f"""<section class="paginahero"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Prijs en offerte", None)])}
  <h1>Hoe krijg je een prijs bij Laaiop?</h1>
  <p class="lead">Elke opdracht is anders. Daarom staan er geen vaste prijzen op de site. Je stuurt ons foto's, krijgt een voorlopige offerte en die bevestigen we nadat we langs zijn geweest. Zo betaal je nooit meer dan afgesproken.</p>
  <div class="knoppen"><a class="knop knop--primair" href="#prijs-aanvragen">Vraag je prijs aan</a><a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="prijzen-hero" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a></div>
</div></div></section>
<section class="sectie"><div class="wrap">
  <div class="kop"><span class="eyebrow">Zo werkt het</span><h2>Van foto tot bevestigde offerte</h2><p>Laden, transport, afvoer en opkuis zitten altijd in de offerte. Btw inbegrepen voor particulieren.</p></div>
  {stappen()}
</div></section>
<section class="sectie sectie--mist"><div class="wrap">
  <div class="kop"><span class="eyebrow">Wat de prijs bepaalt</span><h2>Zes dingen die de prijs bepalen</h2><p>Geen geheimen. Dit is precies waar we naar kijken op je foto's en tijdens ons bezoek.</p></div>
  <div class="factoren">{factoren}</div>
</div></section>
<section class="sectie"><div class="wrap wrap--smal">
  <div class="kop"><span class="eyebrow">Vragen over de prijs</span><h2>Veelgestelde vragen over de prijs</h2></div>{faq_html(faq, eerste_open=True)}
</div></section>""" + prijsblok("Vraag je prijs aan", "Stuur een paar foto's. We proberen je binnen " + ph("{{TERMIJN}}") + " te antwoorden met een voorlopige offerte.")
    voeg_toe("prijzen/", "Prijs en offerte: zo krijg je een prijs | Laaiop",
             "Wat kost een ontruiming bij Laaiop? Stuur foto's en krijg een voorlopige offerte, die we bevestigen nadat we langs zijn geweest. Dit bepaalt de prijs.",
             body, actief="/prijzen/", schema=[faq_schema(faq), kruimel_schema([("Home", "/"), ("Prijs en offerte", None)], "prijzen/")])


# ------------------------------------------------------------------ WERKWIJZE
def werkwijze():
    stromen = "".join(f'<div class="stroom"><span class="stroom__icoon">{icoon(i)}</span><div><strong>{t}</strong><span>{s}</span></div></div>' for i, t, s in [
        ("kringloop", "Bruikbare meubels en huisraad", "Naar een kringwinkel of een goed doel"),
        ("stekker", "Elektro en koelkasten", "Naar een Recupel-inzamelpunt"),
        ("metaal", "Metaal", "Naar de schroothandel"),
        ("blad", "Groenafval", "Naar de groencompostering"),
        ("bakstenen", "Puin, hout en gyproc", "Naar een erkende verwerker"),
        ("vuilzak", "Wat overblijft", "Als restafval, correct verwerkt"),
    ])
    body = f"""<section class="paginahero"><div class="wrap paginahero__in paginahero__in--met-beeld"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Werkwijze", None)])}
  <h1>Zo werkt Laaiop, van foto tot lege ruimte</h1>
  <p class="lead">Vier stappen, een aanspreekpunt en een offerte die vastligt voor we beginnen. Zo weet je op elk moment wat er gebeurt.</p>
  <div class="knoppen"><a class="knop knop--primair" href="#prijs-aanvragen">Vraag je prijs aan</a><a class="knop knop--rand" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="werkwijze-hero" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a></div>
</div>{foto("foto-met-gsm", "Hand die met een gsm een foto neemt van een woonkamer", "Stap 1: een foto met je gsm. Meer heeft Laaiop meestal niet nodig.", "foto--hero")}</div></section>
<section class="sectie sectie--kort" style="padding-bottom:var(--sectie)"><div class="wrap"><div class="artikel" style="margin-inline:auto">
  <span class="eyebrow">Stap voor stap</span>
  <h2>1. Je stuurt duidelijke foto's</h2>
  <p>Neem met je gsm een foto van elke ruimte. Fotografeer liefst vanuit de deuropening, zodat we de hele kamer zien. Vermeld de gemeente, de verdieping en of er een lift is. Stuur je foto's en die informatie via WhatsApp of het formulier op deze site.</p>
  <h2>2. Je krijgt een voorlopige offerte</h2>
  <p>We proberen iedereen binnen {ph("{{TERMIJN}}")} te antwoorden. Op basis van je foto's krijg je een voorlopige offerte. Zo weet je snel of het binnen je budget past.</p>
  <h2>3. We komen langs en bevestigen de offerte</h2>
  <p>Op een foto zie je niet alles. Daarom komen we altijd langs voor we de offerte bevestigen. Zo zien we ook wat er in kasten en op zolder zit, hoe de trap loopt en waar de camionette kan staan. In de offerte zit alles: laden, dragen, demonteren, transport, afvoer en vegen. Je bevestigt en kiest een dag.</p>
  <h2>4. Wij laden op en leveren leeg op</h2>
  <p>Op de afgesproken dag staat de laadploeg voor de deur. We dragen alles naar buiten, demonteren wat niet door de deur kan en sorteren al bij het laden. Persoonlijke spullen leggen we apart. Je hoeft er niet bij te zijn.</p>
  <p>Als we vertrekken, is de ruimte leeg en geveegd. Kon je er niet bij zijn, dan krijg je foto's van elke kamer. Je betaalt na de opdracht, op factuur.</p>
</div></div></section>
<section class="sectie sectie--mist" aria-labelledby="tips-titel"><div class="wrap">
  <div class="kop"><span class="eyebrow">Handig om te weten</span><h2 id="tips-titel">Vijf dingen die je best doet voor wij komen</h2>
  <p>Hoe beter alles voorbereid is, hoe sneller het gaat. En hoe sneller het gaat, hoe lager de prijs.</p></div>
  <ol class="tips">
    <li><strong>Zet apart wat blijft.</strong><span>Plak een sticker op meubels die blijven of zet ze in een aparte kamer.</span></li>
    <li><strong>Zoek papieren en sleutels.</strong><span>Bankpapieren, foto's en reservesleutels zitten vaak in de laatste lade die je opent.</span></li>
    <li><strong>Voorzie een parkeerplaats.</strong><span>Zorg dat onze camionette voor de deur of vlak in de buurt kan staan, bijvoorbeeld op je oprit of een vrije plek in de straat. Borden van de gemeente zijn niet nodig.</span></li>
    <li><strong>Zorg dat water en verlichting beschikbaar zijn.</strong><span>We hebben licht nodig op zolder en in de kelder. We gebruiken water om na te vegen.</span></li>
    <li><strong>Meld trappen en liften.</strong><span>Een smalle draaitrap of geen lift? Zeg het vooraf, dan zit het in de offerte.</span></li>
  </ol>
</div></section>
<section class="sectie"><div class="wrap"><div class="feature">
  <div class="feature__tekst"><span class="eyebrow">Afvoer</span><h2>Wat er gebeurt met wat wij meenemen</h2>
  <p>Laaiop sorteert alles per afvalsoort. Wat nog bruikbaar is, gaat naar een kringwinkel of een goed doel. De rest gaat naar de verwerker die er wettelijk voor bevoegd is. Nooit in een berm of bos.</p>
  {foto("kringloop", "Kringwinkel met kledingrek en fietsen", "Wat bruikbaar is, krijgt een tweede leven via een kringwinkel.")}</div>
  <div class="feature__beeld"><div class="paneel"><div class="stromen">{stromen}</div></div></div>
</div></div></section>
""" + prijsblok()
    voeg_toe("werkwijze/", "Werkwijze: van foto tot lege ruimte | Laaiop",
             "Zo werkt een ontruiming bij Laaiop: foto sturen, voorlopige offerte, bevestiging na ons bezoek, wij laden op en laten alles proper achter. Correct gesorteerd en afgevoerd.",
             body, actief="/werkwijze/", schema=[kruimel_schema([("Home", "/"), ("Werkwijze", None)], "werkwijze/")])


# ------------------------------------------------------------------ REALISATIES
def realisaties():
    items = "".join(voor_na("[Dienst] in [GEMEENTE].", "[Korte beschrijving: wat, hoeveel, hoe lang]") for _ in range(6))
    body = f"""<section class="paginahero"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Realisaties", None)])}
  <h1>Realisaties: voor en na</h1>
  <p class="lead">Zo laat Laaiop het achter. Elke fotoreeks toont de ruimte voor en na de opdracht. Je ziet ook in welke gemeente we werkten en wat we deden.</p>
</div></div></section>
<section class="sectie"><div class="wrap">
  <p class="klein zacht" style="margin-bottom:24px"><mark class="ph">[EIGEN FOTO'S]</mark> Hier komen echte voor-en-na-reeksen van Laaiop. Gebruik hier geen stockfoto's: bezoekers moeten jullie eigen werk zien.</p>
  <div class="realisaties">{items}</div>
</div></section>""" + prijsblok()
    voeg_toe("realisaties/", "Realisaties: ontruimingen voor en na | Laaiop",
             "Voor-en-na-foto's van ontruimingen, garages, zolders en woningen die Laaiop leegmaakte in de provincie Antwerpen.",
             body, actief="/realisaties/", schema=[kruimel_schema([("Home", "/"), ("Realisaties", None)], "realisaties/")])


# ------------------------------------------------------------------ OVER ONS
def over_ons():
    feiten = [("Naam", "Laaiop"), ("Wat", "Opruim- en ontruimingsdienst, ophalen en leveren"), ("Werkgebied", "Provincie Antwerpen"),
              ("Sinds", "{{OPRICHTING}}"), ("Zaakvoerder", "{{ZAAKVOERDER}}"), ("Btw-nummer", "{{BTW}}"), ("Contact", SITE["email"])]
    body = f"""<section class="paginahero paginahero--donker"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Over ons", None)])}
  <h1>De handige buurman die altijd helpt</h1>
  <p class="lead">Laaiop is een laadploeg uit de provincie Antwerpen. We maken leeg wat leeg moet, brengen wat moet komen en laten alles proper achter. Op tijd, met een duidelijke offerte vooraf en een goede babbel erbij.</p>
</div></div></section>
<section class="sectie"><div class="wrap"><div class="twee twee--brede-links">
  <div class="artikel">
    <span class="eyebrow">Ons verhaal</span>
    <h2>Waarom Laaiop bestaat</h2>
    <p>Wie een woning, garage of kantoor moet leegmaken, botst op dezelfde vragen. Wat gaat het kosten? Komen ze wel op tijd? En waar belandt al dat gerief? Laaiop werd opgericht om op elk van die vragen een duidelijk antwoord te geven.</p>
    <p><mark class="ph">[VERHAAL ZAAKVOERDER]</mark> Hier komt in een paar zinnen wie {ph("{{ZAAKVOERDER}}")} is, waarom hij of zij Laaiop startte en wat de klant van hem of haar mag verwachten. Echte namen en een echte foto verhogen het vertrouwen meer dan eender welke slogan.</p>
    <h2>De naam</h2>
    <p>"Laai op" is hoe ze in de provincie Antwerpen zeggen dat iets op de camionette moet. In ons logo zie je het meteen: de L is een steekkar met een oude zetel erop. Wij laden op. Jij ademt op.</p>
  </div>
  <div class="inhetkort" style="align-self:start"><h2>Laaiop in het kort</h2><ul>{"".join("<li><strong>%s</strong><span>%s</span></li>" % (k, ph(v)) for k, v in feiten)}</ul></div>
</div></div></section>
<section class="sectie sectie--mist"><div class="wrap">
  <div class="kop"><span class="eyebrow">Waar we voor staan</span><h2>Vier waarden, elke opdracht opnieuw</h2></div>
  <div class="factoren">
    <div class="factor">{icoon("check")}<h3>Betrouwbaar</h3><p>We doen wat we zeggen. Offerte vooraf, afspraak is afspraak, verzekerd en nooit sluikstorten.</p></div>
    <div class="factor">{icoon("hart")}<h3>Menselijk</h3><p>Respect voor mensen en hun spullen. Discreet bij een overlijden, op het tempo van de klant.</p></div>
    <div class="factor">{icoon("klok")}<h3>Vlot</h3><p>Een voorlopige offerte op basis van foto's, snel ter plaatse en alles in een keer.</p></div>
    <div class="factor">{icoon("kringloop")}<h3>Proper en verantwoord</h3><p>Netjes opgeleverd, correct gesorteerd en een tweede leven voor wat bruikbaar is.</p></div>
  </div>
</div></section>""" + prijsblok()
    voeg_toe("over-ons/", "Over Laaiop, je laadploeg uit de provincie Antwerpen",
             "Laaiop is een opruim- en ontruimingsdienst uit de provincie Antwerpen. Offerte vooraf, netjes opgeleverd. Leer de ploeg kennen.",
             body, actief="/over-ons/", schema=[kruimel_schema([("Home", "/"), ("Over ons", None)], "over-ons/")])


# ------------------------------------------------------------------ PROFESSIONALS
def professionals():
    doelgroepen = "".join(f'<div class="factor">{icoon(i)}<h3>{t}</h3><p>{s}</p></div>' for i, t, s in [
        ("document", "Notarissen", "Woningen in een nalatenschap leeg en geveegd, klaar voor de verkoop. Met fotoverslag voor het dossier."),
        ("sleutel" if False else "huis", "Vastgoedmakelaars", "We maken de woning die te koop staat snel leeg. Zo komt ze beter tot haar recht op foto's en verkoopt ze sneller."),
        ("gebouw", "Syndici en beheerders", "Kelderbergingen, achtergelaten inboedels en gemeenschappelijke delen, op vaste afspraak."),
        ("winkel", "Bedrijven en handelaars", "Kantoren, winkels en magazijnen leeg op de afgesproken datum, ook buiten de openingsuren."),
        ("hart", "Woonzorgcentra en OCMW's", "Kamers en serviceflats snel leeg, met respect voor de familie."),
        ("koelkast", "Meubel- en elektrowinkels", "We leveren bij uw klanten en nemen het oude toestel meteen mee."),
    ])
    body = f"""<section class="paginahero"><div class="wrap paginahero__in paginahero__in--met-beeld"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Voor professionals", None)])}
  <h1>Eén aanspreekpunt voor al uw ontruimingen</h1>
  <p class="lead">Voor notarissen, makelaars, syndici, vastgoedbeheerders en bedrijven maakt Laaiop woningen, kantoren en panden leeg. Met een prijs vooraf, oplevering op de afgesproken datum en foto's als bewijs.</p>
  <div class="knoppen"><a class="knop knop--primair" href="#prijs-aanvragen">Vraag een offerte op maat</a><a class="knop knop--rand" href="{tel_link()}" data-track="klik_telefoon" data-locatie="b2b">{icoon("telefoon")}Bel {tel_tekst()}</a></div>
</div>{foto("sleutels", "Hand die een sleutelbos met huishanger vasthoudt in een lege woning", "Sleutels terug op de afgesproken dag, de woning leeg en geveegd.", "foto--hero")}</div></section>
<section class="sectie"><div class="wrap"><div class="twee">
  <div class="stapel"><span class="eyebrow">Wat u krijgt</span><h2 style="font-size:var(--fs-h2)">Zo werken we met professionals</h2>
  <ul class="vinkjes vinkjes--rustig">
    <li>Eén vaste contactpersoon voor al uw dossiers</li>
    <li>Gratis plaatsbezoek en offerte met vaste prijs</li>
    <li>Sleutels ophalen en terugbezorgen, ook via de notaris of de makelaar</li>
    <li>Oplevering op de afgesproken datum, netjes en geveegd</li>
    <li>Fotoverslag van elke ruimte na afloop</li>
    <li>Factuur met btw op naam van uw kantoor of bedrijf</li>
  </ul></div>
  <div class="stapel"><span class="eyebrow">Samenwerken</span><h2 style="font-size:var(--fs-h2)">Doorverwijzen naar Laaiop</h2>
  <p class="zacht">Heeft u klanten die een woning moeten leegmaken? Verwijs ze door naar Laaiop. Wij nemen binnen {ph("{{TERMIJN}}")} contact op, houden u op de hoogte en bezorgen u het fotoverslag.</p>
  <p class="zacht">Vraag naar onze afspraken voor vaste partners.</p>
  <div class="knoppen"><a class="knop knop--donker" href="#prijs-aanvragen">Neem contact op</a></div></div>
</div></div></section>
<section class="sectie sectie--mist"><div class="wrap">
  <div class="kop"><span class="eyebrow">Voor wie</span><h2>Wie werkt met Laaiop?</h2></div>
  <div class="factoren factoren--compact">{doelgroepen}</div>
</div></section>""" + prijsblok("Vraag een offerte op maat", "Beschrijf het pand en geef aan wanneer het leeg moet zijn. U krijgt een voorlopige offerte, die we na een plaatsbezoek bevestigen, en een vast aanspreekpunt.", "kantoor", True, "offerte")
    voeg_toe("voor-professionals/", "Ontruimingen voor notarissen, makelaars en syndici | Laaiop",
             "Het vaste aanspreekpunt voor ontruimingen in de provincie Antwerpen: voor notarissen, makelaars, syndici en bedrijven. Offerte vooraf, foto's als bewijs.",
             body, schema=[kruimel_schema([("Home", "/"), ("Voor professionals", None)], "voor-professionals/")], formeel=True, ctx="offerte")


# ------------------------------------------------------------------ WERKGEBIED
def werkgebied():
    body = f"""<section class="paginahero"><div class="wrap paginahero__in paginahero__in--met-beeld"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Werkgebied", None)])}
  <h1>Werkgebied: de hele provincie Antwerpen</h1>
  <p class="lead">Laaiop ruimt op, maakt leeg en levert in de stad Antwerpen en alle gemeenten van de provincie: van de Rupelstreek tot de Kempen.</p>
  <div class="knoppen"><a class="knop knop--primair" href="/richtprijs/">Vraag je prijs aan</a></div>
</div>{foto("woonstraat-camionette", "Witte camionette geparkeerd in een rustige woonstraat met bakstenen huizen", "Van een rijhuis in de stad tot een villa in de Kempen: Laaiop rijdt in de hele provincie.", "foto--hero")}</div></section>
<section class="sectie"><div class="wrap">
  <div class="kop"><span class="eyebrow">Gemeenten</span><h2>Hier is Laaiop actief</h2><p>Staat jouw gemeente er niet bij? Ligt ze in de provincie Antwerpen, dan komen we ook. Net buiten de provincie? Vraag het gerust.</p></div>
  {gemeenten_html()}
</div></section>
<section class="sectie sectie--mist"><div class="wrap wrap--smal"><div class="artikel">
  <h2>Parkeren en toegang</h2>
  <p>Op de dag zelf heeft onze camionette een plek nodig voor de deur of vlak in de buurt. Voorzie daarvoor voldoende plaats, bijvoorbeeld je oprit of een vrije plek in de straat. Borden of een parkeerverbod via de gemeente zijn niet nodig. Is parkeren in je straat lastig, zoals in het centrum van Antwerpen, Mechelen of Lier? Zeg het ons vooraf, dan zoeken we samen een oplossing.</p>
  <p>Voor appartementen zonder lift of met een smalle trap zetten we een liftwagen in. Ook dat staat in de offerte die je vooraf krijgt.</p>
</div></div></section>""" + prijsblok()
    voeg_toe("werkgebied/", "Werkgebied: ontruiming in de provincie Antwerpen | Laaiop",
             "Laaiop werkt in de hele provincie Antwerpen: Antwerpen, Mechelen, Lier, Turnhout, Geel, Mol, Herentals, Brasschaat, Schoten, Mortsel, Boom, Kontich.",
             body, schema=[kruimel_schema([("Home", "/"), ("Werkgebied", None)], "werkgebied/")])


# ------------------------------------------------------------------ FAQ
def faq_pagina():
    alle = list(FAQ_ALGEMEEN)
    nav = '<nav class="faqnav" aria-label="Onderwerpen"><a href="#algemeen">Algemeen</a>' + "".join('<a href="#%s">%s</a>' % (d["slug"], d["kort"]) for d in DIENSTEN) + "</nav>"
    blokken = f'<div class="faqgroep" id="algemeen"><h2>Algemeen</h2>{faq_html(FAQ_ALGEMEEN)}</div><h2 class="faqgroep__kop">Per dienst</h2>'
    for d in DIENSTEN:
        blokken += f'<details class="faqgroep faqgroep--klap" id="{d["slug"]}"><summary><h2>{d["naam"]}</h2><span class="faqgroep__aantal">{len(d["faq"])} vragen</span></summary>{faq_html(d["faq"])}<a class="tekstlink" href="/{d["slug"]}/">Meer over {d["naam"].lower()}</a></details>'
        alle += d["faq"]
    body = f"""<section class="paginahero"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Veelgestelde vragen", None)])}
  <h1>Veelgestelde vragen over opruimen en ontruimen</h1>
  <p class="lead">Hier vind je antwoorden over prijzen, planning, afvoer, verzekering en onze diensten. Staat je vraag er niet bij? Stuur ons een berichtje via WhatsApp.</p>
</div></div></section>
<section class="sectie sectie--compact"><div class="wrap wrap--smal">{nav}{blokken}</div></section>""" + prijsblok()
    voeg_toe("veelgestelde-vragen/", "Veelgestelde vragen over ontruimen en opruimen | Laaiop",
             "Antwoorden op de meest gestelde vragen over ontruimingen, prijzen, afvoer, verzekering en elke dienst van Laaiop in de provincie Antwerpen.",
             body, schema=[faq_schema(alle), kruimel_schema([("Home", "/"), ("Veelgestelde vragen", None)], "veelgestelde-vragen/")])


# ------------------------------------------------------------------ RICHTPRIJS
def richtprijs():
    form = contactformulier("v")
    body = f"""<section class="paginahero paginahero--compact"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), ("Prijs aanvragen en contact", None)])}
  <h1>Contact en prijs aanvragen</h1>
  <p class="lead">Laat je gegevens achter, kies waarmee we kunnen helpen en voeg een paar duidelijke foto's toe. We proberen je binnen {ph("{{TERMIJN}}")} te antwoorden met een voorlopige offerte. Die bevestigen we nadat we langs zijn geweest.</p>
</div></div></section>
<section class="sectie sectie--formulier" id="formulier"><div class="wrap"><div class="twee twee--brede-links">
  {form}
  <div class="stapel stapel--groot" id="contact">
    <div class="stapel"><h2 style="font-size:1.6rem">Liever meteen contact?</h2>
    <div class="knoppen"><a class="knop knop--primair" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="contactpagina" target="_blank" rel="noopener">{icoon("chat")}WhatsApp een foto</a>
    <a class="knop knop--rand" href="{tel_link()}" data-track="klik_telefoon" data-locatie="contactpagina">{icoon("telefoon")}Bel {tel_tekst()}</a></div></div>
    <div class="inhetkort"><h2>Contactgegevens</h2><ul>
      <li><strong>Telefoon</strong><span>{tel_tekst()}</span></li>
      <li><strong>WhatsApp</strong><span>{tel_tekst()}</span></li>
      <li><strong>E-mail</strong><span><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></span></li>
      <li><strong>Btw</strong><span>{ph("{{BTW}}")}</span></li>
      <li><strong>Werkgebied</strong><span>Provincie Antwerpen</span></li>
    </ul></div>
    <div class="stapel"><h3>Wat gebeurt er na je aanvraag?</h3><ul class="vinkjes"><li>We bekijken je foto's</li><li>We proberen je binnen {ph("{{TERMIJN}}")} te antwoorden met een voorlopige offerte</li><li>We komen langs en bevestigen de offerte</li><li>Je kiest een dag, wij laden op</li></ul></div>
  </div>
</div></div></section>"""
    voeg_toe("richtprijs/", "Prijs aanvragen | Laaiop, opruimdienst provincie Antwerpen",
             "Vraag in een minuut een prijs aan voor je ontruiming, grofvuil of levering. Voeg foto's toe en krijg een voorlopige offerte, of stuur ze via WhatsApp.",
             body, actief="/richtprijs/", schema=[kruimel_schema([("Home", "/"), ("Prijs aanvragen en contact", None)], "richtprijs/")], ctx="richtprijs")


def bedankt():
    body = f"""<section class="sectie"><div class="wrap wrap--smal"><div class="stapel stapel--groot" style="justify-items:start">
  <span class="bedankt-icoon">{icoon("check")}</span>
  <h1 style="font-size:var(--fs-h1)">Bedankt, we hebben je aanvraag ontvangen.</h1>
  <p class="lead zacht">We bekijken je foto's en proberen je binnen {ph("{{TERMIJN}}")} te antwoorden met een voorlopige offerte. Daarna spreken we af om langs te komen en de offerte te bevestigen. Wil je nog iets toevoegen? Stuur het via WhatsApp.</p>
  <div class="knoppen"><a class="knop knop--primair" href="{wa_link()}" data-track="klik_whatsapp" data-locatie="bedankt" target="_blank" rel="noopener">{icoon("chat")}Stuur extra foto's via WhatsApp</a><a class="knop knop--rand" href="/">Terug naar de homepagina</a></div>
</div></div></section>"""
    voeg_toe("bedankt/", "Bedankt voor je aanvraag | Laaiop", "Je aanvraag is goed ontvangen. Laaiop neemt snel contact met je op met een voorlopige offerte.", body, noindex=True, ctx="bedankt")


def juridisch(pad, titel, h1, secties):
    inhoud = "".join(f"<h2>{t}</h2><p>{p}</p>" for t, p in secties)
    body = f"""<section class="paginahero"><div class="wrap paginahero__in"><div class="paginahero__tekst">
  {kruimel([("Home", "/"), (h1, None)])}<h1>{h1}</h1>
  <p class="lead"><mark class="ph">[JURIDISCH NAKIJKEN]</mark> Ontwerptekst. Laat deze pagina nakijken voor de lancering.</p>
</div></div></section>
<section class="sectie"><div class="wrap wrap--smal"><div class="artikel">{inhoud}<p class="bijgewerkt">Laatst bijgewerkt: {SITE["bijgewerkt"]}</p></div></div></section>"""
    voeg_toe(pad, titel + " | Laaiop", titel + " van Laaiop, opruim- en ontruimingsdienst in de provincie Antwerpen.", body)


def juridische_paginas():
    juridisch("privacybeleid/", "Privacybeleid", "Privacybeleid", [
        ("Wie zijn wij?", "Laaiop, btw " + ph("{{BTW}}") + ", e-mail " + SITE["email"] + ". Wij zijn verantwoordelijk voor de verwerking van je persoonsgegevens."),
        ("Welke gegevens", "Naam, telefoonnummer, e-mailadres, gemeente, de foto's die je ons stuurt en je opmerkingen."),
        ("Waarom", "Om je een prijs te bezorgen, de opdracht uit te voeren en te factureren. De rechtsgrond is de uitvoering van een overeenkomst of het nemen van stappen op jouw verzoek."),
        ("Hoe lang", "Aanvragen zonder opdracht bewaren we maximaal twaalf maanden. Facturen bewaren we zo lang als de wet voorschrijft."),
        ("Met wie", "We delen je gegevens niet met derden, behalve met dienstverleners die ons helpen (zoals onze website- en e-mailhosting) en alleen voor dit doel."),
        ("Je rechten", "Je mag je gegevens inkijken, laten verbeteren of laten wissen. Mail naar " + SITE["email"] + ". Je kunt ook klacht indienen bij de Gegevensbeschermingsautoriteit."),
    ])
    juridisch("cookiebeleid/", "Cookiebeleid", "Cookiebeleid", [
        ("Noodzakelijke cookies", "Deze site bewaart alleen je cookiekeuze in je browser. Daarvoor is geen toestemming nodig."),
        ("Analytische en advertentiecookies", "Als je toestemming geeft, gebruiken we Google Analytics, Google Ads en Meta om te meten welke advertenties werken. Zonder toestemming worden die cookies niet geplaatst (Google Consent Mode v2)."),
        ("Je keuze wijzigen", "Wis de cookies van laaiop.be in je browser. Bij je volgende bezoek kun je opnieuw kiezen."),
    ])
    juridisch("algemene-voorwaarden/", "Algemene voorwaarden", "Algemene voorwaarden", [
        ("Prijs", "De prijs in onze bevestiging is vast en omvat laden, transport, afvoer en vegen, tenzij anders vermeld. Staat er op de dag van uitvoering duidelijk meer of ander afval dan op de foto's of bij het plaatsbezoek? Dan bespreken we een aangepaste prijs voor we het meenemen."),
        ("Wat we niet meenemen", "Asbest, gasflessen, munitie en andere gevaarlijke stoffen nemen we niet mee. " + ph("{{KGA}}")),
        ("Annuleren", "[AF TE SPREKEN] Annulatievoorwaarden en termijn."),
        ("Betaling", "Betaling na uitvoering, op factuur, binnen [TERMIJN] dagen."),
        ("Aansprakelijkheid", ph("{{VERZEKERING}}")),
    ])


def niet_gevonden():
    body = f"""<section class="sectie"><div class="wrap wrap--smal"><div class="stapel stapel--groot">
  <span class="eyebrow">Fout 404</span>
  <h1 style="font-size:var(--fs-h1)">Deze pagina hebben we al opgeladen.</h1>
  <p class="lead zacht">Ze bestaat niet (meer). Zoek je een dienst of een prijs? Of wil je ons contacteren?</p>
  <div class="knoppen"><a class="knop knop--primair" href="/">Naar de homepagina</a><a class="knop knop--rand" href="/diensten/">Alle diensten</a></div>
</div></div></section>"""
    voeg_toe("404.html", "Pagina niet gevonden | Laaiop", "Deze pagina bestaat niet.", body, noindex=True)


def bouw_paginas(g):
    _laad(g)
    home()
    diensten_overzicht()
    for d in DIENSTEN:
        dienstpagina(d)
    prijzen(); werkwijze()
    if VOOR_NA_KLAAR:
        realisaties()
    over_ons(); professionals(); werkgebied(); faq_pagina(); richtprijs(); bedankt()
    juridische_paginas(); niet_gevonden()


def llms_txt(g):
    _laad(g)
    regels = ["# Laaiop", "",
              "> Laaiop is een opruim- en ontruimingsdienst uit de provincie Antwerpen (België). Laaiop maakt woningen, appartementen, garages, zolders, kelders, kantoren en winkelpanden leeg, haalt grofvuil, groenafval en bouwafval op, levert nieuwe meubels en toestellen (en neemt het oude mee) en reinigt of demonteert dampkappen. Laaiop toont geen vaste prijzen: klanten sturen foto's en krijgen (meestal binnen 24 uur) een voorlopige offerte, die na een bezoek ter plaatse bevestigd wordt. Alles wordt gesorteerd afgevoerd en bezemschoon opgeleverd.",
              "", "- Werkgebied: provincie Antwerpen (o.a. Antwerpen, Mechelen, Lier, Turnhout, Geel, Mol, Herentals, Brasschaat, Schoten, Mortsel, Boom, Kontich)",
              "- Taal: Nederlands (Vlaams)", "- Contact: " + SITE["email"], "- Belofte: Wij laden op. Jij ademt op.", "", "## Diensten", ""]
    for d in DIENSTEN:
        regels.append("- [%s](%s/%s/): %s" % (d["naam"], SITE["url"], d["slug"], d["meta"]))
    regels += ["", "## Belangrijke pagina's", "",
               "- [Prijs en offerte](%s/prijzen/): hoe je een prijs krijgt en wat de prijs bepaalt" % SITE["url"],
               "- [Werkwijze](%s/werkwijze/): van foto tot lege ruimte, en hoe afval verwerkt wordt" % SITE["url"],
               "- [Voor professionals](%s/voor-professionals/): notarissen, makelaars, syndici en bedrijven" % SITE["url"],
               "- [Werkgebied](%s/werkgebied/): alle gemeenten" % SITE["url"],
               "- [Veelgestelde vragen](%s/veelgestelde-vragen/)" % SITE["url"],
               "- [Prijs aanvragen](%s/richtprijs/)" % SITE["url"], ""]
    return "\n".join(regels)
