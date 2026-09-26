# Object-Talk – Project State

Letzte Aktualisierung: 26.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/004-pilot-muskelkater/
```

Thema:

**Warum kommt Muskelkater so spät?**

Cover-Hook:

**„Warum kommt Muskelkater so spät?“**

## Zweck von Pilot 004

Pilot 004 ist der erste neue End-to-End-Test nach den globalen Fixes aus dem echten Pilot-003-Render.

Er prueft insbesondere:
1. staerkere Frage-Hook direkt im ersten Satz
2. Hook → Wendung → Payoff innerhalb der ersten ca. 15 Sekunden
3. sichtbarer Text ausschliesslich aus Google Flow
4. Remotion-Textoverlays exakt 0
5. mindestens ca. 60 % Prozess-/Beziehungs-/Vergleichs-/Vorher-Nachher-Visuals
6. klar unterschiedliche Nachbarszenen statt fast identischer Anatomiebilder
7. 1.10x Voice + komprimierte lange TTS-Pausen

## Script-Hard-Lock

Der Einstieg lautet:

`Hast du dich schon mal gefragt, warum Treppen am Tag nach dem Training plötzlich viel härter werden?`

Direkt danach folgt die Wendung:

`Das Überraschende: Schuld ist nicht die Milchsäure – Muskelkater entsteht erst durch Prozesse, die sich nach der Belastung entwickeln.`

Schwache Schulbuch-Einstiege wie `Heute erklaeren wir ...`, `In diesem Video ...` oder abstrakte Definitionen sind weiterhin Hard FAIL.

## Inhaltliche Reise

`Alltags-Hook Treppe → verzögerter Schmerz → ungewohnte Belastung → exzentrische Muskelarbeit → kleine strukturelle Störungen → Reparaturreaktion → Botenstoffe → Schmerzrezeptoren → Zeitverlauf → Laktat-Mythos → Muskelkater ≠ Trainingsqualität/Wachstum → Anpassung bei Wiederholung → Erholung/Schlaf/Ernährung → leichte Bewegung → Warnabgrenzung → Zusammenfassung`

## Produktionsziel

- 35 eindeutige Bilder
- ca. 380 Wörter Voiceover
- Voice 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- erwartete Endlänge ca. 2:05–2:30
- kein Bild länger als 7 Sekunden
- kein Bildasset doppelt
- ein finales Asset pro normale Bildnummer
- nur Cover darf vor Nutzerwahl bis zu 3 Varianten haben

## Sichtbarer Text – nur Google Flow

Verbindlich:
- Cover-Titel kommt aus Flow
- normale Labels kommen aus Flow
- Remotion erzeugt keinen sichtbaren Text
- keine Remotion-Kapitelüberschriften
- keine Remotion-Keywords
- keine Remotion-Callouts
- keine Remotion-Captions
- keine Remotion-Label-Fallbacks
- falsche Flow-Schrift wird in Flow korrigiert/regeneriert

`overlay-plan.json` fuer Pilot 004 ist DISABLED und leer.

Die Cover-Hook **„Warum kommt Muskelkater so spät?“** darf nur auf `Bild_01` sichtbar sein.

## Bildwelt

Verbindlich bleibt:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Pilot-004-Farben:
- Muskel/Muskelfaser = Coral / Salmon / Rot-Orange
- strukturelle Belastung = warmes Orange-Rot
- Botenstoffe/Nervensignale = Cyan / Blau
- Erholung = Teal / Soft-Blau
- Warnung = gedaempftes Orange-Rot
- Hintergrund = Creme / Beige / helles Blau

## Referenzlogik

1. textfreie `EPISODE_STYLE_REFERENCE.png` mit `STYLE-REFERENCE-PROMPT.txt` erzeugen
2. Bild_01 als Cover erzeugen, bis zu 3 Varianten
3. Nutzer waehlt exakt 1 Cover; Rest loeschen/verwerfen
4. Bild_02–Bild_35 nur mit textfreier Referenz erzeugen
5. texttragendes Cover niemals als Follow-up-Referenz verwenden

## Visuelle Vielfalt / Informationswert

- mindestens etwa 60 % der normalen Bilder zeigen Prozess, Beziehung, Ursache/Wirkung, Weg, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander
- benachbarte Szenen unterscheiden sich in mindestens zwei Dimensionen: Komposition, Massstab, Hauptmotiv, Richtung, Zustand oder Visual-Typ
- ca. 20–35 % wichtiger Mechanismusbilder duerfen einen sinnvollen Zusatzdetailpunkt enthalten
- ein schwaches Bild wird nicht mit Editor-Text gerettet, sondern in Flow verbessert

## Fachliche Leitplanken

- Laktat/Milchsaeure NICHT als Ursache von Muskelkater darstellen
- Muskelkater NICHT als verlaessliches Mass fuer Trainingsqualitaet oder Muskelwachstum darstellen
- keine grossflaechig zerrissenen Muskeln als Standarderklaerung
- exzentrische Belastung als typischen starken Ausloeser erklaeren, nicht als einzige moegliche Ursache
- Zeitfenster 1–3 Tage als typischen Bereich, nicht als exakten universellen Peak darstellen
- keine Diagnose-, Medikamenten-, Supplement- oder individuellen Trainingsanweisungen

## Wichtige Dateien

```text
youtube-videos/004-pilot-muskelkater/01_script/VOICEOVER-ZUM-KOPIEREN.txt
youtube-videos/004-pilot-muskelkater/05_info/mechanism-map.md
youtube-videos/004-pilot-muskelkater/05_info/claim-matrix.md
youtube-videos/004-pilot-muskelkater/05_info/phase1-scenes.json
youtube-videos/004-pilot-muskelkater/05_info/sentence-visual-plan.json
youtube-videos/004-pilot-muskelkater/02_bildprompts/STYLE-REFERENCE-PROMPT.txt
youtube-videos/004-pilot-muskelkater/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
youtube-videos/004-pilot-muskelkater/02_bildprompts/label-plan.json
youtube-videos/004-pilot-muskelkater/02_bildprompts/image-review.json
youtube-videos/004-pilot-muskelkater/03_pipeline/overlay-plan.json
youtube-videos/004-pilot-muskelkater/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

## Naechster Ablauf

1. Voice aus `VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. textfreie Episode-Style-Referenz erzeugen.
3. bis zu 3 Coverrichtungen fuer Bild_01 erzeugen.
4. genau 1 Cover waehlen und Rest verwerfen.
5. Bild_02–Bild_35 einzeln produzieren und visuell pruefen.
6. Phase-2-QA inklusive Text-Whitelist, Bildunterschied und Informationswert.
7. Phase 3: Voice 1.10x, Pausen komprimieren, Remotion motion-only rendern.
8. finalen Render komplett pruefen.