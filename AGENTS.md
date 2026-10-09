# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap fuer ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
3. `engine/VISIBLE-TEXT-STANDARD.md`
4. `engine/EXPORT-STANDARD.md`
5. `PROJECT_STATE.md`
6. `config/channel.json`
7. `config/video.json`
8. `THEMEN-GEHIRN.md`
9. `engine/README.md`
10. `engine/SCRIPT-STANDARD.md`
11. `engine/PLANNING-V2.md`
12. `engine/PRESENTATION-OVERLAY-SYSTEM.md`
13. relevante Dateien des aktuellen YouTube-Projekts

Aktive Produktion steht in `PROJECT_STATE.md`.

## VERBINDLICHE BILDWELT

Kanalweit gilt:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Nicht reaktivieren:
- alte 2.5D-/Soft-3D-Regeln
- alte Premium-3D-/Feature-Animation-Regeln
- historische Pilot-Stile als Kanalstandard
- alte Style-Reference-Systeme

## Bildprinzip

Jedes normale Biologie-/Gesundheitsbild soll:
- wie ein sauberer Frame aus einer animierten Biologie-Erklaerserie wirken
- vereinfachte, fachlich erkennbare Anatomie zeigen
- weiche organische Formen, klare Konturen, weiche Verlaeufe und leichte Tiefe verwenden
- hell und uebersichtlich bleiben
- **eine Hauptidee / einen Hauptprozess** zeigen
- bevorzugt nur 2–4 zentrale sichtbare Elemente enthalten
- normalerweise **0–2 kurze deutsche Labels** enthalten

Wenn ein Bild zu viel erklaeren muesste: unwichtige Information weglassen oder neue Szene planen.

## Cover – HARD RULE

`Bild_01` / Cover:
- genau ein sichtbarer Textblock
- nur Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Pfeiltexte

Zusaetzlicher sichtbarer Text auf dem Cover = **REGENERATE**.

## Textkontrast – HARD RULE

- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- kein light-on-light
- kein dark-on-dark
- Text bevorzugt in ruhiger negativer Flaeche

Schlecht lesbarer Text = **REGENERATE**.

## Prompting

Flow-Anweisungen auf Englisch.
Viewer-facing Text nur Deutsch.

Prompts kurz halten:
1. kanonischer Styleblock
2. konkrete Szene
3. Prozess
4. 0–2 Labels nur wenn noetig
5. Kontrastregel fuer sichtbaren Text
6. kurze Negativregel

Keine langen Style-Romane in jedem Szenenprompt.

## HARTE UNSICHTBARKEITSREGEL FUER PRODUKTIONS-IDs

Interne Nummern duerfen nur in Dateien/Planung existieren.

Niemals sichtbar rendern:
- `Bild_01`, `Bild_02`, `Bild 01`
- `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Asset-IDs
- Prompttitel
- Produktionshinweise

Jeder Flow-Prompt muss klarstellen: **Bild-/Szenennummern sind reine Produktionsmetadaten und duerfen nicht Teil des Bildes werden.**

Wenn eine interne Nummer im Bild sichtbar ist: REGENERATE.

## Phase 1 – Creative Director

Muss:
- Fakten pruefen
- Mechanism Map erstellen
- starken Neugier-Hook schreiben
- jeden Speech-Beat als echtes Erklaerbild planen
- Prozesse, Beziehungen, Wege, Ursache/Wirkung, Vergleiche und Massstabwechsel bevorzugen
- maximal zwei isolierte Einzelobjektbilder hintereinander zulassen
- sichtbaren Erklaerwert und Unterschied zu Nachbarbildern definieren
- **0–2 Labels pro normalem Bild**, nur wenn notwendig
- Cover exakt title-only planen
- bei zu hoher Informationsdichte den Beat auf mehr Bilder aufteilen
- **keine Remotion-Texte oder Text-Overlays planen**
- `04_export/` nach `engine/EXPORT-STANDARD.md` vorbereiten


## COVER-FIRST-WORKFLOW – HARTE PRODUKTIONSREIHENFOLGE

Autoritativ: `engine/FLOW-COVER-FIRST-WORKFLOW.md`.

**GENAU EINE vollständige Flow-Promptdatei im sichtbaren Ordner, plus EIN ZIP-Ablageordner.** Derselbe Prompt enthält drei Cover und das vollständige Szenenregister. Flow erzeugt erst drei Cover, zeigt sie und wartet auf Nutzerwahl 1/2/3; erst danach Bilder 02+ intern in Fünfergruppen, ohne weitere Promptdateien oder generische Rückfragen. Alle geplanten Szenen dürfen im Prompt beschrieben stehen, werden aber NIE in einem einzigen Bildgenerierungs-Batch angefordert. Dateinummern nur Metadaten. Finale Bilder-ZIP unter `02_bildprompts/bilder-zip`, interne QA in `05_info`, entpackte Bilder in `03_pipeline/images`.

## Phase 2 – Google Flow

- jedes Bild einzeln erzeugen
- kanonischen Styleblock verwenden
- biologische Labels direkt im Bild erzeugen
- lieber kein Label als ein unnoetiges Label
- Labels kurz halten: bevorzugt 1–2 Woerter, maximal 3
- Textkontrast pruefen
- Cover auf exakt einen Textblock pruefen
- falsche Labels/Schreibweise/Kontrast korrigieren oder regenerieren
- interne Bild-/Szenennummern niemals sichtbar machen
- pro finaler Bildnummer genau ein akzeptiertes Asset behalten
- keine alte Pilot-Bildwelt als Referenz verwenden

## Phase 3 – Editor / Antigravity / Remotion

Grundsatz:
**100 % Vollbild-Illustration. Remotion erzeugt keinen sichtbaren Text.**

Remotion ist nur fuer:
- Audio
- Timing
- leichte Zoom-/Pan-Bewegungen
- statische Frames
- Schnitte
- dezente nicht-textliche Uebergaenge
- Rendering

Remotion darf NICHT erzeugen:
- Zwischenueberschriften
- Key-Facts
- Summary-Zeilen
- Kapiteltexte
- Callouts
- eingebrannte Untertitel/Captions
- anatomische Labels
- Textkarten
- sichtbare Bild-/Szenennummern
- irgendeinen sonstigen viewer-facing Text

`03_pipeline/overlay-plan.json` muss leer/deaktiviert bleiben.

Externe YouTube-Untertitel sind trotzdem Pflicht:
- `04_export/UNTERTITEL-MIT-ZEITEN.txt`
- `04_export/UNTERTITEL-YOUTUBE.srt`
- beide aus finaler `timeline.json` mit `tools/export_subtitles.py`
- Zeitcodes niemals schaetzen

## Timing

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json → export_subtitles.py`

