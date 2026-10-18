# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap fuer ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `engine/KANAL-ANALYSE-2026-10.md` (warum Skripte/Bilder bis 010 zu schwach waren und was ab 011 gilt)
3. `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
4. `engine/VISIBLE-TEXT-STANDARD.md`
5. `engine/CONTINUOUS-IMPROVEMENT.md`
6. `engine/EXPORT-STANDARD.md`
7. `PROJECT_STATE.md`
8. `config/channel.json`
9. `config/video.json`
10. `THEMEN-GEHIRN.md`
11. `engine/README.md`
12. `engine/SCRIPT-STANDARD.md` (inkl. §13 Retention-Handwerk)
13. `engine/TITEL-THUMBNAIL-STANDARD.md`
14. `engine/PLANNING-V2.md` (inkl. §16 Storyboard-v2)
15. `engine/PRESENTATION-OVERLAY-SYSTEM.md`
16. relevante Dateien des aktuellen YouTube-Projekts

## ARBEITSWEISE AB VIDEO 011 – EINE STORYBOARD-QUELLE (verbindlich)

1. Projekt anlegen: `python tools/create_video.py NNN-longform-thema`
2. Recherche, `claim-matrix.md`, `mechanism-map.md` in `.intern/05_info/` schreiben (jede Zahl im Skript belegen).
3. **Nur** `.intern/05_info/storyboard-source.json` (format `storyboard-v2`) schreiben: Sprechtext pro Bild, Bildart, Komposition, Labels, Kapitel, Open Loops, Titel/Cover, Farbcode. Vorbilder: `youtube-videos/011-longform-hunger-v2/`, `youtube-videos/012-longform-verdauung-v2/`.
4. `python tools/build_phase1_package.py youtube-videos/NNN-...` erzeugt Skript, Flow-Prompt, alle Pläne, Caption-Entwurf und Antigravity-Auftrag. Abgeleitete Dateien nie von Hand ändern.
5. `python tools/validate_planning_v2.py youtube-videos/NNN-...` muss PASS sein (Bildregie, Kamerabewegungen, Skriptqualität: Zahlen, Fragen, Absicherungen, Open Loops, Szenendauer).
6. Skripte sind **unterhaltsam und konkret**: Experiment- oder Paradox-Hook, nummerierte Stationen/Gründe, belegte Zahlen, höchstens ein Gesundheitshinweis, Brücke zum Partnervideo. Kanalname für Zuschauer: **Lebenslogik**.

Aktive Produktion steht in `PROJECT_STATE.md`.

## ABSOLUTE NORMALE PRODUKTIONSPRIORITÄT – VERBESSERUNG NACH JEDEM VIDEO

**Autoritativ: `engine/CONTINUOUS-IMPROVEMENT.md` – VOR allen normalen neuen Videoarbeiten lesen.** Jede tatsächlich fertig gerenderte Videoausgabe kritisch anschauen, mindestens drei konkrete Schwächen mit Ursache benennen, 2–5 wirksame globale Workflow-/Prompt-/Toolverbesserungen wirklich umsetzen und testen, danach den Bericht unter `.intern/05_info/improvement-review.json` dokumentieren und mit `tools/improvement_loop.py register` ins Lernprotokoll übernehmen. Vor der nächsten Phase 1 nachweisen, wie **alle aktiven Lessons** im aktuellen Skript/Bildprompt/Workflow eingesetzt wurden (`.intern/05_info/improvement-applied.json`); Validator blockiert unbehandelte Pflichten. Nie Erfolg oder ein gesehenes Video behaupten, wenn keine echte Prüfung stattgefunden hat. Keine zusätzlichen sichtbaren Ordner oder Exportdateien. Historische Videos nicht rückwirkend verändern.


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

## Höchste visuelle Verbesserung seit Video 010

Video 010 wurde vom Nutzer für das Skript gelobt, die Bilder jedoch als zu häufig personenlastig und erklärungsschwach kritisiert. **Ab Video 011 zuerst die sichtbare Wissenschaft gestalten:** dominierende Makro-/Organ-/Gewebe-/Lebensmittel-Innenansichten, Cutaways, Funktionswege und verständliche Vergleiche. Mehr harmonische Farben, klarere bildfüllende Illustrator-Kompositionen. Ganzer Mensch nur mit echtem Lernzweck, keine redundanten Küchen-/Einkaufsposen. Vorgaben und Mixprüfung stehen in `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md` und `engine/PLANNING-V2.md`. Skript deshalb nicht ungefragt umschreiben, nicht bereits gerenderte Videos verändern.

**Update 18.10.2026:** Der Nutzer hat ausdrücklich deutlich bessere, unterhaltsamere Skripte, passendere Bilder und bessere Titel verlangt. Umgesetzt als Neuauflagen 011 (Hunger) und 012 (Verdauung/Pizza). Die alten Ordner 008/010 bleiben unverändert. Für neue Skripte gilt `engine/SCRIPT-STANDARD.md` §13.

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

Separates Cover (neue Produktionen, außerhalb Bild_01):
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
- `03_export/` als einfachen Nutzerexport vorbereiten; technische QA in `.intern/`


## COVER-FIRST-WORKFLOW – HARTE PRODUKTIONSREIHENFOLGE

Autoritativ: `engine/FLOW-COVER-FIRST-WORKFLOW.md`.

**GENAU EINE vollständige Flow-Promptdatei im sichtbaren Ordner, plus EIN ZIP-Ablageordner.** Derselbe Prompt enthält drei Cover und das vollständige Szenenregister. Flow erzeugt erst drei Cover, zeigt sie und wartet auf Nutzerwahl 1/2/3; erst danach Bilder 01+ intern in Fünfergruppen, ohne weitere Promptdateien oder generische Rückfragen. Alle geplanten Szenen dürfen im Prompt beschrieben stehen, werden aber NIE in einem einzigen Bildgenerierungs-Batch angefordert. Dateinummern nur Metadaten. Finale Bilder-ZIP unter `02_bildprompts/bilder-zip`, interne QA in `.intern/05_info`, entpackte Bilder in `.intern/03_pipeline/images`.


## Phase-1-Handoff – ZWEI DIREKTLINKS ANTWORTEN (verbindlich)

**Sobald Phase 1 eines Videos nach tatsächlicher Erstellung und Prüfung erfolgreich abgeschlossen ist, MUSS die Antwort von ChatGPT oder einem anderen Chat-Agenten sofort diese zwei ANKLICKBAREN Links zum AKTUELLEN Video enthalten** (wie die zwei Aktionslinks im Beispiel des Nutzers):

- **Google-Flow-Prompt öffnen** → `https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/<VIDEOORDNER>/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
- **Voice-over-Skript öffnen** → `https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/<VIDEOORDNER>/01_script/script.txt`

