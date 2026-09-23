# Freigegebene Bildwelt – Object-Talk

Status: **FREIGEGEBEN / VERBINDLICH**

Die visuelle Kanalwelt wird ab jetzt primär durch folgende Datei definiert:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Diese Datei ist die Kurzfassung für Produktion und QA.

## Kernlook

Der Kanal nutzt eine **einheitliche virale Object-Talk-3D-Animationswelt** im hochwertigen Feature-Animation-Look.

Verbindlich:

- klar stilisiert und animiert, niemals fotorealistisch
- weiche, gerundete, skulptierte 3D-Formen
- hochwertige matte/satinierte Materialien
- warme filmische Beleuchtung, weiches Rim-Light, starke Tiefe
- kräftige kontrollierte Farben und bewusstes Production Design
- moderne sympathische Object-Talk-Figurensprache
- bei Figuren: konsistenter Augen-, Gesichts- und Mimikstil
- familienfreundlich und hochwertig, aber nicht babyhaft
- kein medizinischer Render-Look
- kein Corporate-/Stock-3D

## Welt zuerst, Thema danach

Gesundheit, Ernährung, Biologie und Alltag werden **innerhalb derselben Object-Talk-Welt** erklärt.

Auch Anatomie bleibt stark stilisiert:

- Organe, Gefäße und Zellen als saubere animierte 3D-Formen
- fachlich erkennbar, aber klar vereinfacht
- keine realistische Haut
- keine nassen Gewebetexturen
- keine Anatomiesoftware-Optik

Die Szene muss zuerst wie **Animationsfilm** und erst danach wie Anatomie wirken.

## Character-Regel

Wenn Lebensmittel, Gegenstände, Organe oder Zellen als Figuren auftreten:

- gleicher Augenstil
- gleiche Mimiklogik
- gleiche Materialwelt
- gleiche Formensprache
- keine zufälligen Character-Designs zwischen Szenen

Nicht jede Mechanismus-Szene braucht ein Gesicht. Aber auch gesichtslose Erklärbilder müssen exakt dieselbe 3D-Welt behalten.

## Bild_01

`Bild_01` ist immer:

- Cover / Hook
- erster Shot
- Master Style Frame
- Referenz für alle Folgebilder

Nach Freigabe wird `Bild_01.png` bei jeder weiteren Generation als exakte Style-/Continuity-Referenz verwendet.

Folgebilder müssen aussehen, als kämen sie aus **demselben Film, demselben Renderprozess und derselben Welt**.

## Prompt-Regel

Jeder Google-Flow-Masterprompt enthält die feste Kanal-DNA aus:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Kurzanker:

```text
Use the fixed channel DNA: premium viral object-talk 3D animated world, high-end stylized feature-animation look, soft rounded sculpted forms, expressive character design when faces are used, clean matte premium materials, warm cinematic lighting, soft rim light, strong depth, rich controlled colors, clearly non-photorealistic, no medical realism, no stock 3D, no toy look, no style drift.
```

## Text

- Flow-Anweisungen: Englisch
- sichtbarer Text: ausschließlich Deutsch
- normale Szenen: nur wichtige kurze Labels
- Cover: starke Hook, keine unnötigen kleinen Labels

## Harte Verbote

- Fotorealismus
- medizinischer CGI-Realismus
- realistische Haut/Poren
- nasses/fleischiges Gewebe
- Anatomiesoftware-Look
- Corporate-Stock-3D
- billiger Plastik-/Spielzeuglook
- Anime
- Comic
- Gore
- Stilwechsel zwischen Bildern
- inkonsistente Augen-/Gesichtsdesigns

## Priorität

Bei Konflikten gilt:

1. `OBJECT-TALK-CHANNEL-DNA.md`
2. `Bild_01.png`
3. diese Datei
4. Szenenprompt
