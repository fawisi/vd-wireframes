---
title: "Paketseite: Weinpaket-Produkttemplate"
type: feat
status: active
date: 2026-03-03
---

# Paketseite: Weinpaket-Produkttemplate

## Overview

Neue `paketseite.html` als eigenständiges Template für Weinpakete (Kennenlernpaket, Probierpaket, Geschenkpaket), das auf der bestehenden `produktseite.html` aufbaut, aber conversion-optimiert auf die Besonderheiten von Paketen zugeschnitten ist. Pakete sind stärker marketing-getrieben als Einzelflaschen und erfordern ein anderes Informationsdesign.

## Problem Statement / Motivation

Die bestehende `produktseite.html` ist für Einzelweine konzipiert. Pakete unterscheiden sich fundamental:

- **Kein Versandkosten-Fortschrittsbalken nötig** — Pakete sind immer versandkostenfrei (Preis > 100 €)
- **Kein Geschmacksprofil** — ein Paket enthält verschiedene Weine mit unterschiedlichen Profilen
- **Einzelweine müssen aufgelistet werden** — der Kunde will wissen, was im Paket ist
- **Sparpreis-Kommunikation** — Streichpreis + Ersparnis-Badge sind conversion-kritisch
- **Marketing-Fokus** — Pakete werden beworben, der emotionale Pitch ist wichtiger als bei Einzelflaschen

Deutsche Weinshops (Hawesko, Vinos, WirWinzer, Weinfreunde) nutzen alle ein spezialisiertes Bundle-Layout mit einer prominenten "Enthaltene Weine"-Section unterhalb der Buy Box.

## Proposed Solution

### Architektur-Entscheidung

Eigene `paketseite.html` als separates Template — kein Conditional innerhalb von `produktseite.html`. Gründe:
- Saubere Trennung, einfacher zu pflegen
- Im späteren Shopify-Build wird es ohnehin ein eigenes Template (`product.bundle.liquid`)
- Wireframe-Dokumentation ist klarer

### Shopify-Konzept: Metafield-basierte Weinverknüpfung

Im Wireframe wird visuell dargestellt, wie Shopify die enthaltenen Weine automatisch aus dem Backend zieht:

```
Shopify Admin → Produkt "Kennenlernpaket" → Metafield "bundle_items"
  Typ: "Product" → "List of Products"
  Verknüpfte Produkte: [Riesling Spätlese, Grauburgunder, Spätburgunder, ...]
```

Im Liquid-Template iteriert eine Section über `product.metafields.custom.bundle_items.value` und rendert pro Wein automatisch: Bild, Name, Rebsorte, Jahrgang, Preis, Link zur Einzelseite. **Keine manuelle Pflege der Weinliste nötig.**

Der Wireframe zeigt dies über eine Pin-Note (`.note`), die das Shopify-Metafield-Konzept erklärt.

### Seitenstruktur: `paketseite.html`

Die Seite folgt dem gleichen globalen Rahmen wie alle anderen Seiten (Announcement Bar, Header, Mobile Nav, Cart Drawer, Newsletter, Footer) und hat folgende paket-spezifische Sections:

---

#### Section 1: Promo Bar (optional)
Wie auf `produktseite.html` — z.B. "Nur noch 12 Pakete auf Lager" oder "Sommeraktion: 20% Extra-Rabatt"

#### Section 2: Product Hero (2-Spalten-Layout, `.pd` Grid)

**Linke Spalte — Sticky Gallery** (identisch zur Produktseite):
- Hauptbild: Gruppenshot aller Flaschen im Paket (statt Einzelflasche)
- 4 Thumbnails: 1x Lifestyle-Bild, 2x Einzelflaschen-Detailshots, 1x Verpackung/Geschenkbox
- Pin-Note: "Galerie zeigt Gruppenshot als Hero + Einzelflaschen als Thumbnails"

**Rechte Spalte — Buy Box** (`.pd__info`, angepasst):

