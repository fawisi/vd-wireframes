# Winzer-Shop Wireframe Prototyp — Projektdokumentation

## Projektbeschreibung

HTML/CSS-Wireframe-Prototyp zur Veranschaulichung der idealen Informationsarchitektur und Seitenstruktur eines Familienweingut-Onlineshops. Der Prototyp dient als Kommunikationsmittel zwischen UX/Strategie und Design/Entwicklung.

**Auftraggeber:** Fabian Willis-Simon
**Projekt:** VD FFM Shop-Wireframes
**Status:** Phase 5 — Finales Polish & Konsistenz-Check abgeschlossen, alle Seiten fertig
**Letztes Update:** 2026-03-03

---

## Technischer Stack

- **Reine HTML5 + CSS3** (kein Framework, kein Build-Tool)
- **Fonts:** Google Fonts — Cormorant Garamond (Display) + Outfit (Body)
- **Design:** Minimales Wireframe-Aesthetic mit grünen Bild-Platzhaltern (`#E8EFEA`)
- **JS:** IntersectionObserver (Fade-in), Sticky Header, Smooth Scroll, Cart Drawer, Widerrufs-Formular
- **Server:** Python3 HTTP-Server auf `/tmp/wf-site/` (macOS Sandbox-Workaround)
- **Bilder:** Alle durch grüne Platzhalter (`.ph-img`) ersetzt — keine echten Bilder mehr im HTML

---

## Dateistruktur

```
/Users/fabianwillisimon/Documents/VD Wireframes/
  index.html              — Startseite (Homepage) ✅ FERTIG
  kategorie.html          — Kategorie-/Listing-Seite (Weine) ✅ FERTIG
  produktseite.html       — Produktdetailseite ✅ FERTIG
  ueber-uns.html          — Über Uns (Weingut, Team, Terroir) ✅ FERTIG
  events.html             — Events & Weinproben ✅ FERTIG
  kontakt.html            — Kontaktseite ✅ FERTIG
  widerrufsrecht.html     — Vertrag widerrufen (§356a BGB) ✅ FERTIG
  styles.css              — Shared CSS Design System ✅
  PROJEKTPLAN.md          — Diese Dokumentation
  BILD-PROMPTS.md         — 63 detaillierte Bild-Prompts (für spätere KI-Generierung)
  serve.py                — Python3 Dev-Server
  server.rb               — Ruby Dev-Server (Alternative)
  winzer-shop-wireframe.html — Original-Wireframe (Archiv, nicht mehr aktiv)
  .claude/launch.json     — Dev-Server-Konfiguration

  img/                    — 63 Platzhalterbilder (von picsum.photos, aktuell nicht im HTML verwendet)
```

### Dev-Server starten

```bash
# 1. Dateien nach /tmp/wf-site/ kopieren (macOS Sandbox-Workaround)
mkdir -p /tmp/wf-site
for f in index.html kategorie.html produktseite.html ueber-uns.html events.html kontakt.html widerrufsrecht.html styles.css; do
  cp "/Users/fabianwillisimon/Documents/VD Wireframes/$f" /tmp/wf-site/
done

# 2. Server starten
python3 /tmp/wf/serve.py
# -> http://localhost:8080
```

Claude Code launch.json Config: `.claude/launch.json` mit `"wireframe-preview"` auf Port 8080.

---

## Platzhalter-System

### Bild-Platzhalter (`.ph-img`)
Alle echten Bilder (background-image, picsum.photos) wurden durch einheitliche grüne Platzhalter ersetzt:

```css
.ph-img {
  background: #E8EFEA;
  border: 1.5px dashed #B8C8BA;
  border-radius: var(--r);
  display: flex; align-items: center; justify-content: center;
  flex-direction: column; gap: 6px;
  color: #8A9E8E; font-size: 0.8rem;
}
```

Jeder Platzhalter enthält ein SVG-Icon und eine Beschreibung des geplanten Inhalts:
```html
<div class="ph-img" style="height:480px;">
  <svg>...</svg>
  <span>Hero-Bild — 480px / Weingut-Panorama oder Winzerfamilie im Weinberg</span>
</div>
```

