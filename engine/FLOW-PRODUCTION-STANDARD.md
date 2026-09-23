# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik für Google Flow.

## 1. Oberste Stilreferenz

Für **jedes** Video gilt zuerst:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Danach:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

Grundsatz:

**Welt zuerst, Thema danach.**

Gesundheit, Ernährung, Biologie und Alltag werden immer innerhalb derselben viralen Object-Talk-3D-Animationswelt dargestellt.

## 2. Fester DNA-Block in jedem Masterprompt

Jeder Google-Flow-Masterprompt muss sinngemäß diesen Block enthalten:

```text
Use the fixed channel DNA: premium viral object-talk 3D animated world, high-end stylized feature-animation look, soft rounded sculpted forms, expressive character design when faces are used, clean matte premium materials, warm cinematic lighting, soft rim light, strong depth, rich controlled colors, clear visual hierarchy, friendly modern animated-film quality, clearly non-photorealistic. Keep the same eye design, face language, materials, lighting logic and overall world across every image. No medical realism, no realistic skin, no wet tissue, no anatomy-software CGI, no corporate stock 3D, no cheap toy render, no anime, no comic, no gore, no style drift.
```

Bei jedem Folgebild zusätzlich:

```text
Using Bild_01 as the exact style reference, keep the exact same object-talk 3D animated world, eye design, character language, materials, lighting, color feeling and feature-animation quality.
```

## 3. Character- und Objekt-Sprache

Wenn Objekte, Lebensmittel, Organe oder Zellen personifiziert werden:

- gleicher Augenstil
- gleicher Mimikstil
- gleiche Materialwelt
- gleiche Formensprache
- keine zufälligen neuen Character-Designs

Nicht jede Szene braucht ein Gesicht. Mechanismus-Szenen dürfen gesichtslos sein, müssen aber dieselbe animierte 3D-Welt behalten.

## 4. Biologie-Regel

Biologie darf **niemals** in medizinischen Realismus kippen.

Organe, Zellen, Gefäße, Alveolen usw.:

- stark stilisiert
- weich und sauber
- fachlich erkennbar
- keine realistische Haut
- keine Poren
- keine nassen Gewebetexturen
- kein Anatomiesoftware-/Medical-CGI-Look

Die Szene muss zuerst wie Animationsfilm und erst danach wie Anatomie aussehen.

## 5. Prompt- und Textregel

- Flow-Anweisungen: Englisch
- sichtbarer Text: ausschließlich Deutsch
- normale Szenen: 1–3 wichtige kurze Labels
- Cover: Hook, keine unnötigen kleinen Labels
- keine langen Textblöcke
- keine englischen sichtbaren Wörter

## 6. Bild_01

`Bild_01` ist immer:

1. Cover / Hook
2. erster Shot
3. Master Style Frame
4. Referenz für alle weiteren Bilder

Ablauf:

1. kompletten Auftrag lesen
2. ausschließlich `Bild_01` erzeugen
3. intern prüfen
4. bei FAIL selbst neu erzeugen
5. bei PASS als `Bild_01.png` speichern
6. **genau einmal** Nutzerfreigabe einholen

FAIL, wenn Bild_01 wie medizinisches CGI, Anatomiesoftware, Corporate-Stock-3D, billige Kinderanimation oder Fotorealismus aussieht.

## 7. Nach Freigabe von Bild_01: keine weiteren Rückfragen

Nach der einzigen Freigabe von Bild_01:

- automatisch bis zum letzten Bild weiterarbeiten
- nicht nach jedem Block fragen
- nicht „Soll ich weitermachen?“ fragen
- 5er-Blöcke nur intern für QA verwenden
- jedes Bild einzeln generieren
- Fehlernummern sammeln
- Recovery automatisch ausführen
- nur bei echtem technischen Blocker nach mehreren Versuchen stoppen

## 8. 5er-Blöcke

Beispiel:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
...
```

Nach jedem Block intern prüfen:

- gleicher Object-Talk-Look
- gleicher Augen-/Gesichtsstil, falls Figuren vorkommen
- gleiche Materialwelt
- gleiche Lichtlogik
- gleiche Farbwelt
- kein Realismus-Drift
- kein Stock-3D-Drift

Danach **automatisch** mit dem nächsten Block fortfahren.

## 9. Szenenprompts

Nach Bild_01:

- so kurz wie möglich, so genau wie nötig
- normalerweise 2–5 Sätze
- Szene
- sichtbarer Prozess
- Perspektive/Komposition
- deutsche Labels
- DNA-Kurzanker + Bild_01-Referenz

Nicht jedes Mal einen langen Stilroman wiederholen.

## 10. Recovery

Bei FAIL:

1. Bildnummer notieren
2. regulären Lauf fortsetzen
3. am Ende Recovery-Pass
4. bis zu 3 automatische Neuversuche pro fehlerhafter Szene
5. keine Ersatznummern erfinden

## 11. Finaler Bilderordner

Am Ende genau einen finalen Ordner erstellen:

```text
<video-id>_bilder/
```

Darin ausschließlich:

```text
Bild_01.png
Bild_02.png
...
Bild_NN.png
```

Regeln:

- keine Lücken
- jede Nummer genau einmal
- keine Namen wie `final2`, `neu`, `copy`, `v3`
- nur akzeptierte Varianten
- 16:9

Zusätzlich eine ZIP desselben Ordners erstellen.

## 12. Harte Verbote

Flow darf niemals:

- die Kanal-DNA ignorieren
- einen neuen Stil pro Szene erfinden
- in Fotorealismus oder Medical-CGI driften
- realistische Haut/Gewebe erzeugen
- zufällige Augen-/Gesichtsdesigns erzeugen
- nach Bild_01 weitere Freigaben verlangen
- Szenen erfinden, löschen oder zusammenlegen
- englische sichtbare Texte erzeugen
- fehlgeschlagene Bilder vergessen
