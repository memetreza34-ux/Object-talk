# Produktionsplan – 008 Longform Verdauung

## Thema
**Was passiert mit Essen in deinem Körper?**

## Status
Erstes reguläres Longform-Video nach Abschluss der Testphase.

## Ziel
Eine vollständige, kausale Reise eines Bissens erklären: vom Mund über Magen und Dünndarm bis zur Aufnahme der Nährstoffe und zur Verarbeitung der Reste im Dickdarm.

## Laufzeit
- Nutzerziel: **6–7 Minuten**
- Script: ca. **1.110 Wörter**
- Standard-Voice: 1.10x
- Zielbereich nach echter Voice-Verarbeitung: 6:00–7:00
- nicht künstlich strecken

## Dramaturgie

### Hook / Einleitung
- scheinbar verschwindender Bissen
- Wendung: Verdauung beginnt bereits im Mund
- Payoff: aus sichtbarem Essen werden Bausteine in Blut, Leber und Zellen

### Hauptteil
1. Mund: Kauen, Oberfläche, Speichel, Amylase
2. Schlucken und Peristaltik
3. Magen: Mischen, Säure, Pepsin, Schutzschicht
4. Dünndarm: Pankreas, Bicarbonat, Enzyme
5. Galle und Fett
6. Zerlegung der Makronährstoffe
7. Darmzotten/Mikrovilli
8. Zucker/Aminosäuren → Blut → Leber
9. viele Fette → Chylomikronen → Lymphe → Blut
10. Nutzung der Bausteine im Körper
11. Dickdarm: Wasser, Mikroorganismen, Ballaststoffe
12. Enddarm und Ausscheidung

### Schluss
- gesamte Kausalkette kurz visuell schließen
- Anfangsfrage beantworten
- keine neue Nebenfrage öffnen

## Bilder
- **77 eindeutige Illustrationen**
- ca. 3–6 Sekunden pro Bild als Ziel
- harte Obergrenze 7 Sekunden
- keine Duplikate
- lieber zusätzliches Bild als Informationsüberladung
- ein Hauptprozess pro Bild
- bevorzugt 2–4 sichtbare Kernelemente

## Bildwelt
**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

## Textregeln
- Cover: exakt nur `Was passiert mit Essen?`
- keine weiteren Cover-Labels
- normale Bilder 0–2 Labels, bevorzugt 0–1
- nur notwendige Begriffe
- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- schwacher Kontrast = regenerieren
- keine Produktionsnummern sichtbar

## Remotion
**0 sichtbarer Text.**

Remotion nur für:
- Voice
- Timing
- Vollbildbilder
- dezente Zooms/Pans
- Schnitte
- nicht-textliche Übergänge
- Render

## Export / YouTube-ready Paket

Nach Phase 3 liegt die komplette Veröffentlichung unter:
`04_export/`

Pflicht:
- `04_export/fertiges-video/Object-Talk-008-Verdauung-YOUTUBE.mp4`
- `04_export/YOUTUBE-UPLOAD-PAKET.md`
- `04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt`
- `04_export/YouTube-Caption.md`
- `04_export/render-report.md`
- `04_export/quality-scorecard.md`
- `04_export/postmortem.md`

Der Ordner `fertiges-video/` enthält nur die endgültige Master-MP4. Keine Preview- oder Draft-Dateien als final behalten.

Titel, Beschreibung und Caption sind individuell für Video 008 vorbereitet und werden nach Sichtung des echten Finalrenders noch einmal gegen den tatsächlichen Inhalt geprüft.

## Qualitätsziel
- wissenschaftliche Sicherheit >= 8/10
- jedes Bild >= 8/10
- sofort verständlicher Mechanismus
- keine überladenen Frames
- hohe visuelle Abwechslung über Maßstab und Komposition
- keine Rückkehr zu alter 2.5D-/3D-Bildwelt
- keine UI-/PowerPoint-Optik

## Produktionsreihenfolge
1. Phase-1-Validator ausführen.
2. Voice erzeugen und kanonisieren.
3. 77 Flow-Bilder einzeln generieren.
4. jedes Bild gegen Label-, Kontrast-, Wissenschafts- und Dichte-QA prüfen.
5. Phase-2-Validator ausführen.
6. Whisper/Timeline erzeugen.
7. Remotion textfrei direkt nach `04_export/fertiges-video/Object-Talk-008-Verdauung-YOUTUBE.mp4` rendern.
8. kompletten finalen Film visuell sichten.
9. Renderbericht + Scorecard + Postmortem ausfüllen.
10. YouTube-Titel, Beschreibung und Caption gegen den finalen Film prüfen.
11. Erst danach Status `YouTube-ready`.

## Besonderer Anspruch
Dieses Video ist kein weiterer Kurztest. Es soll als erster echter Produktionslauf zeigen, dass die getestete Pipeline eine längere, zusammenhängende biologische Geschichte mit hoher Bildqualität tragen kann.