Standard:
- Voice 1.10x
- lange Pausen komprimieren
- kein Standbild ueber 7 Sekunden
- kein Bildasset doppelt verwenden

## Export – Pflicht

Jedes fertige Video braucht:
- `04_export/CAPTION-YOUTUBE.txt` mit Titel + Beschreibung + max. 5 Hashtags
- `04_export/UNTERTITEL-MIT-ZEITEN.txt` mit komplettem Script und echten Zeitabschnitten
- `04_export/UNTERTITEL-YOUTUBE.srt` als hochladbare YouTube-Untertiteldatei
- finale YouTube-MP4
- Renderbericht
- Quality-Scorecard
- Postmortem

Ohne diese Dateien kein `YouTube-ready`.

## Fail-closed

STOP bei:
- schwachem Script-Hook
- Script/Audio-Mismatch
- fehlenden/doppelten Bildern
- wissenschaftlich falscher Kernaussage
- mehr als einer Hauptidee im selben ueberladenen Bild
- mehr als 2 Labels in einem normalen Bild
- Zusatztext auf dem Cover
- schwachem Textkontrast
- unleserlichen/falschen Labels
- sichtbarer interner Bild-/Szenennummer
- altem 2.5D-/3D-Look statt der freigegebenen Illustrationswelt
- drei oder mehr isolierten Objektportraits hintereinander
- nicht-leerem Remotion-Textoverlay
- irgendeinem von Remotion erzeugten sichtbaren Text
- fehlender/leer bleibender Untertiteldatei nach Phase 3
- geschaetzten statt echten Untertitel-Zeitcodes

## Longform 008 – bewährter Referenzstandard

Fuer neue 6–7-Minuten-Videos `engine/LONGFORM-008-MASTERSTANDARD.md` verwenden: zuerst die Dateien aus `008-longform-verdauung` auf Prompt-Struktur, wissenschaftliche Abschnittsplanung, Bildwelt, Render und Export abgleichen, danach **nur Thema und fachliche Visuals/Skript anpassen**. Keine neue Bildwelt erfinden. Original-008-Frames müssen als reale Bilder in Flow bereitstehen; das ausgewählte und 008-konforme Cover wird als SEKUNDÄRER Referenzanker dazugenommen, nicht als alleiniger Stilgeber. Dokumentation und Medienstatus sauber unterscheiden.


## 008 Original-Video-Fingerabdruck (Pflicht vor Flow)

`bildwelt/008-ORIGINAL-VIDEO-STYLE-REFERENCE.md` lesen und 2–4 der dort dokumentierten echten 008-Frames im externen Flow-Chat tatsächlich hochladen. Der kurze Styleblock allein wurde bereits als unzureichend nachgewiesen. Nach Coverwahl das gewählte Cover als zusätzliche Referenz mitlaufen lassen. Keine neue Folge mit isolierten Lehrbuchsymbolen, leuchtenden Neon-Gehirnen oder Animefiguren als '008-Bildwelt' freigeben. Reale JPGs sind noch NICHT automatisch im GitHub-Repo eingecheckt; die Referenz-ZIP muss separat eingespielt werden.
