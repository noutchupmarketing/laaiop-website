/* Laaiop website: menu, formulieren, tracking. Geen externe libraries. */
(function () {
  "use strict";

  // Bij openen van een pagina altijd bovenaan starten (behalve bij een #anker)
  // (scrollTo(0, 0) zonder opties: oudere Safari kent behavior "instant" niet en stopt dan het hele script)
  try { if ("scrollRestoration" in history) history.scrollRestoration = "manual"; } catch (e) {}
  function naarBoven() {
    if (location.hash) return;
    var html = document.documentElement, oud = html.style.scrollBehavior;
    html.style.scrollBehavior = "auto";
    window.scrollTo(0, 0);
    html.style.scrollBehavior = oud;
  }
  naarBoven();
  document.addEventListener("DOMContentLoaded", naarBoven);
  window.addEventListener("pageshow", naarBoven);
  var CFG = window.LAAIOP || {};
  window.dataLayer = window.dataLayer || [];
  function track(event, data) {
    var obj = { event: event };
    for (var k in data || {}) obj[k] = data[k];
    window.dataLayer.push(obj);
  }

  /* Header schaduw bij scrollen */
  var header = document.querySelector(".header");
  if (header) {
    var opScroll = function () { header.classList.toggle("is-gescrold", window.scrollY > 8); };
    window.addEventListener("scroll", opScroll, { passive: true });
    opScroll();
  }

  /* Mobiel menu */
  var menu = document.getElementById("mobielmenu");
  var open = document.querySelectorAll("[data-menu-open]");
  var sluit = document.querySelectorAll("[data-menu-sluit]");
  function zetMenu(aan) {
    if (!menu) return;
    menu.hidden = !aan;
    document.body.style.overflow = aan ? "hidden" : "";
    open.forEach(function (b) { b.setAttribute("aria-expanded", aan ? "true" : "false"); });
    if (aan) { var eerste = menu.querySelector("a, button"); if (eerste) eerste.focus(); }
  }
  open.forEach(function (b) { b.addEventListener("click", function () { zetMenu(true); }); });
  sluit.forEach(function (b) { b.addEventListener("click", function () { zetMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu && !menu.hidden) zetMenu(false); });
  if (menu) menu.addEventListener("click", function (e) { if (e.target.closest("a")) zetMenu(false); });

  /* Dienstenmenu in de header (klik, toetsenbord en hover) */
  var ddKnop = document.querySelector("[data-dropdown]");
  var dd = document.getElementById("dienstenmenu");
  function zetDd(aan) { if (!dd) return; dd.hidden = !aan; ddKnop.setAttribute("aria-expanded", aan ? "true" : "false"); }
  if (ddKnop && dd) {
    ddKnop.addEventListener("click", function (e) { e.stopPropagation(); zetDd(dd.hidden); });
    document.addEventListener("click", function (e) { if (!e.target.closest(".nav__diensten")) zetDd(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !dd.hidden) { zetDd(false); ddKnop.focus(); } });
    var li = ddKnop.closest(".nav__diensten"); var t;
    if (window.matchMedia("(hover: hover)").matches) {
      li.addEventListener("mouseenter", function () { clearTimeout(t); zetDd(true); });
      li.addEventListener("mouseleave", function () { t = setTimeout(function () { zetDd(false); }, 180); });
    }
    li.addEventListener("focusout", function (e) { if (!li.contains(e.relatedTarget)) zetDd(false); });
  }

  /* Menulink naar de pagina waar je al bent: menu dicht en naar het begin van de pagina */
  document.addEventListener("click", function (e) {
    var a = e.target.closest(".header a, .mobielmenu a");
    if (!a || a.hash || a.target || a.origin !== location.origin || a.pathname !== location.pathname) return;
    e.preventDefault();
    zetMenu(false);
    if (dd) zetDd(false);
    window.scrollTo(0, 0);
  });

  /* Footerlijsten dicht op gsm */
  if (window.matchMedia("(max-width: 719px)").matches) document.querySelectorAll(".footer__groep").forEach(function (d) { d.open = false; });

  /* Actiebalk verbergen zolang het toetsenbord open is */
  var tTypt;
  document.addEventListener("focusin", function (e) { if (e.target.matches("input:not([type=radio]):not([type=file]), textarea, select")) { clearTimeout(tTypt); document.body.classList.add("typt"); } });
  document.addEventListener("focusout", function () { tTypt = setTimeout(function () { document.body.classList.remove("typt"); }, 150); });

  /* Klik-tracking voor WhatsApp en telefoon (conversies in GA4 / Google Ads) */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-track]");
    if (!a) return;
    track(a.getAttribute("data-track"), { link_locatie: a.getAttribute("data-locatie") || "onbekend" });
  });

  /* Formulieren */
  document.querySelectorAll("form[data-richtprijs]").forEach(function (form) {
    var stappen = form.querySelectorAll("[data-stap]");
    var indicator = form.querySelectorAll("[data-stap-indicator]");
    var huidig = 0;

    function toonStap(i) {
      huidig = i;
      stappen.forEach(function (s, n) { s.hidden = n !== i; });
      indicator.forEach(function (s, n) { s.classList.toggle("is-actief", n <= i); });
      var st = form.querySelector("[data-stap-tekst]"); if (st) st.textContent = "Stap " + (i + 1) + " van " + stappen.length;
      var vg = form.querySelector("[data-voortgang]"); if (vg) vg.style.width = ((i + 1) / stappen.length * 100) + "%";
      if (stappen.length > 1 && form.dataset.gestart) {
        var r = form.getBoundingClientRect();
        if (r.top < 70 || r.top > window.innerHeight * 0.6) window.scrollTo({ top: window.scrollY + r.top - 90, behavior: "smooth" });
      }
      form.dataset.gestart = "1";
      if (stappen.length > 1) {
        var veld = stappen[i].querySelector("input:not([type=hidden]), select, textarea");
        if (veld && i > 0) veld.focus({ preventScroll: true });
      }
    }

    function fout(veld, tekst) {
      var houder = veld.closest(".veld");
      var melding = houder && houder.querySelector(".veld__fout");
      if (tekst) {
        veld.setAttribute("aria-invalid", "true");
        if (!melding && houder) { melding = document.createElement("p"); melding.className = "veld__fout"; melding.setAttribute("role", "alert"); houder.appendChild(melding); }
        if (melding) melding.textContent = tekst;
      } else {
        veld.removeAttribute("aria-invalid");
        if (melding) melding.remove();
      }
    }

    function controleer(houder) {
      var ok = true;
      houder.querySelectorAll("[required]").forEach(function (veld) {
        var leeg;
        if (veld.type === "radio") {
          leeg = !form.querySelector('input[name="' + veld.name + '"]:checked');
          var groep = veld.closest("fieldset");
          if (groep) {
            var m = groep.querySelector(".veld__fout");
            if (leeg && !m) { m = document.createElement("p"); m.className = "veld__fout"; m.setAttribute("role", "alert"); m.textContent = "Kies een van de mogelijkheden."; groep.appendChild(m); }
            if (!leeg && m) m.remove();
          }
          if (leeg) ok = false;
          return;
        }
        leeg = !veld.value.trim();
        if (leeg) { fout(veld, "Vul dit veld in."); ok = false; return; }
        if (veld.type === "tel" && veld.value.replace(/[^0-9]/g, "").length < 9) { fout(veld, "Dit telefoonnummer lijkt te kort."); ok = false; return; }
        if (veld.type === "email" && veld.value && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(veld.value)) { fout(veld, "Dit e-mailadres klopt niet."); ok = false; return; }
        fout(veld, null);
      });
      if (!ok) { var eerste = houder.querySelector('[aria-invalid="true"], .veld__fout'); if (eerste) eerste.scrollIntoView({ block: "center", behavior: "smooth" }); }
      return ok;
    }

    form.querySelectorAll("[data-volgende]").forEach(function (b) {
      b.addEventListener("click", function () {
        if (controleer(stappen[huidig])) { toonStap(huidig + 1); track("formulier_stap_" + (huidig + 1), { formulier: form.getAttribute("data-richtprijs") }); }
      });
    });
    form.querySelectorAll("[data-vorige]").forEach(function (b) {
      b.addEventListener("click", function () { toonStap(huidig - 1); });
    });
    form.addEventListener("input", function (e) { if (e.target.getAttribute("aria-invalid")) fout(e.target, null); });
    form.addEventListener("change", function (e) {
      if (e.target.type === "radio") { var g = e.target.closest("fieldset"); var m = g && g.querySelector(".veld__fout"); if (m) m.remove(); }
      // Dienst gekozen in stap 1: meteen door naar stap 2
      if (e.target.type === "radio" && stappen.length > 1 && huidig === 0) setTimeout(function () { toonStap(1); track("formulier_stap_2", { formulier: form.getAttribute("data-richtprijs") }); }, 220);
    });

    /* Foto's: voorbeeldjes, maximum 10, wissen en duidelijke fouten */
    var upload = form.querySelector('input[type="file"]');
    var voorbeelden = form.querySelector(".voorbeelden");
    var zone = upload && upload.closest(".upload");
    var wis = form.querySelector("[data-wis-fotos]");
    var teller = zone && zone.querySelector("[data-teller]");
    function toonFout(tekst) {
      var houder = upload.closest(".veld"); var f = houder.querySelector(".upload__fout");
      if (!tekst) { if (f) f.remove(); return; }
      if (!f) { f = document.createElement("p"); f.className = "upload__fout"; f.setAttribute("role", "alert"); houder.appendChild(f); }
      f.textContent = tekst;
    }
    if (upload && voorbeelden) {
      upload.addEventListener("change", function () {
        voorbeelden.innerHTML = "";
        var alle = Array.prototype.slice.call(upload.files || []);
        var beelden = alle.filter(function (f) { return /^image\//.test(f.type); });
        var fouten = [];
        if (beelden.length < alle.length) fouten.push("Alleen foto's kunnen mee.");
        if (beelden.length > 10) fouten.push("Maximum 10 foto's: we nemen de eerste 10.");
        toonFout(fouten.join(" "));
        beelden.slice(0, 10).forEach(function (f) {
          var img = document.createElement("img");
          img.alt = "Voorbeeld van " + f.name;
          img.src = URL.createObjectURL(f);
          voorbeelden.appendChild(img);
        });
        var n = Math.min(beelden.length, 10);
        if (teller) teller.textContent = n ? n + (n === 1 ? " foto gekozen" : " foto's gekozen") : "Tot 10 foto's";
        if (wis) wis.hidden = !alle.length;
        if (zone) zone.classList.toggle("is-gevuld", n > 0);
      });
      if (wis) wis.addEventListener("click", function () {
        upload.value = ""; voorbeelden.innerHTML = ""; wis.hidden = true; toonFout(null);
        if (teller) teller.textContent = "Tot 10 foto's"; if (zone) zone.classList.remove("is-gevuld");
      });
      if (zone) {
        ["dragenter", "dragover"].forEach(function (ev) { zone.addEventListener(ev, function () { zone.classList.add("is-sleep"); }); });
        ["dragleave", "drop"].forEach(function (ev) { zone.addEventListener(ev, function () { zone.classList.remove("is-sleep"); }); });
      }
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!controleer(stappen.length ? stappen[huidig] : form)) return;
      var knop = form.querySelector('button[type="submit"]');
      if (knop) { knop.disabled = true; knop.dataset.tekst = knop.textContent; knop.textContent = "Even geduld..."; }
      track("formulier_verzonden", { formulier: form.getAttribute("data-richtprijs") });
      var naarBedankt = function () { window.location.href = form.getAttribute("data-bedankt"); };
      if (!CFG.formEndpoint) { setTimeout(naarBedankt, 400); return; }
      fetch(CFG.formEndpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw new Error("status " + r.status); naarBedankt(); })
        .catch(function () {
          if (knop) { knop.disabled = false; knop.textContent = knop.dataset.tekst; }
          var m = form.querySelector(".formulier__melding");
          if (!m) { m = document.createElement("p"); m.className = "veld__fout formulier__melding"; m.setAttribute("role", "alert"); form.appendChild(m); }
          m.textContent = "Verzenden lukte niet. Probeer opnieuw, of stuur je foto's via WhatsApp.";
        });
    });

    if (stappen.length) toonStap(0);
  });

  /* Dienst vooraf aanvinken via ?dienst= (bv. vanuit een dienstpagina) */
  try {
    var dienst = new URLSearchParams(window.location.search).get("dienst");
    if (dienst) { var r = document.querySelector('input[name="dienst"][value="' + dienst.replace(/"/g, "") + '"]'); if (r) r.checked = true; }
  } catch (e) { /* oude browser */ }

  /* Cookiebanner + Consent Mode v2: alleen als er tracking is ingesteld */
  if (CFG.gtmId) {
    var KEUZE = "laaiop_cookiekeuze";
    var bewaard = null;
    try { bewaard = localStorage.getItem(KEUZE); } catch (e) {}
    var pas = function (ja) {
      window.gtag && window.gtag("consent", "update", { ad_storage: ja ? "granted" : "denied", analytics_storage: ja ? "granted" : "denied", ad_user_data: ja ? "granted" : "denied", ad_personalization: ja ? "granted" : "denied" });
    };
    if (bewaard) { pas(bewaard === "ja"); }
    else {
      var b = document.getElementById("cookie");
      if (b) {
        b.hidden = false;
        b.addEventListener("click", function (e) {
          var k = e.target.closest("[data-cookie]"); if (!k) return;
          var ja = k.getAttribute("data-cookie") === "ja";
          try { localStorage.setItem(KEUZE, ja ? "ja" : "nee"); } catch (err) {}
          pas(ja); b.hidden = true;
        });
      }
    }
  }

  // FAQ-pagina: groep openklappen als je via een onderwerp-link of #anker binnenkomt
  function openGroep() {
    if (!location.hash) return;
    var el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (el && el.tagName === "DETAILS") { el.open = true; el.scrollIntoView(); }
  }
  openGroep();
  window.addEventListener("hashchange", openGroep);
})();

