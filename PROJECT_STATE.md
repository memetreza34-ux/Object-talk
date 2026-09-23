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

Die Bildpipeline ist **Reference-First** und die Bildwelt wurde nach dem letzten Test erneut geschaerft.

Der letzte Flow-Test war weiterhin falsch, weil Flow aus „3D-Animation + Anatomie“ laechelnde Menschen, Torso-Cutaways und schulbuchartige Anatomieposter gebaut hat.

Ab jetzt gilt deshalb zusaetzlich verbindlich:

- **kein Mensch als Standard-Hauptmotiv**
- **kein sichtbares Gesicht als Cover-Hero**
- **kein Kind/Erwachsener als Presenter**
- **kein Torso-Mannequin / Anatomie-Schulmodell**
- **keine flache Anatomieposter-/Lehrtafel-Komposition**
- biologische Prozesse und Organe sind die Hauptdarsteller
- menschlicher Kontext nur wenn fachlich noetig, dann gesichtslos und klar sekundär
- echter 3D-Animationsfilm-Frame mit Perspektive, Tiefe und filmischer Inszenierung

## Verbindliche Kanal-DNA

Oberste Stilreferenz:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Dauerhafte Flow-Regeln:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Verbindlicher Look:

- premium theatrale 3D-Feature-Animation
- hell, freundlich, sauber und modern
- nicht babyhaft
- weiche gerundete Formen
- matte/satinierte Premium-Materialien
- warmes Key-Light + weiches Fill-Light + dezentes Rim-Light
- klare Vordergrund-/Mittelgrund-/Hintergrundstaffelung
- frische Farben: Creme, Apricot, Coral, warmes Rot, Himmelblau, Teal
- kein kosmischer / Weltraum-artiger Look
- keine dunkle violette Sci-Fi-Mikrowelt
- kein Medical-CGI
- kein Anatomiesoftware-/Schulbuch-Look
- kein Corporate-Stock-3D
- kein billiger Toy-Look

## Pilot 001 – feste Objektregeln

Der Sauerstoff-Pilot nutzt **keinen O2-Guide und kein Dauermaskottchen**.

- O2 = zwei verbundene blass-cyanfarbene Kugeln ohne Gesicht
- CO2 = neutral-violett/graue Drei-Kugel-Form ohne Gesicht
- rote Blutkoerperchen = tiefe warmrote bikonkave Scheiben ohne Gesicht
- Haemoglobin = burgunderrote vereinfachte Struktur
- Organe/Zellen = stark stilisiert, weich, rund und gesichtslos

## Bild_01 – neue harte Regel

`Bild_01` darf nur PASS sein, wenn:

- **kein Mensch** vorkommt
- **kein sichtbares Gesicht** vorkommt
- **kein Torso / Mannequin / Koerper-Cutaway** das Cover dominiert
- Lunge + Herz + Sauerstoffweg als eigenstaendige filmische 3D-Objekte inszeniert sind
- die Szene wie ein echter hochwertiger Animationsfilm-Frame aussieht
- die Hook **„So reist Sauerstoff durch deinen Körper“** sichtbar und korrekt ist
- die Labels **„Lunge“** und **„Herz“** korrekt sind
- kein Poster-/Schulbuch-/Medical-/Kosmos-Look entsteht

## Reference-First

Geplante kanalweite Referenz:

```text
assets/channel/STYLE_REFERENCE.png
```

Status: **noch nicht vorhanden**.

Bis zur Freigabe:

```text
neues Bild_01 aus der korrigierten Kanal-DNA erzeugen
→ alle Menschen-/Torso-/Poster-Varianten automatisch verwerfen
→ beste filmische Organ-Komposition zeigen
→ Nutzerfreigabe
→ Bild_01.png als echtes Flow Reference/Ingredient verwenden
→ erst dann Bild_02–28
```

Ein textlicher Satz wie `Using Bild_01 as reference` zaehlt nicht als tatsaechliche Referenz.

## Textregel

Sichtbarer Text bleibt Teil der Bilder:

- Cover-Hook direkt im Cover
- normale Bilder normalerweise 1–3 kurze deutsche Labels
- Begriffe aus `02_bildprompts/label-plan.json`
- ausschliesslich Deutsch
- falsche Schreibweise = Regeneration
- Remotion nur als exakter Fallback bei wiederholtem KI-Textfehler

## Naechster Produktionsschritt

1. Alten Flow-Lauf und seine drei Covervarianten **nicht** als Referenz verwenden.
2. Aktualisierte `engine/FLOW-AGENT-INSTRUCTIONS.md` setzen.
3. Aktualisierten Pilot-Prompt verwenden.
4. Nur `Bild_01` neu erzeugen.
5. Alle Varianten mit Mensch, Gesicht, Torso oder Poster-Look automatisch FAIL setzen.
6. Erst ein akzeptiertes organ-zentriertes Filmframe als `Bild_01.png` freigeben.
7. Danach Bild_02–28 mit diesem Bild als echter visueller Referenz erzeugen.
