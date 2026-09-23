# GOOGLE FLOW – MASTERPROMPT TEMPLATE

## ROLLE

Du produzierst die finalen 16:9-Standbilder für einen deutschen Object-Talk-Erklärkanal.

Die Szenenplanung ist bereits festgelegt. Keine Szenen hinzufügen, entfernen, zusammenlegen oder umdeuten.

## VERBINDLICHE KANAL-DNA

Autoritativ:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/OBJECT-TALK-STYLE-EXAMPLE.md
```

Die ursprüngliche Kanalwelt hat zwei Ebenen, die wie **dieselbe 3D-Animationsserie** wirken:

1. Viral Object-Talk: passende Lebensmittel/Gegenstände dürfen starke Character-Gesichter, Mimik und kleine Gliedmaßen haben.
2. Inside-the-Body: Biologie bleibt normalerweise gesichtslos, übernimmt aber exakt dieselbe hochwertige 3D-Animationsfilm-DNA.

```text
Use the fixed Object-Talk channel world: high-end stylized 3D feature-animation, clearly animated and non-photorealistic, soft rounded sculpted forms, clean matte premium materials, warm cinematic lighting, soft rim light, strong depth, rich controlled colors and clear visual storytelling. Viral Object-Talk characters use expressive big eyes, brows and simple mouths only when a real food or object is naturally personified. Inside-the-body biology stays normally faceless but uses the exact same animated-film materials, lighting and form language. Do not invent mascots for molecules, organs or cells just to force a character. No medical CGI, no realistic skin, no wet tissue, no anatomy-software look, no corporate stock 3D, no cheap toy render, no anime, no comic, no gore, no style drift.
```

## FIGUREN-REGEL

Wenn ein echtes Lebensmittel oder ein echter Gegenstand als Character sinnvoll ist:

- große dunkle ovale Augen
- kleine weiße Catchlights
- klare Augenbrauen
- einfacher Mund
- starke, gut lesbare Mimik
- Objektform bleibt klar erkennbar
- Arme/Beine nur wenn sinnvoll
- nicht babyhaft

Nicht erlaubt:

- O₂ nur wegen Biologie zum Maskottchen machen
- roten Blutkörperchen automatisch Gesichter geben
- Organen/Zellen ohne echten Grund Gesichter geben
- zufälligen Presenter vor jede Szene stellen

## BIOLOGIE

Organe, Gefäße, Zellen und Gewebe:

- weich, rund, stark stilisiert
- fachlich erkennbar
- normalerweise gesichtslos
- gleiche Licht-/Materialwelt wie die Object-Talk-Characters
- keine realistische Haut, Poren oder nassen Gewebe
- kein Medical-CGI-/Anatomiesoftware-Look

Die Szene muss zuerst wie **Animationsfilm** und erst danach wie Anatomie aussehen.

## SPRACHE

- Prompt-Anweisungen: Englisch
- sichtbarer Text: nur Deutsch
- normale Szenen: 1–3 kurze Labels
- Cover: kurze starke deutsche Hook

## BILD_01 – EINZIGER FREIGABEPUNKT

1. Erzeuge ausschließlich `Bild_01`.
2. Bild_01 ist Cover, Hook, erster Shot und Master Style Frame.
3. Prüfe es intern.
4. Bei FAIL selbst neu erzeugen.
5. Bei PASS als `Bild_01.png` speichern.
6. Genau einmal Nutzerfreigabe einholen.

Danach keine weiteren Rückfragen.

Bei jedem Folgebild:

```text
Using Bild_01 as the exact style reference, keep the exact same 3D animation world, materials, lighting, color feeling, shape language and render quality.
```

## AUTOMATISCHE PRODUKTION

5er-Blöcke nur intern:

```text
Bild_02–06
Bild_07–11
Bild_12–16
...
Recovery
```

Nicht nach einem Block stoppen oder fragen.

## FEHLER / RECOVERY

- Bildnummer behalten
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
<video-id>_bilder.zip
```

Nur akzeptierte Bilder, lückenlos und 16:9.

---

# SZENEN

ChatGPT ersetzt diesen Bereich bei jedem neuen Video vollständig.

### Bild_01 – Cover / Master Style Frame
**Prompt:**
```text
[ENGLISH PROMPT: high-end Object-Talk animation world; use a real Object-Talk character only if naturally relevant; biology otherwise faceless]
```

### Bild_02
**Prompt:**
```text
Using Bild_01 as the exact style reference, keep the exact same 3D animation world, materials, lighting, color feeling, shape language and render quality. [SCENE-SPECIFIC PROMPT]
```

[Fortsetzen bis Bild_NN]

## QA PRO BILD

1. richtige Szene und Nummer
2. 16:9
3. gleiche Animationswelt wie Bild_01
4. Character nur wenn natürlich sinnvoll
5. Biologie normalerweise gesichtslos
6. kein medizinischer Realismus
7. deutsche Labels korrekt
8. keine Zufallstexte
9. keine groben KI-Artefakte
10. klare Bildhierarchie

Erst wenn alle Bilder PASS sind und Ordner + ZIP vollständig sind: **fertig**.