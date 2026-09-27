# Qualitäts-Scorecard – Object-Talk

## Zweck

Ein technisch erfolgreicher Render ist nicht automatisch veröffentlichungsbereit. `PROJECT_CONTRACT.md` bleibt die oberste Regel.

## Freigabe

Ein Video darf nur als veröffentlichungsbereit gelten, wenn:
- kein hartes Ausschlusskriterium verletzt ist
- wissenschaftliche Sicherheit bestanden ist
- jedes finale Pflichtbild einzeln freigegeben ist
- der Gesamtscore mindestens 8,0/10 beträgt

## Bewertung

### 1. Wissenschaftliche Sicherheit – 20 %
- Stimmen Skript, Claim-Matrix, Visualisierung und Labels überein?
- Sind Anatomie, Pfeile und räumliche Beziehungen plausibel?

Unter 8/10 = harter Blocker.

### 2. Verständlichkeit – 15 %
- Kann ein Laie den zentralen Mechanismus erkennen?
- Sind Ursache, Prozess und Wirkung klar getrennt?
- Ist das Bild schnell erfassbar?

### 3. Voice-over ↔ Visual-Match – 15 %
- Zeigt jedes Bild genau die Aussage seines Sprachabschnitts?
- Gibt es keine dekorativen Bilder ohne Erklärfunktion?

### 4. Visuelle Erklärtiefe – 10 %
- Sind Ausgangszustand, Auslöser, Weg und Wirkung sichtbar?
- Werden komplexe Vorgänge in verständliche Teilbilder zerlegt?

### 5. Bildqualität und Konsistenz – 10 %

Alle Bilder muessen zur **Clean Animated Biology Illustration** passen:
- klare animierte Illustration statt Render-Look
- vereinfachte, erkennbare Anatomie
- weiche organische Formen und saubere Konturen
- weiche Verläufe, subtile Schatten und leichte Tiefe
- helle ruhige Hintergründe
- klare biologische Farben
- niedrige Komplexität
- keine Drift in Medical-CGI, glossy 3D, Feature-Animation oder Corporate-Infografik

### 6. Bildrhythmus und Abwechslung – 10 %
- Wechseln Perspektive, Maßstab und Visual-Typ sinnvoll?
- Wiederholen sich Nachbarbilder nicht ohne neue Aussage?
- Werden Cutaway, Querschnitt, Makro, Prozess, Vergleich und Maßstabswechsel sinnvoll gemischt?

### 7. Labels und Text – 5 %
- Sind normalerweise nur 1–3 wichtige deutsche Labels vorhanden?
- Sind Labels korrekt geschrieben und eindeutig zugeordnet?
- Sind Hinweislinien/Pfeile sauber?
- Gibt es keinen englischen sichtbaren Text?
- Gibt es keine unnötigen Textblöcke?

### 8. Audio und Synchronität – 5 %
- Ist das Voice-over vollständig, verständlich und technisch sauber?
- Basieren Szenenzeiten auf echten Wortzeitstempeln?

### 9. Technische Qualität – 5 %
- 1920×1080, 30 fps
- Audio vollständig
- keine schwarzen Frames
- keine fehlenden oder doppelten Bildnummern
- finaler Renderbericht vorhanden

### 10. Zuschauerbindung – 5 %
- Funktioniert Bild_01 sofort als Hook/Cover?
- Entwickelt sich die Erklärung sichtbar weiter?
- Liefert das Ende eine klare Auflösung statt bloßer Wiederholung?

## Bild-Einzelreview

Jedes finale Bild erhält mindestens:

```text
Scientific accuracy:      __ /10
Voice-over match:         __ /10
Immediate clarity:        __ /10
Style continuity:         __ /10
Composition:              __ /10
Complexity control:       __ /10
Label accuracy:           __ /10
AI artifact check:        PASS / FAIL
Scene difference:         PASS / FAIL
Overall:                   __ /10
Decision:                  ACCEPT / REGENERATE
```

Mindestziel pro Bild: 8,0/10.

## Harte Ausschlusskriterien

Keine Freigabe bei:
- wissenschaftlicher Sicherheit unter 8/10
- fachlich falscher Anatomie mit Einfluss auf die Erklärung
- falschem oder missverständlichem Label
- englischem sichtbarem Text
- sichtbar ueberladenem Bild
- deutlichem Stilbruch gegen `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- Drift in fotorealistischen Medizin-Look, Medical-CGI oder glossy 3D
- Voice-over und Bild widersprechen sich
- fehlendem Pflichtbild
- doppelter/falscher Bildnummer
- schwerem KI-Artefakt im Hauptmotiv
- nicht dokumentiertem Review bei einem Pflichtbild

## Gesamtwert

```text
Wissenschaftliche Sicherheit: __ /10 × 20 %
Verständlichkeit:             __ /10 × 15 %
VO ↔ Visual:                  __ /10 × 15 %
Visuelle Erklärtiefe:         __ /10 × 10 %
Bildqualität/Konsistenz:      __ /10 × 10 %
Bildrhythmus:                 __ /10 × 10 %
Labels/Text:                  __ /10 ×  5 %
Audio/Sync:                   __ /10 ×  5 %
Technik:                      __ /10 ×  5 %
Zuschauerbindung:             __ /10 ×  5 %

Gesamt:                       __ /10
Freigabe:                     JA / NEIN
```
