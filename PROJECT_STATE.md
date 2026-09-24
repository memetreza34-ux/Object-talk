# Object-Talk – Project State

Letzte Aktualisierung: 24.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 ist jetzt als **exakter 2:30-Minuten-Produktionspilot** festgelegt.

Ziel:

- 150 Sekunden
- 28 Szenen
- 343 Voiceover-Woerter
- ca. 137 Woerter/Minute
- 16:9 / 1920×1080 / 30 fps

Autoritative Timing-Datei:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/05_info/timeline-2m30.json
```

Produktionsplan:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/03_pipeline/VIDEO-2M30-PRODUCTION.md
```

## Aktueller Bildwelt-Status

Die Explainer-Bildwelt wurde am 24.09.2026 nach mehreren Flow-Tests **inhaltlich freigegeben und im Repo verankert**.

Verbindliche Richtung:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Die Richtung ist bewusst:

- klar animiert / illustriert
- nicht fotorealistisch
- nicht medizinisch
- nicht uebertrieben kindlich
- etwas Volumen und Tiefe, aber keine realistische 3D-Anatomiewelt
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
- ein Erklaerziel pro Bild
- wenige Objekte
- semantische Farben

## Autoritative Stil-Dateien

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
engine/FLOW-AGENT-INSTRUCTIONS.md
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

## Pilot 001 – feste Objektregeln

- O2 = kleine cyanfarbene / tuerkise Partikel oder verbundene Kugeln, ohne Gesicht
- CO2 = weiche violette Drei-Komponenten-Form, ohne Gesicht
- rote Blutkoerperchen = vereinfachte tiefrote Scheiben
- Haemoglobin = vereinfachte burgunderrote Struktur
- Organe/Zellen = stark stilisiert, weich, rund und gesichtslos

## Bild_01 – Cover-Regel

`Bild_01` ist Cover, erster Shot und Episode-Master-Frame.

PASS nur wenn:

- Soft-3D / 2.5D Explainer-Look eingehalten
- kein Photorealismus / Medical-CGI
- keine Menschen / Presenter / Torso-Mannequins
- Thema sofort lesbar
- Hook **„So reist Sauerstoff durch deinen Körper“** sichtbar und korrekt
- keine zusaetzlichen Anatomie-Labels
- Cover darf etwas kontrastreicher sein als normale Szenen, bleibt aber dieselbe Bildwelt

## Normale Szenen

- pro Bild genau eine Hauptaussage
- 0–2 kurze deutsche Labels bevorzugt
- maximal 3 nur bei echtem Bedarf
- keine Textwaende
- keine ueberladenen Hintergruende
- Richtung / Start / Ziel muessen ohne Voiceover grob erkennbar sein

## Reference-First

Geplante kanalweite Referenz:

```text
assets/channel/STYLE_REFERENCE.png
```

Status: **noch keine echte Bilddatei im Repo**.

Bis dahin:

```text
Bild_01 aus der kanonischen Soft-3D-Bildwelt erzeugen
→ Nutzerfreigabe
→ Bild_01.png als echtes Flow Reference/Ingredient verwenden
→ Folgeframes mit identischer Stil-/Farblogik erzeugen
```

## Produktionsstatus

Bereit:

- Voiceover-Inhalt
- 2:30-Timing
- 28 Szenen
- Szenenbewegungen
- Bildwelt
- Label-Logik
- Flow-Prompt
- Remotion-Produktionsplan

Noch benoetigt fuer den finalen MP4-Render:

1. freigegebenes `Bild_01`
2. finale `Bild_02`–`Bild_28`
3. finales Voice-Audio

Danach kann der Pilot gemaess `VIDEO-2M30-PRODUCTION.md` zusammengesetzt und gerendert werden.
