// Vercel-functie: ontvangt het contactformulier en mailt de aanvraag (met foto's als bijlage) via Resend.
// Instellen in Vercel > Settings > Environment Variables:
//   RESEND_API_KEY  (verplicht)  sleutel van resend.com
//   MAIL_TO         (optioneel)  standaard info@laaiop.be
//   MAIL_FROM       (optioneel)  bv. "Laaiop website <formulier@laaiop.be>" zodra laaiop.be geverifieerd is in Resend

const MAIL_TO = process.env.MAIL_TO || "info@laaiop.be";
const MAIL_FROM = process.env.MAIL_FROM || "Laaiop website <onboarding@resend.dev>";
const MAX_FOTOS = 10;

const esc = (s) => String(s || "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const json = (status, data) => Response.json(data, { status });

export async function POST(request) {
  if (!process.env.RESEND_API_KEY) return json(500, { ok: false, fout: "RESEND_API_KEY ontbreekt" });

  let form;
  try { form = await request.formData(); } catch { return json(400, { ok: false, fout: "Ongeldig formulier" }); }

  // Honeypot: echte bezoekers zien dit veld niet
  if (form.get("website")) return json(200, { ok: true });

  const veld = (k) => String(form.get(k) || "").trim().slice(0, 4000);
  const naam = veld("naam"), telefoon = veld("telefoon"), email = veld("email");
  if (!naam || !telefoon) return json(400, { ok: false, fout: "Naam en telefoon zijn verplicht" });

  const rijen = [
    ["Dienst", veld("dienst")],
    ["Gemeente", veld("gemeente")],
    ["Naam", naam],
    ["Telefoon", telefoon],
    ["E-mail", email],
    ["Bericht", veld("bericht")],
    ["Pagina", veld("pagina")],
  ].filter(([, v]) => v);

  const fotos = form.getAll("fotos").filter((f) => f && typeof f === "object" && f.size > 0).slice(0, MAX_FOTOS);
  const bijlagen = await Promise.all(fotos.map(async (f, i) => ({
    filename: f.name || `foto-${i + 1}.jpg`,
    content: Buffer.from(await f.arrayBuffer()).toString("base64"),
  })));

  const html = `<h2>Nieuwe aanvraag via laaiop.be</h2>
<table cellpadding="6" style="border-collapse:collapse;font-family:sans-serif;font-size:15px">
${rijen.map(([k, v]) => `<tr><td style="color:#666;vertical-align:top"><strong>${esc(k)}</strong></td><td style="white-space:pre-wrap">${esc(v)}</td></tr>`).join("\n")}
</table>
<p style="font-family:sans-serif;color:#666">${bijlagen.length ? bijlagen.length + " foto('s) als bijlage." : "Geen foto's meegestuurd."}</p>`;
  const text = rijen.map(([k, v]) => `${k}: ${v}`).join("\n") + `\n\n${bijlagen.length} foto('s) als bijlage.`;

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: MAIL_FROM,
      to: MAIL_TO.split(",").map((s) => s.trim()),
      reply_to: /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) ? email : undefined,
      subject: `Aanvraag: ${veld("dienst") || "contact"} - ${naam}${veld("gemeente") ? " (" + veld("gemeente") + ")" : ""}`,
      html, text,
      attachments: bijlagen.length ? bijlagen : undefined,
    }),
  });
  if (!r.ok) {
    console.error("Resend fout", r.status, await r.text());
    return json(502, { ok: false, fout: "Mail versturen mislukt" });
  }
  return json(200, { ok: true });
}