| Element | Produktseite (Einzelwein) | Paketseite (NEU) |
|---------|--------------------------|-------------------|
| Badge | — | "Kennenlernpaket" oder "Bestseller" (`.pd__badge`) |
| Titel (h1) | "Riesling Spätlese 2023" | "Rotwein-Probierpaket Pfalz" |
| Bewertungen | Gleich | Gleich |
| Meta-Zeile | Rebsorte \| Jahrgang \| Region | "6 Flaschen \| 4,5 Liter \| Pfalz" |
| Beschreibung | Sensorische Weinbeschreibung | Emotionaler Paket-Pitch (Thema, Anlass, Versprechen) |
| "Was der Winzer sagt" | Gleich | Gleich (Winzer empfiehlt das Paket persönlich) |
| Geschmacksprofil | 5 Skalen (Süße, Säure, ...) | **ENTFÄLLT** |
| "Passt hervorragend zu" | Einzelne Empfehlung | **ENTFÄLLT** |
| **Kurzliste enthaltene Weine** | — | **NEU**: Kompakte Liste (Name + Menge pro Wein), z.B. "2x Riesling Spätlese, 2x Grauburgunder, 2x Spätburgunder" + Anker-Link "Alle Weine im Detail ↓" |
| Preis-Block | 24,90 € (einfach) | **Spar-Preis-Block**: Streichpreis "Einzelpreis gesamt: 89,40 €" + Paketpreis "49,90 €" + Ersparnis-Badge "Sie sparen 44%" (grüner Pill) |
| Liter-Preis | (33,20 €/l) | (11,09 €/l) |
| Legal | inkl. MwSt., zzgl. Versand | inkl. MwSt. · **Versandkostenfrei** · Enthält Sulfite |
| OMNIBUS-Hinweis | — | **NEU**: "Niedrigster Preis der letzten 30 Tage: 49,90 €" (EU-Pflicht bei Streichpreisen) |
| Shipping Bar | "Noch 85,10 € bis Versandkostenfrei" | **ENTFÄLLT** — stattdessen grüner Badge "Versandkostenfrei" |
| Qty-Selector + ATC | Gleich | Gleich |
| Trust Badges | ✓ Versand ab 69 € / SSL / 2-4 Tage | ✓ **Versandkostenfrei** / SSL / 2-4 Tage |
| Passende Weine (Cross-Sell) | 3 Mini-Cards | **ENTFÄLLT** — die enthaltenen Weine ersetzen Cross-Selling |

**Neue Buy-Box-Elemente im Detail:**

**a) Badge (`.pd__badge`)**
Pill-Shape über dem Titel: "Kennenlernpaket", "Bestseller", "Limitiert" — je nach Paket-Typ.

**b) Kompakte Weinliste in der Buy Box**
Kein Grid, sondern eine einfache Liste unter der Beschreibung:
```
Im Paket enthalten:
• 2× Riesling Spätlese 2023
• 2× Grauburgunder trocken 2023
• 2× Spätburgunder Ortswein 2022
↓ Alle 6 Weine im Detail ansehen
```
Der Anker-Link scrollt sanft zur ausführlichen Section weiter unten.

**c) Spar-Preis-Block**
```
Einzelpreis gesamt: 89,40 €  ← durchgestrichen, grau
Paketpreis:         49,90 €  ← groß, fett, schwarz
                [Sie sparen 44%]  ← grüner Pill-Badge
(11,09 €/l) · inkl. MwSt. · Versandkostenfrei · Enthält Sulfite

Niedrigster Preis der letzten 30 Tage: 49,90 €  ← klein, grau (OMNIBUS)
```

**d) Versandkostenfrei-Badge** (ersetzt Shipping Bar)
Statt der grünen Fortschrittsleiste ein statischer grüner Badge:
```
✓ Versandkostenfrei — keine Mindestbestellwert nötig
```

#### Section 3: Sticky Add-to-Cart Bar
Identisch zu `produktseite.html` — erscheint per Scroll-Event wenn `.pd__cart-row` aus dem Viewport scrollt. Zeigt: Paket-Titel (gekürzt), Paketpreis, Qty-Selector, ATC-Button.

#### Section 4: USP Bar
Wie auf `produktseite.html`, aber angepasste USPs:
- "Versandkostenfrei" (statt "Familienweingut seit 1876")
- "6 handverlesene Weine"
- "Bis zu 44% günstiger als Einzelkauf"