`<VIDEOORDNER>` zwingend durch den tatsächlich gerade erstellten Videoordner ersetzen; echte Pfade/Dateiinhalte vor dem Link überprüfen. Niemals die Template-Platzhalter oder Links eines älteren Videos ausgeben. Links als Markdown-Klicklinks oder als zwei bedienbare Öffnen-Schaltflächen in der Chat-Antwort präsentieren, **nicht nur Dateipfade, einen allgemeinen Repository-Link oder eine Erklärung**. Beide Dateien öffnen die komplette Datei in GitHub und sind auch im mobilen Browser/Tablet zugänglich (bei privaten Repos mit GitHub-Anmeldung). Nutzer kann Text von dort 1:1 in Google Flow bzw. seine Voice-KI kopieren. Ein GitHub-Dateilink öffnet **nicht automatisch** Google Flow selbst; nichts anderes behaupten.

Die Übergabe darf KEINE zusätzliche Bestätigung abfragen und soll direkt nach dem Phase-1-Abschluss erfolgen. Keine weiteren sichtbaren Dateien im Videoordner erzeugen; `01_script/script.txt` und der eine Flow-TXT reichen. Wenn eine der Dateien fehlt, unvollständig oder ein Template ist, Phase 1 NICHT als fertig behaupten und keine falschen Links ausgeben. Nach erfolgreichem `python tools/validate_planning_v2.py youtube-videos/<VIDEOORDNER>` druckt der Validator exakt diese zwei Links als Handoff-Vorlage.

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

`.intern/03_pipeline/overlay-plan.json` muss leer/deaktiviert bleiben.

Externe YouTube-Untertitel sind trotzdem Pflicht:
- `03_export/UNTERTITEL-MIT-ZEITEN.txt`
- `.intern/UNTERTITEL-YOUTUBE.srt`
- beide aus finaler `timeline.json` mit `tools/export_subtitles.py`
- Zeitcodes niemals schaetzen

