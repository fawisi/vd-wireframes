# Winzer-Shop Wireframe Prototyp — Projektdokumentation

## Projektbeschreibung

HTML/CSS-Wireframe-Prototyp zur Veranschaulichung der idealen Informationsarchitektur und Seitenstruktur eines Familienweingut-Onlineshops. Der Prototyp dient als Kommunikationsmittel zwischen UX/Strategie und Design/Entwicklung.

**Auftraggeber:** Fabian Willis-Simon
**Projekt:** VD FFM Shop-Wireframes
**Status:** Phase 6 — Mobile-Optimierung, Versandkosten-Bar & Kategorien-Update abgeschlossen
**Letztes Update:** 2026-03-03

---

## Technischer Stack

- **Reine HTML5 + CSS3** (kein Framework, kein Build-Tool)
- **Fonts:** Google Fonts — Cormorant Garamond (Display) + Outfit (Body)
- **Design:** Minimales Wireframe-Aesthetic mit grünen Bild-Platzhaltern (`#E8EFEA`)
- **JS:** IntersectionObserver (Fade-in), Sticky Header, Smooth Scroll, Cart Drawer, Widerrufs-Formular, Mobile-Navigation Toggle
- **Server:** `npx http-server -p 8080 -c-1` (konfiguriert in `.claude/launch.json`)
- **Bilder:** Alle durch grüne Platzhalter (`.ph-img`) ersetzt — keine echten Bilder im HTML
- **Git Remote:** `git@github.com:fawisi/vd-wireframes.git` (SSH), Branch: `main`

---

## Dateistruktur

```
/Users/fabianwillisimon/Documents/VD Wireframes/
  index.html              — Startseite (Homepage) ✅ FERTIG
  weine.html              — Alle-Weine-Übersicht (Kategorie-Bubbles + Produkt-Grid) ✅ FERTIG
  kategorie.html          — Einzelkategorie-Seite (Kategorie-Header + Produkte) ✅ FERTIG
  produktseite.html       — Produktdetailseite (2-Spalten-Layout, sticky Galerie) ✅ FERTIG
  weinberatung.html       — Weinberatung (Food-Pairings + Weinmomente) ✅ FERTIG
  ueber-uns.html          — Über Uns (Weingut, Team, Terroir) ✅ FERTIG
  events.html             — Events & Weinproben ✅ FERTIG
  kontakt.html            — Kontaktseite ✅ FERTIG
  widerrufsrecht.html     — Vertrag widerrufen (§356a BGB) ✅ FERTIG
  styles.css              — Shared CSS Design System ✅
  PROJEKTPLAN.md          — Diese Dokumentation
  BILD-PROMPTS.md         — 63 detaillierte Bild-Prompts (für spätere KI-Generierung)
  .claude/launch.json     — Dev-Server-Konfiguration
```

### Dev-Server starten

```bash
npx http-server -p 8080 -c-1
# -> http://localhost:8080
```

Claude Code launch.json Config: `.claude/launch.json` mit `"wireframe-preview"` auf Port 8080.

> **Hinweis:** `python3 -m http.server` hat PermissionError auf macOS — immer `npx http-server` nutzen.

---

## Seitenarchitektur: Weine

Es gibt zwei unterschiedliche Weinübersichts-Seiten:

| Seite | Datei | Inhalt |
|-------|-------|--------|
| **Alle Weine** | `weine.html` | Kategorie-Bubbles oben (6 Stück), kein Kategorie-Text/Video, "96 Weine gefunden", Qualitätspyramide, weitere Kategorien |
| **Einzelkategorie** | `kategorie.html` | Kategorie-Header mit Titel + Quickview-Produkt + "Über diese Kategorie" Section (Text + Video), z.B. "Rotweine aus dem Rheingau" |

Nav-Link "Alle Weine" → `weine.html`, Mega-Menu "Alle Weine" → `weine.html`.

---

## Navigation

### Hauptnavigation (Desktop)
```
Startseite | Alle Weine (mit Mega Menu) | Weinberatung | Über Uns | Events & Weinprobe | Kontakt
```

