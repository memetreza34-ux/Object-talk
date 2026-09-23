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

Die Bildpipeline ist **Reference-First**, aber sichtbarer deutscher Text bleibt Teil der Bilder.

Das bedeutet:

- echte visuelle Referenzen sind autoritativ
- `Bild_01` muss nach Freigabe als echte visuelle Referenz fuer jedes Folgebild angehaengt werden
- `STYLE_REFERENCE.png` wird kanalweit genutzt, sobald eine saubere Referenz freigegeben wurde
- die Bildwelt ist hell, freundlich und hochwertige 3D-Animation statt kosmisch/dunkel/medizinisch
- `Bild_01` enthaelt die deutsche Cover-Hook direkt im Bild
- normale Bilder enthalten normalerweise 1–3 kurze deutsche Labels
- Remotion ist nur Text-Fallback, wenn Flow einen Begriff wiederholt falsch schreibt

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
- hell, freundlich, sauber und leicht verstaendlich
- weiche gerundete Formen
- matte/satinierte Premium-Materialien
- warmes Hauptlicht + weiches Fill-Light + dezentes Rim-Light
- klare Tiefe und frische kontrollierte Farben
- kein kosmischer / Weltraum-artiger Look
- keine dunkle violette Sci-Fi-Mikrowelt als Standard
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
Bild_01 aus der kanonischen hellen Kanal-DNA erzeugen
→ deutsche Cover-Hook muss sichtbar sein
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
→ intern auf Stil, deutsche Hook, Anatomie und Artefakte pruefen
→ bei Fehlern regenerieren
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

Sichtbarer Text ist verbindlicher Teil der Erklaerung.

- Cover-Hook fuer Pilot 001: **„So reist Sauerstoff durch deinen Körper“**
- normale Bilder: normalerweise 1–3 kurze deutsche Labels
- Begriffe kommen aus `02_bildprompts/label-plan.json`
- sichtbarer Text ausschliesslich Deutsch
- falsche Flow-Schreibweise = Regeneration
- Remotion nur als exakter Fallback fuer Begriffe, die Flow wiederholt nicht korrekt schreibt
- finales Video darf die geplanten Labels nicht verlieren

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
3. Zuerst nur `Bild_01` erzeugen.
4. Pruefen: heller Premium-3D-Animationsfilm-Look, keine kosmische Welt, deutsche Hook sichtbar und korrekt.
5. `Bild_01` freigeben.
6. Danach `Bild_01.png` bei jeder Folgegeneration als echtes visuelles Reference/Ingredient anhaengen.
7. Alle Folgeframes mit den vorgegebenen kurzen deutschen Labels erzeugen.
8. Alte kosmische/dunkle Pilotbilder nicht weiterverwenden.