## Timing

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json → export_subtitles.py`

Standard:
- Voice 1.10x
- lange Pausen komprimieren
- kein Standbild ueber 7 Sekunden
- kein Bildasset doppelt verwenden

## Export – genau vier sichtbare Dateien bei neuen Produktionen

**Autoritativ: `engine/EXPORT-STANDARD.md`.** Nach der Produktion stehen im sichtbaren `03_export/` ausschließlich:
- `VIDEO.mp4`: finaler Film, ohne YouTube-Cover als Anfangsszene.
- `COVER.png`: separates, vom Nutzer gewähltes YouTube-Thumbnail.
- `CAPTION-YOUTUBE.txt`: einmaliger YouTube-Titel + individuelle Beschreibung + bis zu fünf Hashtags.
- `UNTERTITEL-MIT-ZEITEN.txt`: vollständiges tatsächlich gesprochenes Script mit echten Audiotimestamps zum Kopieren.

Keine weiteren sichtbaren Exportdateien oder Unterordner (kein `fertiges-video`, keine zweiten Captions, keine SRT, keine QA-Berichte, keine Postmortems, keine Placeholder). **Technische** SRT, Renderbericht, Scorecard, Postmortem, Audio-/Video-QA und `timeline.json` werden weiterhin erstellt/geprüft, liegen aber nur in `.intern/`. Keine Mediendateien oder echte Zeitstempel vortäuschen, bevor sie existieren.

Diese Regel gilt nur für **zukünftige Produktionen**. Vorhandene Videos/Exportordner nicht rückwirkend verändern.

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

**Ab Video 011:** 008 liefert nur noch Bildwelt, Cover-first-Ablauf und Fünfergruppen. Promptaufbau, Planungsdateien, Antigravity-Auftrag und Dramaturgie kommen ausschließlich aus `.intern/05_info/storyboard-source.json` und `tools/build_phase1_package.py` (`engine/PLANNING-V2.md` §16, `engine/SCRIPT-STANDARD.md` §13); der Export folgt `engine/EXPORT-STANDARD.md`. Die Dramaturgie von 008 gilt laut `engine/KANAL-ANALYSE-2026-10.md` als zu lehrbuchhaft und wird nicht mehr kopiert.

Fuer neue 6–7-Minuten-Videos `engine/LONGFORM-008-MASTERSTANDARD.md` verwenden: zuerst die Dateien aus `008-longform-verdauung` auf Prompt-Struktur, wissenschaftliche Abschnittsplanung, Bildwelt, Render und Export abgleichen, danach **nur Thema und fachliche Visuals/Skript anpassen**. Keine neue Bildwelt erfinden. Wie im Verdauungsfilm 008 ohne Bildvorlagen arbeiten: ein Textprompt, drei Cover, Nutzer wählt, danach Fünfergruppen in derselben schriftlichen Bildwelt; kein Cover als Bildreferenz. Dokumentation und Medienstatus sauber unterscheiden.


## Ohne visuelle Vorlagen produzieren
Die Bildwelt von 008 durch den immer gleichen ausführlichen Textstil und konkrete biologische Szenenbeschreibungen nachbilden. Weder 008-JPGs noch gewähltes Cover als Bildvorlage hochladen. Google Flow darf keinen Referenz-Upload verlangen. Die visuelle Qualität wird an den tatsächlich generierten Bildern geprüft.


## Neue 3-Ordner-Regel ab Video 009 (verbindlich)

Sichtbar nur `01_script/`, `02_bildprompts/`, `03_export/`. Technische Planungs- und Renderdateien unter verstecktem `.intern/`. Das Google-Flow-Cover ist ein **eigenes YouTube-Thumbnail `03_export/COVER.png` und KEINE Szene `Bild_01`**. Bild_01 ist sofort die erste normale biologische Illustration, nur die normal nummerierten Bilder in die Bilder-ZIP und das MP4. Nach Coverwahl Bilder 01–05, danach 06–10 usw. Untertitel aus echter Audioausrichtung nach `03_export/UNTERTITEL-MIT-ZEITEN.txt`. Alle Labels sollen häufig dann erscheinen, wenn sie einen Vorgang verständlicher machen, ansonsten textfrei; höchstens 2 kurze Wörter/Gruppen pro Bild. Keine Vorlagen-Uploads, keine Remotion-Textlayer, keine überfüllten Szenen.
