# -*- coding: utf-8 -*-
"""
LAAIOP WEBSITE: INSTELLINGEN EN TEKSTEN
=======================================
Alles wat de klant nog moet aanleveren staat in PLACEHOLDERS.
Vul een waarde in (tekst tussen aanhalingstekens) en draai `python3 build.py`.
Zolang een waarde None is, toont de site een geel gemarkeerde placeholder.
"""

# ---------------------------------------------------------------------------
# 1. SITE-INSTELLINGEN
# ---------------------------------------------------------------------------
SITE = {
    "naam": "Laaiop",
    "url": "https://www.laaiop.be",          # productiedomein (canonical, sitemap)
    "email": "info@laaiop.be",
    "telefoon_link": "+32471795515",                    # bv. "+32470123456"  (voor tel:-links)
    "whatsapp_nummer": "32471795515",                  # bv. "32470123456"   (zonder + of spaties)
    "gtm_id": None,                           # bv. "GTM-ABC1234"  (activeert ook cookiebanner)
    "intro": True,                            # laadscherm bij het eerste bezoek per sessie (False = uit)
    "form_endpoint": None,                    # bv. Formspree/Make/GHL-webhook URL
    "noindex": True,                          # True zolang de site een demo is. Bij lancering: False
    "bijgewerkt": "2026-10-05",
}

# ---------------------------------------------------------------------------
# 2. PLACEHOLDERS  (None = nog in te vullen door de klant)
# ---------------------------------------------------------------------------
PLACEHOLDERS = {
    "TELEFOON": "0471 79 55 15",                 # zichtbaar nummer, bv. "0470 12 34 56"
    "SCORE": None,                    # Google-score, bv. "4,9"
    "AANTAL_REVIEWS": None,           # bv. "34"
    "TERMIJN": None,                  # hoe snel een prijs, bv. "24 uur"
    "TERMIJN_UITVOERING": None,       # hoe snel ter plaatse, bv. "een week"
    "DUUR_WONING": None,              # bv. "een tot twee dagen"
    "MINIMUMTARIEF": None,            # bv. "95 euro"
    "PRIJS_LOSSE_STUKKEN": None,
    "PRIJS_GARAGE": None,
    "PRIJS_APPARTEMENT": None,
    "PRIJS_WONING": None,
    "PRIJS_GROEN": None,
    "PRIJS_BOUW": None,
    "PRIJS_LEVERING": None,
    "PRIJS_DAMPKAP": None,
    "PRIJS_KANTOOR": None,
    "INBOEDEL_VERREKENEN": None,      # antwoord: verrekenen, opkopen of doneren?
    "KGA": None,                      # klein gevaarlijk afval (verf, olie): ja/nee?
    "ARCHIEF": None,                  # vertrouwelijk archief vernietigen: hoe?
    "AANSLUITEN": None,               # toestellen aansluiten bij levering: ja/nee?
    "WEEKEND": None,                  # werken op zaterdag: ja/nee?
    "ZAAKVOERDER": "Keanu Bosmans",              # naam van het gezicht van Laaiop
    "ADRES": None,
    "BTW": None,
    "VERZEKERING": None,              # bv. "BA-verzekering bij ..."
    "OPRICHTING": "2026",               # jaar van oprichting
}

# Werkgebied (alleen tekst, geen aparte gemeentepagina's)
WERKGEBIED = [
    ("Antwerpen en districten", ["Antwerpen", "Berchem", "Borgerhout", "Borsbeek", "Deurne", "Ekeren", "Hoboken", "Merksem", "Wilrijk", "Berendrecht-Zandvliet-Lillo"]),
    ("Rond Antwerpen", ["Mortsel", "Edegem", "Kontich", "Aartselaar", "Hemiksem", "Schelle", "Boom", "Niel", "Brasschaat", "Schoten", "Kapellen", "Stabroek", "Wijnegem", "Wommelgem", "Ranst", "Zoersel", "Malle", "Brecht"]),
    ("Mechelen en Rivierenland", ["Mechelen", "Lier", "Duffel", "Rumst", "Willebroek", "Puurs-Sint-Amands", "Bonheiden", "Sint-Katelijne-Waver", "Berlaar", "Nijlen", "Heist-op-den-Berg"]),
    ("Kempen", ["Turnhout", "Geel", "Mol", "Herentals", "Westerlo", "Kasterlee", "Grobbendonk", "Herenthout", "Hoogstraten", "Zandhoven", "Olen", "Beerse", "Vosselaar"]),
]

