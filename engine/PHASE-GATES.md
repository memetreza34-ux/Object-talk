# Phase-Gates

Keine spätere Produktionsphase startet, bevor die vorherige Phase bestanden hat.

`PROJECT_CONTRACT.md` bleibt die oberste Regel.
`engine/VISIBLE-TEXT-STANDARD.md` ist fuer sichtbaren Text und Informationsdichte verbindlich.

## Interner Testmodus

Wenn ein Projekt eine gültige Datei `05_info/test-mode.json` mit `test_mode: true` besitzt, darf die dort dokumentierte Testlaufzeit anstelle der normalen 300-Sekunden-Grenze verwendet werden.

Alle wissenschaftlichen, visuellen, Asset-, Sync- und Qualitäts-Gates bleiben aktiv.

## PHASE-1-PASS

Erforderlich:
- Thema gegen `THEMEN-GEHIRN.md` geprüft
- Recherche abgeschlossen
- Kernclaims geprüft
- `script.txt` ist finaler gesprochener Text
- Mechanism Map vollständig
- Satz-Visual-Plan vollständig
- Szenengrenzen und Bild-IDs konsistent
- jede Szene besitzt genau ein geplantes `Bild_XX`
- `Bild_XX`/Szenennummern sind reine Produktionsmetadaten und niemals als sichtbarer Bildtext geplant
- Szene 01 ist Cover-/Hook-Szene
- Cover plant **genau einen sichtbaren Textblock = Titel/Hook**, ohne Zusatzlabels
- Label-Plan vollständig
- normale Bilder planen **0–2 Labels, maximal 2**
- Labels bevorzugt 1–2 Woerter, maximal 3 Woerter
- kein Bild nur dekorativ geplant
- pro Bild genau eine dominante Hauptaussage / ein Hauptprozess
- Bildkomplexität niedrig geplant: bevorzugt 2–4 zentrale Elemente
- ueberladene Beats werden auf mehrere Bilder aufgeteilt
- unwichtige Nebeninformation wird weggelassen
- Textkontrast ist geplant: hell → dunkel, dunkel → hell
- Flow-Prompts nutzen die kanonische Bildwelt `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- Flow-Prompts verbieten sichtbar gerenderte Asset-/Bild-/Szenennummern
- `03_pipeline/overlay-plan.json` ist `DISABLED` und `scenes` ist leer
- keinerlei Remotion-Text geplant
- `04_export/` ist im Projekt angelegt
- `04_export/YOUTUBE-UPLOAD-PAKET.md` ist fuer das konkrete Video vorbereitet
- `python tools/validate_planning_v2.py VIDEOORDNER` besteht

Bei FAIL: keine Voice- oder Bildproduktion starten.

## PHASE-2-PASS

Erforderlich:
- rohe Voice-Datei vorhanden
- kanonisches `final-voiceover.wav` erstellt
- Audio entspricht inhaltlich exakt `script.txt`
- Bilder-ZIP vorhanden und sicher importiert
- exakt die erwarteten Bilddateien vorhanden
- keine Duplikate
- Bilder ungefähr 16:9
- technische Mindestauflösung bestanden
- jedes Bild passt zur **Clean Animated Biology Illustration**
- vereinfachte, erkennbare Anatomie
- Hauptprozess sofort erkennbar
- keine überladenen Bilder
- normale Bilder enthalten maximal 2 Labels
- Labels kurz, korrekt, deutsch und eindeutig zugeordnet
- keine unnötigen Labels
- Textkontrast = PASS
- Label-Lesbarkeit = PASS
- Informationsdichte = PASS
- Cover title-only = PASS
- Cover exakt ein sichtbarer Textblock = PASS
- kein Medical-CGI, kein glossy 3D, kein alter 2.5D-/Premium-3D-Look
- keine sichtbaren schweren KI-Fehler
- keine sichtbare Bild-/Szenennummer
- kein sichtbarer Dateiname, Asset-ID oder Prompttitel
- `image-review.json` enthält jedes finale Pflichtbild
- jedes akzeptierte Bild erreicht mindestens 8,0/10
- `python tools/validate_planning_v2.py VIDEOORDNER --phase2` besteht

Bei FAIL: kein Timing/Render starten.

## PHASE-3-PASS

Erforderlich:
- Whisper-Wortzeiten aus dem finalen kanonischen Audio
- vollständige strenge Script↔Audio-Ausrichtung bestanden
- jede Szene auf exakte Wortzeiten gemappt
- gesamte Sprache ohne Lücke oder Überlappung abgedeckt
- `timeline.json` valide
- Renderer-Runtime erfolgreich gebaut
- finaler Render technisch erfolgreich
- 1920×1080 / 30 fps
- Audio vorhanden und vollständig
- kein unerwarteter langer schwarzer Abschnitt
- 100 % Vollbild-Illustration
- Remotion erzeugt exakt 0 sichtbare Textelemente
- `overlay-plan.json` bleibt deaktiviert und leer
- keine sichtbaren Bild-/Szenennummern, Dateinamen oder Asset-IDs
- Cover zeigt weiterhin nur den Titel
- alle Flow-Texte bleiben im finalen Render kontrastreich und lesbar
- kein Frame wirkt informationsüberladen
- keine permanenten Rahmen, Seitenleisten oder Dashboard-/PowerPoint-Aufteilung
- finaler Sichtcheck bestanden

### Veröffentlichungs-Export – Pflicht

`04_export/` muss vollständig sein und enthalten:
- `YOUTUBE-UPLOAD-PAKET.md`
- `YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt`
- `YouTube-Caption.md`
- `render-report.md`
- `quality-scorecard.md`
- `postmortem.md`
- `fertiges-video/[VIDEO-ID]-YOUTUBE.mp4`

Zusätzlich gilt:
- `fertiges-video/` enthält nur die finale YouTube-Masterdatei, keine Preview-/Draft-Dateien
- YouTube-Titel ist individuell für genau dieses Video
- Beschreibung ist individuell, deutsch und inhaltlich korrekt
- Caption ist individuell und passt zum finalen Video
- maximal 5 sinnvolle Hashtags
- Titel/Beschreibung/Caption wurden nach dem echten Finalrender noch einmal gegen den Inhalt geprüft
- Renderbericht ausgefüllt
- `04_export/quality-scorecard.md` ausgefüllt
- wissenschaftliche Sicherheit mindestens 8,0/10
- gewichteter Gesamtscore mindestens 8,0/10
- erst danach Status `YouTube-ready`

Nach dem Finalrender wird `04_export/postmortem.md` gemäß `engine/POSTMORTEM-STANDARD.md` ausgefüllt.

## Grundsatz

`WARNUNG` darf weiterlaufen, wenn sie dokumentiert und unkritisch ist.
`FEHLER` oder `FAIL` stoppt die Pipeline.