### Mega Menu (5 Spalten)
| Spalte | Inhalt |
|--------|--------|
| Sortiment | Weißweine, Rotweine, Rosé, Sekt & Secco, Spirituosen, Alkoholfrei, Alle Weine |
| Terroir | Unsere Böden, Muschelkalk, Löss & Lehm, Einzellagen, Lagenkarte |
| Sonstiges | Neuheiten, Bestseller, Kennenlernpakete, Geschenksets |
| Qualitätsstufen | Gutswein, Ortswein, Lagenwein |
| Produkt-Teaser | Kennenlernpaket mit Bild, Preis und CTA |

### Mobile Navigation
- Hamburger-Button (3 Balken, CSS-animiert zu X)
- Fullwidth Overlay-Nav mit allen 6 Links
- Active-State auf aktueller Seite
- JS: `toggleMobileNav()` — Toggle-Funktion auf allen 9 Seiten

---

## Platzhalter-System

### Bild-Platzhalter (`.ph-img`)
Alle echten Bilder durch einheitliche grüne Platzhalter ersetzt:

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
Gelbe Sticky-Notes mit Pin-Icon für Wireframe-spezifische Hinweise:
```html
<div class="note">Alternativ: Auch als Paket oder Kennenlernset darstellbar</div>
```

---

## Globale Elemente (auf allen 9 Seiten konsistent)

### 1. Announcement Bar
Schmaler Banner oben: "Versandkostenfrei ab 100 € | Jetzt Kennenlernpaket sichern"

### 2. Header + Mega Menu
- Sticky Header mit Blur-Backdrop
- Navigation: Startseite, Alle Weine (mit Mega Menu), Weinberatung, Über Uns, Events & Weinprobe, Kontakt
- Mega Menu: 5 Spalten (Sortiment, Terroir, Sonstiges, Qualitätsstufen + Paket-Teaser)
- Icons: Suche, Mein Konto, Warenkorb (mit Badge "2" + `onclick="openCartDrawer()"`)
- Hamburger-Button (`header__burger`) vor Icons — nur auf Mobile sichtbar

### 3. Mobile Navigation
Auf ALLEN 9 Seiten identischer HTML-Block:
```html
<nav class="mobile-nav" id="mobile-nav">
  <div class="mobile-nav__links">
    <a href="index.html">Startseite</a>
    <a href="weine.html">Alle Weine</a>
    <a href="weinberatung.html">Weinberatung</a>
    <a href="ueber-uns.html">Über Uns</a>
    <a href="events.html">Events & Weinprobe</a>
    <a href="kontakt.html">Kontakt</a>
  </div>
</nav>
```
- Sichtbar ab `max-width: 768px` (Desktop-Nav wird ausgeblendet)
- `class="active"` auf dem jeweiligen Seitenlink
- JS-Toggle: Burger bekommt `class="active"` (animiert zu X), Nav bekommt `class="open"`

### 4. Cart Drawer (Warenkorb)
Auf ALLEN 9 Seiten identischer HTML/JS-Block:
- Slide-in von rechts (CSS transform), Overlay dahinter
- 2 Beispiel-Produkte: Riesling Spätlese 2023 (14,90 €), Grauburgunder trocken 2023 (10,90 €)
- Mengensteuerung (Eurus-Stil: Pill-Shape `border-radius: 999px`)
- Upsell-Sektion: "Das könnte dir auch gefallen" mit Chardonnay Réserve + Kennenlernpaket
- **Versandkosten-Fortschrittsleiste** (Shipping Bar) im Footer des Drawers
- Zwischensumme: 36,70 €, Versandhinweis, "Zur Kasse" + "Weiter einkaufen"
- ESC-Taste zum Schließen
- **Full-width auf Tablets** (ab `max-width: 768px`)

```javascript
function openCartDrawer(){...}
function closeCartDrawer(){...}
document.addEventListener('keydown', function(e){ if(e.key==='Escape') closeCartDrawer(); });
```

### 5. Versandkosten-Fortschrittsleiste (Shipping Bar)
Grüne Fortschrittsleiste mit 100-€-Schwelle für kostenfreien Versand:

```html
<div class="shipping-bar">
  <div class="shipping-bar__text">Noch <strong>63,30 €</strong> bis Versandkostenfrei</div>
  <div class="shipping-bar__track">
    <div class="shipping-bar__fill" style="width:37%"></div>
  </div>
</div>
```

