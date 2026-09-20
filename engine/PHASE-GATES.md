# Phase-Gates

Keine spätere Produktionsphase startet, bevor die vorherige Phase bestanden hat.

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

Bei FAIL: Video nicht als fertig markieren.

## Grundsatz

`WARNUNG` darf weiterlaufen, wenn sie dokumentiert und unkritisch ist.

`FEHLER` oder `FAIL` stoppt die Pipeline. Kein Agent darf fehlende Daten still schätzen oder ersetzen.