### Wireframe-Anmerkungen (`.note`)
Gelbe Sticky-Notes mit 📌 Pin-Icon für Wireframe-spezifische Hinweise:
```html
<div class="note">Alternativ: Auch als Paket oder Kennenlernset darstellbar</div>
```

---

## Globale Elemente (auf allen 7 Seiten konsistent)

### 1. Announcement Bar
Schmaler Banner oben: "Versandkostenfrei ab 69 € | Jetzt Kennenlernpaket sichern"

### 2. Header + Mega Menu
- Sticky Header mit Blur-Backdrop
- Navigation: Startseite, Weine (mit Mega Menu), Weingut, Über Uns, Events, Kontakt
- Mega Menu: 5 Spalten (Sortiment, Terroir, Sonstiges, Qualitätsstufen + Paket-Teaser)
- Icons: Suche, Mein Konto, Warenkorb (mit Badge "2" + `onclick="openCartDrawer()"`)

### 3. Cart Drawer (Warenkorb)
Auf ALLEN 7 Seiten identischer HTML/JS-Block:
- Slide-in von rechts (CSS transform), Overlay dahinter
- 2 Beispiel-Produkte: Riesling Spätlese 2023 (14,90 €), Grauburgunder trocken 2023 (10,90 €)
- Mengensteuerung (+/- Buttons)
- Upsell-Sektion: "Das könnte dir auch gefallen" mit Chardonnay Réserve + Kennenlernpaket
- Zwischensumme: 36,70 €, Versandhinweis, "Zur Kasse" + "Weiter einkaufen"
- ESC-Taste zum Schließen

```javascript
function openCartDrawer(){...}
function closeCartDrawer(){...}
document.addEventListener('keydown', function(e){ if(e.key==='Escape') closeCartDrawer(); });
```

### 4. Newsletter-Formular
Auf 5 Seiten (index, kategorie, produktseite, ueber-uns, events):
- **2-Spalten-Grid-Layout:** Links Infotext (`nl__text`), rechts Formular (`nl__form`)
- Headline: "Newsletter & 10 % Rabatt"
- Beschreibung: "Erhalten Sie exklusive Angebote, Weinempfehlungen und Einladungen zu Events — max. 2x im Monat."
- Formular: Vorname + Nachname (2-spaltig via `nl__form-row`), E-Mail-Adresse, Button "Anmelden und 10 % Rabatt sichern"
- Alle Inputs + Button einheitlich `height: 44px`
- Legal: "Mit der Anmeldung stimmen Sie unserer Datenschutzerklärung zu. Abmeldung jederzeit möglich."
- **Responsive:** Unter 768px stapelt sich alles in einer Spalte, Text zentriert

### 5. Footer
4-spaltiges Grid:
- Spalte 1: Logo, Beschreibung, Adresse, Telefon, E-Mail
- Spalte 2: Service (Kontakt → kontakt.html, FAQ, Versand, Retouren, Gutscheine, Weinberatung)
- Spalte 3: Lieferung & Zahlung (Versandkostenfrei ab 69 €, 2-4 Werktage, Klimaneutral, SSL, Rechnung, Ratenzahlung)
- Spalte 4: Unternehmen (Über Uns → ueber-uns.html, Nachhaltigkeit, Events → events.html, Presse, Karriere, Händler)
- Bottom: Impressum, Datenschutz, AGB, **"Vertrag widerrufen"** → widerrufsrecht.html (als Button-Link `.footer__widerruf`), © 2026
- Payment: VISA, MC, PayPal, Klarna, DHL, DPD
- Social: Instagram, Facebook, YouTube

### 6. SVG-Qualitätspyramide
Auf 4 Seiten (index, ueber-uns, produktseite = dark; kategorie = light):