/* Beweging (technieken van notchup.be). Werkt alleen als de head de klasse "beweeg" zette,
   dus niet bij beperkte beweging. Alles is een laag bovenop de inhoud: zonder deze code staat alles er gewoon. */
(function () {
  "use strict";
  var w = document.documentElement;
  if (!w.classList.contains("beweeg") || !("IntersectionObserver" in window)) return;
  var CFG = window.LAAIOP || {};
  var fijn = !!(window.matchMedia && window.matchMedia("(hover: hover) and (pointer: fine)").matches);
  var elk = function (sel, f, wortel) { Array.prototype.forEach.call((wortel || document).querySelectorAll(sel), f); };
  var klem = function (v) { return v < 0 ? 0 : v > 1 ? 1 : v; };
  var metIntro = w.classList.contains("intro") && !w.classList.contains("intro--klaar");
  function naIntro(f) {
    if (!w.classList.contains("intro") || w.classList.contains("intro--klaar")) f();
    else document.addEventListener("laaiop:klaar", f, { once: true });
  }
  function kijk(sel, opties, klaar) {
    var o = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { klaar(e.target); o.unobserve(e.target); } });
    }, opties);
    elk(sel, function (el) { o.observe(el); });
  }
  // Staat het al in beeld bij het laden (zonder laadscherm)? Dan niet eerst verbergen, anders knippert het.
  function alInBeeld(el) { var r = el.getBoundingClientRect(); return !metIntro && r.top < window.innerHeight && r.bottom > 0; }

  /* Koppen: woord per woord uit een masker omhoog */
  function splits(el) {
    var n = 0;
    (function loop(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (k) {
        if (k.nodeType === 3) {
          var frag = document.createDocumentFragment();
          k.textContent.split(/(\s+)/).forEach(function (d) {
            if (!d) return;
            if (/^\s+$/.test(d)) { frag.appendChild(document.createTextNode(d)); return; }
            var buiten = document.createElement("span"); buiten.className = "w";
            var binnen = document.createElement("span"); binnen.className = "w__in";
            binnen.style.setProperty("--w", n++);
            binnen.textContent = d;
            buiten.appendChild(binnen); frag.appendChild(buiten);
          });
          node.replaceChild(frag, k);
        } else if (k.nodeType === 1 && !/^(svg|br)$/i.test(k.tagName)) { loop(k); }
      });
    })(el);
    el.classList.add("gesplitst");
  }
  var KOPPEN = "main .kop h2, main .feature__tekst h2, main .rustig h2, main .prijsblok h2, main .lokaal h2, .slotcta__titel";
  elk("main h1, .statement__tekst", splits);
  elk(KOPPEN, function (h) {
    splits(h);
    if (alInBeeld(h)) h.classList.add("in-beeld");
  });
  naIntro(function () { setTimeout(function () { elk("main h1", function (h) { h.classList.add("in-beeld"); }); }, metIntro ? 250 : 0); });
  kijk(KOPPEN.split(", ").map(function (s) { return s + ":not(.in-beeld)"; }).join(", "), { rootMargin: "0px 0px -10% 0px", threshold: 0.2 }, function (el) { el.classList.add("in-beeld"); });
  kijk(".voet__woord", { threshold: 0.1 }, function (el) { el.classList.add("in-beeld"); });

  /* Onthullen bij scrollen; blokken naast elkaar komen na elkaar binnen */
  var ONTHUL = [".strook li", ".kop", ".tegel", ".ingang", ".stap", ".feature__tekst", ".feature__beeld", ".prijskaart", ".review", ".googlescore",
    ".faq details", ".factor", ".situatie", ".inhetkort", ".dienstprijs", ".prijsblok__tekst", ".prijsblok .formulier", ".gerelateerd a", ".tips li",
    ".artikel > *", ".lokaal .stapel", ".rustig", ".foto", ".gemeenten > div", ".realisaties > *", ".twee > *", ".faqnav", ".faqgroep", ".tabelhouder", ".cta-rij"];
  var items = [];
  elk(ONTHUL.map(function (s) { return "main " + s; }).join(", "), function (el) {
    if (el.closest(".hero, .paginahero, .onthul") || el.querySelector(".onthul") || alInBeeld(el)) return;
    el.classList.add("onthul"); items.push(el);
  });
  elk("main .fotokader, main .lokaal__beeld, main .voorna", function (el) {
    if (el.closest(".hero, .paginahero") || alInBeeld(el)) return;
    el.classList.add("onthul-beeld"); items.push(el);
  });
  items.forEach(function (el) {
    var p = el.parentElement;
    if (!p || p.lgGeteld) return;
    p.lgGeteld = true;
    var broers = Array.prototype.filter.call(p.children, function (c) { return c.classList.contains("onthul"); });
    if (broers.length > 1) broers.forEach(function (b, i) { b.style.setProperty("--i", i % 6); });
  });
  var waarnemer = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("zichtbaar"); waarnemer.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
  naIntro(function () { items.forEach(function (el) { waarnemer.observe(el); }); });

  /* Hero: het WhatsApp-gesprek speelt zich af, met "aan het typen" tussen de berichten */
  (function () {
    var chat = document.querySelector(".hero .gsm__chat");
    if (!chat) return;
    var bellen = Array.prototype.slice.call(chat.querySelectorAll(".bel")).filter(function (b) { return getComputedStyle(b).display !== "none"; });
    if (bellen.length < 2) return;
    bellen.forEach(function (b) { b.classList.add("is-wacht"); });
    var typen = document.createElement("div");
    typen.className = "bel bel--zij bel--typen is-wacht";
    typen.setAttribute("aria-hidden", "true");
    typen.innerHTML = "<i></i><i></i><i></i>";
    function toon(el) { el.classList.remove("is-wacht"); el.classList.add("is-nieuw"); }
    naIntro(function () {
      var t = 900;
      bellen.forEach(function (b) {
        if (b.classList.contains("bel--zij")) {
          setTimeout(function () { typen.style.top = b.offsetTop + "px"; b.parentNode.appendChild(typen); toon(typen); }, t);
          t += 1100;
          setTimeout(function () {
            typen.remove(); toon(b);
            var prijs = b.querySelector(".bel__prijs .ph"); if (prijs) prijs.classList.add("is-nieuw");
          }, t);
        } else {
          setTimeout(function () { toon(b); }, t);
        }
        t += 900;
      });
    });
  })();

  /* Scrollvoortgang in de menubalk, statement kleurt in, gekleurde secties vouwen open */
  var header = document.querySelector(".header");
  var lijn = null;
  if (header) {
    lijn = document.createElement("span");
    lijn.className = "scrollbalk";
    lijn.setAttribute("aria-hidden", "true");
    header.appendChild(lijn);
  }
  var statement = document.querySelector(".statement__tekst");
  var stWoorden = statement ? statement.querySelectorAll(".w__in") : [];
  var vlakken = document.querySelectorAll(".sectie--perzik, .slotcta, .sectie--donker");
  var wacht = false;
  function scrol() {
    wacht = false;
    var y = window.scrollY, vh = window.innerHeight, max = document.documentElement.scrollHeight - vh;
    if (lijn) lijn.style.transform = "scaleX(" + (max > 0 ? Math.min(1, y / max) : 0).toFixed(4) + ")";
    if (statement) {
      var r = statement.getBoundingClientRect();
      if (r.top < vh && r.bottom > 0) {
        var n = Math.round(klem((vh * 0.85 - r.top) / (vh * 0.6)) * stWoorden.length);
        Array.prototype.forEach.call(stWoorden, function (wd, i) { wd.classList.toggle("aan", i < n); });
      }
    }
    Array.prototype.forEach.call(vlakken, function (d) {
      var r = d.getBoundingClientRect();
      if (r.top > vh || r.bottom < 0) return;
      var q = klem((vh - r.top) / (vh * 0.65));
      d.style.setProperty("--dx", ((1 - q) * Math.min(56, window.innerWidth * 0.05)).toFixed(1) + "px");
      d.style.setProperty("--dr", ((1 - q) * 40).toFixed(1) + "px");
    });
  }
  window.addEventListener("scroll", function () { if (!wacht) { wacht = true; requestAnimationFrame(scrol); } }, { passive: true });
  window.addEventListener("resize", scrol);
  scrol();

  /* Looptekst: snelheid en richting volgen je scrollbeweging */
  (function () {
    var band = document.querySelector(".band");
    if (!band) return;
    var sporen = band.querySelectorAll(".band__spoor");
    band.classList.add("band--js");
    var stand = Array.prototype.map.call(sporen, function () { return 0; });
    var vorigeY = window.scrollY, snelheid = 0, richting = 1, zichtbaar = false, loopt = false;
    function stap() {
      var y = window.scrollY, dy = y - vorigeY;
      vorigeY = y;
      if (dy) richting = dy > 0 ? 1 : -1;
      snelheid += (Math.min(28, Math.abs(dy) * 0.45) - snelheid) * 0.1;
      Array.prototype.forEach.call(sporen, function (sp, i) {
        var set = sp.firstElementChild, breed = set ? set.offsetWidth : 0;
        if (!breed) return;
        var r = parseFloat(sp.getAttribute("data-richting")) || 1;
        stand[i] -= (0.8 + snelheid) * r * richting;
        if (stand[i] <= -breed) stand[i] += breed;
        if (stand[i] > 0) stand[i] -= breed;
        sp.style.transform = "translate3d(" + stand[i].toFixed(1) + "px,0,0)";
      });
      if (zichtbaar) requestAnimationFrame(stap); else loopt = false;
    }
    new IntersectionObserver(function (e) {
      zichtbaar = e[0].isIntersecting;
      if (zichtbaar && !loopt) { loopt = true; vorigeY = window.scrollY; requestAnimationFrame(stap); }
    }).observe(band);
  })();

  /* Knoppen: tekst rolt bij hover (niet de verzendknoppen: het formulier zet daar zelf tekst op) */
  elk(".knop", function (k) {
    if (k.type === "submit") return;
    var t = null;
    Array.prototype.forEach.call(k.childNodes, function (c) { if (c.nodeType === 3 && c.textContent.trim()) t = c; });
    if (!t) return;
    var rol = document.createElement("span"); rol.className = "knop__rol";
    var binnen = document.createElement("span"); binnen.textContent = t.textContent.trim();
    var kopie = document.createElement("span"); kopie.className = "knop__kopie"; kopie.setAttribute("aria-hidden", "true");
    kopie.textContent = binnen.textContent;
    rol.appendChild(binnen); rol.appendChild(kopie);
    k.replaceChild(rol, t);
  });

  /* Bedankt: dozen en confetti in de Laaiop-kleuren */
  (function () {
    var icoon = document.querySelector(".bedankt-icoon");
    if (!icoon || !Element.prototype.animate || CFG.rustig) return;
    naIntro(function () {
      setTimeout(function () {
        var r = icoon.getBoundingClientRect(), kleuren = ["#FF6B2C", "#14213D", "#FFE3D6", "#2E4A7D"];
        var vak = document.createElement("div");
        vak.className = "confetti"; vak.setAttribute("aria-hidden", "true");
        document.body.appendChild(vak);
        for (var i = 0; i < 42; i++) {
          var s = document.createElement("i"), maat = 7 + Math.random() * 10;
          s.style.cssText = "left:" + (r.left + r.width / 2) + "px;top:" + (r.top + r.height / 2) + "px;width:" + maat + "px;height:" + maat + "px;background:" + kleuren[i % kleuren.length];
          vak.appendChild(s);
          var hoek = Math.random() * Math.PI * 2, kracht = 110 + Math.random() * 240;
          var dx = Math.cos(hoek) * kracht, dy = Math.sin(hoek) * kracht - 150;
          s.animate([
            { transform: "translate(-50%,-50%) rotate(0deg) scale(.4)", opacity: 1 },
            { transform: "translate(calc(-50% + " + dx.toFixed(0) + "px),calc(-50% + " + dy.toFixed(0) + "px)) rotate(" + (Math.random() * 540 - 270).toFixed(0) + "deg) scale(1)", opacity: 1, offset: 0.55 },
            { transform: "translate(calc(-50% + " + (dx * 1.2).toFixed(0) + "px),calc(-50% + " + (dy + 320).toFixed(0) + "px)) rotate(" + (Math.random() * 900 - 450).toFixed(0) + "deg) scale(.8)", opacity: 0 }
          ], { duration: 1500 + Math.random() * 700, easing: "cubic-bezier(.2,.7,.3,1)", fill: "forwards" });
        }
        setTimeout(function () { vak.remove(); }, 2600);
      }, 500);
    });
  })();

  if (!fijn) return;

  /* Knoppen trekken licht naar de muis */
  elk(".knop", function (k) {
    if (k.closest(".cookie, .mobielmenu, .actiebalk")) return;
    k.addEventListener("pointermove", function (e) {
      var r = k.getBoundingClientRect();
      k.style.setProperty("--kx", (((e.clientX - r.left) / r.width - 0.5) * 12).toFixed(1) + "px");
      k.style.setProperty("--ky", (((e.clientY - r.top) / r.height - 0.5) * 10).toFixed(1) + "px");
    });
    k.addEventListener("pointerleave", function () { k.style.setProperty("--kx", "0px"); k.style.setProperty("--ky", "0px"); });
  });

  /* Licht dat de muis volgt over kaarten */
  document.addEventListener("pointermove", function (e) {
    var k = e.target.closest && e.target.closest(".tegel, .review, .factor, .ingang, .situatie, .stap");
    if (!k) return;
    var r = k.getBoundingClientRect();
    k.style.setProperty("--mx", (e.clientX - r.left).toFixed(0) + "px");
    k.style.setProperty("--my", (e.clientY - r.top).toFixed(0) + "px");
  }, { passive: true });

  /* Diensttegels kantelen in 3D */
  elk(".tegel", function (k) {
    k.addEventListener("pointermove", function (e) {
      var r = k.getBoundingClientRect();
      k.style.setProperty("--tx", (((e.clientY - r.top) / r.height - 0.5) * -7).toFixed(2) + "deg");
      k.style.setProperty("--ty", (((e.clientX - r.left) / r.width - 0.5) * 9).toFixed(2) + "deg");
    });
    k.addEventListener("pointerleave", function () { k.style.setProperty("--tx", "0deg"); k.style.setProperty("--ty", "0deg"); });
  });

  /* Het WhatsApp-gesprek in de hero kantelt mee met de muis */
  var held = document.querySelector(".heldbeeld"), kaart = held && held.querySelector(".chatkaart");
  if (kaart) {
    held.addEventListener("pointermove", function (e) {
      var r = held.getBoundingClientRect();
      kaart.style.setProperty("--rx", (((e.clientY - r.top) / r.height - 0.5) * -6).toFixed(2) + "deg");
      kaart.style.setProperty("--ry", (((e.clientX - r.left) / r.width - 0.5) * 8).toFixed(2) + "deg");
    });
    held.addEventListener("pointerleave", function () { kaart.style.setProperty("--rx", "0deg"); kaart.style.setProperty("--ry", "0deg"); });
  }

  /* Op rustige pagina's (na overlijden, professionals) geen speelse extra's */
  if (CFG.rustig) return;

  /* Letters van het woordmerk springen op */
  elk(".voet__woord span", function (l) {
    l.addEventListener("pointerenter", function () { l.classList.remove("wip"); void l.offsetWidth; l.classList.add("wip"); });
    l.addEventListener("animationend", function () { l.classList.remove("wip"); });
  });

  /* Cursorvolger: oranje bolletje, ring op links, "Bekijk" op diensten */
  var volger = document.createElement("div");
  volger.className = "volger";
  volger.setAttribute("aria-hidden", "true");
  volger.innerHTML = '<span class="volger__vorm"><span class="volger__tekst">Bekijk</span></span>';
  document.body.appendChild(volger);
  var mx = -200, my = -200, vx = mx, vy = my;
  document.addEventListener("pointermove", function (e) {
    mx = e.clientX; my = e.clientY;
    volger.classList.add("aan");
    var t = e.target.closest ? e.target : null;
    var kaartje = t && t.closest(".tegel");
    var link = t && t.closest("a, button, summary, input, select, textarea, label");
    volger.classList.toggle("volger--kaart", !!kaartje);
    volger.classList.toggle("volger--link", !kaartje && !!link);
  }, { passive: true });
  w.addEventListener("mouseleave", function () { volger.classList.remove("aan"); });
  (function volg() {
    vx += (mx - vx) * 0.2; vy += (my - vy) * 0.2;
    volger.style.transform = "translate3d(" + vx.toFixed(1) + "px," + vy.toFixed(1) + "px,0)";
    requestAnimationFrame(volg);
  })();
})();