# ---------------------------------------------------------------------------
# 3. DIENSTEN
#    toon: "je" of "u"  |  icoon: naam uit ICONEN in build.py
# ---------------------------------------------------------------------------
DIENSTEN = [
    {
        "slug": "huis-leegmaken-na-overlijden",
        "naam": "Huis leegmaken na overlijden",
        "kort": "Woning na overlijden",
        "tegel": "Met respect leeggemaakt, op uw tempo. Persoonlijke papieren houden we apart.",
        "icoon": "huis",
        "toon": "u",
        "seo_titel": "Huis leegmaken na overlijden provincie Antwerpen | Laaiop",
        "meta": "Een woning leegmaken na een overlijden? Laaiop neemt het met respect van u over. Prijs vooraf afgesproken, netjes opgeleverd, gratis plaatsbezoek.",
        "h1": "Huis leegmaken na een overlijden",
        "intro": "Een woning leegmaken na een afscheid vraagt tijd en zorg. Laaiop maakt de woning met respect leeg. U krijgt ze leeg en geveegd terug, klaar voor de notaris, de verhuurder of de verkoop.",
        "cta": "Plan een gratis plaatsbezoek",
        "kort_feiten": [
            ("Wat", "Volledige woning leegmaken, sorteren en netjes opleveren"),
            ("Prijs", "Indicatie via foto's, offerte na een gratis plaatsbezoek"),
            ("Aanwezig zijn", "Niet nodig. U krijgt foto's van de lege woning"),
            ("Persoonlijk", "Papieren, foto's en waardevolle spullen houden we apart"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Een gratis en vrijblijvend plaatsbezoek, op een moment dat voor u past",
            "Persoonlijke documenten, foto's, juwelen en sleutels houden we apart in een doos voor u",
            "U duidt vooraf aan wat de familie wil houden. Dat blijft staan",
            "Wat bruikbaar is, krijgt een tweede leven via een kringwinkel of een goed doel",
            "De rest sorteren we en voeren we correct af. Nooit in een berm of bos",
            "Bezemschone oplevering, met foto's als u er niet bij kunt zijn",
            "Ook appartementen, serviceflats en kamers in een woonzorgcentrum. Voor appartementen zetten we ook een liftwagen in.",
        ],
        "foto": ('herinneringen', "Handen die oude familiefoto's in een album aanwijzen", "Foto's, brieven, een trouwalbum. Laaiop legt persoonlijke spullen apart voor de familie. Dat doen we voordat we iets afvoeren."),

        "prijs": "Elke woning is anders. Op basis van foto's krijgt u eerst een prijsindicatie. De definitieve offerte maken we na een plaatsbezoek, inclusief laden, afvoer en opkuis. Ter indicatie: een appartement kost meestal {{PRIJS_APPARTEMENT}}, een gezinswoning {{PRIJS_WONING}}.",
        "faq": [
            ("Hoe snel kan de woning leeg zijn?", "Meestal kunnen we binnen {{TERMIJN_UITVOERING}} na uw akkoord beginnen. Een gemiddelde gezinswoning maken we in {{DUUR_WONING}} leeg. Heeft u meer tijd nodig, dan volgen wij uw tempo."),
            ("Moet ik aanwezig zijn tijdens de ontruiming?", "Nee. Veel families geven ons de sleutel of laten de notaris of makelaar openen. Na afloop krijgt u foto's van elke lege kamer."),
            ("Wat gebeurt er met waardevolle spullen en documenten?", "We leggen alles wat persoonlijk lijkt apart in een afgesloten doos. Denk aan papieren, foto's, juwelen, bankkaarten en sleutels. Die krijgt u terug, ook als u niet aanwezig was."),
            ("Wordt de waarde van de inboedel verrekend?", "{{INBOEDEL_VERREKENEN}}"),
            ("Werken jullie samen met de notaris of de makelaar?", "Ja. Als u dat wenst, maken we rechtstreeks afspraken met de notaris of de makelaar over de sleutels en de opleverdatum. We sturen dan ook de foto's van de lege woning door."),
            ("Is de woning daarna klaar voor verkoop of overdracht?", "Ja. Alle kamers, de kelder, de zolder en het tuinhuis zijn leeg. De vloeren zijn geveegd. Dat noemen we bezemschoon: zo kan de woning naar de koper, de verhuurder of de volgende huurder."),
        ],
        "zoekwoorden": ["huis leegmaken na overlijden", "woning leegmaken na overlijden", "inboedel na overlijden", "woningontruiming"],
    },
    {
        "slug": "inboedel-opruimen",
        "naam": "Inboedel opruimen",
        "kort": "Inboedel",
        "tegel": "Een kamer of de volledige inboedel. Jij kiest wat blijft. Wij nemen de rest mee.",
        "icoon": "doos",
        "toon": "je",
        "seo_titel": "Inboedel opruimen provincie Antwerpen, vaste prijs | Laaiop",
        "meta": "Inboedel laten opruimen bij verhuis, verkoop of te veel gerief? Laaiop haalt alles weg, sorteert en voert correct af. Prijs vooraf, alles proper achtergelaten.",
        "h1": "Inboedel opruimen, volledig of gedeeltelijk",
        "intro": "Verhuis, verkoop of gewoon te veel gerief? Laaiop haalt een deel of de volledige inboedel weg, sorteert alles en voert het correct af. Jij kiest wat blijft. Wij doen het sleuren.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Meubels, huisraad, kleding, elektro, alles wat weg moet"),
            ("Hoeveel", "Van een kamer tot een volledige woning"),
            ("Prijs", "Indicatie via foto's, offerte op locatie"),
            ("Inbegrepen", "Demonteren, laden, afvoeren en vegen"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Kamer per kamer of de hele woning in een keer",
            "Kasten, bedden en wandmeubels demonteren we zelf",
            "Kasten hoeven niet leeg: wij ledigen ze ook",
            "Elektrische toestellen gaan naar een Recupel-inzamelpunt",
            "Bruikbare meubels en huisraad krijgen een tweede leven",
            "Ook kelder, zolder, tuinhuis en garage in dezelfde beurt",
        ],
        "foto": ('kamer-vol-dozen', 'Kamer volgestapeld met dozen, zakken en oud gerief', 'Zo begint het vaak: een kamer vol dozen en gerief. Laaiop neemt mee wat weg mag en laat staan wat blijft.'),

        "prijs": "Je prijs hangt af van het volume, de verdieping en de afvoer. Een kamer of berging kost meestal {{PRIJS_GARAGE}}, een volledige inboedel van een appartement {{PRIJS_APPARTEMENT}}.",
        "faq": [
            ("Kan ik een deel van de inboedel laten staan?", "Ja. Duid aan wat blijft, met een sticker of op een foto. Wij nemen alleen mee wat weg mag."),
            ("Moeten de kasten leeg zijn voor jullie komen?", "Nee. We ledigen ze zelf en kijken daarbij uit naar papieren of spullen die je misschien wil houden."),
            ("Nemen jullie ook elektrische toestellen mee?", "Ja. Koelkasten, wasmachines, tv's en klein elektro brengen we naar een erkend inzamelpunt van Recupel."),
            ("Hoe lang duurt een inboedelruiming?", "Een kamer of berging is meestal in enkele uren leeg. Een volledige woning leegmaken duurt {{DUUR_WONING}}."),
            ("Wat kost een inboedelruiming?", "Dat hangt af van het volume, de verdieping en wat er in de inboedel zit. Stuur ons een paar duidelijke foto's: binnen {{TERMIJN}} krijg je een prijsindicatie. De definitieve offerte maken we op locatie."),
        ],
        "zoekwoorden": ["inboedel opruimen", "inboedel leegmaken", "inboedelruiming", "huis leeghalen"],
    },
    {
        "slug": "appartement-leegmaken",
        "naam": "Appartement leegmaken",
        "kort": "Appartement",
        "tegel": "Ook op de vijfde verdieping, met een liftwagen als de trap te smal is.",
        "icoon": "appartement",
        "toon": "je",
        "seo_titel": "Appartement leegmaken in de provincie Antwerpen | Laaiop",
        "meta": "Appartement of serviceflat leegmaken? Laaiop regelt de liftwagen en de parkeerplaats, maakt alles leeg en laat alles proper achter. Prijs vooraf.",
        "h1": "Appartement of serviceflat leegmaken",
        "intro": "Een appartement leegmaken is vooral een kwestie van trappen, liften en parkeren. Laaiop regelt dat. Jij krijgt een duidelijke offerte en een lege, propere flat, klaar voor de verhuurder of de verkoop.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Appartement, studio, serviceflat of kamer in een woonzorgcentrum"),
            ("Trappen en lift", "Liftwagen als de trap of lift te klein is"),
            ("Prijs", "Offerte op locatie, inclusief kelderberging"),
            ("Oplevering", "Leeg en geveegd, met foto's voor de verhuurder"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Het volledige appartement leegmaken, inclusief kelderberging en terras",
            "Liftwagen voor zetels en kasten die niet door de trapzaal passen",
            "Wij zeggen je of er een tijdelijk parkeerverbod nodig is",
            "Beschermen van de lift en de gemeenschappelijke delen",
            "Afspraken met de syndicus of conciërge, als je dat wil",
            "Bezemschone oplevering en foto's voor de plaatsbeschrijving",
        ],
        "foto": ('lege-kamer', 'Lege, geveegde woonkamer met raam naar buiten', 'Zo levert Laaiop een appartement op: leeg, geveegd en klaar voor de plaatsbeschrijving.'),

        "prijs": "De prijs hangt af van het volume, de verdieping en of er een liftwagen nodig is. Een appartement kost meestal {{PRIJS_APPARTEMENT}}, alles inbegrepen.",
        "faq": [
            ("Het gebouw heeft geen lift. Is dat een probleem?", "Nee. We dragen alles naar beneden of zetten een liftwagen in. Vermeld de verdieping in je aanvraag, dan zit het in de prijs."),
            ("Wie vraagt het parkeerverbod aan?", "We zeggen je vooraf of het nodig is. In de meeste gemeenten vraag je een tijdelijk parkeerverbod aan bij de stad of gemeente, enkele dagen op voorhand."),
            ("Hoe snel kan een serviceflat leeg zijn?", "Woonzorgcentra en serviceflats geven vaak weinig tijd. Laat ons de uiterste datum weten: we plannen de ontruiming op tijd in."),
            ("Nemen jullie ook de kelderberging mee?", "Ja. Kelderberging, zolderkamer en terras horen er gewoon bij. Zeg het wel even in je aanvraag."),
            ("Krijg ik foto's voor de verhuurder?", "Ja. Na afloop krijg je foto's van elke kamer, handig voor de plaatsbeschrijving en de huurwaarborg."),
        ],
        "zoekwoorden": ["appartement leegmaken", "appartement leeghalen", "serviceflat leegmaken"],
    },
    {
        "slug": "garage-zolder-kelder-opruimen",
        "naam": "Garage, zolder en kelder opruimen",
        "kort": "Garage en zolder",
        "tegel": "Tien jaar gerief in een paar uur weg. Ook voor kleine opdrachten.",
        "icoon": "garage",
        "toon": "je",
        "seo_titel": "Garage, zolder of kelder laten opruimen | Laaiop",
        "meta": "Garage, zolder of kelder vol gerief? Stuur een foto en krijg snel een prijsindicatie. Laaiop laadt alles op, voert correct af en veegt na. Provincie Antwerpen.",
        "h1": "Garage, zolder of kelder opruimen",
        "intro": "Tien jaar gerief in de garage? Stuur een foto. Je krijgt snel een prijsindicatie. Wij laden alles op en vegen na. Meestal is het in een paar uur gedaan. Wij laden op, jij ademt op.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Garage, zolder, kelder, tuinhuis, berging of carport"),
            ("Hoe lang", "Meestal een paar uur"),
            ("Prijs", "Indicatie via foto, offerte op locatie"),
            ("Minimum", "Ook kleine opdrachten, vanaf {{MINIMUMTARIEF}}"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Alles wat weg mag, in een keer: oude fietsen, meubels, dozen, rekken",
            "Rekken en kasten demonteren we ter plaatse",
            "Je hoeft vooraf niets te sorteren",
            "Metaal, hout en elektro gaan elk naar de juiste verwerker",
            "Bruikbare spullen gaan naar de kringwinkel",
            "Na afloop vegen we de ruimte",
        ],
        "foto": ('volle-garage', 'Garage vol rekken, gereedschap en oud gerief', "Herkenbaar? Stuur Laaiop zo'n foto en je krijgt snel een prijsindicatie om alles op te laden en af te voeren."),

        "prijs": "Voor een garage, zolder of kelder heb je meestal genoeg aan een foto. De meeste opdrachten kosten {{PRIJS_GARAGE}}, inclusief afvoer.",
        "faq": [
            ("Is het de moeite voor een kleine opdracht?", "Ja. We komen ook voor een halve garage of een volle kelder. Het minimumtarief is {{MINIMUMTARIEF}}."),
            ("Moet ik vooraf sorteren?", "Nee. Zet alleen apart wat je wil houden. Het sorteren doen wij, bij het laden en bij de afvoer."),
            ("Nemen jullie verfpotten en chemicaliën mee?", "{{KGA}}"),
            ("Kunnen jullie op zaterdag komen?", "{{WEEKEND}}"),
            ("Hoe snel kunnen jullie komen?", "Meestal binnen {{TERMIJN_UITVOERING}}. Is het dringend, zeg het dan in je bericht."),
        ],
        "zoekwoorden": ["garage opruimen", "zolder leegmaken", "kelder opruimen", "rommel laten ophalen"],
    },
    {
        "slug": "kantoor-winkelpand-leegmaken",
        "naam": "Kantoor en winkelpand leegmaken",
        "kort": "Kantoor en winkel",
        "tegel": "Meubilair, archief en rekken. Op de afgesproken datum, ook buiten de openingsuren.",
        "icoon": "winkel",
        "toon": "u",
        "seo_titel": "Kantoor of winkelpand leegmaken | Laaiop provincie Antwerpen",
        "meta": "Kantoor, winkelpand of handelszaak leegmaken? Eén aanspreekpunt, een prijs vooraf en oplevering op de afgesproken datum, ook buiten de openingsuren.",
        "h1": "Kantoor of winkelpand leegmaken",
        "intro": "Uw pand moet op een vaste datum leeg zijn. Uw zaak moet zo kort mogelijk dicht. Laaiop werkt met één aanspreekpunt, een afgesproken prijs en een oplevering op de afgesproken dag. Ook 's avonds of in het weekend.",
        "cta": "Vraag een offerte op maat",
        "kort_feiten": [
            ("Wat", "Kantoren, winkels, praktijkruimtes, horeca en opslag"),
            ("Timing", "Op de afgesproken datum, ook buiten de openingsuren"),
            ("Prijs", "Offerte na plaatsbezoek, factuur met btw"),
            ("Oplevering", "Netjes opgeleverd, met fotoverslag voor de verhuurder"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Bureaus, kasten, stoelen, rekken, toonbanken en vitrines",
            "Demontage van werkplekken en wandrekken",
            "Elektro en IT-materiaal naar een erkende verwerker",
            "Archief: {{ARCHIEF}}",
            "Bruikbaar meubilair krijgt een tweede leven",
            "Fotoverslag bij de oplevering voor de verhuurder of eigenaar",
        ],
        "foto": ('leeg-kantoor', 'Lege kantoorruimte na een ontruiming', "Een lege verdieping, klaar voor de verhuurder. Laaiop levert op de afgesproken datum op, met foto's als bewijs."),

        "prijs": "Voor bedrijven werken we met een offerte op maat na een plaatsbezoek. Een kleine winkel of een klein kantoor leegmaken kost meestal {{PRIJS_KANTOOR}}. U krijgt een factuur met btw.",
        "faq": [
            ("Kunnen jullie buiten de openingsuren werken?", "Ja. We plannen de ontruiming 's avonds, vroeg in de ochtend of in het weekend, zodat uw zaak zo kort mogelijk dicht is."),
            ("Hoe gaan jullie om met vertrouwelijk archief?", "{{ARCHIEF}}"),
            ("Krijg ik een factuur?", "Ja, een factuur met btw op naam van uw bedrijf."),
            ("Kan bruikbaar meubilair een tweede leven krijgen?", "Ja. Bureaus, stoelen en kasten in goede staat gaan naar een kringwinkel of een goed doel. Dat verlaagt ook de afvoerkosten."),
            ("Werken jullie ook voor makelaars en syndici?", "Ja. Zie onze pagina voor professionals: één aanspreekpunt, vaste afspraken en foto's als bewijs."),
        ],
        "zoekwoorden": ["kantoor leegmaken", "winkelpand leegmaken", "bedrijfsontruiming", "kantoormeubilair afvoeren"],
    },
    {
        "slug": "grofvuil-ophalen",
        "naam": "Grofvuil en losse stukken ophalen",
        "kort": "Grofvuil",
        "tegel": "Een zetel, matras of oude koelkast. We halen het binnen op. Je hoeft het niet op het voetpad te zetten.",
        "icoon": "zetel",
        "toon": "je",
        "seo_titel": "Grofvuil laten ophalen: zetel, matras, koelkast | Laaiop",
        "meta": "Een oude zetel, matras, kast of koelkast laten ophalen? Laaiop haalt het binnen op, ook van de verdieping, en voert het correct af. Prijs per stuk.",
        "h1": "Grofvuil en losse stukken laten ophalen",
        "intro": "Eén oude zetel, een matras of een koelkast: te groot voor de auto, te klein voor een container. Laaiop haalt het op. Binnen, van de verdieping, zonder dat jij moet tillen.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Zetels, matrassen, kasten, bedden, koelkasten, wasmachines"),
            ("Waar ophalen", "Binnen of buiten, ook van de verdieping"),
            ("Prijs", "Per stuk of per laadbeurt"),
            ("Afvoer", "Correct gesorteerd, elektro via Recupel"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Eén stuk of een hele lading",
            "We halen binnen op: jij hoeft niets naar het voetpad te sleuren",
            "Ook van de verdieping, met of zonder lift",
            "Koelkasten en diepvriezers gaan veilig naar Recupel",
            "Bruikbare meubels gaan naar de kringwinkel",
            "Combineer gerust: zetel, matras en kast in dezelfde rit",
        ],
        "foto": ('matras-dragen', 'Man draagt een oude matras door een straat met bakstenen huizen', 'Een matras naar buiten sleuren? Dat hoeft niet. Laaiop haalt grofvuil binnen op, ook van de verdieping.'),

        "prijs": "Voor losse stukken rekenen we per stuk of per laadbeurt. Reken op {{PRIJS_LOSSE_STUKKEN}}, ophalen en afvoer inbegrepen.",
        "faq": [
            ("Komen jullie ook voor één stuk?", "Ja. Eén zetel of één matras is genoeg. Het minimumtarief is {{MINIMUMTARIEF}}."),
            ("Moet het grofvuil buiten klaarstaan?", "Nee. We halen het op waar het staat, ook op zolder of op de derde verdieping."),
            ("Wat gebeurt er met een oude koelkast?", "Koelkasten en diepvriezers bevatten koelgassen. We brengen ze naar een Recupel-inzamelpunt, waar ze veilig verwerkt worden."),
            ("Is dit niet goedkoper via het containerpark?", "Als je zelf een aanhangwagen en twee sterke armen hebt, wel. Zo niet, dan bespaar je met Laaiop een namiddag sleuren en rijden."),
            ("Hoe snel kunnen jullie het ophalen?", "Meestal binnen {{TERMIJN_UITVOERING}}. Vaak combineren we het met een rit in de buurt."),
        ],
        "zoekwoorden": ["grofvuil laten ophalen", "grof huisvuil ophalen", "zetel laten ophalen", "matras ophalen"],
    },
    {
        "slug": "groenafval-ophalen",
        "naam": "Groenafval ophalen",
        "kort": "Groenafval",
        "tegel": "Snoeiafval, takken en tuinafval, ook na een tuinrenovatie.",
        "icoon": "blad",
        "toon": "je",
        "seo_titel": "Groenafval en snoeiafval laten ophalen | Laaiop",
        "meta": "Snoeiafval, takken of tuinafval laten ophalen? Laaiop laadt alles op en brengt het naar de groencompostering. Prijs vooraf, provincie Antwerpen.",
        "h1": "Groenafval en snoeiafval laten ophalen",
        "intro": "De haag is gesnoeid en de boom is gekapt. Nu ligt de oprit vol takken. Laaiop laadt het op en brengt het naar de groencompostering. Jij hoeft niets in zakken te steken.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Snoeiafval, takken, haagscheersel, bladeren en tuinafval"),
            ("Hoe", "Los of in zakken, wij laden alles op"),
            ("Prijs", "Per laadbeurt, vooraf afgesproken"),
            ("Afvoer", "Naar de groencompostering"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Takken, haagscheersel, bladeren en gemaaid gras",
            "Los op een hoop of in zakken: wij laden het op",
            "Ook na een tuinrenovatie of het rooien van een haag",
            "Oude tuinmeubels en bloembakken kunnen mee in dezelfde rit",
            "Afgevoerd naar de groencompostering",
            "We vegen de oprit na",
        ],
        "foto": ('snoeiafval', 'Hoop gesnoeide takken', 'Takken, haagscheersel en snoeiafval: Laaiop laadt het op en brengt het naar de groencompostering.'),

        "prijs": "Groenafval rekenen we per laadbeurt. Een volle camionette kost {{PRIJS_GROEN}}, laden en afvoer inbegrepen.",
        "faq": [
            ("Moet ik het groenafval in zakken doen?", "Nee. Een hoop op de oprit of in de tuin is prima. Wij laden het op."),
            ("Nemen jullie ook boomstronken en aarde mee?", "Kleine stronken wel. Grote hoeveelheden aarde of zware stronken bekijken we op basis van een foto."),
            ("Hoeveel past er in een laadbeurt?", "Dat hangt af van hoe los of samengedrukt het groenafval ligt. Stuur een foto. Dan zeggen we hoeveel ritten er nodig zijn."),
            ("Kan ik regelmatig laten ophalen?", "Ja, bijvoorbeeld na elke snoeibeurt in het voorjaar en het najaar. Vraag ernaar in je bericht."),
        ],
        "zoekwoorden": ["groenafval laten ophalen", "snoeiafval ophalen", "tuinafval afvoeren"],
    },
    {
        "slug": "bouwafval-ophalen",
        "naam": "Bouwafval ophalen",
        "kort": "Bouwafval",
        "tegel": "Puin, hout, gyproc en tegels na een renovatie. Gesorteerd afgevoerd.",
        "icoon": "bakstenen",
        "toon": "je",
        "seo_titel": "Bouwafval en renovatieafval laten ophalen | Laaiop",
        "meta": "Puin, hout, gyproc of een oude keuken laten ophalen? Laaiop laadt bouwafval op en voert het gesorteerd af. Geen container nodig. Prijs vooraf.",
        "h1": "Bouwafval en renovatieafval laten ophalen",
        "intro": "Na een verbouwing blijft er altijd een berg over: puin, oude tegels, gyproc, hout van een oude keuken. Laaiop laadt het op en voert het gesorteerd af. Geen container voor de deur, geen parkeerverbod voor een week.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Puin, tegels, hout, gyproc, isolatie, oude keukens en badkamers"),
            ("Geen container", "Wij laden op en rijden meteen weg"),
            ("Prijs", "Per laadbeurt, vooraf afgesproken"),
            ("Niet", "Asbest: daarvoor is een erkende asbestverwijderaar nodig"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Puin, stenen, tegels en beton in zakken of los",
            "Hout, gyproc, isolatie en oude plafonds",
            "Oude keukens, badkamermeubels en sanitair",
            "Gesorteerd per afvalsoort afgevoerd naar een erkende verwerker",
            "Ook voor aannemers en renovatiebedrijven",
            "Werf of oprit na afloop geveegd",
        ],
        "foto": ('puinzakken', 'Zakken puin en oude betontegels tegen een bakstenen gevel', 'Zakken puin en oude tegels tegen de gevel? Laaiop voert renovatieafval gesorteerd af, zonder container voor de deur.'),

        "prijs": "De prijs voor bouwafval berekenen we per laadbeurt. Hij hangt af van het gewicht en van hoe gemengd het afval is. Gesorteerd afval is goedkoper. Reken op {{PRIJS_BOUW}}.",
        "faq": [
            ("Nemen jullie asbest mee?", "Nee. Asbest mag alleen door een erkende asbestverwijderaar of volgens de regels van je gemeente afgevoerd worden. Twijfel je over golfplaten of oude leien? Stuur een foto, dan zeggen we het je."),
            ("Moet ik het bouwafval sorteren?", "Het hoeft niet, maar het helpt. Puin, hout en gyproc apart zetten maakt de afvoer goedkoper. Dat zie je in de prijs."),
            ("Waarom geen container?", "Een container staat dagen voor de deur en vraagt vaak een parkeerverbod. Wij komen, laden op en rijden weg. Voor kleinere hoeveelheden is dat sneller en vaak goedkoper."),
            ("Werken jullie ook voor aannemers?", "Ja. Voor aannemers en renovatiebedrijven plannen we vaste ophaalmomenten per werf, met factuur."),
        ],
        "zoekwoorden": ["bouwafval laten ophalen", "puin afvoeren", "renovatieafval ophalen"],
    },
    {
        "slug": "meubels-toestellen-leveren",
        "naam": "Meubels en toestellen leveren",
        "kort": "Leveren",
        "tegel": "Wij halen het nieuwe op en nemen het oude meteen mee.",
        "icoon": "koelkast",
        "toon": "je",
        "seo_titel": "Meubels en toestellen laten leveren, oud mee | Laaiop",
        "meta": "Nieuwe koelkast, zetel of kast gekocht? Laaiop haalt hem op, zet hem op zijn plaats en neemt het oude meteen mee. Ook voor aankopen via 2dehands.",
        "h1": "Meubels en toestellen leveren, het oude nemen we mee",
        "intro": "Nieuwe koelkast gekocht? Wij halen hem op in de winkel, zetten hem op zijn plaats en nemen de oude meteen mee. Eén rit, één prijs. Dat doen weinig opruimers.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Wat", "Koelkasten, wasmachines, zetels, kasten, bedden, tafels"),
            ("Van waar", "Winkel, magazijn of verkoper via 2dehands en Marketplace"),
            ("Het oude", "Nemen we in dezelfde rit mee"),
            ("Prijs", "Per levering, vooraf afgesproken"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Ophalen in de winkel, het magazijn of bij een particulier",
            "Tweedehands gekocht? Wij halen het op bij de verkoper",
            "Naar binnen en op zijn plaats gezet, ook op de verdieping",
            "Het oude meubel of toestel nemen we meteen mee",
            "Aansluiten: {{AANSLUITEN}}",
            "Ook voor winkels die hun klanten een levering willen aanbieden",
        ],
        "foto": ('nieuwe-koelkast', 'Nieuwe inox koelkast op zijn plaats in een lichte keuken', 'Nieuwe koelkast op zijn plaats, oude mee naar buiten. Eén rit en één prijs bij Laaiop.'),

        "prijs": "Een levering kost {{PRIJS_LEVERING}}, inclusief het meenemen van je oude toestel of meubel.",
        "faq": [
            ("Halen jullie ook op bij een particulier, bijvoorbeeld via 2dehands?", "Ja. Geef ons het adres van de verkoper en een moment dat past. Wij halen het op en brengen het naar jou."),
            ("Nemen jullie het oude toestel mee?", "Ja, in dezelfde rit. Oude koelkasten en wasmachines brengen we naar een Recupel-inzamelpunt."),
            ("Sluiten jullie het toestel ook aan?", "{{AANSLUITEN}}"),
            ("Is mijn meubel verzekerd tijdens het transport?", "{{VERZEKERING}}"),
            ("Werken jullie samen met winkels?", "Ja. Meubel- en elektrowinkels kunnen hun klanten een levering door Laaiop aanbieden. Neem contact op voor een samenwerking."),
        ],
        "zoekwoorden": ["meubels laten leveren", "koelkast laten leveren", "transport zetel", "oude koelkast meenemen"],
    },
    {
        "slug": "dampkap-afbreken-reinigen",
        "naam": "Dampkap afbreken of reinigen",
        "kort": "Dampkappen",
        "tegel": "We demonteren je vette dampkap of ontvetten ze grondig. Een dienst die andere opruimers niet bieden.",
        "icoon": "dampkap",
        "toon": "je",
        "seo_titel": "Dampkap laten reinigen of afbreken | Laaiop",
        "meta": "Dampkap laten ontvetten of demonteren en afvoeren? Laaiop reinigt filters, kap en ventilator, of breekt de oude dampkap af. Prijs vooraf.",
        "h1": "Dampkap laten reinigen of afbreken",
        "intro": "Een dampkap die jaren vet heeft opgevangen, zuigt slecht en ruikt. Laaiop ontvet je dampkap grondig. Wil je de oude dampkap weg, bijvoorbeeld voor een nieuwe keuken? Dan demonteren we ze en voeren we ze af. Geen enkele andere opruimer in de regio biedt dit aan.",
        "cta": "Vraag je prijs aan",
        "kort_feiten": [
            ("Reinigen", "Filters, binnenkant en ventilator ontvet"),
            ("Afbreken", "Oude dampkap gedemonteerd en afgevoerd"),
            ("Voor wie", "Particulieren, verhuurders en kleine zaken"),
            ("Prijs", "Per dampkap"),
            ("Waar", "Heel de provincie Antwerpen"),
        ],
        "wat": [
            "Vetfilters reinigen of vervangen",
            "Binnenkant van de kap en de ventilator ontvetten",
            "Oude dampkap demonteren, bijvoorbeeld voor een nieuwe keuken",
            "Afvoer van de oude kap, metaal naar de schroothandel",
            "Keuken en werkblad na afloop proper achtergelaten",
            "Te combineren met een volledige keukenontruiming",
        ],
        "foto": ('dampkap', 'Inox dampkap boven een fornuis in een witte keuken', 'Een dampkap die jaren vet opving, zuigt slecht. Laaiop ontvet je dampkap of haalt de oude weg voor je nieuwe keuken.'),

        "prijs": "Een dampkap reinigen of afbreken kost {{PRIJS_DAMPKAP}}. Stuur een foto van de dampkap en vermeld het merk. Dan krijg je een prijsindicatie. De definitieve prijs bevestigen we ter plaatse.",
        "faq": [
            ("Hoe vaak moet een dampkap gereinigd worden?", "De vetfilters reinig je best om de paar maanden. De kap en de ventilator reinig je om de één à twee jaar, afhankelijk van hoeveel je kookt. Een vette kap zuigt slechter en is een brandrisico."),
            ("Wat houdt een reinigingsbeurt in?", "We ontvetten de filters, de binnenkant van de kap en de ventilator. Je keuken laten we proper achter."),
            ("Kunnen jullie ook een nieuwe dampkap plaatsen?", "Nee, plaatsen en aansluiten laten we aan de keukenplaatser of een elektricien. Wij halen de oude weg, zodat zij meteen kunnen beginnen."),
            ("Doen jullie dit ook voor horeca?", "Voor kleine zaken wel. Voor grote horecakeukens met afzuigkanalen is een gespecialiseerd bedrijf nodig. We verwijzen je graag door."),
        ],
        "zoekwoorden": ["dampkap reinigen", "dampkap afbreken", "dampkap ontvetten"],
    },
]

