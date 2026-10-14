# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widerspruechen gilt zuerst eine ausdrueckliche aktuelle Nutzeranweisung, danach dieser Contract.

## HÖCHSTE PRODUKTIONSPRIORITÄT: Kontinuierliche Verbesserung

**JEDES fertig gerenderte Video muss eine neue, beweisgestützte Lernrunde auslösen, BEVOR das nächste Video als fertig geplant gilt.** Pflicht: echte Videosichtung, Ursachenanalyse, mindestens 2 wirksame getestete Änderungen an der globalen Produktion, interner Verbesserungsbericht, Aktualisierung des zentralen Ledgers und nachweisliche Übernahme aller aktiven Lehren in die nächste Phase 1. Bewertungszahlen und Verbesserungen niemals ohne Belege erfinden. Das ist wichtiger als schneller Videoausstoß. Vollständiger Ablauf und technische Prüfer: `engine/CONTINUOUS-IMPROVEMENT.md`, `tools/improvement_loop.py`. Alle technischen Berichte bleiben in `.intern/`, die sichtbaren drei Nutzerordner bleiben unverändert. Ältere Videos 000–009 werden nicht rückwirkend migriert.

## Ziel

Object-Talk produziert deutschsprachige YouTube-Erklaervideos zu Ernaehrung, Gesundheit, menschlichem Koerper und Biologie.

Harte Grundregeln:
- normale Kanalvideos mindestens 5:00 Minuten, sofern der Nutzer nicht bewusst einen kuerzeren Testpilot bestellt
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- generierte Standbilder bleiben die visuelle Basis
- hohe visuelle Dichte statt langer statischer Bildhaltezeiten
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wissenschaftlich relevante Aussagen pruefen

## Script-Standard – Neugier zuerst

Die ersten 5–10 Sekunden muessen sofort Neugier erzeugen.

Bevorzugt:
- direkte Zuschauerfrage
- ueberraschende Aussage
- Mythos / Fehlannahme
- Alltagsraetsel
- klarer Kontrast

Opening:
1. Hook
2. unerwartete Antwort / Wendung
3. klares Payoff-Versprechen innerhalb der ersten ca. 15 Sekunden

Autoritativ: `engine/SCRIPT-STANDARD.md`

## Audio-/Pacing-Standard

Sofern nichts anderes beschlossen wird:
- finales Voiceover 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- finales verarbeitetes `final-voiceover.wav` ist die Timing-Quelle
- Video nicht durch Pausen oder lange Bild-Holds kuenstlich strecken

## Visuelle Dichte / Bildwechsel

- ein Standbild normalerweise etwa 3–6 Sekunden
- harte Obergrenze 7.0 Sekunden
- bei mehreren Lehrbeats neue eindeutige Szene planen
- dasselbe Bild nicht wiederverwenden, um Zeit zu fuellen
- **ein dominanter Lehrpunkt pro Bild**
- Prozesse, Beziehung, Ursache/Wirkung, Wege, Vergleiche, Vorher/Nachher und Kontext bevorzugen
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander
- benachbarte Szenen sollen sich in mindestens zwei visuellen Dimensionen unterscheiden
- wenn ein Bild mehrere Hauptaussagen braucht: **Beat teilen und mehr Bilder verwenden**

## VERBINDLICHE KANAL-BILDWELT

Seit 27.09.2026 gilt kanalweit:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Kernregeln:
- animierte Biologie-Illustration statt Render-Look
- vereinfachte, fachlich erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Farbverlaeufe und subtile Schatten
- leichte Tiefe ohne 3D-CGI-Wirkung
- helle ruhige Hintergruende
- starke, klar getrennte biologische Farben
- wenige wichtige Elemente
- ein klarer biologischer Prozess oder Zusammenhang pro Bild
- normale Bilder **0–2 kurze deutsche Labels**, nur wenn wirklich noetig

