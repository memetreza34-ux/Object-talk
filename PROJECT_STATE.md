# Object-Talk – Project State

Letzte Aktualisierung: 23.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 ist der erste echte 2–3-Minuten-Pilotfilm.

## Aktueller Schwerpunkt

Die Bildpipeline wurde auf **Reference-First** umgestellt.

Das bedeutet:

- Stil wird nicht mehr nur durch lange Textprompts beschrieben
- echte visuelle Referenzen sind autoritativ
- `Bild_01` muss nach Freigabe als tatsaechliche visuelle Referenz fuer jedes Folgebild angehaengt werden
- `STYLE_REFERENCE.png` wird kanalweit genutzt, sobald eine saubere Referenz vom Nutzer freigegeben wurde
- Flow erzeugt standardmaessig keine Labels oder Hook-Texte mehr
- Text/Labels werden spaeter kontrolliert in Remotion gerendert

Dauerhafte Flow-Agent-Instructions:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Produktionsstandard:

```text
engine/FLOW-PRODUCTION-STANDARD.md
```

## Verbindliche Kanal-DNA

Oberste schriftliche Stilreferenz:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Die Kanalidee besteht aus zwei Ebenen derselben hochwertigen 3D-Animationsserie:

1. **Viral Object-Talk** – passende Lebensmittel/Gegenstaende duerfen sprechende 3D-Figuren mit klarer Mimik sein.
2. **Inside-the-Body** – Organe, Blut, Zellen und biologische Prozesse bleiben normalerweise gesichtslos.

Verbindlich:

- hochwertige stilisierte 3D-Feature-Animation
- weiche gerundete Formen
- matte/satinierte Premium-Materialien
- warme filmische Beleuchtung + Rim-Light
- starke Tiefe und kontrollierte kraeftige Farben
- kein Medical-CGI
- keine realistische Haut/Poren
- keine nassen Gewebetexturen
- kein Corporate-Stock-3D
- kein billiger Toy-Look
- keine erfundenen Maskottchen nur um Object-Talk zu erzwingen

## Pilot 001 – feste Objektregeln

Der Sauerstoff-Pilot nutzt **keinen O2-Guide und kein Dauermaskottchen**.

- O2 = zwei verbundene blass-cyanfarbene Kugeln ohne Gesicht
- CO2 = neutral-violett/graue Drei-Kugel-Form ohne Gesicht
- rote Blutkoerperchen = tiefe warmrote bikonkave Scheiben ohne Gesicht
- Haemoglobin = burgunderrote vereinfachte Struktur
- Organe/Zellen = stark stilisiert, weich, rund und gesichtslos

## Referenzstatus

Geplante kanalweite Referenz:

```text
assets/channel/STYLE_REFERENCE.png
```

Status: **noch nicht vorhanden**.

Bis zur ausdruecklichen Freigabe gilt Bootstrap-Modus:

```text
Bild_01 ohne kanalweite Bildreferenz erzeugen
→ visuell pruefen
→ Nutzerfreigabe
→ Bild_01.png als echtes Flow-Reference/Ingredient verwenden
→ erst danach Bild_02–28
```

Ein textlicher Satz wie `Using Bild_01 as the exact style reference` zaehlt nicht als visuelles Anhaengen der Referenz.

## Flow-Regel – genau eine Freigabe

Flow stoppt nur nach `Bild_01`:

```text
Bild_01 erzeugen
→ intern pruefen/regenerieren
→ Bild_01 zeigen
→ einmalige Nutzerfreigabe
```

Danach automatisch:

```text
Bild_02–06
→ interne visuelle QA
→ Bild_07–11
→ interne visuelle QA
→ Bild_12–16
→ interne visuelle QA
→ Bild_17–21
→ interne visuelle QA
→ Bild_22–26
→ interne visuelle QA
→ Bild_27–28
→ Recovery
→ finaler Ordner
→ ZIP
```

Keine weiteren Fragen wie „Soll ich weitermachen?“.

## Textregel

Flow-Bilder bleiben standardmaessig textfrei.

- Cover-Hook -> Remotion
- deutsche Labels -> `02_bildprompts/label-plan.json` -> Remotion
- keine KI-Schrift direkt im Bild

## Aktuelle Nutzerdateien

Flow-Szenenauftrag:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Dauerhafte Agent-Regeln:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Voice:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Antigravity/Remotion:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

## Naechster Produktionsschritt

1. Dauerhafte Flow-Agent-Instructions aus `engine/FLOW-AGENT-INSTRUCTIONS.md` setzen.
2. Pilot-Flow-Prompt verwenden.
3. Zuerst nur textfreies `Bild_01` erzeugen.
4. `Bild_01` visuell freigeben.
5. Danach `Bild_01.png` bei jeder Folgegeneration als echtes visuelles Reference/Ingredient anhaengen.
6. Alte O2-Maskottchen-Bilder nicht weiterverwenden.