#### Section 5: "Im Paket enthaltene Weine" — **NEUE SECTION** (`.bundle-wines`)

**Dies ist die Kern-Neuerung der Paketseite.** Eine prominente Section mit voller Breite unterhalb der Buy Box.

**Layout:**
- Section-Label: "Paketinhalt"
- Headline: "Diese Weine sind im Paket enthalten"
- Subtext: "Jeder Wein ist auch als Einzelflasche erhältlich"
- Pin-Note (Shopify): "In Shopify werden die Weine automatisch über das Metafield `bundle_items` (Typ: Produktliste) verknüpft. Beim Anlegen des Pakets wählt man die Einzelweine aus dem Backend — Bild, Name, Rebsorte, Jahrgang und Preis werden automatisch ausgespielt."

**Wein-Cards (`.bundle-wine-card`):**
Grid: 3 Spalten Desktop, 2 Spalten Tablet, 1 Spalte Mobile.

Pro Karte:
```
┌─────────────────────────────────┐
│  [Flaschenbild]    120px hoch   │
│                                 │
│  2× im Paket         ← Badge   │
│  Riesling Spätlese 2023  ← h4  │
│  Weißwein · Trocken · Pfalz    │
│  ★★★★☆ 4,2 (87)               │
│                                 │
│  Einzelpreis: 14,90 €           │
│  (19,87 €/l)                    │
│                                 │
│  [Zur Einzelansicht →]  ← Link │
└─────────────────────────────────┘
```

Für das Wireframe-Beispiel: **6 Wein-Cards** (Standard-Paket), die das 3-Spalten-Grid füllen. Die Karten sind kleiner als die regulären `.pcard` Produktkarten, aber deutlich mehr als eine reine Textliste.

**Varianten-Badges für verschiedene Paketgrößen:**
Unterhalb der Section (oder oberhalb) Pill-Buttons wie auf `ueber-uns.html`:
```
[3er Probierpaket]  [6er Kennenlernpaket ✓]  [12er Vorratspaket]
```
Diese simulieren Shopify-Varianten — der aktive ist ausgefüllt, die anderen als Outline.

#### Section 6: Details & Paketinfo (Akkordeon)

Ersetzt "Details & Lagerempfehlung" der Einzelwein-Seite. Statt 4-spaltigem Weindetail-Grid ein angepasstes Akkordeon:

**Panel 1: "Über dieses Paket"**
- Ausführlicherer Text zum Paket-Thema, zur Zusammenstellung, zum Anlass
- Warum diese Weine zusammenpassen

**Panel 2: "Versand & Verpackung"**
- Versandkostenfrei
- Bruchsichere Spezialverpackung
- Lieferzeit 2-4 Werktage
- Klimaneutraler Versand

**Panel 3: "Häufige Fragen zum Paket"**
- "Kann ich einzelne Weine austauschen?" → Nein, feste Zusammenstellung
- "Wie lagere ich das Paket?" → Kühl und dunkel, liegend
- "Inhalt kann je nach Verfügbarkeit variieren" (Standardhinweis dt. Weinhandel)

#### Section 7: Kategorie-Beschreibung + Bild
Wie auf `produktseite.html` — "Über diese Kategorie" mit Link zurück zur Paket-Übersichtsseite.

#### Section 8: Social Proof
Wie auf `produktseite.html` — Google-Badge + Testimonials. Testimonials idealerweise paket-spezifisch ("Das Kennenlernpaket war eine wunderbare Entdeckungsreise...").

#### Section 9: Weingut Pitch
Wie auf `produktseite.html` — 2-spaltiger Weingut-Pitch.

#### Section 10: Qualitätspyramide (dark)
Wie auf `produktseite.html`.

#### Section 11: Kategorien (6 Kreise)
Wie auf `produktseite.html`.

#### Section 12: Wein verschenken & abonnieren
Wie auf `produktseite.html` — 2 Cards + Pin-Note.

#### Section 13-16: Newsletter, Footer, Cart Drawer
Identisch zu allen anderen Seiten.

---

### Verlinkung innerhalb der Website

Nach Erstellung von `paketseite.html` müssen folgende Links aktualisiert werden:

