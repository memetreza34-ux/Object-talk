# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik für Google Flow.

## Ziel

Flow soll konsistente, verständliche und robuste Erklärbilder für lange faceless YouTube-Erklärvideos erzeugen.

Die Bilder sind keine Dekoration. Sie müssen den gesprochenen Inhalt sichtbar erklären.

## Grundregel: Explainer vor Mascot

Standard sind echte Erklärbilder:

- anatomische Cutaways
- transparente Körperansichten
- Prozessdarstellungen
- Organ-/Gewebe-/Zellvisualisierungen
- Mikro-/Makro-Zooms
- Vergleiche
- Vorher-/Nachher-Darstellungen
- klare Ursache→Prozess→Folge-Kompositionen

Personifizierte Lebensmittel oder Object-Talk-Figuren dürfen nur selten und gezielt eingesetzt werden, wenn sie das Verständnis verbessern. Sie dürfen nicht als dauerhafte Sprecherfigur vor dem eigentlichen Inhalt stehen.

## Globale Style-DNA

```text
high-quality semi-realistic 3D educational explainer style, faceless YouTube explainer visual language, premium animated educational series look, consistent cinematic lighting, clean composition, scientifically recognizable but simplified anatomy and biology, strong visual clarity, process-focused explainer imagery, transparent body cutaways, cross-sections, macro-to-micro transitions, elegant German educational labels, family-friendly but not childish, clearly animated but not photorealistic, no mascot-heavy composition, no random cartoon focus, no clutter, no gore, no disturbing medical realism
```

Negative Leitplanken:

```text
do not make mascot-heavy scenes, do not overuse cute object-talk presenters, do not place a character as the main focus unless explicitly required, do not turn every scene into a presenter shot, do not use random decorative food mascots, do not reduce complex explanations to a character standing next to anatomy, do not create cluttered compositions with too many ideas at once, no photorealistic medical photography, no live action, no surgery, no gore, no horror anatomy, no unreadable text, no English labels when German labels are required
```

## Phase A – Master Style Frame

1. Lies zuerst den kompletten Video-Prompt.
2. Erzeuge zunächst **ausschließlich `Bild_01`**.
3. Erzeuge noch kein weiteres Bild.
4. Prüfe `Bild_01` vollständig:
   - Thema sofort verständlich?
   - 16:9?
   - hochwertige faceless Explainer-Optik?
   - keine unnötige Mascot-Inszenierung?
   - Anatomie plausibel?
   - keine falschen/zufälligen Texte?
   - genug Rand für spätere Zooms/Pans?
5. Bei FAIL wird nur `Bild_01` neu erzeugt.
6. Erst bei PASS wird es final als `Bild_01.png` gespeichert.
7. `Bild_01` ist ab dann gleichzeitig:
   - Cover-/Hook-Frame
   - erster Shot
   - visueller Episode-Anchor
   - Master Style Frame für alle weiteren Bilder

## Wie `Bild_01` als Referenz verwendet wird

Für jede nachfolgende Bildgeneration soll `Bild_01.png`, soweit Flow dies technisch unterstützt, als Style-/Continuity-Referenz mitgegeben werden.

Von `Bild_01` übernehmen:

- Rendergrad
- Verhältnis Animation/Realismus
- Beleuchtung
- Farbtemperatur und Farbharmonie
- Materialgefühl
- Tiefenwirkung
- Kontrast
- visuelle Sauberkeit
- allgemeine Explainer-Sprache

Nicht blind übernehmen:

- konkrete Anatomie
- Pose
- Motiv
- Bildaufbau
- Organe
- Texte/Labels

Jede neue Szene muss weiterhin ihren eigenen fachlich richtigen Inhalt zeigen.

## Phase B – Produktion in 5er-Blöcken

Nach `Bild_01` erfolgt die weitere Produktion in 5er-Blöcken:

```text
Block 1: Bild_02–Bild_06
Block 2: Bild_07–Bild_11
Block 3: Bild_12–Bild_16
Block 4: Bild_17–Bild_21
Block 5: Bild_22–Bild_26
Block 6: Bild_27–Bild_31
Block 7: Bild_32–Bild_36
```

Bei Videos mit anderer Szenenzahl wird das Muster entsprechend fortgeführt.

Wichtig:

- Ein Block bedeutet **nicht**, fünf Bilder in einer einzigen Generierung zu erzeugen.
- Innerhalb des Blocks wird jedes Bild einzeln generiert.
- Nach jedem Bild sofort Einzel-QA.
- Nach jedem 5er-Block kurzer Block-QA: Stil driftet nicht, Nummerierung stimmt, keine unnötige Mascot-Zunahme.
- Erst danach nächster Block.

## Phase C – Fehlerliste statt Abbruch

Wenn Flow meldet, dass ein Bild nicht erstellt werden konnte, die Antwort abbricht oder ein Bild qualitativ durchfällt:

1. betroffene Bildnummer exakt notieren
2. Status `FEHLERHAFT` oder `FEHLT` setzen
3. keine Ersatznummer vergeben
4. nicht denselben Gesamtauftrag abbrechen
5. mit der nächsten regulären Bildnummer im aktuellen Durchlauf fortfahren

Beispiel:

```text
Bild_07 PASS
Bild_08 FEHLERHAFT
Bild_09 PASS
Bild_10 PASS
Bild_11 PASS

Recovery-Liste:
- Bild_08
```

## Phase D – Recovery-Pass

Nach Abschluss aller normalen Blöcke:

1. Recovery-Liste lesen.
2. Nur die dort aufgeführten Bildnummern erneut erzeugen.
3. Dabei weiterhin `Bild_01` als Style-Referenz verwenden.
4. Jedes Recovery-Bild einzeln prüfen.
5. Bei erneutem FAIL bleibt dieselbe Nummer auf der Recovery-Liste.
6. Recovery wiederholen, bis alle Bilder PASS sind.

Eine technisch fehlgeschlagene Flow-Generation darf niemals still als erledigte Szene gelten.

## Phase E – Finale Vollständigkeitsprüfung

Vor ZIP-Ausgabe:

- `Bild_01.png` bis `Bild_NN.png` lückenlos vorhanden
- jede Nummer genau einmal
- keine verworfenen Varianten
- keine Temp-Dateien
- keine fehlgeschlagenen Platzhalter
- alle Bilder 16:9
- alle Pflichtlabels korrekt
- keine offensichtlichen Anatomiefehler
- keine starken Stilbrüche
- keine unbeabsichtigte Mascot-/Presenter-Dominanz

Erst dann ZIP erstellen.

## Regel für Prompts

Ein Bildprompt soll möglichst **eine primäre visuelle Aussage** besitzen.

Vermeiden:

- zu viele verschiedene Vorgänge in einem einzelnen Shot
- Character + komplette Anatomie + mehrere Prozesse + viele Labels gleichzeitig, wenn es sich aufteilen lässt
- dekorative Requisiten ohne Erklärfunktion

Bevorzugen:

```text
Was wird erklärt?
→ Welcher einzelne sichtbare Mechanismus zeigt das am besten?
→ Welche 0–3 Labels sind wirklich nötig?
→ Welche Kameraperspektive macht es sofort verständlich?
```

## Harte Abschlussregel

Flow produziert die Bilder. Flow darf niemals:

- das Script ändern
- neue Szenen erfinden
- Szenen zusammenlegen
- Szenen entfernen
- Bildnummern neu interpretieren
- fehlgeschlagene Bilder vergessen
- aus einem faceless Erklärbild ohne Anweisung eine Mascot-Szene machen