Die Bildwelt muss fuer Muskel, Blut, Zellen, Nerven, Organe, Gewebe, Molekuele, Verdauung, Kreislauf, Immunsystem und weitere Biologie-Themen funktionieren.

## Informationsbudget – HARD RULE

Ein Bild soll innerhalb etwa einer Sekunde grob verstanden werden koennen.

Bevorzugt:
- 2–4 zentrale sichtbare Elemente
- 1 Hauptprozess / 1 Hauptaussage
- 0–2 Labels
- klare Blickfuehrung

Wenn mehr Inhalt noetig ist:
1. unwichtige Information weglassen, oder
2. ein weiteres Bild planen.

**Mehr einfache Bilder sind besser als ein ueberladenes Bild.**

## Cover – HARD RULE

Das separate YouTube-Cover (ab Video 009; ältere Videos unverändert) darf genau **einen sichtbaren Textblock** enthalten:

- nur den geplanten deutschen Titel / Hook
- bevorzugt 3–7 Woerter
- keine Anatomie-Labels
- keine Zusatzinfo
- keine Unterzeile
- keine Pfeiltexte

Wenn neben dem Titel irgendein weiterer sichtbarer Text erscheint: **FAIL → Flow-Bild neu generieren.**

## Sichtbarer Text – einzige erlaubte Quelle

Sichtbarer Text darf nur bereits Bestandteil eines final akzeptierten Google-Flow-Bildes sein.

Normale Bilder:
- 0–2 Labels, maximal 2
- Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- keine ganzen Saetze
- keine dekorativen Anfuehrungszeichen
- nur Begriffe, die fuer den aktuellen Lehrpunkt wirklich gebraucht werden