| Stelle | Datei(en) | Aktueller Link | Neuer Link |
|--------|-----------|----------------|------------|
| Mega Menu → "Kennenlernpakete" | alle 9 HTML | `kategorie.html` | `paketseite.html` |
| Mega Menu → Produkt-Teaser "Kennenlernpaket" | alle 9 HTML | (kein href) | `paketseite.html` |
| Announcement Bar "Jetzt Kennenlernpaket sichern" | alle 9 HTML | `#` | `paketseite.html` |
| index.html → Kennenlernpaket-Pitch "bestellen" | index.html | `produktseite.html` | `paketseite.html` |
| produktseite.html → Kennenlernpaket-Section | produktseite.html | `produktseite.html` | `paketseite.html` |
| ueber-uns.html → Kennenlernpaket-Section | ueber-uns.html | (kein href) | `paketseite.html` |
| Cart Drawer → Upsell "Kennenlernpaket" | alle 9 HTML | (kein href) | `paketseite.html` |

---

## CSS-Änderungen in `styles.css`

### Neue Klassen

| Klasse | Beschreibung |
|--------|-------------|
| `.pd__badge` | Pill-Badge über dem Titel (z.B. "Kennenlernpaket") |
| `.pd__price--bundle` | Spar-Preis-Block mit Streichpreis + Ersparnis-Badge |
| `.pd__price-original` | Durchgestrichener Einzelpreis (grau, `text-decoration: line-through`) |
| `.pd__price-savings` | Grüner Pill-Badge "Sie sparen 44%" |
| `.pd__omnibus` | OMNIBUS-Hinweis (klein, grau) |
| `.pd__free-shipping` | Grüner "Versandkostenfrei"-Badge (ersetzt `.shipping-bar`) |
| `.pd__bundle-list` | Kompakte Weinliste in der Buy Box |
| `.bundle-wines` | Section-Container für die Wein-Card-Übersicht |
| `.bundle-wine-card` | Einzelne Wein-Card im Paketinhalt |
| `.bundle-wine-card__img` | Flaschenbild (120px) |
| `.bundle-wine-card__qty` | Mengen-Badge (z.B. "2×") |
| `.bundle-wine-card__meta` | Rebsorte · Geschmack · Region |
| `.bundle-wine-card__price` | Einzelpreis |
| `.bundle-wine-card__link` | Link zur Einzelansicht |
| `.bundle-variants` | Pill-Buttons für Paketgrößen (3er/6er/12er) |
| `.bundle-variants__pill` | Einzelner Pill-Button (aktiv/inaktiv) |

### Responsive Verhalten

| Breakpoint | `.bundle-wines` Grid |
|------------|---------------------|
| Desktop (> 1024px) | 3 Spalten |
| Tablet (768px–1024px) | 2 Spalten |
| Mobile (< 768px) | 1 Spalte (Cards horizontal: Bild links, Info rechts) |
| Small Mobile (< 480px) | 1 Spalte (Cards vertikal gestapelt) |

---

## Acceptance Criteria

### Funktionale Anforderungen
- [ ] `paketseite.html` erstellt als eigenständige Datei basierend auf `produktseite.html`
- [ ] Alle globalen Elemente identisch (Announcement Bar, Header, Mega Menu, Mobile Nav, Cart Drawer, Newsletter, Footer)
- [ ] Buy Box zeigt: Badge, Pakettitel, Bewertungen, Flaschen-Meta, Beschreibung, Winzer-Zitat
- [ ] Geschmacksprofil und "Passt hervorragend zu" sind NICHT auf der Paketseite
- [ ] Versandkosten-Fortschrittsleiste ist NICHT auf der Paketseite — stattdessen "Versandkostenfrei"-Badge
- [ ] Spar-Preis-Block mit Streichpreis, Paketpreis, Ersparnis-Badge und OMNIBUS-Hinweis
- [ ] Kompakte Weinliste in der Buy Box mit Anker-Link zur Detail-Section
- [ ] "Im Paket enthaltene Weine" Section mit 6 Wein-Cards (3-Spalten-Grid)
- [ ] Wein-Cards zeigen: Bild, Menge, Name, Jahrgang, Rebsorte, Bewertung, Einzelpreis, Link
- [ ] Varianten-Badges für Paketgrößen (3er/6er/12er) als Pill-Buttons
- [ ] Details-Akkordeon angepasst (Paketinfo statt Weindetails)
- [ ] Sticky Add-to-Cart Bar funktioniert (Scroll-Event)
- [ ] Pin-Note erklärt Shopify-Metafield-Konzept für automatische Weinverknüpfung