# Dienstnamen voor het formulier (waarde, label)
FORM_DIENSTEN = [
    ("woning", "Woning leegmaken"),
    ("inboedel", "Inboedel"),
    ("garage", "Garage, zolder of kelder"),
    ("kantoor", "Kantoor of winkel"),
    ("losse-stukken", "Losse stukken"),
    ("groenafval", "Groenafval"),
    ("bouwafval", "Bouwafval"),
    ("levering", "Levering"),
    ("dampkap", "Dampkap"),
]
SLUG_NAAR_FORM = {
    "huis-leegmaken-na-overlijden": "woning", "inboedel-opruimen": "inboedel", "appartement-leegmaken": "woning",
    "garage-zolder-kelder-opruimen": "garage", "kantoor-winkelpand-leegmaken": "kantoor", "grofvuil-ophalen": "losse-stukken",
    "groenafval-ophalen": "groenafval", "bouwafval-ophalen": "bouwafval", "meubels-toestellen-leveren": "levering",
    "dampkap-afbreken-reinigen": "dampkap",
}

# Algemene veelgestelde vragen (home en FAQ-pagina)
FAQ_ALGEMEEN = [
    ("Wat kost een ontruiming bij Laaiop?", "Dat hangt af van het volume, de verdieping en wat er weg moet. Op basis van je foto's krijg je eerst een prijsindicatie. De definitieve offerte maken we op locatie, inclusief laden, transport, afvoer en opkuis. Op onze prijzenpagina staan richtprijzen per type opdracht."),
    ("Hoe snel krijg ik een prijs?", "Stuur ons een paar duidelijke foto's via WhatsApp of het formulier. Binnen {{TERMIJN}} krijg je een prijsindicatie. Daarna komen we kijken en maken we de definitieve offerte op locatie."),
    ("Waarom komen jullie ter plaatse?", "Op een foto zie je niet alles: wat er in kasten zit, hoe smal de trap is of waar we kunnen parkeren. Daarom maken we de definitieve offerte altijd op locatie. Zo is de prijs in je offerte ook de prijs die je betaalt."),
    ("Moet ik aanwezig zijn?", "Nee. Je kunt ons de sleutel geven of iemand laten openen. Na afloop krijg je foto's van de lege ruimte."),
    ("Wat gebeurt er met spullen die nog bruikbaar zijn?", "Die krijgen een tweede leven via een kringwinkel of een goed doel. Metaal, hout, elektro en puin gaan elk naar de juiste verwerker. Niets belandt in een berm of bos."),
    ("Zijn jullie verzekerd?", "Ja. {{VERZEKERING}}"),
    ("In welke gemeenten werken jullie?", "In de hele provincie Antwerpen: van Antwerpen en Mechelen tot Lier, Turnhout, Geel, Mol en Herentals, en alle gemeenten daartussen."),
    ("Nemen jullie asbest mee?", "Nee. Asbest vraagt een erkende asbestverwijderaar. Twijfel je? Stuur een foto, dan zeggen we het je."),
    ("Krijg ik een factuur?", "Ja. Particulieren en bedrijven krijgen een factuur. Bedrijven met een btw-nummer krijgen een factuur op naam van het bedrijf."),
]