- **Im Cart Drawer:** Alle 9 Seiten, im `cart-drawer__footer` (63,30 € verbleibend, 37% Füllstand)
- **Auf Produktseite:** Zusätzlich neben dem Warenkorb-Button (85,10 € verbleibend, 15% Füllstand)
- Grüner Farbverlauf: `linear-gradient(90deg, #66BB6A, #2E7D32)`
- Pill-Shape Track: `border-radius: 999px`
- Modifier `--complete`: Volles Grün wenn Schwelle erreicht

### 6. Newsletter-Formular
Auf 6 Seiten (index, weine, kategorie, produktseite, ueber-uns, weinberatung):
- **2-Spalten-Grid-Layout:** Links Infotext (`nl__text`), rechts Formular (`nl__form`)
- Headline: "Newsletter & 10 % Rabatt"
- Beschreibung: "Erhalten Sie exklusive Angebote, Weinempfehlungen und Einladungen zu Events — max. 2x im Monat."
- Formular: Vorname + Nachname (2-spaltig via `nl__form-row`), E-Mail-Adresse, Button "Anmelden und 10 % Rabatt sichern"
- Alle Inputs + Button einheitlich `height: 44px`
- Legal: "Mit der Anmeldung stimmen Sie unserer Datenschutzerklärung zu. Abmeldung jederzeit möglich."
- **Responsive:** Unter 768px stapelt sich alles in einer Spalte, Text zentriert

### 7. Footer
4-spaltiges Grid:
- Spalte 1: Logo, Beschreibung, Adresse, Telefon, E-Mail
- Spalte 2: Service (Kontakt → kontakt.html, FAQ, Versand, Retouren, Gutscheine, Weinberatung → weinberatung.html)
- Spalte 3: Lieferung & Zahlung (Versandkostenfrei ab 100 €, 2-4 Werktage, Klimaneutral, SSL, Rechnung, Ratenzahlung)
- Spalte 4: Unternehmen (Über Uns → ueber-uns.html, Nachhaltigkeit, Events → events.html, Presse, Karriere, Händler)
- Bottom: Impressum, Datenschutz, AGB, **"Vertrag widerrufen"** → widerrufsrecht.html (als Button-Link `.footer__widerruf`), © 2026
- Payment: VISA, MC, PayPal, Klarna, DHL, DPD
- Social: Instagram, Facebook, YouTube

### 8. Kategorie-Bubbles
6 Kategorien (umbenannt in Phase 6):

| Bubble | Verlinkung |
|--------|-----------|
| Weißwein | kategorie.html |
| Rotwein | kategorie.html |
| Rosé | kategorie.html |
| Sekt & Seco | kategorie.html |
| Spirituosen | kategorie.html |
| Alkoholfrei | kategorie.html |

Auf 4 Seiten: index.html, weine.html (2x: oben + weitere Kategorien), kategorie.html, produktseite.html.

### 9. SVG-Qualitätspyramide
Auf 5 Seiten (index, weine, ueber-uns, produktseite = dark; kategorie = light):

Wording in allen Pyramiden identisch:
- Lagenwein: "PRESTIGE AUS EINZELLAGEN"
- Ortswein: "CHARAKTER UNSERER BESTEN LAGEN"
- Gutswein: "VIELSEITIGE ALLTAGSBEGLEITER"

### 10. "Wein verschenken & Abo" Section
Auf 4 Seiten (index, weine, kategorie, produktseite):
- 2 Cards: Geschenkset + Abo
- **Pin-Note:** "Dieser Bereich ist frei anpassbar — z.B. Events, Weinabo, Rebpatenschaft, Gutscheine oder saisonale Aktionen. Ideal für Cross-Selling und wiederkehrende Erlöse."

---

## Seitenübersicht (aktueller Stand)

