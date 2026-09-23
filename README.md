# Object-Talk

Produktionssystem fuer den deutschen YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Deutschsprachige Erklaervideos ueber Ernaehrung, Gesundheit, menschlichen Koerper und Biologie.

Standard:

- mindestens 5:00 Minuten fuer normale Kanalvideos
- 16:9 / 1920×1080 / 30 fps
- hohe visuelle Dichte aus generierten Standbildern
- stark stilisierte hochwertige 3D-Animationsfilm-Welt
- wissenschaftlich plausibel und leicht verstaendlich
- keine unnoetige Themenwiederholung

## Aktueller Pilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 ist ein interner 2–3-Minuten-Test fuer die visuelle Pipeline.

## Verbindliche Bildwelt

- premium stilisierte 3D-Feature-Animation
- weiche gerundete Formen
- matte/satinierte Premium-Materialien
- warme filmische Beleuchtung
- starke Tiefenwirkung
- freundlich, modern, familiengeeignet
- kein medizinischer Fotorealismus
- kein Anatomiesoftware-Look
- kein Corporate-Stock-3D
- kein billiger Toy-Look
- kein Anime, Comic, Gore oder Horror

Die Kanal-DNA steht in:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

## Reference-First Bildpipeline

Die Bildproduktion arbeitet nicht mehr nach dem Prinzip „lange Stilbeschreibung und hoffen“.

Prioritaet:

1. `assets/channel/STYLE_REFERENCE.png` – sobald vom Nutzer freigegeben
2. `Bild_01.png` – Episode-Style- und Continuity-Referenz
3. wiederkehrende Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Wichtig:

**Eine Textzeile wie `Using Bild_01 as the exact style reference` ersetzt nicht das tatsaechliche Anhaengen von Bild_01 als visueller Referenz/Ingredient in Flow.**

Solange noch keine kanalweite `STYLE_REFERENCE.png` existiert, darf nur `Bild_01` im Bootstrap-Modus aus den schriftlichen Stilregeln erzeugt werden. Nach Freigabe muss `Bild_01.png` an jede Folgegeneration angehaengt werden.

## Flow Agent Instructions

Dauerhafte Flow-Regeln:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Produktionslogik:

```text
engine/FLOW-PRODUCTION-STANDARD.md
```

Die Agent Instructions enthalten Kanal-DNA, Verbote, Referenzregeln, Textregeln, QA und Recovery. Der konkrete Video-Prompt bleibt dadurch auf die jeweilige Szene fokussiert.

## Flow erzeugt Visuals – Remotion erzeugt Text

Flow-Bilder sind standardmaessig textfrei.

Das bedeutet:

- keine KI-Labels
- keine KI-Pfeile
- keine KI-Typografie
- Cover-Hook nicht direkt in Flow

Deutsche Labels bleiben Teil der Erklaerung, werden aber spaeter kontrolliert in Remotion gesetzt.

Quelle:

```text
02_bildprompts/label-plan.json
```

Dadurch werden Rechtschreibfehler, falsche Pointer und unnoetige Bildregenerationen vermieden.

## Bild_01

`Bild_01` ist immer:

- Cover-Grundbild
- erster Shot
- Master Style Frame
- Episode-Referenz fuer alle Folgebilder

Ablauf:

```text
STYLE_REFERENCE anhaengen, falls vorhanden
→ nur Bild_01 erzeugen
→ wenn moeglich mehrere Varianten
→ echtes Bild visuell pruefen
→ beste PASS-Variante speichern
→ einmalige Nutzerfreigabe
→ Bild_01 als echte visuelle Referenz an alle Folgebilder anhaengen
```

## Folgeprompts

Nach Bild_01 folgt jeder Szenenprompt diesem Schema:

```text
SUBJECT
→ VISIBLE PROCESS
→ SPATIAL LAYOUT
→ CAMERA / SCALE
→ CONTINUITY REFERENCES
→ FORBIDDEN ELEMENTS
```

Ziel: wenig Interpretationsspielraum bei Raumaufteilung, biologischer Richtung, Massstab und Wiedererkennung.

## Produktion in 5er-Bloecken

Nach freigegebenem Bild_01:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
Bild_22–26
Bild_27–31
...
```

Jedes Bild innerhalb eines Blocks wird einzeln erzeugt und visuell geprueft. Die 5er-Bloecke dienen nur der Organisation und QA.

## Echte Bild-QA

Ein `ACCEPT` in JSON reicht nicht.

Vor Akzeptanz muss die tatsaechliche finale `Bild_XX.png` existieren und visuell geprueft worden sein.

Phase-2-Validator:

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

Er verlangt unter anderem:

- finale PNG-Datei vorhanden
- wissenschaftliche Genauigkeit >= 8/10
- Voice-over-Match >= 8/10
- sofortige Verstaendlichkeit >= 8/10
- Stilkontinuitaet >= 8/10
- Komposition >= 8/10
- AI-Artefakt-Check PASS
- Gesamtscore >= 8/10
- keine offenen PENDING/TODO/TBD-Werte

## Drei Phasen

### Phase 1 – Creative Director

```text
Thema
→ Recherche
→ Claim-Check
→ Mechanism Map
→ finales Script
→ Satz-Visual-Plan
→ Szenenplan
→ Label-Plan
→ praezise Flow-Szenenprompts
→ scene-map.json
→ overlay-plan.json
```

### Phase 2 – Nutzer + Voice-KI + Google Flow

```text
Voice erzeugen
→ Flow Agent Instructions setzen
→ nur Bild_01
→ Nutzerfreigabe
→ Bild_01 als echte visuelle Referenz anhaengen
→ Folgeframes einzeln erzeugen
→ echte Bild-QA
→ Recovery
→ finale ZIP
```

### Phase 3 – Antigravity + Tools + Remotion

```text
Audio vorbereiten
→ Flow-ZIP importieren
→ Assets validieren
→ faster-whisper
→ Script↔Audio-Ausrichtung
→ timeline.json
→ Hook/Labels/Overlays aus Plaenen
→ Remotion
→ Render
→ Final-QA
→ Scorecard
→ Postmortem
```

## Aktueller Pilot – naechster Schritt

1. `engine/FLOW-AGENT-INSTRUCTIONS.md` als dauerhafte Flow-Agent-Regeln setzen.
2. `youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` verwenden.
3. Zuerst ausschliesslich textfreies `Bild_01` erzeugen.
4. Bild_01 freigeben.
5. Danach `Bild_01.png` bei jeder Folgegeneration als echtes Visual Reference/Ingredient anhaengen.

## Goldene Regel

**Nicht raten. Nicht nur beschreiben – referenzieren.**