# Richtprijskaart per dienst: (label, placeholder) + wat inbegrepen is (uit de bestaande teksten)
PRIJS_KAART = {
    "huis-leegmaken-na-overlijden": ([("Appartement", "PRIJS_APPARTEMENT"), ("Gezinswoning", "PRIJS_WONING")], "Inclusief laden, afvoer en opkuis"),
    "inboedel-opruimen": ([("Kamer of berging", "PRIJS_GARAGE"), ("Inboedel appartement", "PRIJS_APPARTEMENT")], "Inclusief demonteren, laden, afvoeren en vegen"),
    "appartement-leegmaken": ([("Appartement", "PRIJS_APPARTEMENT")], "Alles inbegrepen"),
    "garage-zolder-kelder-opruimen": ([("Garage, zolder of kelder", "PRIJS_GARAGE")], "Inclusief afvoer"),
    "kantoor-winkelpand-leegmaken": ([("Kleine winkel of klein kantoor", "PRIJS_KANTOOR")], "Factuur met btw"),
    "grofvuil-ophalen": ([("Losse stukken", "PRIJS_LOSSE_STUKKEN")], "Ophalen en afvoer inbegrepen"),
    "groenafval-ophalen": ([("Volle camionette", "PRIJS_GROEN")], "Laden en afvoer inbegrepen"),
    "bouwafval-ophalen": ([("Per laadbeurt", "PRIJS_BOUW")], "Gesorteerd afval is goedkoper"),
    "meubels-toestellen-leveren": ([("Levering", "PRIJS_LEVERING")], "Inclusief het meenemen van je oude toestel of meubel"),
    "dampkap-afbreken-reinigen": ([("Per dampkap", "PRIJS_DAMPKAP")], "Reinigen of afbreken"),
}