### 1. Startseite (`index.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Hero (2-spaltig: Headline, Subheadline, 3 USPs, 2 Buttons, 4 Avatar-Icons + 4,9/5 Bewertungen)
5. Trust Bar ("Bekannt aus" — Essen & Trinken, Gault & Millau, Falstaff, Vinum, Feinschmecker)
6. Kennenlernpaket Pitch (2-spaltig: Text + Produktkarte mit "Bestseller" Badge)
7. Weingut Pitch (2-spaltig: Text + Bild-Platzhalter)
8. Kategorien (6 Kreise: Weißwein, Rotwein, Rosé, Sekt & Seco, Spirituosen, Alkoholfrei)
9. Terroir & Handwerk (2-spaltig: Bild + Text)
10. Die Menschen hinter dem Wein (2-spaltig: Text + Familienfoto)
11. **Qualitätspyramide (dark)** — SVG-Pyramide
12. Social Proof (Google-Reviews-Badge 4,9 + 3 Testimonial-Cards)
13. Wein verschenken & abonnieren (2 Cards + Pin-Note)
14. Newsletter (2-Spalten-Grid)
15. Footer
16. Cart Drawer (mit Shipping Bar)

### 2. Alle Weine (`weine.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Kategorie-Bubbles (6 Kreise) + Titel "Alle Weine" + Beschreibungstext
5. **Produkt-Grid:** Filter-Sidebar + 24 Produkte in 4 Spalten + "96 Weine gefunden" + Sortierung + Pagination
6. Kategorie-Beschreibung + Bild
7. **Qualitätspyramide (dark)** — SVG-Pyramide
8. Weitere Kategorien (6 Kreise)
9. Wein verschenken & abonnieren (2 Cards + Pin-Note)
10. Newsletter (2-Spalten-Grid)
11. Footer
12. Cart Drawer (mit Shipping Bar)

**Unterschied zu `kategorie.html`:** Kein Kategorie-Header-Text/Video, nur Bubbles oben.

### 3. Einzelkategorie (`kategorie.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Kategorie-Header + Banner (kurzer SEO-Text)
5. Quickview-Card (kompakt, max-width:220px) + Pin-Note
6. **Produkt-Grid (SOFORT sichtbar, kein fade-in)**: Filter-Sidebar + 24 Produkte in 4 Spalten + Pagination
7. "Über diese Kategorie" Section (Text + Video)
8. **Qualitätspyramide (light)** — SVG-Pyramide
9. Weitere Kategorien (6 Kreise)
10. Wein verschenken & abonnieren (2 Cards + Pin-Note)
11. **SEO-Textblöcke** (6 Blöcke in 3-Spalten-Grid)
12. Newsletter (2-Spalten-Grid)
13. Footer
14. Cart Drawer (mit Shipping Bar)

**Produkt-Cards (`.pcard`):**
- Hover-Effekt: Hintergrund wird gelb (`#FFFDE7`), SVG/Text verschwinden, "Produktvideo" erscheint via `::after` Pseudo-Element
- Badge: `.pcard__flip` (z.B. "Bestseller", "Neu") oben links
- Mengenauswahl (Pill-Shape) + "In den Warenkorb" (Outline-Button)
- Preisangabe: "inkl. MwSt., zzgl. Versandkosten"

### 4. Produktseite (`produktseite.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Promo Bar (Aktionshinweis)
5. **Produktdetail (2-spaltig):**
   - Links: **Sticky Gallery** (`position:sticky;top:90px`) — Hauptbild (380px) + 4 Thumbnails
   - Rechts: Titel, Bewertungen, Meta, Beschreibung, **Preis mit "inkl. MwSt. zzgl. Versand"**, **Versandkosten-Fortschrittsleiste (15% / 85,10 € verbleibend)**, Mengenauswahl (Pill-Shape), Warenkorb-Button, "Passende Weine" (3-spaltig inline)
6. **USPs (3 nebeneinander, kompakt):** Familienweingut, Versandkostenfrei ab 100€, 14 Tage Rückgabe
7. **"Details & Lagerempfehlung"** — Expandierbar mit Chevron-SVG, 4-spaltig innen
8. Kategorie-Beschreibung + Bild
9. Social Proof (Google-Badge + 5 Avatare mit Zitaten)
10. Weingut Pitch (2-spaltig)
11. Kennenlernpaket (Box mit Varianten-Badges)
12. **Qualitätspyramide (dark)** — SVG-Pyramide
13. Kategorien (6 Kreise)
14. Wein verschenken & abonnieren (2 Cards + Pin-Note)
15. Newsletter (2-Spalten-Grid)
16. Footer
17. Cart Drawer (mit Shipping Bar)

