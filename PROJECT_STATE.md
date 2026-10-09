# Object-Talk – Project State

Letzte Aktualisierung: 08.10.2026

## Aktive Produktion

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

## WICHTIG: Reale Video-008-Bildreferenzen (Stand 09.10.2026)

Die visuelle Original-MP4 von 008 wurde erneut geprüft. Die frühere Übernahme allein des generischen `Clean Animated Biology Illustration`-Stils war unzureichend. Der neue verbindliche Stilanker sind echte Standbilder aus 008 (Referenzanalyse `bildwelt/008-ORIGINAL-VIDEO-STYLE-REFERENCE.md`, technisches Extraktionstool `tools/build_008_style_refs.py`). Das vom Nutzer gewählte Cover ist nach 008-Abgleich eine **zusätzliche** Referenz, nicht Ersatz des Originalmaterials.

**AKTUELLER BLOCKER:** Der Acht-Bilder-Referenz-ZIP wurde im Chat als Datei bereitgestellt, aber ist NICHT automatisch in GitHub hochgeladen und ist NICHT automatisch im Google Flow-Kontext verfügbar. Vor neuem 009-Render echte 008-JPGs in Flow importieren. `05_info/style-reference-review.json` steht absichtlich auf PENDING; Phase 2 verweigert Freigabe ohne echten Nachweis. Ein Promptcommit repariert keine bereits falsch generierten 009-Bilder.