Nicht erlaubt als sichtbarer Text:
- interne Assetnamen
- `Bild_01`, `Bild_02`, `Bild 01`, `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Prompttitel
- Produktionshinweise
- interne IDs oder Nummerierungen

**Harte Regel:** Bildnummern und Szenennummern sind reine Produktionsmetadaten und duerfen niemals in einem finalen Bild oder Video sichtbar sein.

Wenn Flow eine interne Nummer, einen falschen Text oder unnoetigen Zusatztext sichtbar rendert, ist das Bild FAIL und wird neu erzeugt.

## Textkontrast – HARD RULE

Jeder sichtbare Text muss sofort lesbar sein.

- heller Hintergrund → **dunkle Schrift**
- dunkler Hintergrund → **helle Schrift**
- niemals helle Schrift auf hellem Hintergrund
- niemals dunkle Schrift auf dunklem Hintergrund
- Text bevorzugt in ruhiger negativer Flaeche platzieren
- bei unruhigem Hintergrund: Textposition verschieben statt schwachen Kontrast akzeptieren

Schwacher Kontrast / schwer lesbare Schrift = **FAIL → neu generieren**.

## Verbindliches Praesentationssystem: 100 % Vollbild-Illustration

Fuer alle neuen Videos gilt:

- die finalen Illustrationen bleiben vollformatig
- Remotion erzeugt **keinen sichtbaren Text**
- keine Zwischenueberschriften
- keine Key-Facts
- keine Summary-Zeilen
- keine Kapiteltexte
- keine Untertitel/Captions als Standard
- keine Callouts
- keine Textkarten
- keine UI-/Dashboard-/PowerPoint-Elemente
- keine sichtbaren Bild- oder Szenennummern

Remotion darf ausschliesslich:
- finales Audio einbinden
- Bilder nach der Voice-Timeline schneiden
- statische Frames zeigen
- leichte Push-/Pull-Bewegungen ausfuehren
- leichte Pans ausfuehren
- saubere Schnitte und sehr dezente nicht-textliche Uebergaenge erzeugen
- das finale Video rendern

`.intern/03_pipeline/overlay-plan.json` muss fuer neue Projekte deaktiviert bzw. leer bleiben.

Autoritativ fuer die technische Umsetzung:
`engine/PRESENTATION-OVERLAY-SYSTEM.md`

## Harte Stilverbote

- fotorealistischer Medizin-Look
- Medical-CGI / Anatomiesoftware-Look
- glossy Plastik-3D
- Pixar-/Feature-Film-Look als Standard
- Spielzeug-/Kinderbuch-Look
- sterile Corporate-Stock-Grafik
- ueberladene Infografik
- leere weisse Studioflaeche als Standard
- random Icons ohne Lehrfunktion
- mehr als 2 Labels in normalen Bildern
- Zusatzlabels auf dem Cover
- helle Schrift auf hellem Hintergrund
- dunkle Schrift auf dunklem Hintergrund
- zu viele Pfeile
- Gore / Horror / nasses Gewebe
- unnoetige Kleinststrukturen

## Bildtypen / Vielfalt

Erlaubt und erwuenscht sind stark unterschiedliche Kompositionen innerhalb derselben Bildwelt:
- Cutaway
- Querschnitt
- Makro-Nahaufnahme
- Zell-Innenansicht
- Prozess
- Transportweg
- Ursache → Wirkung
- Vorher / Nachher
- Vergleich
- Massstabswechsel Koerper → Organ → Gewebe → Zelle
- einfache Alltagsszene mit biologischem Fokus

Nicht alle Bilder duerfen wie ein zentriertes Einzelobjekt mit Labels aussehen.

## Prompt-Standard

Prompts fuer Flow bleiben kurz:
1. kanonischer Styleblock
2. konkrete Szene
3. sichtbarer Prozess
4. 0–2 deutsche Labels nur wenn wirklich noetig
5. explizite Kontrastregel fuer sichtbaren Text
6. kurze Negativregel

Prompt-Anweisungen auf Englisch, sichtbare Texte Deutsch.

Jeder Flow-Auftrag muss ausdruecklich sagen:
**Asset-/Bild-/Szenennummern sind nur Dateinamen/Produktionsmetadaten und duerfen NICHT im Bild erscheinen.**

Cover-Prompt muss zusaetzlich ausdruecklich sagen:
**Exactly one visible text block: the title only. No labels, no subtitle, no extra text.**

## Bildwelt ohne Vorlagen
Wie beim erfolgreichen Verdauungs-Longform 008 wird Google Flow **ausschließlich mit einem vollständigen Textprompt** geführt. Keine JPG-/Video-Frames, externe Stilbilder, Referenz-ZIPs oder Coverbilder als Bildvorlage an Flow geben. Die kanonische Beschreibung in `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`, der wortgleiche 008-Stilblock und konkret komponierte Szenen sind verbindlich. Die drei Cover werden per Text erzeugt; die Auswahl bestimmt nur das separate YouTube-Cover `03_export/COVER.png`, niemals die erste Videoszene `Bild_01`.
## Asset-Hygiene

- pro finaler Bildnummer genau ein retained Asset
- FAIL wird ersetzt, nicht dauerhaft gesammelt
- keine Bildduplikate fuer mehrere Szenen
- keine Luecken im finalen nummerierten Set
- Assetnummern bleiben ausschliesslich im Dateisystem und in Produktionsdaten

## Cover-Auswahl und Bildbatches – HARD RULE

Alle neuen normalen Videos starten die Flow-Medienphase nach `engine/FLOW-COVER-FIRST-WORKFLOW.md`: **erst 3 unterschiedliche Cover einzeln erzeugen und anzeigen → genau 1 Nutzerwahl abwarten → erst dann Bilder 01+ in Gruppen von maximal 5**. Der nach der Auswahl sofort folgende erste Fünferbatch benötigt keine zweite Start-Erlaubnis. Ein vollständiger einzelner Flow-Prompt darf alle 85 Szenen enthalten; Flow erzeugt trotzdem immer nur kleine Fünfergruppen, niemals alles in einem Bildgenerierungs-Aufruf. Der sichtbare Ordner enthält nur `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` und `bilder-zip/`. Interne QA liegt in `.intern/05_info`, entpackte Szenenbilder in `.intern/03_pipeline`. Image-IDs bleiben unsichtbare Metadaten; das gewählte Cover liegt separat in `03_export/COVER.png` und NICHT in der Videotimeline.

## Drei Phasen

### Phase 1 – Creative Director
Recherche → Claim-Check → Script → Mechanism Map → Satz-Visual-Plan → Szenenplan → Informationsbudget pruefen → Label-Plan → kurze Flow-Prompts.


## Phase-1-Handoff – ZWEI DIREKTLINKS ANTWORTEN (verbindlich)

**Sobald Phase 1 eines Videos nach tatsächlicher Erstellung und Prüfung erfolgreich abgeschlossen ist, MUSS die Antwort von ChatGPT oder einem anderen Chat-Agenten sofort diese zwei ANKLICKBAREN Links zum AKTUELLEN Video enthalten** (wie die zwei Aktionslinks im Beispiel des Nutzers):

- **Google-Flow-Prompt öffnen** → `https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/<VIDEOORDNER>/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
- **Voice-over-Skript öffnen** → `https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/<VIDEOORDNER>/01_script/script.txt`