**Dark-Variante** (section--dark Hintergrund):
```html
<svg viewBox="0 0 400 300" style="width:100%;max-width:400px;">
  <polygon points="200,10 380,290 20,290" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1.5"/>
  <line x1="140" y1="103" x2="260" y2="103" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
  <line x1="80" y1="196" x2="320" y2="196" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
  <polygon points="200,10 260,103 140,103" fill="rgba(255,255,255,0.12)"/>
  <polygon points="140,103 260,103 320,196 80,196" fill="rgba(255,255,255,0.06)"/>
  <polygon points="80,196 320,196 380,290 20,290" fill="rgba(255,255,255,0.02)"/>
  <!-- Lagenwein (oben), Ortswein (mitte), Gutswein (unten) -->
</svg>
```

Wording in allen Pyramiden identisch:
- Lagenwein: "PRESTIGE AUS EINZELLAGEN"
- Ortswein: "CHARAKTER UNSERER BESTEN LAGEN"
- Gutswein: "VIELSEITIGE ALLTAGSBEGLEITER"

**Light-Variante** (kategorie.html): Gleiche Geometrie, aber `var(--gray-900)` Text, `var(--gray-*)` Fills.

---

## Seitenübersicht (aktueller Stand)

### 1. Startseite (`index.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu
3. Hero (2-spaltig: Headline, Subheadline, 3 USPs, 2 Buttons, 4 Avatar-Icons + 4,9/5 Bewertungen)
4. Trust Bar ("Bekannt aus" — Essen & Trinken, Gault & Millau, Falstaff, Vinum, Feinschmecker)
5. Kennenlernpaket Pitch (2-spaltig: Text + Produktkarte mit "Bestseller" Badge)
6. Weingut Pitch (2-spaltig: Text + Bild-Platzhalter)
7. Kategorien (7 Kreise: Trocken, Aromatik, Weißburgunder, Rosé/Sekt, Spätburgunder, Spirits, Mix & Match)
8. Terroir & Handwerk (2-spaltig: Bild + Text)
9. Die Menschen hinter dem Wein (2-spaltig: Text + Familienfoto)
10. **Qualitätspyramide (dark)** — SVG-Pyramide
11. Social Proof (Google-Reviews-Badge 4,9 + 3 Testimonial-Cards)
12. Wein verschenken & abonnieren (2 Cards)
13. Newsletter (2-Spalten-Grid)
14. Footer

### 2. Kategorie (`kategorie.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu
3. Kategorie-Header + Banner (kurzer SEO-Text)
4. Quickview-Card (kompakt, max-width:220px) + Pin-Note ("Auch als Paket oder Kennenlernset darstellbar")
5. **Produkt-Grid (SOFORT sichtbar, kein fade-in)**: Filter-Sidebar + 24 Produkte in 4 Spalten + Pagination
6. Kategorie-Beschreibung + Bild
7. **Qualitätspyramide (light)** — SVG-Pyramide
8. Weitere Kategorien (7 Kreise)
9. Wein verschenken & abonnieren
10. **SEO-Textblöcke** (eigene Section 9b): 6 Blöcke in 3-Spalten-Grid (Rotwein, Weißwein, Verschenken, Abo, Rheingau, Bio)
11. Newsletter (2-Spalten-Grid)
12. Footer

**Produkt-Cards (`.pcard`):**
- Hover-Effekt: Hintergrund wird gelb (`#FFFDE7`), SVG/Text verschwinden, "Produktvideo" erscheint via `::after` Pseudo-Element
- Badge: `.pcard__flip` (z.B. "Bestseller", "Neu") oben links

### 3. Produktseite (`produktseite.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu
3. Promo Bar (Aktionshinweis)
4. **Produktdetail (2-spaltig):**
   - Links: **Sticky Gallery** (`position:sticky;top:90px`) — Hauptbild (380px) + 4 Thumbnails
   - Rechts: Titel, Bewertungen, Meta, Beschreibung, **Preis mit "inkl. MwSt. zzgl. Versand"**, Mengenauswahl, Warenkorb-Button, "Passende Weine" (3-spaltig inline)
