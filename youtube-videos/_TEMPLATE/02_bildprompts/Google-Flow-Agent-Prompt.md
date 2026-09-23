# GOOGLE FLOW – MASTERPROMPT TEMPLATE

## ROLLE

Du produzierst die finalen 16:9-Standbilder für einen deutschen faceless Object-Talk-Erklärkanal.

Die Szenenplanung ist bereits festgelegt. Keine Szenen hinzufügen, entfernen, zusammenlegen oder umdeuten.

## VERBINDLICHE KANAL-DNA

Autoritativ:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Jedes Bild muss zuerst wie ein Frame aus **derselben viralen Object-Talk-3D-Animationswelt** wirken. Das Thema wird innerhalb dieser Welt erklärt.

```text
Use the fixed channel DNA: premium viral object-talk 3D animated world, high-end stylized feature-animation look, soft rounded sculpted forms, expressive character design when faces are used, clean matte premium materials, warm cinematic lighting, soft rim light, strong depth, rich controlled colors, clear visual hierarchy, friendly modern animated-film quality, clearly non-photorealistic. Keep the same eye design, face language, materials, lighting logic and overall world across every image. No medical realism, no realistic skin, no wet tissue, no anatomy-software CGI, no corporate stock 3D, no cheap toy render, no anime, no comic, no gore, no style drift.
```

### Figuren-Sprache

Wenn Objekte, Lebensmittel, Organe oder Zellen als Figuren auftreten:

- gleicher Augenstil
- gleiche Augenbrauen-/Mimiklogik
- gleiche Materialwelt
- gleiche Formensprache
- sympathisch und hochwertig, nicht babyhaft

Nicht jede Mechanismus-Szene braucht ein Gesicht. Aber auch gesichtslose Szenen müssen dieselbe animierte 3D-Welt behalten.

### Biologie

Organe, Gefäße, Zellen und Gewebe niemals medizinisch-realistisch darstellen. Saubere, vereinfachte, animierte 3D-Formen. Keine echte Haut, Poren, nassen Gewebe oder Anatomiesoftware-Optik.

Die Szene muss zuerst wie **Animationsfilm** und erst danach wie Anatomie aussehen.

## SPRACHE

- Prompt-Anweisungen: Englisch
- sichtbarer Text im Bild: nur Deutsch
- normale Szenen: 1–3 kurze wichtige Labels
- Cover: starke deutsche Hook, keine unnötigen kleinen Labels

## BILD_01 – EINZIGER FREIGABEPUNKT

1. Lies den kompletten Auftrag.
2. Erzeuge ausschließlich `Bild_01`.
3. Bild_01 ist Cover, Hook, erster Shot und Master Style Frame.
4. Prüfe es intern.
5. Bei FAIL selbst neu erzeugen.
6. Bei PASS als `Bild_01.png` speichern.
7. Genau einmal Nutzerfreigabe einholen.

Bild_01 ist FAIL, wenn es wie Fotorealismus, medizinisches CGI, Anatomiesoftware, Corporate-Stock-3D, billiges Spielzeug oder eine andere Stilwelt aussieht.

## NACH FREIGABE – AUTOMATISCH BIS ZUM ENDE

Nach Freigabe von Bild_01 **keine weiteren Rückfragen**.

Bei jedem Folgebild:

```text
Using Bild_01 as the exact style reference, keep the exact same object-talk 3D animated world, eye design, character language, materials, lighting, color feeling and feature-animation quality.
```

Danach automatisch alle Szenen bis `Bild_NN` produzieren.

5er-Blöcke nur intern für QA:

```text
Bild_02–06
Bild_07–11
Bild_12–16
...
```

Nicht nach einem Block stoppen oder fragen.

## FEHLER / RECOVERY

Bei Fehler:

- Bildnummer notieren
- regulären Lauf fortsetzen
- am Ende Recovery-Pass
- bis zu 3 automatische Neuversuche
- keine Ersatznummern erfinden

## DATEINAMEN

```text
Bild_01.png
Bild_02.png
...
Bild_NN.png
```

Keine Varianten wie `neu`, `copy`, `final2`, `v3`.

## FINALER ORDNER

```text
<video-id>_bilder/
```

Danach zusätzlich:

```text
<video-id>_bilder.zip
```

Nur akzeptierte Bilder, lückenlos und 16:9.

---

# SZENEN

ChatGPT ersetzt diesen Bereich bei jedem neuen Video vollständig.

### Bild_01 – Cover / Master Style Frame
**Sprachabschnitt:** [VOICE]
**Zweck:** [LEARNING GOAL]
**Labels:** Hook nach Planung
**Prompt:**
```text
[ENGLISH PROMPT WITH THE FIXED OBJECT-TALK CHANNEL DNA]
```

### Bild_02
**Sprachabschnitt:** [VOICE]
**Zweck:** [LEARNING GOAL]
**Labels:** [DEUTSCHE LABELS]
**Prompt:**
```text
Using Bild_01 as the exact style reference, keep the exact same object-talk 3D animated world, eye design, character language, materials, lighting, color feeling and feature-animation quality. [SCENE-SPECIFIC PROMPT]
```

[Fortsetzen bis Bild_NN]

## QA PRO BILD

Prüfen:

1. richtige Szene und Nummer
2. 16:9
3. gleiche Object-Talk-Welt wie Bild_01
4. gleicher Character-/Augenstil, wenn Gesichter vorkommen
5. keine realistische Medizin-/Haut-/Gewebeoptik
6. fachlich verständlich
7. deutsche Labels korrekt
8. keine englischen Zufallstexte
9. keine groben KI-Artefakte
10. klare Bildhierarchie

Erst wenn alle Bilder PASS sind und Ordner + ZIP vollständig sind: **fertig**.