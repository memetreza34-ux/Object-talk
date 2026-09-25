# Object-Talk – Project State

Letzte Aktualisierung: 25.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

## Neuer Status nach Review des ersten Render-Tests

Der erste Render-Test wurde visuell und technisch geprueft. Dabei wurden mehrere konkrete Produktionsfehler erkannt und jetzt im Repo als Hard Rules behoben.

Wichtigste Korrekturen:

- Voice standardmaessig **1.10x**
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- keine kuenstliche Streckung auf exakt 150 Sekunden
- verarbeitetes `final-voiceover.wav` ist einzige Timing-Quelle
- maximale stille Voice-Pause im finalen verarbeiteten Audio: **<0.50s**
- maximale Standbilddauer: **7.0s**
- lange Speech-Beats in neue eindeutige Bilder splitten
- Pilot jetzt **35 eindeutige Szenen/Bilder** statt 28 mit langen Holds
- kein Bildasset zweimal in der Timeline
- sichtbare Bildnummern / Szenennummern / Prompt-Titel sind Hard FAIL
- sichtbarer Text ist Whitelist-basiert
- nur beim Cover sind vor Auswahl mehrere Varianten erlaubt

Erwartete Pilotlaufzeit nach 1.10x + Pausenkompression:

**ca. 120–140 Sekunden**, ohne kuenstliche Leerzeit.

## Aktuelle Bildwelt

Verbindliche Richtung:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Die Richtung ist bewusst:
- klar animiert / illustriert
- nicht fotorealistisch
- nicht medizinisch
- nicht uebertrieben kindlich
- etwas Volumen und Tiefe
- einfach, anschaulich und schnell verstaendlich

## Zwei Kanalmodi

### Object-Talk Character Mode
Fuer sprechende Lebensmittel / Alltagsobjekte:
- hochwertiger stilisierter 3D-Character-Look
- Augen, Mimik, ggf. kleine Gliedmassen
- bekannte Object-Talk-Reel-Aesthetik

### Educational Explainer Mode
Fuer Biologie / Organe / Zellen / Prozesse:
- 2.5D / Soft-3D Illustration
- gesichtslos
- stark vereinfacht
- ein dominanter Lehrpunkt pro Bild
- ca. 20–30 % der wichtigen Frames duerfen einen sinnvollen Zusatzdetailpunkt haben
- semantische Farben

## Autoritative Dateien

```text
PROJECT_CONTRACT.md
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/FLOW-PRODUCTION-STANDARD.md
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
youtube-videos/001-pilot-sauerstoff-im-blut/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

## Semantische Farben

- Sauerstoff = Cyan / Tuerkis
- rote Blutkoerperchen = tiefes warmes Rot
- Blutgefaesse = Coral / Rot
- Organe = Peach / Coral
- Muskelzellen = Orange / Apricot
- CO2 = weiches Violett
- ATP / Energie = warmes Gelb / Gold
- Hintergrund = Creme / helles Blau / weiches Beige

## Cover-Regel

`Bild_01` ist Cover, erster Shot und Episode-Master-Frame.

Nur beim Cover:
- bis zu 3 unterschiedliche Varianten erlaubt
- Nutzer waehlt genau 1
- alle anderen Covervarianten danach loeschen/verwerfen
- final existiert genau ein `Bild_01.png`

Cover sichtbarer Text:
- nur **„So reist Sauerstoff durch deinen Körper“**
- keine Zusatzlabels
- keine interne Bildnummer

## Normale Bild-Regel

Bild_02–Bild_35:
- pro Bildnummer genau ein retained asset
- FAIL ersetzt dieselbe Nummer
- keine Alternativversionen sammeln
- kein Asset doppelt fuer eine zweite Szene verwenden
- jede Szene hat eine neue eindeutige Bildnummer

## Sichtbarer Text

Whitelist-Prinzip:
- Cover: nur exakte Hook
- normale Szene: nur exakt geplante Labels aus `label-plan.json`
- wenn 0 Labels geplant sind, kein sichtbarer Text

Hard FAIL:
- `Bild 19`
- `Bild_19`
- `BILD_12 – O2 BINDET`
- `Scene 19`
- `IMAGE 19`
- Dateiname / Asset-ID
- Prompt-Ueberschrift
- erfundener Szenentitel
- englischer Zusatztext

## Audio / Timing

Zwingend vor Whisper/Timeline:

```bash
python tools/prepare_audio.py RAW_AUDIO \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --speed 1.10
```

Danach:
- Whisper auf `final-voiceover.wav`
- Timeline aus den echten Worttimings
- kein fixes 150s-Raster
- `tools/build_timeline.py` FAIL bei >7s pro Bild
- `tools/qa_final.py` prueft Speed und lange Pausen

## Pilot 001 – aktueller Szenenplan

Aktuell:
- **35 eindeutige Bilder**
- lange alte Szenen 12/18/27/28 wurden sinnvoll aufgeteilt
- Finale wurde in mehrere eigene Visuals geteilt statt ein einziges Bild ca. 20s zu halten
- Ende zeigt neue Ziel-/Zusammenfassungsbilder statt wiederholt dasselbe Covermotiv

## Produktionsstatus

Bereit:
- Script
- neue 35-Szenen-Planung
- 1.10x Audio-Pipeline
- Pausenkompression
- 7s-Visual-Density-Guard
- Text-Whitelist
- Duplicate-Asset-Guard
- Flow-Prompt fuer 35 Bilder
- Remotion-/Antigravity-Regeln
- Final-QA fuer Voice-Speed und Pausen

Naechster echter Test:
1. Voice mit `prepare_audio.py` neu erzeugen.
2. Covervarianten erzeugen, eine waehlen, Alternativen entfernen.
3. Bild_02–Bild_35 jeweils genau einmal finalisieren.
4. Phase 3 neu ausfuehren.
5. finalen Render gegen die neuen QA-Regeln pruefen.
