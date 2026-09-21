# Phase-Gates

Keine spätere Produktionsphase startet, bevor die vorherige Phase bestanden hat.

`PROJECT_CONTRACT.md` bleibt die oberste Regel. Die zusätzlichen V2-Anforderungen gelten für Projekte, die aus dem aktualisierten `_TEMPLATE` angelegt wurden. Bestehende Projekte wie Video 001 werden dadurch nicht rückwirkend blockiert.

## PHASE-1-PASS

Erforderlich:

- Thema gegen `THEMEN-GEHIRN.md` geprüft
- Thema bietet mindestens 5 Minuten echten Inhalt
- Recherche abgeschlossen
- Kernclaims geprüft
- `script.txt` ist finaler gesprochener Text
- Script enthält keine Regieanweisungen
- `phase1-scenes.json` deckt das Script lückenlos ab
- `scene-map.json` entspricht exakt denselben Szenengrenzen
- jede Szene besitzt genau ein geplantes `Bild_XX`
- Szene 01 ist Cover-/Hook-Szene
- Google-Flow-Agent-Prompt enthält alle Szenen
- wissenschaftlich wichtige Labels sind definiert

Zusätzlich für neue V2-Projekte:

- `05_info/mechanism-map.md` vollständig ohne Platzhalter
- `05_info/sentence-visual-plan.json` vollständig
- jeder Satz/Satzblock besitzt Lernziel, Visualfunktion und stabile Bild-ID
- `scene_difference` ist für jedes geplante Visual beschrieben
- alle Bild-IDs stimmen mit `phase1-scenes.json` überein
- `02_bildprompts/label-plan.json` ist vollständig
- kein Bild ist nur dekorativ geplant
- `python tools/validate_planning_v2.py VIDEOORDNER` besteht

Bei FAIL: keine Voice- oder Bildproduktion starten.

## PHASE-2-PASS

Erforderlich:

- rohe Voice-Datei vorhanden
- kanonisches `final-voiceover.wav` erstellt
- finale Audio-Dauer mindestens 300 Sekunden
- Audio entspricht inhaltlich exakt `script.txt`
- Bilder-ZIP vorhanden
- ZIP sicher importiert
- exakt die erwarteten Bildnummern vorhanden
- keine Duplikate
- Bilder ungefähr 16:9
- technische Mindestauflösung bestanden
- visueller Sichtcheck bestanden
- biologische Labels korrekt
- keine sichtbaren schweren KI-Fehler

Zusätzlich für neue V2-Projekte:

- `02_bildprompts/image-review.json` enthält jedes finale Pflichtbild
- jedes akzeptierte Bild erreicht mindestens 8,0/10
- `scientific_accuracy` erreicht mindestens 8,0/10
- klare Fachfehler oder falsche Labels führen zu Regeneration
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
- finales Video mindestens 300 Sekunden
- kein unerwarteter langer schwarzer Abschnitt
- finaler Sichtcheck bestanden
- Renderbericht erzeugt

Zusätzlich für neue V2-Projekte vor Veröffentlichung:

- `04_export/quality-scorecard.md` auf Basis des echten Renders ausgefüllt
- wissenschaftliche Sicherheit mindestens 8,0/10
- gewichteter Gesamtscore mindestens 8,0/10
- keine harten Ausschlusskriterien aus `engine/QUALITY-SCORECARD.md`

Nach dem echten Finalrender wird zusätzlich `04_export/postmortem.md` gemäß `engine/POSTMORTEM-STANDARD.md` ausgefüllt. Das Postmortem ist die Lernschleife, nicht die technische Renderfreigabe.

Bei FAIL: Video nicht als fertig markieren.

## Grundsatz

`WARNUNG` darf weiterlaufen, wenn sie dokumentiert und unkritisch ist.

`FEHLER` oder `FAIL` stoppt die Pipeline. Kein Agent darf fehlende Daten still schätzen oder ersetzen.
