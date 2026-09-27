# Produktionsregeln – Object-Talk Longform

Diese Regeln gelten fuer jedes lange YouTube-Video im Repository. `PROJECT_CONTRACT.md` ist uebergeordnet.

## 1. Videolaenge
- harte Mindestlaenge final: 5:00 Minuten, ausser dokumentierter Testmodus
- normaler Zielbereich: 5:30–8:00 Minuten
- kein kuenstliches Strecken

## 2. Script
`01_script/script.txt` enthaelt ausschliesslich den final gesprochenen Text.

Sprachstil:
- kurze verstaendliche Saetze
- Fachbegriffe direkt erklaeren
- konkrete Beispiele
- keine unnoetigen Wiederholungen
- neugierig und klar, nicht babyhaft

## 3. Semantische Szenen
Die Bildanzahl wird nicht kuenstlich vorher festgelegt.

`finales Script → echte visuelle Sinnwechsel → Szenen → Bildanzahl`

- ein Satz darf mehrere Bilder bekommen
- mehrere Saetze duerfen ein Bild teilen, wenn dieselbe visuelle Aussage gilt
- keine Fuellbilder

## 4. Bildrhythmus
- Hook / schneller Einstieg: etwa 2–4 Sekunden
- normale Erklaerszene: etwa 3–6 Sekunden
- harte Obergrenze: 7 Sekunden pro Standbild
- lange Standzeiten nicht allein durch Zoom/Pan kaschieren
- neues Bild bei echtem Wechsel von Ort, Massstab, Struktur, Zustand, Prozess, Vergleich oder Kernaussage

## 5. Bildformat
- 16:9 horizontal
- 1920×1080 Ziel
- genug Rand fuer dezente Bewegung
- Illustration bleibt vollformatig

## 6. Nummerierung
`Szene 01 = Bild_01`, `Szene 02 = Bild_02`, usw.

Diese Nummerierung ist ausschliesslich interne Produktionsmetadaten.

**Niemals sichtbar im finalen Bild/Video:**
- `Bild_01`, `Bild 01`, `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Asset-IDs
- Prompttitel

Keine Luecke, keine doppelte Nummer im Dateisystem; aber keine Nummer darf Teil der sichtbaren Illustration werden.

## 7. Verbindliche visuelle Hauptsprache

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Pflicht:
- animierte Illustration statt Render-Look
- vereinfachte, erkennbare Anatomie
- weiche organische Formen und saubere Konturen
- weiche Verlaeufe und subtile Schatten
- leichte Tiefe ohne CGI-Wirkung
- helle ruhige Hintergruende
- klare biologische Farben
- wenige wichtige Elemente
- ein dominanter Prozess/Zusammenhang
- normalerweise 1–3 kurze deutsche Labels

## 8. Visuelle Vielfalt

Bevorzugt:
- Cutaway
- Querschnitt
- Makro-Nahaufnahme
- Zell-Innenansicht
- Prozess
- Transportweg
- Ursache → Wirkung
- Vorher / Nachher
- Vergleich
- Massstabswechsel
- Alltagsszene mit biologischem Fokus

Regeln:
- maximal zwei isolierte Objektportraits hintereinander
- benachbarte Szenen in mindestens zwei Dimensionen sichtbar unterscheiden
- keine Bildduplikate zum Zeitfuellen
- nicht immer dieselbe zentrierte Objektkomposition verwenden

## 9. Komplexitaet

Ein Bild soll schnell verstanden werden koennen.

Richtwert:
- 2–5 zentrale sichtbare Elemente
- 1 Hauptprozess
- 1–3 Labels

Mehr Inhalt = neues Bild, nicht mehr Kleinteile.

## 10. Prompt-Sprache

- Generierungsanweisungen auf Englisch
- viewer-facing Text nur Deutsch
- Prompts kurz halten
- kanonischen Styleblock verwenden
- interne Bildnummern, Dateinamen und Prompttitel niemals sichtbar
- jeder Flow-Auftrag muss ausdruecklich sagen, dass Produktions-IDs nicht gerendert werden duerfen

## 11. Labels in Google Flow

Biologische Labels werden standardmaessig direkt in Google Flow erzeugt.

- 1–3 kurze deutsche Begriffe
- klare Sans-Serif-Schrift
- duenne Hinweislinien/Pfeile
- eindeutige Zuordnung
- falsche Schreibweise oder falsche Zuordnung = regenerieren/korrigieren
- keine Textwaende

Remotion ersetzt, ergaenzt oder korrigiert diese Labels nicht.

## 12. Praesentationssystem: 100 % Vollbild

Kanalstandard fuer kuenftige Videos:
- **100 % Vollbild-Illustration**
- Remotion erzeugt keinen sichtbaren Text
- keine Zwischenueberschriften
- keine Key-Facts
- keine Summary-Zeilen
- keine Kapiteltexte
- keine Callouts
- keine Untertitel/Captions als Standard
- keine Textkarten
- keine dauerhaften Seitenleisten, Rahmen oder Presenter-Layouts

Remotion darf nur:
- Audio
- Timing
- leichte Push-/Pull-/Pan-Bewegungen
- statische Frames
- Schnitte
- dezente nicht-textliche Uebergaenge
- Rendering

`03_pipeline/overlay-plan.json` muss deaktiviert und leer sein.

Details: `engine/PRESENTATION-OVERLAY-SYSTEM.md`.

## 13. Referenzsystem

Die schriftliche Bildwelt ist die oberste Stilautoritaet.

Eine spaetere `assets/channel/STYLE_REFERENCE.png` ist optional und nur zusaetzlicher visueller Anker nach ausdruecklicher Nutzerfreigabe.

`Bild_01` ist nicht automatisch der Master-Stilanker fuer alle Folgeframes.

## 14. Harte Stil-/Produktions-Fails

- fotorealistischer Medizin-Look
- Medical-CGI / Anatomiesoftware
- glossy Plastik-3D
- Feature-Animation/Pixar-Look als Standard
- Spielzeug-/Kinderbuch-Look
- Corporate-Stock-Grafik
- ueberladene Infografik
- zu viele Labels/Pfeile
- random Icons ohne Lehrfunktion
- Gore / nasses Gewebe
- sichtbare interne Bild-/Szenennummer
- sichtbarer Dateiname / Asset-ID / Prompttitel
- irgendein von Remotion erzeugter sichtbarer Text
- nicht-leerer Remotion-Overlay-Plan

## 15. QA

- wissenschaftlich plausibel
- passend zum Voiceover
- Hauptaussage sofort erkennbar
- Komplexitaet niedrig
- Labels korrekt und lesbar
- Stilkontinuitaet zur kanonischen Bildwelt
- 100 % Vollbild-Illustration
- 0 Remotion-Textelemente
- 0 sichtbare Produktions-IDs
- kein schwerer KI-Artefakt
- keine unnoetige Wiederholung
- korrekte interne Assetnummerierung