`<VIDEOORDNER>` zwingend durch den tatsächlich gerade erstellten Videoordner ersetzen; echte Pfade/Dateiinhalte vor dem Link überprüfen. Niemals die Template-Platzhalter oder Links eines älteren Videos ausgeben. Links als Markdown-Klicklinks oder als zwei bedienbare Öffnen-Schaltflächen in der Chat-Antwort präsentieren, **nicht nur Dateipfade, einen allgemeinen Repository-Link oder eine Erklärung**. Beide Dateien öffnen die komplette Datei in GitHub und sind auch im mobilen Browser/Tablet zugänglich (bei privaten Repos mit GitHub-Anmeldung). Nutzer kann Text von dort 1:1 in Google Flow bzw. seine Voice-KI kopieren. Ein GitHub-Dateilink öffnet **nicht automatisch** Google Flow selbst; nichts anderes behaupten.

Die Übergabe darf KEINE zusätzliche Bestätigung abfragen und soll direkt nach dem Phase-1-Abschluss erfolgen. Keine weiteren sichtbaren Dateien im Videoordner erzeugen; `01_script/script.txt` und der eine Flow-TXT reichen. Wenn eine der Dateien fehlt, unvollständig oder ein Template ist, Phase 1 NICHT als fertig behaupten und keine falschen Links ausgeben. Nach erfolgreichem `python tools/validate_planning_v2.py youtube-videos/<VIDEOORDNER>` druckt der Validator exakt diese zwei Links als Handoff-Vorlage.

### Phase 2 – Google Flow
Bild fuer Bild erzeugen → Cover auf Titel-only pruefen → Labels und Textkontrast pruefen → Informationsdichte pruefen → sicherstellen, dass keine internen IDs/Nummern sichtbar sind → wissenschaftliche/visuelle QA → finale eindeutige Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio kanonisieren → Whisper → Timeline → Vollbild-Illustrationen + leichte Bildbewegung/Schnitt → Render → Final-QA.

**Phase 3 erzeugt keinerlei sichtbaren Text.**

## Autoritative Reihenfolge

1. aktuelle ausdrueckliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
4. `engine/VISIBLE-TEXT-STANDARD.md`
5. `PROJECT_STATE.md`
6. `config/channel.json`
7. aktuelle Engine-Regeln
8. aktuelles Projekt
9. historische Piloten nur als Lern-/Fehlerhistorie

## Google Flow – Sicherheits- und Richtlinienregel