5. **USPs (3 nebeneinander, kompakt):** Familienweingut, Versandkostenfrei ab 69€, 14 Tage Rückgabe
6. **"Details & Lagerempfehlung"** (umbenannt von "Technische Details") — Expandierbar mit Chevron-SVG, 4-spaltig innen (Rebsorte, Jahrgang, Alkohol, etc.)
7. Kategorie-Beschreibung + Bild
8. Social Proof (Google-Badge + 5 Avatare mit Zitaten)
9. Weingut Pitch (2-spaltig)
10. Kennenlernpaket (Box mit Varianten-Badges)
11. **Qualitätspyramide (dark)** — SVG-Pyramide (Section-Titel: "Unsere Sortimentsstruktur")
12. Kategorien (7 Kreise)
13. Wein verschenken & abonnieren
14. Newsletter (2-Spalten-Grid)
15. Footer

**Wichtig:** Die obere Qualitätspyramide (ehemals Section 7) wurde entfernt — nur noch eine Pyramide (Section 11).

### 4. Über Uns (`ueber-uns.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu
3. _(keine Promo Bar)_
4. Weingut Pitch + Video-Platzhalter (2-spaltig)
5. Team (3 Portraits: Friedrich/Seniorwinzer, Katharina/Geschäftsführung, Maximilian/Kellermeister — mit Generationen-Badges + Lieblingswein)
6. Terroir & Klima + Video-Platzhalter (2-spaltig)
7. Lagenkarte (interaktiv, Platzhalter)
8. **Qualitätspyramide (dark)** — SVG-Pyramide
9. Kennenlernpaket (Box mit Varianten-Badges)
10. **Erlebnisse vor Ort** (2 Cards: Weinverkostung + Veranstaltungen) — **zentriert** (`text-align:center` auf Section + Container)
11. Newsletter (2-Spalten-Grid)
12. Footer

### 5. Events (`events.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu
3. Hero Banner (Vollbild mit dunklem Overlay)
4. Persönliche Ansprache (zentrierter Text)
5. Termine & Veranstaltungen (3 Event-Cards: Weinlese, Silvester, Kunst & Wein)
6. Erkundungstouren (2-spaltig mit Zeitplan-Tabelle: Fr/Sa/So, Preis, Gruppen)
7. Weinberg für Gruppen (großes Banner mit Overlay + 3 Galerie-Bilder)
8. Kontaktformular
9. Service-Icons (4er-Grid: Telefon, Kalender, Standort, E-Mail)
10. Mehr entdecken (2 verlinkte Bilder: Events, Über Uns)
11. Familientradition CTA (dunkler Banner)
12. Newsletter (2-Spalten-Grid)
13. Footer

**Keine Pyramide auf dieser Seite** (bestätigt durch Konsistenz-Check).

### 6. Kontaktseite (`kontakt.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu
3. Kontakt Hero (zentrierter Text)
4. **2-spaltiges Layout:**
   - Links: Kontaktformular (Vorname, Nachname, E-Mail, Telefon, Betreff-Dropdown, Nachricht, Datenschutz-Hinweis)
   - Rechts: 3 Kontakt-Karten (Adresse, Telefon, E-Mail) + Öffnungszeiten + Google Maps Platzhalter
5. Footer (kein Newsletter auf dieser Seite)

### 7. Widerrufsrecht (`widerrufsrecht.html`) — ✅ FERTIG

Implementiert gemäß **§356a BGB** (ab 19. Juni 2026):
- Headline: "Vertrag widerrufen"
- **2-Schritt-Formular:**
  - Schritt 1: Vorname, Nachname, E-Mail, Bestellnummer, Bestelldatum (Date-Picker), Bestätigung per E-Mail/Post
  - Hinweis: "Die Angabe eines Widerrufsgrundes ist nicht erforderlich."
  - Schritt 2: Zusammenfassung aller Angaben + "Widerruf bestätigen" Button
  - Erfolgs-Meldung: Checkmark-Icon + "Widerruf erfolgreich" + "Bestätigung innerhalb von 24 Stunden"