### 5. Weinberatung (`weinberatung.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Hero-Banner (Vollbild mit dunklem Overlay, 2 Buttons: "Wein zum Essen" + "Weinmomente")
5. **Wein zum Essen — Icon-Strip** (dark Section): 9 Food-Icons (Braten, Geflügel, Wild, Fisch, Käse, Pasta, Vegetarisch, Apéro, Dessert)
6. **Wein zum Essen — Bild-Cards**: Asymmetrisches Grid (2er-Row 60/40 + 3er-Row), Overlay-Cards mit Hover-Effekt + Shopify-Hinweis Pin-Note
7. **Weinmomente — Pill-Strip** (alt Section): 6 Mood-Pills (Zweisamkeit, Gesellschaft, Draußen, Feierabend, Schenken, Saisonal)
8. **Weinmomente — Card-Grid**: Asymmetrisches 2-Spalten-Grid (4 Rows alternierend groß/klein), 8 Moment-Cards mit Overlay + Shopify-Hinweis Pin-Note
9. **Persönliche Beratung — CTA-Box**: "Nicht das Richtige gefunden?" mit 2 Buttons
10. Newsletter (2-Spalten-Grid)
11. Footer
12. Cart Drawer (mit Shipping Bar)

**Spezielle CSS-Klassen:**
| Klasse | Verwendung |
|--------|-----------|
| `.fstrip` / `.fstrip__item` / `.fstrip__icon` | Food-Icon-Leiste (horizontal scrollbar auf Mobile) |
| `.fcard` / `.fcard__img` / `.fcard__overlay` | Food-Pairing Bild-Cards mit Hover-Overlay |
| `.fcard-grid` / `.fcard-grid--3` | Asymmetrisches Card-Layout (60/40 + 3-spaltig) |
| `.mstrip` / `.mstrip__pill` | Weinmomente Pill-Navigation |
| `.mcard` / `.mcard__img` / `.mcard__overlay` | Weinmoment-Cards mit Overlay |
| `.mcard-grid` | Asymmetrisches 2-Spalten-Grid (alternierend groß/klein) |
| `.wf-cta` / `.wf-cta__box` | CTA-Box für persönliche Beratung |

### 6. Über Uns (`ueber-uns.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Weingut Pitch + Video-Platzhalter (2-spaltig)
5. Team (3 Portraits: Friedrich/Seniorwinzer, Katharina/Geschäftsführung, Maximilian/Kellermeister — mit Generationen-Badges + Lieblingswein)
6. Terroir & Klima + Video-Platzhalter (2-spaltig)
7. Lagenkarte (interaktiv, Platzhalter)
8. **Qualitätspyramide (dark)** — SVG-Pyramide
9. Kennenlernpaket (Box mit Varianten-Badges)
10. **Erlebnisse vor Ort** (2 Cards: Weinverkostung + Veranstaltungen) — **zentriert**
11. Newsletter (2-Spalten-Grid)
12. Footer
13. Cart Drawer (mit Shipping Bar)

### 7. Events & Weinprobe (`events.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Hero Banner (Vollbild mit dunklem Overlay)
5. Persönliche Ansprache (zentrierter Text)
6. Termine & Veranstaltungen (3 Event-Cards: Weinlese, Silvester, Kunst & Wein)
7. Erkundungstouren (2-spaltig mit Zeitplan-Tabelle: Fr/Sa/So, Preis, Gruppen)
8. Weinberg für Gruppen (großes Banner mit Overlay + 3 Galerie-Bilder)
9. Kontaktformular
10. Service-Icons (4er-Grid: Telefon, Kalender, Standort, E-Mail)
11. Mehr entdecken (2 verlinkte Bilder: Events, Über Uns)
12. Familientradition CTA (dunkler Banner)
13. Newsletter (2-Spalten-Grid)
14. Footer
15. Cart Drawer (mit Shipping Bar)

**Keine Pyramide auf dieser Seite.**

### 8. Kontaktseite (`kontakt.html`) — ✅ FERTIG

