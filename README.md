# Object-Talk

Produktionssystem fuer den deutschen YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Deutschsprachige Erklaervideos ueber Ernaehrung, Gesundheit, menschlichen Koerper und Biologie.

Standard:

- normale Kanalvideos mindestens 5:00 Minuten
- 16:9 / 1920×1080 / 30 fps
- hohe visuelle Dichte aus generierten Standbildern
- helle hochwertige 3D-Animationsfilm-Welt
- wissenschaftlich plausibel und leicht verstaendlich
- wichtige sichtbare Dinge knapp auf Deutsch beschriften

## Aktueller Pilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 ist ein interner 2–3-Minuten-Test fuer die visuelle Pipeline.

## Verbindliche Bildwelt

Die Zielrichtung ist eine **helle, freundliche Premium-3D-Animationsfilm-Welt**.

Verbindlich:

- stark stilisierte hochwertige 3D-Feature-Animation
- klar animiert, nicht fotorealistisch
- helle, freundliche Grundstimmung
- weiche gerundete Formen
- matte/satinierte Premium-Materialien
- warmes Hauptlicht + weiches Fill-Light + dezentes Rim-Light
- klare Tiefenwirkung
- frische kontrollierte Farben: Creme, Apricot, Coral, warmes Rot, Himmelblau, Teal
- familiengeeignet, aber nicht babyhaft
- vereinfachte, erkennbare Biologie

Nicht verwenden:

- kosmische / Weltraum-artige Bildwelten
- Galaxie-, Nebel- oder Sternenhintergruende
- dunkle violette Sci-Fi-Mikrowelt als Standard
- Medical-CGI / Anatomiesoftware
- nasse realistische Gewebeoptik
- Corporate-Stock-3D
- billiger Toy-Look
- Anime, Comic, Gore oder Horror

Kanal-DNA:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

## Reference-First Bildpipeline

Prioritaet:

1. `assets/channel/STYLE_REFERENCE.png` – sobald vom Nutzer freigegeben
2. `Bild_01.png` – Episode-Style- und Continuity-Referenz
3. wiederkehrende Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Eine Textzeile wie `Using Bild_01 as the exact style reference` ersetzt **nicht** das tatsaechliche Anhaengen von Bild_01 als visueller Referenz/Ingredient in Flow.

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

## Sichtbarer deutscher Text ist Pflicht

Flow-Bilder sind **nicht textfrei**.

### Bild_01 / Cover

- kurze starke deutsche Hook direkt im Bild
- normalerweise 3–7 Woerter
- darf nicht ohne Text akzeptiert werden

### Normale Bilder

- normalerweise 1–3 kurze deutsche Labels
- nur die wichtigsten sichtbaren Strukturen/Prozesse
- saubere Sans-Serif-Typografie
- keine Textwaende
- kein englischer sichtbarer Text

Quelle der Labels:

```text
02_bildprompts/label-plan.json
```

Wenn Flow einen Begriff falsch schreibt, wird zuerst regeneriert. Remotion ist nur der exakte Text-Fallback bei wiederholtem KI-Schriftfehler.

## Bild_01

`Bild_01` ist immer:

- Cover
- erster Shot
- Master Style Frame
- Episode-Referenz fuer alle Folgebilder

Ablauf:

```text
STYLE_REFERENCE anhaengen, falls vorhanden
→ nur Bild_01 erzeugen
→ mehrere Varianten, wenn moeglich
→ hellen 3D-Stil + deutsche Hook + Anatomie pruefen
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
→ REQUIRED GERMAN TEXT
→ FORBIDDEN ELEMENTS
```

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

Jedes Bild wird einzeln erzeugt und visuell geprueft. Die Bloecke dienen nur der Organisation.

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
- Label-Genauigkeit >= 8/10
- AI-Artefakt-Check PASS
- Gesamtscore >= 8/10

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
→ nur Bild_01 mit deutscher Hook
→ Nutzerfreigabe
→ Bild_01 als echte visuelle Referenz anhaengen
→ Folgeframes einzeln mit deutschen Labels erzeugen
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
→ nur fehlerhafte/missing Flow-Texte per Remotion ersetzen
→ Remotion
→ Render
→ Final-QA
→ Scorecard
→ Postmortem
```

## Aktueller Pilot – naechster Schritt

1. `engine/FLOW-AGENT-INSTRUCTIONS.md` als dauerhafte Flow-Agent-Regeln setzen.
2. `youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` verwenden.
3. Zuerst ausschliesslich `Bild_01` erzeugen.
4. Pruefen: **heller Premium-3D-Animationsfilm-Look, keine kosmische Welt, deutsche Hook korrekt sichtbar.**
5. Bild_01 freigeben.
6. Danach `Bild_01.png` bei jeder Folgegeneration als echtes Visual Reference/Ingredient anhaengen.

## Goldene Regel

**Hell, klar, 3D-animiert, deutsch beschriftet und wirklich referenziert.**
