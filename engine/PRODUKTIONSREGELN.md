# Produktionsregeln – Object-Talk Longform

Diese Regeln gelten fuer jedes lange YouTube-Video im Repository. `PROJECT_CONTRACT.md` ist uebergeordnet.

Zusaetzlich verbindlich:
`engine/VISIBLE-TEXT-STANDARD.md`

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
- wenn ein Speech-Beat mehrere Hauptideen enthaelt, auf mehrere Bilder aufteilen

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
- `engine/VISIBLE-TEXT-STANDARD.md`

Pflicht:
- animierte Illustration statt Render-Look
- vereinfachte, erkennbare Anatomie
- weiche organische Formen und saubere Konturen
- weiche Verlaeufe und subtile Schatten
- leichte Tiefe ohne CGI-Wirkung
- helle ruhige Hintergruende
- klare biologische Farben
- **eine Hauptidee pro Bild**
- bevorzugt 2–4 wichtige sichtbare Elemente
- normale Bilder **0–2 kurze deutsche Labels**, nur wenn wirklich noetig

## 8. Cover – HARD RULE

`Bild_01` / Cover:
- genau ein sichtbarer Textblock
- nur Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Pfeiltexte

Zusatztext auf dem Cover = regenerieren.

## 9. Visuelle Vielfalt

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

## 10. Informationsdichte

Ein Bild soll schnell verstanden werden koennen.

Richtwert:
- 1 Hauptaussage / 1 Hauptprozess
- 2–4 zentrale sichtbare Elemente
- 0–2 Labels

Wenn mehr Inhalt noetig ist:
1. unwichtige Information weglassen, oder
2. neues Bild planen.

**Lieber mehr Bilder als mehr Text oder Details in einem Frame.**

## 11. Prompt-Sprache

- Generierungsanweisungen auf Englisch
- viewer-facing Text nur Deutsch
- Prompts kurz halten
- kanonischen Styleblock verwenden
- interne Bildnummern, Dateinamen und Prompttitel niemals sichtbar
- jeder Flow-Auftrag muss ausdruecklich sagen, dass Produktions-IDs nicht gerendert werden duerfen
- jeder Cover-Prompt muss title-only explizit festlegen
- bei sichtbarem Text muss der Kontrast explizit geregelt werden

## 12. Labels in Google Flow

Biologische Labels werden standardmaessig direkt in Google Flow erzeugt.

- 0–2 kurze deutsche Begriffe, maximal 2
- bevorzugt 0 oder 1, wenn die Szene schon klar ist
- Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- klare Sans-Serif-Schrift
- keine dekorativen Anfuehrungszeichen
- duenne Hinweislinien/Pfeile nur wenn noetig
- eindeutige Zuordnung
- falsche Schreibweise, falsche Zuordnung, unnoetiges Label oder schwacher Kontrast = regenerieren/korrigieren
- keine Textwaende

Remotion ersetzt, ergaenzt oder korrigiert diese Labels nicht.

## 13. Textkontrast

- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- kein hell-auf-hell
- kein dunkel-auf-dunkel
- Text bevorzugt in ruhiger negativer Flaeche platzieren

Schlecht lesbarer Text = regenerieren.

## 14. Praesentationssystem: 100 % Vollbild

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

## 15. Referenzsystem

Die schriftliche Bildwelt ist die oberste Stilautoritaet.

Eine spaetere `assets/channel/STYLE_REFERENCE.png` ist optional und nur zusaetzlicher visueller Anker nach ausdruecklicher Nutzerfreigabe.

`Bild_01` ist nicht automatisch der Master-Stilanker fuer alle Folgeframes.

## 16. Harte Stil-/Produktions-Fails

- fotorealistischer Medizin-Look
- Medical-CGI / Anatomiesoftware
- glossy Plastik-3D
- Feature-Animation/Pixar-Look als Standard
- Spielzeug-/Kinderbuch-Look
- Corporate-Stock-Grafik
- ueberladene Infografik
- mehrere konkurrierende Hauptideen im selben Frame
- mehr als 2 Labels im normalen Bild
- Label mit mehr als 3 Woertern
- Zusatztext auf dem Cover
- schwacher Textkontrast
- helle Schrift auf hellem Hintergrund
- dunkle Schrift auf dunklem Hintergrund
- unnoetige Labels/Pfeile/Nebeninformation
- random Icons ohne Lehrfunktion
- Gore / nasses Gewebe
- sichtbare interne Bild-/Szenennummer
- sichtbarer Dateiname / Asset-ID / Prompttitel
- irgendein von Remotion erzeugter sichtbarer Text
- nicht-leerer Remotion-Overlay-Plan

## 17. QA

- wissenschaftlich plausibel
- passend zum Voiceover
- genau eine Hauptaussage sofort erkennbar
- Komplexitaet niedrig
- normale Bilder max. 2 Labels
- Labels korrekt, notwendig und lesbar
- Textkontrast PASS
- Informationsdichte PASS
- Cover title-only PASS
- Stilkontinuitaet zur kanonischen Bildwelt
- 100 % Vollbild-Illustration
- 0 Remotion-Textelemente
- 0 sichtbare Produktions-IDs
- kein schwerer KI-Artefakt
- keine unnoetige Wiederholung
- korrekte interne Assetnummerierung