### Konsistenz
- [ ] Alle Links zu "Kennenlernpaket" auf allen 9 bestehenden Seiten zeigen auf `paketseite.html`
- [ ] Konsistenz-Matrix in `PROJEKTPLAN.md` um Zeile für `paketseite.html` erweitert
- [ ] `paketseite.html` in Dateistruktur-Übersicht im PROJEKTPLAN aufgenommen

### Design
- [ ] Eurus-Stil beibehalten (Pill-Shape Buttons, Qty-Selector)
- [ ] Platzhalter-System beibehalten (grüne `.ph-img`)
- [ ] Wireframe-Anmerkungen (`.note`) an relevanten Stellen
- [ ] Responsive: funktioniert auf allen 4 Breakpoints (1600px+, 1024px, 768px, 480px)

---

## Implementierungs-Phasen

### Phase 1: HTML-Gerüst (~60% des Aufwands)
1. `produktseite.html` kopieren → `paketseite.html`
2. Title + Meta anpassen
3. Buy Box umbauen:
   - Badge hinzufügen
   - Titel + Meta auf Paket anpassen
   - Geschmacksprofil + "Passt zu" entfernen
   - Kompakte Weinliste einfügen
   - Spar-Preis-Block aufbauen
   - Shipping Bar durch Versandkostenfrei-Badge ersetzen
   - Trust Badges anpassen
   - Cross-Selling ("Passende Weine") entfernen
4. "Im Paket enthaltene Weine" Section erstellen (6 Cards)
5. Varianten-Badges (3er/6er/12er) einfügen
6. Details-Akkordeon anpassen (3 Panels statt 4-spaltig)
7. USP Bar Texte anpassen
8. Sticky ATC Bar: Paket-Titel + Paketpreis

### Phase 2: CSS (~25% des Aufwands)
1. Neue Klassen in `styles.css` anlegen (`.pd__badge`, `.bundle-wines`, `.bundle-wine-card`, etc.)
2. Spar-Preis-Block Styling (Streichpreis, Savings-Badge)
3. Versandkostenfrei-Badge Styling
4. Bundle-Wine-Card Grid + Responsive
5. Varianten-Pills Styling

### Phase 3: Verlinkung + Dokumentation (~15% des Aufwands)
1. Links auf allen 9 bestehenden Seiten aktualisieren (Mega Menu, Announcement Bar, Kennenlernpaket-Sections, Cart Drawer Upsell)
2. `PROJEKTPLAN.md` aktualisieren (Dateistruktur, Seitenübersicht, Konsistenz-Matrix)
3. `MEMORY.md` aktualisieren

---

## Referenzen

### Interne Referenzen
- Bestehende Produktseite: `produktseite.html` (Basis-Template)
- Design-System: `styles.css` (Custom Properties, BEM-Klassen)
- Kennenlernpaket-Section: `ueber-uns.html:332-359` (Varianten-Badges Muster)
- Produkt-Card Pattern: `kategorie.html` (`.pcard` als Referenz für `.bundle-wine-card`)
- Projektdoku: `PROJEKTPLAN.md`

### Externe Referenzen (Best Practices)
- Hawesko Weinpakete: Streichpreis + Ersparnis-Badge als Standard
- Vinos.de: Prominente "Enthaltene Weine" Section unterhalb Buy Box
- mein-weinladen.com (Shopify): Metafield-basierte Bundle-Verknüpfung
- Weinfreunde: Tiered-Pricing mit % Rabatt-Anzeige
- OMNIBUS-Richtlinie: "Niedrigster Preis der letzten 30 Tage" bei Streichpreisen (EU-Pflicht)
- Shopify Docs: Product Metafield Typ "List of Products" für Bundle-Items
- Baymard Institute: Akkordeon-Panels > Horizontal Tabs (nur 8% Übersehrate)
