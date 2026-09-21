# Qualitäts-Scorecard – Object-Talk

## Zweck

Ein technisch erfolgreicher Render ist nicht automatisch veröffentlichungsbereit. Diese Scorecard ergänzt die bestehenden Phase-Gates und den `VISUAL-QUALITY-GATE.md` um eine einheitliche inhaltliche Bewertung.

`PROJECT_CONTRACT.md` bleibt die oberste Regel.

## Freigabe

Ein Video darf nur als veröffentlichungsbereit gelten, wenn:

- kein hartes Ausschlusskriterium verletzt ist,
- wissenschaftliche Sicherheit bestanden ist,
- jedes finale Pflichtbild einzeln freigegeben ist,
- der Gesamtscore mindestens **8,0/10** beträgt.

## Bewertung

### 1. Wissenschaftliche Sicherheit – 20 %

- Stimmen Skript, Claim-Matrix, Visualisierung und Labels überein?
- Wird Unsicherheit korrekt dargestellt?
- Wird keine stärkere Aussage gezeigt als die Quellen tragen?
- Sind Anatomie, Pfeile und räumliche Beziehungen plausibel?

**Unter 8/10 = harter Blocker.**

### 2. Verständlichkeit – 15 %

- Kann ein Laie den zentralen Mechanismus wiedergeben?
- Sind Ursache, Prozess und Wirkung klar getrennt?
- Werden Fachbegriffe erklärt statt nur genannt?

### 3. Voice-over ↔ Visual-Match – 15 %

- Zeigt jedes Bild genau die Aussage seines Sprachabschnitts?
- Beginnt kein neues Visual deutlich vor oder nach der zugehörigen Aussage?
- Gibt es keine dekorativen Bilder ohne Erklärfunktion?

### 4. Visuelle Erklärtiefe – 10 %

- Sind Ausgangszustand, Auslöser, Weg und Wirkung sichtbar?
- Sind Maßstabswechsel fachlich sinnvoll?
- Werden komplexe Vorgänge in verständliche Teilbilder zerlegt?

### 5. Bildqualität und Konsistenz – 10 %

- Wirken alle Bilder wie dieselbe hochwertige semi-realistische 3D-Serie?
- Passen Materialien, Licht, Rendergrad und Bildsprache zusammen?
- Bleibt `Bild_01` als Episoden-Style-Anker erkennbar?

### 6. Bildrhythmus und Abwechslung – 10 %

- Wechseln Perspektive, Maßstab oder Erklärfunktion nur bei echtem Mehrwert?
- Bleibt kein Bild unnötig lange dominant?
- Wiederholen sich Nachbarbilder nicht ohne neue Aussage?

### 7. Labels und Text – 5 %

- Sind nur wichtige Strukturen beschriftet?
- Sind deutsche Labels korrekt geschrieben und eindeutig zugeordnet?
- Gibt es keine unnötigen Textblöcke?

### 8. Audio und Synchronität – 5 %

- Ist das Voice-over vollständig, verständlich und technisch sauber?
- Basieren Szenenzeiten auf echten Wortzeitstempeln?
- Gibt es keine Lücken oder ungewollten Überlappungen?

### 9. Technische Qualität – 5 %

- 1920×1080, 30 fps
- Audio vollständig
- keine schwarzen Frames
- keine fehlenden oder doppelten Bildnummern
- finaler Renderbericht vorhanden

### 10. Zuschauerbindung – 5 %

- Ist der Hook sofort verständlich?
- Entwickelt sich die Erklärung sichtbar weiter?
- Gibt es keine lange Phase ohne neue Erkenntnis?
- Liefert das Ende eine klare Auflösung statt Wiederholung?

## Bild-Einzelreview

Jedes finale Bild erhält mindestens:

```text
Scientific accuracy:      __ /10
Voice-over match:         __ /10
Immediate clarity:        __ /10
Style continuity:         __ /10
Composition:              __ /10
Label accuracy:           __ /10
AI artifact check:        PASS / FAIL
Scene difference:         PASS / FAIL
Overall:                   __ /10
Decision:                  ACCEPT / REGENERATE
```

Mindestziel pro Bild: **8,0/10**. Ein klarer Fachfehler oder falsches Label führt unabhängig vom Durchschnitt zu `REGENERATE`.

## Harte Ausschlusskriterien

Keine Freigabe bei:

- wissenschaftlicher Sicherheit unter 8/10
- unbelegter oder widersprüchlicher Kernbehauptung
- fachlich falscher Anatomie mit Einfluss auf die Erklärung
- falschem oder missverständlichem Label
- Voice-over und Bild widersprechen sich
- fehlendem Pflichtbild
- doppelter oder falscher Bildnummer
- Script↔Audio-Ausrichtung nicht bestanden
- finaler Render technisch unvollständig
- sichtbarem schweren KI-Artefakt im Hauptmotiv
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