- JS: Step-Toggle, Summary-Population, deutsches Datumsformat (DD.MM.YYYY)
- Kein Newsletter auf dieser Seite
- Footer identisch mit allen anderen Seiten

---

## CSS Design System (styles.css)

### Custom Properties
```css
--black: #1A1A1A
--gray-900: #2C2C2C   (Buttons, Header, Footer)
--gray-700: #555      (Body Text)
--gray-500: #888      (Meta/Sekundärtext)
--gray-400: #AAA      (Labels, Charcount)
--gray-300: #CCC      (Borders)
--gray-200: #E2E2E2   (Leichte Borders)
--gray-100: #F0F0F0   (Hintergründe)
--gray-50: #F7F7F7    (Section Alt)
--white: #FFFFFF
--font-display: 'Cormorant Garamond'  (Headlines)
--font-body: 'Outfit'                 (Fließtext)
```

### Wichtige CSS-Klassen
| Klasse | Verwendung |
|--------|-----------|
| `.container` | Max 1200px, zentriert, padding 0 40px |
| `.section` / `.section--alt` / `.section--dark` | Sektions-Container (padding 80px 0) |
| `.grid-2` / `.grid-3` / `.grid-4` | CSS Grid Layouts |
| `.ph-img` | Grüner Bild-Platzhalter (#E8EFEA, dashed #B8C8BA) |
| `.ph` | Grauer Wireframe-Platzhalter |
| `.label` | Section-Label (Uppercase, 0.68rem, letter-spacing 2.5px) |
| `.note` | Wireframe-Anmerkung (gelber Hintergrund mit 📌) |
| `.char` | Zeichenanzahl-Angabe |
| `.btn--dark` / `.btn--outline` / `.btn--white` | Button-Varianten (mit Pfeil-Arrow) |
| `.mega__grid--wide` | 5-spaltiges Mega Menu |
| `.footer__widerruf` | Widerrufsrecht-Button im Footer (Border, Hover) |
| `.pcard` / `.pcard__img` | Produktkarte + Hover-Effekt (gelb + "Produktvideo") |
| `.pcard__flip` | Badge auf Produktkarte (z.B. "Bestseller") |
| `.tcard` / `.tcard__avatar` | Testimonial-Card + Avatar |
| `.gcard` | Geschenk/Abo-Card |
| `.kp` / `.kp__grid` | Kennenlernpaket-Box |
| `.pd` | Produktdetail (2-spaltig, align-items:start) |
| `.ecard` / `.ecard__img` | Event-Card + Bild |
| `.cats` / `.cats__circle` | Kategorie-Bubbles (7 Stück) |
| `.filters` | Filter-Sidebar (sticky) |
| `.lkarte` | Lagenkarte |
| `.cart-overlay` / `.cart-drawer` | Warenkorb-Drawer (slide from right) |
| `.cart-drawer__upsell` | Upsell-Sektion im Cart |
| `.nl` / `.nl__block` / `.nl__text` / `.nl__form` / `.nl__form-row` / `.nl__legal` | Newsletter 2-Spalten-Layout |
| `.fade-in` / `.visible` | IntersectionObserver Fade-in Animation |

### Entfernte CSS-Klassen
- `.video-play` — Play-Button CSS wurde komplett entfernt (alle Play-Buttons aus HTML entfernt)
- `.pyramide` / `.pyramide__lvl` — Alte rechteckige Pyramide, ersetzt durch inline SVG

---

## Änderungsprotokoll

### Phase 1: Grundgerüst (Session 1)
- Startseite, Kategorieseite, Produktseite, Über-Uns, Events als HTML/CSS erstellt
- Mega Menu, Footer, Announcement Bar auf allen Seiten
- 63 Stock-Platzhalterbilder (picsum.photos) heruntergeladen

### Phase 2: Bilder & Feedback (Session 1-2)
- Benutzer-Feedback auf Startseite eingearbeitet (Sektionen entfernt/vereinfacht)
- background-image Referenzen in alle Seiten eingefügt
- BILD-PROMPTS.md mit 63 KI-Bild-Prompts erstellt

### Phase 3: Rework & neue Seiten (Session 2-3)
- Alle echten Bilder durch grüne `.ph-img` Platzhalter ersetzt
- Promo-Bars von Unterseiten entfernt (nur Startseite behält Announcement Bar)
- kontakt.html erstellt (2-spaltiges Layout: Formular + Kontaktdaten)
- events.html überarbeitet
- Kontakt-Links auf allen Seiten aktualisiert → kontakt.html

### Phase 4: Finales Feedback & Konsistenz (Session 3 — aktuell)

#### Runde 1 — Produktseite + Kategorieseite:
| Änderung | Datei | Status |
|----------|-------|--------|
| Produkt-Card Hover: gelb + "Produktvideo" Text via `::after` | styles.css | ✅ |
| Produktseite Gallery: sticky (scrollt mit rechter Spalte) | produktseite.html | ✅ |
| Preis: "inkl. MwSt. zzgl. Versand" hinzugefügt | produktseite.html | ✅ |
| USPs: 3 nebeneinander, kompaktere Texte und Icons | produktseite.html | ✅ |
| "Technische Details" → "Details & Lagerempfehlung" (Chevron, 4-spaltig) | produktseite.html | ✅ |
| Obere Qualitätspyramide (Section 7) entfernt | produktseite.html | ✅ |
| Untere Pyramide: SVG-Dreieck mit 3 Bändern + besseres Wording | produktseite.html | ✅ |
| Layout: 3-spaltig → 2-spaltig (Sidebar inline verschoben) | produktseite.html, styles.css | ✅ |

#### Runde 2 — Globale Änderungen:
| Änderung | Dateien | Status |
|----------|---------|--------|
| Alle Play-Buttons (.video-play) entfernt | alle 5+ HTML | ✅ |
| .video-play CSS entfernt (Dead Code Cleanup) | styles.css | ✅ |
| Cart Drawer erstellt (rechts, Produkte + Upsell) | alle 7 HTML, styles.css | ✅ |
| Newsletter: 3 Felder (Vorname, Nachname, E-Mail) + konsistenter Text | 5 HTML | ✅ |
| widerrufsrecht.html erstellt (§356a BGB, 2-Step-Formular) | NEU | ✅ |
| Footer: "Vertrag widerrufen" → widerrufsrecht.html auf allen Seiten | alle 7 HTML | ✅ |
| SVG-Pyramide konsistent auf allen 4 Seiten (dark/light) | 4 HTML | ✅ |
| Kategorieseite: Produkt-Grid sofort sichtbar (kein fade-in) | kategorie.html | ✅ |
| Kategorieseite: Quickview kompakter + Pin-Note hinzugefügt | kategorie.html | ✅ |
| Kategorieseite: SEO-Texte als eigene Section (nicht in "Wein verschenken") | kategorie.html | ✅ |
| Über-Uns: "Erlebnisse vor Ort" zentriert | ueber-uns.html | ✅ |
| Finaler Konsistenz-Check über alle 7+1 Dateien | alle | ✅ |

### Phase 5: Finales Polish (Session 4)

#### Newsletter Redesign (alle 5 Seiten):
| Änderung | Dateien | Status |
|----------|---------|--------|
| Newsletter: 2-Spalten-Grid (links Text, rechts Formular) | styles.css, 5 HTML | ✅ |
| Alle Inputs einheitlich `height:44px` (vorher E-Mail höher als Vorname/Nachname) | styles.css | ✅ |
| CTA-Button: "10 % sichern" → "Anmelden und 10 % Rabatt sichern" | 5 HTML | ✅ |
| `flex:1` Bug entfernt (E-Mail-Input kollabierte auf 20px in Flex-Column) | styles.css | ✅ |
| Responsive: Unter 768px Einspalt-Stack mit zentriertem Text | styles.css | ✅ |

#### Weitere Fixes:
| Änderung | Dateien | Status |
|----------|---------|--------|
| "Erlebnisse vor Ort" Body-Text zentriert (`margin:auto`) | ueber-uns.html | ✅ |
| Smooth Scroll JS hinzugefügt (fehlte für Anker-Links) | events.html | ✅ |
| Active Nav `class="active"` auf "Weine" korrigiert | produktseite.html | ✅ |
| Konsistenz-Check über alle 7 Seiten | alle | ✅ |

---

## Text-Regeln

1. **Alle Texte sind deutsche Blindtexte** — KEIN Lorem Ipsum
2. Jeder Text erklärt die **psychologische Funktion** des Elements
3. Am Ende jedes Texts steht die **Zeichenanzahl**: `(XX Zeichen)` oder `(ca. XX-YY Zeichen empfohlen)`
4. **Headlines max. 6-8 Wörter**
5. CSS-Klassen: `.char` für Zeichenangaben, `.note` für Wireframe-Anmerkungen

---

## Konsistenz-Matrix (verifiziert am 03.03.2026)

| Element | index | kategorie | produktseite | ueber-uns | events | kontakt | widerrufsrecht |
|---------|:-----:|:---------:|:------------:|:---------:|:------:|:-------:|:--------------:|
| Announcement Bar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Header + Mega Menu | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cart onclick | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cart Drawer HTML/JS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Newsletter (2-Spalten-Grid) | ✅ | ✅ | ✅ | ✅ | ✅ | — | — |
| Smooth Scroll JS | ✅ | — | — | — | ✅ | — | — |
| Active Nav | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| SVG Pyramide | ✅ dark | ✅ light | ✅ dark | ✅ dark | — | — | — |
| Footer (4 Spalten) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| "Vertrag widerrufen" Link | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Kontakt → kontakt.html | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Play Buttons | ❌ entf. | ❌ entf. | ❌ entf. | ❌ entf. | ❌ entf. | — | — |
| Grüne Platzhalter | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

---

## Für die nächste LLM-Session

### Sofort-Kontext
- **Projektordner:** `/Users/fabianwillisimon/Documents/VD Wireframes/`
- **8 Dateien:** index.html, kategorie.html, produktseite.html, ueber-uns.html, events.html, kontakt.html, widerrufsrecht.html, styles.css
- **Server-Workaround:** Dateien nach `/tmp/wf-site/` kopieren, Server via `python3 /tmp/wf/serve.py` starten
- **Alle Seiten sind fertig und konsistenz-gecheckt** — kein offenes Rework mehr
- **Newsletter:** 2-Spalten-Grid-Layout (links Text, rechts Formular), alle Inputs 44px

### Wichtige Design-Entscheidungen
- **Keine echten Bilder im HTML** — alles grüne `.ph-img` Platzhalter mit Beschreibungstext
- **SVG-Pyramide statt CSS** — weil CSS clip-path Borders abschneidet
- **2-spaltig statt 3-spaltig** auf Produktseite (Sidebar inline verschoben)
- **Produkt-Card Hover** rein CSS (`::after` Pseudo-Element, kein JS nötig)
- **Widerrufsbutton** per §356a BGB (ab 19.06.2026): "Vertrag widerrufen", 2-Step-Formular, kein Grund nötig

### Mögliche nächste Schritte
- [ ] Responsive-Tests auf Mobile/Tablet (Media Queries vorhanden aber ungetestet)
- [ ] Generische Bilder durch weingut-spezifische KI-Bilder ersetzen (Prompts in BILD-PROMPTS.md)
- [ ] Accessibility-Check (Kontraste, Alt-Texte, Keyboard-Navigation)
- [ ] Hover-States für Mega Menu auf Touch-Devices
- [ ] AGB-Seite / Impressum-Seite erstellen
- [ ] Datenschutz-Seite erstellen
- [ ] Cookie-Banner Wireframe
- [ ] Checkout-Flow Wireframes (Warenkorb → Adresse → Zahlung → Bestätigung)