Die gesamte Bildproduktion muss die Richtlinien des externen Bildgenerators einhalten. Für Object-Talk nur neutrale nicht-grafische, wissensbasierte Illustrationen ohne invasive Körperbilder oder medizinische Heilungsversprechen anfordern. Die erste Flow-Generierung ist nur der separat begrenzte **3-Cover-Schritt**, auch wenn eine einzige Promptdatei alle späteren Szenen enthält. Bei einer Richtlinienablehnung sofort stoppen, keine Filterumgehung und keine erfundenen Testergebnisse. Google Flow entscheidet selbst, ob ein Prompt angenommen wird; eine Garantie dafür gibt es nicht.

## Goldene Regel

**Cover nur Titel. Normale Bilder 0–2 kurze Labels. Ein Bild = eine Hauptidee. Hoher Textkontrast. Lieber mehr Bilder als mehr Text oder Details. Remotion erzeugt niemals Text.**
## Longform-008-Referenz (verbindlich fuer 6–7-Minuten-Serie)

`engine/LONGFORM-008-MASTERSTANDARD.md` ist die praktische Referenz fuer Promptgestalt, 77-Szenen-/13-Abschnitte-Planung, denselben Clean Animated Biology Illustration Look, ausfuehrlichen Antigravity-Workflow und vollstaendigen YouTube-Export. Bei neuen Themen wird nur fachlicher Inhalt ersetzt, keine komplett neue Stilrichtung oder Pipeline entworfen. Die Nutzeroberflaeche bleibt vereinfachtes `02_bildprompts/` mit EINER Flow-Promptdatei + `bilder-zip/`.


## Ausschließlich Textprompts – feste Entscheidung
Bei 008 wurden keine Bildvorlagen benutzt. Auch 009 und alle folgenden Longforms werden ohne visuelle Referenzbilder generiert. Nicht nach Stil-ZIPs, JPGs oder Uploads fragen. Konsistenz über klare unveränderte Stilbeschreibung, lebendige bildfüllende Biologieszenen und anschließende Sichtprüfung sicherstellen. Das gewählte Cover ist nur das **separate Thumbnail** und wird nicht als Image-to-Image-Vorlage oder erste Videoszene verwendet. Ein generatives Modell garantiert trotzdem keine pixelidentischen Stile.


## Neue 3-Ordner-Regel ab Video 009 (verbindlich)

Sichtbar nur `01_script/`, `02_bildprompts/`, `03_export/`. Technische Planungs- und Renderdateien unter verstecktem `.intern/`. Das Google-Flow-Cover ist ein **eigenes YouTube-Thumbnail `03_export/COVER.png` und KEINE Szene `Bild_01`**. Bild_01 ist sofort die erste normale biologische Illustration, nur die normal nummerierten Bilder in die Bilder-ZIP und das MP4. Nach Coverwahl Bilder 01–05, danach 06–10 usw. Untertitel aus echter Audioausrichtung nach `03_export/UNTERTITEL-MIT-ZEITEN.txt`. Alle Labels sollen häufig dann erscheinen, wenn sie einen Vorgang verständlicher machen, ansonsten textfrei; höchstens 2 kurze Wörter/Gruppen pro Bild. Keine Vorlagen-Uploads, keine Remotion-Textlayer, keine überfüllten Szenen.

## Zukunftsregel: sauberer Export – keine Migration bestehender Videos

Für alle **neu erstellten** Videoordner ist `engine/EXPORT-STANDARD.md` verbindlich. `03_export/` enthält **nach Fertigstellung nur** `VIDEO.mp4`, `COVER.png`, `CAPTION-YOUTUBE.txt`, `UNTERTITEL-MIT-ZEITEN.txt`. Keine weiteren Dateien oder Unterordner. Renderberichte, JSON, SRT, QA und Postmortem bleiben für die Automatisierung erhalten, aber nur verborgen unter `.intern/`. Das Cover wird separat ausgeliefert, nicht im Video. Zeitstempel müssen aus echter finaler Audio-Ausrichtung stammen. Bestehende Projekte (insbesondere 008 und 009) bleiben bei dieser Änderung **unangetastet**.