Sektionen:
1. Announcement Bar
2. Header + Mega Menu + Hamburger
3. Mobile Navigation
4. Kontakt Hero (zentrierter Text)
5. **2-spaltiges Layout:**
   - Links: Kontaktformular (Vorname, Nachname, E-Mail, Telefon, Betreff-Dropdown, Nachricht, Datenschutz-Hinweis)
   - Rechts: 3 Kontakt-Karten (Adresse, Telefon, E-Mail) + Öffnungszeiten + Google Maps Platzhalter
6. Footer (kein Newsletter auf dieser Seite)
7. Cart Drawer (mit Shipping Bar)

### 9. Widerrufsrecht (`widerrufsrecht.html`) — ✅ FERTIG

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
- Cart Drawer (mit Shipping Bar)

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
| `.note` | Wireframe-Anmerkung (gelber Hintergrund mit Pin) |
| `.char` | Zeichenanzahl-Angabe |
| `.btn--dark` / `.btn--outline` / `.btn--white` | Button-Varianten (mit Pfeil-Arrow) |
| `.mega__grid--wide` | 5-spaltiges Mega Menu |
| `.header__burger` | Hamburger-Button (3 Balken, animiert zu X) |
| `.mobile-nav` / `.mobile-nav__links` | Mobile Overlay-Navigation |
| `.shipping-bar` / `__text` / `__track` / `__fill` | Versandkosten-Fortschrittsleiste (grün) |
| `.footer__widerruf` | Widerrufsrecht-Button im Footer (Border, Hover) |
| `.pcard` / `.pcard__img` | Produktkarte + Hover-Effekt (gelb + "Produktvideo") |
| `.pcard__flip` | Badge auf Produktkarte (z.B. "Bestseller") |
| `.pcard__cart` / `.pcard__qty` | Warenkorb-Button + Mengenauswahl (Pill-Shape) |
| `.tcard` / `.tcard__avatar` | Testimonial-Card + Avatar |
| `.gcard` | Geschenk/Abo-Card |
| `.kp` / `.kp__grid` | Kennenlernpaket-Box |
| `.pd` | Produktdetail (2-spaltig, align-items:start) |
| `.ecard` / `.ecard__img` | Event-Card + Bild |
| `.cats` / `.cats__circle` | Kategorie-Bubbles (6 Stück) |
| `.filters` | Filter-Sidebar (sticky) |
| `.lkarte` | Lagenkarte |
| `.cart-overlay` / `.cart-drawer` | Warenkorb-Drawer (slide from right) |
| `.cart-drawer__upsell` | Upsell-Sektion im Cart |
| `.nl` / `.nl__block` / `.nl__text` / `.nl__form` | Newsletter 2-Spalten-Layout |
| `.fstrip` / `.fcard` / `.fcard-grid` | Weinberatung: Food-Pairings (Icons + Cards) |
| `.mstrip` / `.mcard` / `.mcard-grid` | Weinberatung: Weinmomente (Pills + Cards) |
| `.wf-cta` / `.wf-cta__box` | Weinberatung: CTA-Box |
| `.fade-in` / `.visible` | IntersectionObserver Fade-in Animation |

### Responsive Breakpoints
| Breakpoint | Verhalten |
|-----------|-----------|
| `min-width: 1600px` | Extra-große Screens: Container 1400px, größere Grids |
| `max-width: 1024px` | Tablet Landscape: 3-Spalten-Grids → 2-spaltig, Container-Padding reduziert |
| `max-width: 768px` | Tablet Portrait: Desktop-Nav ausblenden, Hamburger + Mobile-Nav zeigen, Cart Drawer full-width, 2-spaltig → 1-spaltig |
| `max-width: 480px` | Mobile: Font-Sizes reduziert, Container-Padding 16px, einspaltiges Layout |

### Eurus-Design-Elemente
- `border-radius: 999px` (Pill-Shape) für Buttons, Qty-Selectors, Shipping-Bar-Track
- Outline-Buttons: `#d0d0d0` Border, transparent Background für "In den Warenkorb"
- Shipping Bar: Grüner Gradient (`#66BB6A` → `#2E7D32`)

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

