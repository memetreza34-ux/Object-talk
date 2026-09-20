# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widersprüchen gilt zuerst eine ausdrückliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert ausschließlich lange deutschsprachige YouTube-Erklärvideos zu Ernährung, Gesundheit und Biologie.

Harte Grundregeln:

- finales Video mindestens 5:00 Minuten
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- narrative Bildwelt ausschließlich aus Standbildern; Bewegung entsteht im Schnitt/Remotion
- einheitliche semi-realistische 3D-Animationswelt
- Verbindung aus Viral Object-Talk und verständlichen Inside-the-Body-Darstellungen
- biologische Inhalte vereinfachen, aber nicht fachlich verfälschen
- wichtige Strukturen knapp und auf Deutsch beschriften
- keine unnötigen Wiederholungen bereits produzierter Themen

## Nutzer-Dateien

Alle Inhalte, die der Nutzer selbst öffnen und in ein externes Tool kopieren soll, müssen zusätzlich als normale `.txt`-Datei vorliegen.

Pflicht pro Video:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Diese Dateien dürfen inhaltlich nicht von den zugehörigen kanonischen Projektdateien abweichen. Interne technische Dateien dürfen weiterhin `.md`, `.json`, `.py` usw. verwenden.

Details: `engine/USER-FILES-STANDARD.md`.

## Drei Phasen

### Phase 1 – ChatGPT / Creative Director

ChatGPT erstellt vor jeder Medienproduktion vollständig:

1. Themenprüfung gegen `THEMEN-GEHIRN.md`
2. Recherche und Claim-Check
3. finales gesprochenes `script.txt`
4. identisches `VOICEOVER-ZUM-KOPIEREN.txt`
5. semantischen Szenenplan aus exakt dem finalen Skript
6. vollständigen Google-Flow-Agent-Prompt
7. identisches `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
8. `scene-map.json` mit lückenloser Sprachabdeckung
9. Antigravity-/Editor-Anweisung
10. `ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt`
11. YouTube-Titel, Beschreibung und maximal 5 Hashtags
12. `YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt`

Phase 1 erzeugt keine finalen Flow-Bilder und keine geschätzten Zeitcodes.

Phase 1 ist erst vollständig, wenn alle vier Nutzer-`.txt`-Dateien aktuell vorhanden sind.

### Phase 2 – Nutzer + Voice-KI + Google Flow

Der Nutzer:

1. kopiert `VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die gewählte Voice-KI
2. legt das rohe Voiceover in `01_script/audio/`
3. kopiert `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` vollständig in Google Flow
4. erzeugt mit dem Google-Flow-Agenten jedes Bild einzeln
5. Szene 01 = Bild_01 = Cover-/Hook-Szene
6. Bilder streng numerisch erzeugen und prüfen
7. alle finalen Bilder als ZIP in `02_bildprompts/bilder-zip/` ablegen

Google Flow darf keine Szenengrenzen neu erfinden.

### Phase 3 – Antigravity + Tools + Remotion

Phase 3 ist technisch, nicht kreativ. Wenn der Nutzer Antigravity manuell beauftragt, wird `ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt` verwendet.

Phase 3:

1. Audio kanonisch vorbereiten
2. Flow-ZIP sicher importieren
3. Assets validieren
4. finales Audio mit Whisper transkribieren
5. Whisper-Ausgabe streng gegen `script.txt` ausrichten
6. `scene-map.json` exakt auf Wort-Zeitstempel abbilden
7. `timeline.json` erzeugen
8. Runtime für Remotion bauen
9. Standbilder mit dezenten Push-ins, Pull-outs und Pans inszenieren
10. rendern
11. technische QA durchführen
12. finales Video + Untertitel + Renderbericht exportieren

Phase 3 darf Skript, wissenschaftliche Aussage, Bildreihenfolge oder Szenengrenzen nicht still verändern.

Nach erfolgreichem Export nutzt der Nutzer `YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt` für YouTube Studio.

## Autoritative Reihenfolge

1. aktuelle ausdrückliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `PROJECT_STATE.md` für aktuellen Arbeitsstand
4. `config/*.json`
5. `engine/*.md`
6. `bildwelt/*.md`
7. `THEMEN-GEHIRN.md`
8. projektspezifische Dateien

## Fail-closed

Die Pipeline soll bei Unsicherheit stoppen statt raten.

Insbesondere kein automatisches Weiterarbeiten bei:

- Script und gesprochenes Audio stimmen nicht überein
- fehlenden oder doppelten Bildnummern
- falschem Seitenverhältnis
- unklarer Szenenzuordnung
- nicht gefundenen Wortankern
- wissenschaftlich ungeklärten Kernbehauptungen
- sichtbar falschen biologischen Beschriftungen

## Visuelle Konstanz

Sobald der Nutzer eine finale Kanalreferenz akzeptiert hat, wird sie als `assets/channel/STYLE_REFERENCE.png` gespeichert. Diese Referenz ist dann der dauerhafte Style-Anchor für Google Flow und darf nur auf ausdrücklichen Nutzerwunsch ersetzt werden.

Wiederkehrende Food-Charaktere können zusätzlich eigene Character References unter `assets/channel/characters/` erhalten.

## Themen-Gedächtnis

Vor jeder neuen Produktion wird `THEMEN-GEHIRN.md` geprüft und aktualisiert. Ein bereits behandelter Kernmechanismus darf nicht nur unter neuem Titel erneut produziert werden.
