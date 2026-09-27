# Phase-Gates

Keine spätere Produktionsphase startet, bevor die vorherige Phase bestanden hat.

`PROJECT_CONTRACT.md` bleibt die oberste Regel.

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
- Szene 01 ist Cover-/Hook-Szene
- Label-Plan vollständig
- kein Bild nur dekorativ geplant
- Bildkomplexität niedrig geplant: bevorzugt 2–5 zentrale Elemente, 1 Hauptprozess, 1–3 Labels
- Flow-Prompts nutzen die kanonische Bildwelt `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `python tools/validate_planning_v2.py VIDEOORDNER` besteht

Bei FAIL: keine Voice- oder Bildproduktion starten.

## PHASE-2-PASS

Erforderlich:
- rohe Voice-Datei vorhanden
- kanonisches `final-voiceover.wav` erstellt
- Audio entspricht inhaltlich exakt `script.txt`
- Bilder-ZIP vorhanden und sicher importiert
- exakt die erwarteten Bildnummern vorhanden
- keine Duplikate
- Bilder ungefähr 16:9
- technische Mindestauflösung bestanden
- jedes Bild passt zur **Clean Animated Biology Illustration**
- vereinfachte, erkennbare Anatomie
- Hauptprozess sofort erkennbar
- keine überladenen Bilder
- Labels kurz, korrekt, deutsch und eindeutig zugeordnet
- kein Medical-CGI, kein glossy 3D, kein alter 2.5D-/Premium-3D-Look
- keine sichtbaren schweren KI-Fehler
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
- finaler Sichtcheck bestanden
- Renderbericht erzeugt
- `04_export/quality-scorecard.md` ausgefüllt
- wissenschaftliche Sicherheit mindestens 8,0/10
- gewichteter Gesamtscore mindestens 8,0/10

Nach dem Finalrender wird `04_export/postmortem.md` gemäß `engine/POSTMORTEM-STANDARD.md` ausgefüllt.

## Grundsatz

`WARNUNG` darf weiterlaufen, wenn sie dokumentiert und unkritisch ist.
`FEHLER` oder `FAIL` stoppt die Pipeline.