### Phase 4: Finales Feedback & Konsistenz (Session 3)

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
| Alle Play-Buttons (.video-play) entfernt | alle HTML | ✅ |
| .video-play CSS entfernt (Dead Code Cleanup) | styles.css | ✅ |
| Cart Drawer erstellt (rechts, Produkte + Upsell) | alle HTML, styles.css | ✅ |
| Newsletter: 3 Felder (Vorname, Nachname, E-Mail) + konsistenter Text | HTML | ✅ |
| widerrufsrecht.html erstellt (§356a BGB, 2-Step-Formular) | NEU | ✅ |
| Footer: "Vertrag widerrufen" → widerrufsrecht.html auf allen Seiten | alle HTML | ✅ |
| SVG-Pyramide konsistent auf allen Seiten (dark/light) | HTML | ✅ |
| Kategorieseite: Produkt-Grid sofort sichtbar (kein fade-in) | kategorie.html | ✅ |
| Kategorieseite: Quickview kompakter + Pin-Note hinzugefügt | kategorie.html | ✅ |
| Kategorieseite: SEO-Texte als eigene Section | kategorie.html | ✅ |
| Über-Uns: "Erlebnisse vor Ort" zentriert | ueber-uns.html | ✅ |
| Finaler Konsistenz-Check über alle Dateien | alle | ✅ |

### Phase 5: Finales Polish (Session 4)

#### Newsletter Redesign:
| Änderung | Dateien | Status |
|----------|---------|--------|
| Newsletter: 2-Spalten-Grid (links Text, rechts Formular) | styles.css, HTML | ✅ |
| Alle Inputs einheitlich `height:44px` | styles.css | ✅ |
| CTA-Button: "Anmelden und 10 % Rabatt sichern" | HTML | ✅ |
| Responsive: Unter 768px Einspalt-Stack mit zentriertem Text | styles.css | ✅ |

#### Weitere Fixes:
| Änderung | Dateien | Status |
|----------|---------|--------|
| "Erlebnisse vor Ort" Body-Text zentriert | ueber-uns.html | ✅ |
| Smooth Scroll JS hinzugefügt | events.html | ✅ |
| Active Nav korrigiert | produktseite.html | ✅ |

#### Neue Seiten:
| Änderung | Dateien | Status |
|----------|---------|--------|
| weine.html erstellt (Alle-Weine-Übersicht) | NEU | ✅ |
| weinberatung.html erstellt (Food-Pairings + Weinmomente, 7 Sections) | NEU | ✅ |
| Eurus-Design (Pill-Shape) für Buttons und Qty-Selectors | styles.css | ✅ |
| Mengenauswahl + Warenkorb-Button auf Kategorie- und Produktseite | kategorie.html, produktseite.html | ✅ |
| Rechtliche Preisangaben (inkl. MwSt., zzgl. Versandkosten) | HTML | ✅ |
| Navigation: "Weingut" entfernt (redundant mit "Über Uns") | alle HTML | ✅ |

### Phase 6: Mobile-Optimierung & Versandkosten-Bar (Session 5 — aktuell)

| Änderung | Dateien | Status |
|----------|---------|--------|
| **Responsive Design** mit 4 Breakpoints (1600px+, 1024px, 768px, 480px) | styles.css | ✅ |
| **Hamburger-Menü** + Mobile-Navigation auf allen 9 Seiten | alle 9 HTML, styles.css | ✅ |
| **Versandkosten-Fortschrittsleiste** (Shipping Bar) im Cart Drawer | alle 9 HTML, styles.css | ✅ |
| **Versandkosten-Bar auf Produktseite** (neben Add-to-Cart) | produktseite.html | ✅ |
| **Kategorie-Bubbles umbenannt** (6 statt 7): Weißwein, Rotwein, Rosé, Sekt & Seco, Spirituosen, Alkoholfrei | 4 HTML | ✅ |
| **Navigation aktualisiert**: "Weine" → "Alle Weine", "Events" → "Events & Weinprobe" | alle 9 HTML | ✅ |
| **Versandkostenfrei-Schwelle** von 69 € auf 100 € erhöht | alle 9 HTML | ✅ |
| **Mega Menu**: "Alkoholfrei" zum Sortiment hinzugefügt | alle 9 HTML | ✅ |
| **Pin-Note** für "Wein verschenken & Abo" Section | 4 HTML | ✅ |
| **Cart Drawer full-width** ab 768px (statt 420px) | styles.css | ✅ |
| **`overflow-x: hidden`** auf `html` (verhindert horizontalen Overflow durch Cart Drawer) | styles.css | ✅ |
| **toggleMobileNav() JS** auf allen 9 Seiten | alle 9 HTML | ✅ |

