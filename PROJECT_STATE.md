# Object-Talk / Lebenslogik – Aktueller Projektstand

Letzte Aktualisierung: 14.10.2026

## AKTIVE PRODUKTION – VIDEO 010

`youtube-videos/010-longform-hunger/`

**Thema:** Warum du nach dem Essen so schnell wieder Hunger hast?
**YouTube-Kanal:** Lebenslogik (technisches Repo: Object-Talk).
**Status:** Phase-1-Material erstellt und statisch konsistent, Flow-/Audio-/MP4-Produktion NOCH NICHT durchgeführt. Keine finale Videodauer bestätigt.

- **1044 Sprecherwörter**, 9 Kapitel, 72 individuelle normale Flow-Videoszenen, 27 davon mit 1–2 sinnvollen deutschen Labels.
- 3 separate Coverkandidaten; danach Nutzerwahl und erste normale Videoszenen 01–05, anschließend Fünfergruppen.
- Ein EINZIGER Flow-Prompt unter `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` und ein Fließtext-Skript `01_script/script.txt`.
- 3 sichtbare Ordner; `03_export/` soll final genau Video, separates Cover, YouTube-Beschreibung und echt zeitgestempelte Untertitel enthalten. Bis Medien erstellt sind nur Entwurfstexte; keine falsche MP4.
- Frühere Fehler aus 008/009 in `.intern/05_info/improvement-applied.json` konkret nachgewiesen: klare biologisch nachvollziehbare Bilder, sicherer Flow-Workflow, schlanker Export.
- Nächster Schritt: zuerst drei Cover in Google Flow erzeugen, Nutzer wählt 1/2/3, danach 72 Szenen, Voice und Render.
- `tools/improvement_loop.py` ist in der Phase-1-Prüfung integriert; GitHub Actions waren zuletzt fehlgeschlagen. Ein vollständig ausgeführter Python-Test ist derzeit **nicht bestätigt**. Statische Querverweisprüfungen der 72 Szenen wurden durchgeführt.

## Bisherige Produktionsnotizen / Video 009

`youtube-videos/009-longform-schlaf/`

**Thema:** Was passiert in deinem Körper, während du schläfst?

**Status: PHASE 1 VORBEREITET / MEDIEN AUSSTEHEND; 008-PRODUKTIONSSTRUKTUR 1:1 ÜBERNOMMEN.** Es gibt noch keine finale Voice, keine akzeptierten Flow-Bilder und kein YouTube-MP4 im neuen Projekt.

## Referenz – Video 008 Verdauung

Das freigegebene erste Longform-Video 008 ist für 009 das strukturelle und visuelle Vorbild: 77 eindeutige Bilder, 13 Mechanismusabschnitte, dieselbe Flow-Promptgliederung/Zeichensprache, derselbe ausführliche Antigravity-Auftrag und Export/QA. Nur Thema, Script und biologische Motive wurden geändert. Eine einzige Flow-Promptdatei plus bilder-zip/ bleibt Nutzeroberfläche. Ein tatsächlicher neuer Flow-/MP4-Render ist noch NICHT geprüft.

## Ziel für Video 009

- Laufzeit: **6:00–7:00 Minuten** nach echter Audioverarbeitung bestätigen.
- Script: **986 Wörter**, 77 einzigartige semantische Bilder.
- 16:9, 1920×1080, 30fps; finales Voice 1.10×.
- Cover nur Titel `Was macht dein Körper nachts?` und zeitlich kurz.
- Starke Hook → Schlafdruck/innere Uhr → Schlafstadien → Tiefschlaf/Körper → Gedächtnis → Immunsystem → REM/Träume → Zyklen → Schluss.
- Jeder Frame: eine Hauptaussage, höchstens zwei kurze Labels, Kontrast Pflicht, keine Mehrfachtafeln.
- Mehr Licht-/Farbvariation (Dämmerung, Dunkelblau, warme Körperfarben, Morgenlicht).
- 0 sichtbarer Remotion-Text und 0 sichtbare Produktionsnummern.
- keine Bildduplikate; nie länger als 7 Sekunden pro Bild.

## Recherche und Dateien

- NIH/NHLBI, NICHD, CDC als Quellen.
- `01_script/script.txt` und kopierbarer Voice-Text.
- `05_info/Recherche.md`, Claim-Matrix, Mechanism Map, 77 Szenen und 13 thematische Mechanismus-Indizes (wie 008).
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` für 77 Bilder mit deutscher Text-Whitelist.
- `03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt`, deaktivierter Overlayplan.
- `04_export/` mit Videoziel, individueller Caption, YouTube-SRT und komplettem zeitcodiertem Script.
- SRT und Zeit-Script bleiben bis zur finalen `timeline.json` ausdrücklich PENDING.

## Vorherige Produktion 008

`youtube-videos/008-longform-verdauung/` ist das vorherige Longform-Thema. Der Nutzer hat einen gerenderten Film zur Besprechung bereitgestellt. Im GitHub-Repo ist die finale Master-MP4 samt echten Zeitdaten noch nicht als geprüftes Exportpaket abgelegt. Nicht fälschlich als repo-seitig YouTube-ready deklarieren.

## Nächster Produktionsschritt

1. `python tools/validate_planning_v2.py youtube-videos/009-longform-schlaf`
2. Finale Voice aufnehmen/generieren und Laufzeit prüfen.
3. Alle 77 Flow-Bilder erstellen, einzeln wissenschaftlich und visuell reviewen.
4. `python tools/validate_planning_v2.py youtube-videos/009-longform-schlaf --phase2`
5. `python tools/prepare_phase3.py youtube-videos/009-longform-schlaf`.
6. MP4 rendern, komplette Sicht-/Tonprüfung, Untertitel aus echter Timeline, Export-QA.

## Historie

Pilotphase 000–007 abgeschlossen; Bildwelt: **Clean Animated Biology Illustration**.

## Produktionsentscheidung: keine Bildvorlagen (10.10.2026)
Wie beim erfolgreichen Verdauungsvideo 008 wird Google Flow **ausschließlich mit einem vollständigen Textprompt** bedient. Keine externen Stilbilder, 008-Frame-ZIP-Dateien oder Cover-als-Referenz. Erst genau drei separate Cover erstellen, Auswahl abwarten, dann Szenen 02–77 in Fünfergruppen. Die bekannte organisch-illustrative Bildwelt ist im Prompt positiv beschrieben. Bild-QA bleibt Pflicht; eine exakte Reproduktion ist mit generativer KI nicht garantiert.

## Tablet-Handoff nach Phase 1 (dauerhaft)

Bei jeder abgeschlossenen Phase 1 direkt in der Chat-Antwort zwei anklickbare Dateilinks ausgeben, niemals nur einen Sammellink oder Ordnerpfade:

**Google-Flow-Prompt öffnen:** https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/009-longform-schlaf/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt

**Voice-over-Skript öffnen:** https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/009-longform-schlaf/01_script/script.txt

Diese URLs gelten NUR für das aktuelle Video 009. Bei späteren Videos immer den zugehörigen Projektordner einsetzen. Als Markdown-Klicklinks oder funktionierende Öffnen-Schaltflächen in der Antwort präsentieren. Die Dateien sind Text zum direkten Kopieren auf Tablet/PC; Login kann erforderlich sein. Details: `AGENTS.md`, `PROJECT_CONTRACT.md`.
