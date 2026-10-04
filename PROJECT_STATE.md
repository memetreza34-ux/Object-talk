# Object-Talk – Project State

Letzte Aktualisierung: 04.10.2026

## Aktive Produktion

`youtube-videos/008-longform-verdauung/`

Thema:
**Was passiert mit Essen in deinem Körper?**

Status:
**ERSTES REGULÄRES LONGFORM-VIDEO / PHASE 1 VORBEREITET**

Die Testphase 000–007 ist abgeschlossen. Neue Produktionen sollen grundsätzlich als reguläre Longform-Videos geplant werden, sofern der Nutzer nicht ausdrücklich einen neuen Test bestellt.

## Ziel für 008

- finale Laufzeit: **6:00–7:00 Minuten**
- Script: ca. **1.110 Wörter**
- **77 eindeutige Illustrationen**
- 16:9 / 1920×1080 / 30 fps
- Voice standardmäßig 1.10x
- keine künstliche Laufzeitstreckung
- kein Standbild länger als 7 Sekunden
- keine Bildduplikate

## Dramaturgie

1. Hook: Was wird aus einem Bissen nach dem Schlucken?
2. Wendung: Verdauung beginnt bereits im Mund.
3. Mund: Kauen, Speichel, Amylase.
4. Schlucken und Peristaltik.
5. Magen: Mischen, Säure, Pepsin, Schutzschicht.
6. Dünndarm: Pankreas, Bicarbonat, Verdauungsenzyme.
7. Leber/Gallenblase: Galle und Fettverdauung.
8. Aufspaltung der Nährstoffe.
9. Darmzotten/Mikrovilli und Aufnahme.
10. Zucker/Aminosäuren → Blut → Leber.
11. viele Fette → Chylomikronen → Lymphe → Blut.
12. Nutzung der Nährstoffbausteine.
13. Dickdarm, Wasseraufnahme, Mikroorganismen und Reste.
14. Schluss: Aus Essen werden nutzbare Bausteine.

## Verbindliche Bildwelt

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

## Harte Bild-/Textregeln

- **Cover = exakt ein sichtbarer Textblock, nur Titel**
- Cover 008: `Was passiert mit Essen?`
- keine Zusatzlabels auf dem Cover
- normale Bilder: 0–2 Labels, bevorzugt 0–1
- jedes Label maximal 3 Wörter
- wenn ein Bild ohne Label verständlich ist: kein Label
- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- schwacher Kontrast = FAIL / regenerieren
- eine Hauptidee pro Bild
- bevorzugt 2–4 zentrale sichtbare Elemente
- lieber mehr Bilder als ein überladener Frame
- Produktionsnummern/Dateinamen niemals sichtbar

## Präsentationssystem

**100 % Vollbild-Illustration. Remotion erzeugt keinen sichtbaren Text.**

Remotion darf nur:
- Audio
- Timing
- statische Vollbildbilder
- sanfte Push-/Pull-/Pan-Bewegungen
- Schnitte
- dezente nicht-textliche Übergänge
- Rendering

`03_pipeline/overlay-plan.json` bleibt deaktiviert und leer.

## Phase 1 vorbereitet

Vorhanden:
- finales Script
- Voiceover-Zum-Kopieren
- Recherche
- Claim-Matrix
- Mechanism Map
- 77 semantische Szenen
- Visual-Plan
- Label-Plan
- kompletter Google-Flow-Prompt für 77 Bilder
- Flow-Agent-Regeln
- Bild-QA-Gate
- deaktivierter Overlay-Plan
- Antigravity-/Phase-3-Prompt
- Produktionsplan

## Nächster Produktionsschritt

1. `python tools/validate_planning_v2.py youtube-videos/008-longform-verdauung`
2. Voice aus `01_script/VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
3. Voice auf 1.10x kanonisieren und echte Laufzeit prüfen.
4. 77 Flow-Bilder einzeln erzeugen.
5. Jedes Bild wissenschaftlich, visuell, textlich und auf Informationsdichte prüfen.
6. Phase-2-Validator ausführen.
7. Whisper/Timeline erstellen.
8. textfreien Remotion-Render bauen.
9. kompletten finalen Film visuell prüfen.
10. Scorecard + Postmortem ausfüllen.

## Testphase

Die Piloten `000` bis `007` bleiben als Lern- und Fehlerhistorie erhalten, sind aber nicht mehr aktive Produktion.