---

## Text-Regeln

1. **Alle Texte sind deutsche Blindtexte** — KEIN Lorem Ipsum
2. Jeder Text erklärt die **psychologische Funktion** des Elements
3. Am Ende jedes Texts steht die **Zeichenanzahl**: `(XX Zeichen)` oder `(ca. XX-YY Zeichen empfohlen)`
4. **Headlines max. 6-8 Wörter**
5. CSS-Klassen: `.char` für Zeichenangaben, `.note` für Wireframe-Anmerkungen

---

## Konsistenz-Matrix (verifiziert am 03.03.2026)

| Element | index | weine | kategorie | produktseite | weinberatung | ueber-uns | events | kontakt | widerrufsrecht |
|---------|:-----:|:-----:|:---------:|:------------:|:------------:|:---------:|:------:|:-------:|:--------------:|
| Announcement Bar (100 €) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Header + Mega Menu | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hamburger-Button | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mobile Navigation | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nav "Alle Weine" | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nav "Events & Weinprobe" | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cart Drawer HTML/JS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Shipping Bar (Cart) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Shipping Bar (Produkt) | — | — | — | ✅ | — | — | — | — | — |
| Mega Menu "Alkoholfrei" | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Kategorie-Bubbles (6x) | ✅ | ✅ 2x | ✅ | ✅ | — | — | — | — | — |
| Pin-Note "Wein verschenken" | ✅ | ✅ | ✅ | ✅ | — | — | — | — | — |
| Newsletter (2-Spalten-Grid) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — |
| SVG Pyramide | ✅ dark | ✅ dark | ✅ light | ✅ dark | — | ✅ dark | — | — | — |
| Active Nav | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| toggleMobileNav JS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Footer (4 Spalten, 100 €) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| "Vertrag widerrufen" Link | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Kontakt → kontakt.html | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Grüne Platzhalter | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

---

## Für die nächste LLM-Session

### Sofort-Kontext
- **Projektordner:** `/Users/fabianwillisimon/Documents/VD Wireframes/`
- **9 HTML-Dateien** + `styles.css` — alle fertig und konsistenz-gecheckt
- **Server:** `npx http-server -p 8080 -c-1` (in `.claude/launch.json` konfiguriert)
- **Git Remote:** `git@github.com:fawisi/vd-wireframes.git` (SSH, Branch: `main`)
- **Alle Seiten haben:** Announcement Bar, Header + Mega Menu, Hamburger + Mobile Nav, Cart Drawer mit Shipping Bar, Footer

### Wichtige Design-Entscheidungen
- **Keine echten Bilder im HTML** — alles grüne `.ph-img` Platzhalter mit Beschreibungstext
- **SVG-Pyramide statt CSS** — weil CSS clip-path Borders abschneidet
- **2-spaltig statt 3-spaltig** auf Produktseite (Sidebar inline verschoben)
- **Produkt-Card Hover** rein CSS (`::after` Pseudo-Element, kein JS nötig)
- **Widerrufsbutton** per §356a BGB (ab 19.06.2026): "Vertrag widerrufen", 2-Step-Formular
- **Eurus-Design:** Pill-Shape (`border-radius: 999px`) für Buttons, Qty-Selectors, Shipping Bar
- **6 Kategorien:** Weißwein, Rotwein, Rosé, Sekt & Seco, Spirituosen, Alkoholfrei
- **100 € Versandkostenfrei-Schwelle** (vorher 69 €)

### Mögliche nächste Schritte
- [ ] Generische Bilder durch weingut-spezifische KI-Bilder ersetzen (Prompts in BILD-PROMPTS.md)
- [ ] Accessibility-Check (Kontraste, Alt-Texte, Keyboard-Navigation)
- [ ] Hover-States für Mega Menu auf Touch-Devices
- [ ] AGB-Seite / Impressum-Seite erstellen
- [ ] Datenschutz-Seite erstellen
- [ ] Cookie-Banner Wireframe
- [ ] Checkout-Flow Wireframes (Warenkorb → Adresse → Zahlung → Bestätigung)
- [ ] Suchergebnisseite Wireframe
