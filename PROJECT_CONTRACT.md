# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widerspruechen gilt zuerst eine ausdrueckliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert deutschsprachige YouTube-Erklaervideos zu Ernaehrung, Gesundheit und Biologie.

Harte Grundregeln:
- normale Kanalvideos mindestens 5:00 Minuten, sofern der Nutzer nicht bewusst einen kuerzeren Testpilot bestellt
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- generierte Standbilder bleiben die visuelle Basis
- hohe visuelle Dichte statt langer statischer Bildhaltezeiten
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wichtige sichtbare Dinge knapp auf Deutsch beschriften
- wissenschaftlich relevante Aussagen pruefen

## Script-Standard – Neugier zuerst

Der Einstieg darf nicht wie ein Schulbuch beginnen.

Die ersten 5–10 Sekunden muessen sofort Neugier erzeugen. Bevorzugte Hook-Muster:
- direkte Frage an den Zuschauer, bevorzugt im Stil `Hast du dich schon mal gefragt, warum ...?`
- ueberraschende Aussage
- Mythos / verbreitete Fehlannahme
- Alltagsraetsel
- klarer Kontrast wie `Du denkst X – tatsaechlich passiert Y.`

Verbindlicher Opening-Aufbau:
1. **Hook** – Frage, ueberraschende Aussage, Mythos oder Kontrast
2. **unerwartete Antwort / Wendung** – direkt danach, ohne lange Einleitung
3. **Payoff-Versprechen** – der Zuschauer versteht innerhalb der ersten ca. 15 Sekunden, was er gleich lernen wird

Verbotene / schwache Einstiege:
- `In diesem Video ...`
- `Heute erklaeren wir ...`
- `X ist ein komplexer Prozess ...`
- reine Definition ohne Neugier
- lange Kontextpassage vor der eigentlichen Frage

Schreibstil:
- gesprochen statt geschrieben
- kurze aktive Saetze
- konkrete Bilder und Verben
- keine unnötige Fachsprache
- keine leeren Fuellsaetze
- wichtige Abschnitte duerfen mit einer kurzen Frage, einem Kontrast, einer Konsequenz oder einem Mythos neu Interesse erzeugen
- der Hook wird nicht wortwoertlich in jedem Kapitel wiederholt

Autoritativ:

```text
engine/SCRIPT-STANDARD.md
```

## Audio-/Pacing-Standard

Sofern der Nutzer fuer ein Video nichts anderes vorgibt:
- finales Voiceover wird mit **1.10x** verarbeitet
- lange TTS-Pausen werden vor Whisper/Timeline komprimiert
- kurze natuerliche Mikro-Pausen bleiben erhalten
- das VERARBEITETE `final-voiceover.wav` ist die einzige Timing-Quelle
- Whisper und Timeline duerfen niemals auf dem Roh-TTS basieren, wenn spaeter ein anderes Tempo gerendert wird
- stille Voice-Pausen >=0.50s sind im finalen Explainer-Output nicht akzeptiert
- Video wird nicht kuenstlich durch Pausen oder lange Standbild-Holds auf eine Zielzeit gestreckt

Autoritativ:

```text
tools/prepare_audio.py
tools/build_timeline.py
tools/qa_final.py
```

## Visuelle Dichte / Bildwechsel

Der Kanal darf nicht wie eine Diashow wirken.

Verbindlich:
- ein Standbild normalerweise etwa 3–6 Sekunden
- harte Standardobergrenze: **7.0 Sekunden pro Bild**
- wenn ein Sprachabschnitt laenger ist oder zwei echte Lehrbeats enthaelt, wird er in mehrere NEUE eindeutige Szenen geteilt
- jede neue Szene erhaelt eine neue fortlaufende Bildnummer
- dasselbe Bild darf nicht zweimal verwendet werden, um Zeit zu fuellen
- lieber mehr eindeutige Bilder als ein Bild 10–20 Sekunden stehen lassen

Informationsdichte:
- ein DOMINANTER Lehrpunkt pro Bild
- ca. **20–35 %** wichtiger Mechanismus-/Zusammenfassungsbilder duerfen EINEN zusaetzlichen sinnvollen Detailpunkt enthalten
- wenn mehr Information noetig ist: neues Bild statt Textwand oder ueberladener Infografik
- mindestens etwa **60 %** der normalen Explainerbilder sollen einen Prozess, eine Beziehung, Ursache/Wirkung, Vorher/Nachher, Weg, Vergleich oder Kontext sichtbar machen
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander; danach bevorzugt ein Prozess-, Weg-, Ursache/Wirkung-, Vergleichs- oder Kontextbild
- gleiche Uebersichtskomposition spaeter nicht einfach wiederholen; wiederkehrende Konzepte brauchen neuen Massstab, Zustand, Richtung oder visuellen Zweck
- zwei benachbarte Szenen muessen sich in mindestens zwei Punkten unterscheiden: Kameramassstab, Layout, Hauptmotiv, Prozessrichtung, Kontext oder Visual-Typ

## Zwei verbindliche Bildmodi

### A. Object-Talk Character Mode

Fuer sprechende Lebensmittel und Alltagsgegenstaende:
- hochwertiger stilisierter 3D-Character-Look
- klare Objektform
- expressive Augen / Brauen / Mund
- freundlich, modern, animiert
- nicht fotorealistisch

### B. Educational Explainer Mode

Fuer Biologie, Koerper, Organe, Zellen und Prozesse:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:
**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Autoritative Details:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
```

## Educational Explainer – harte Stilregeln

Verbindlich:
- klar animiert / illustriert, nicht realistisch
- weiche gerundete vereinfachte Formen
- matte bis leicht satinierte Oberflaechen
- weiche Farbverlaeufe
- subtile Schatten und leichte Tiefenstaffelung
- ruhige helle Hintergruende
- dominanter Lehrpunkt sofort lesbar
- wenige Objekte
- visuelle Klarheit vor Detailgrad
- vereinfachte, aber erkennbare Anatomie

Harte Stilverbote:
- Photorealismus
- Medical-CGI / Anatomiesoftware
- nasses realistisches Gewebe
- Mikroskop-Fotorealismus
- kosmische / Weltraum-artige Welten
- Sci-Fi-Tunnel / Neon-Labor
- dunkle violette Mikrowelt als Standard
- Anatomie-Mannequins / Torso-Modelle
- Corporate-Stock-3D
- billiger Toy-Look
- Gore / Horror
- ueberladene Infografik

## Menschen-Regel

Der Kanal ist kein Presenter-Kanal.
Menschen nur, wenn fachlich noetig, dann stark vereinfacht, gesichtslos und sekundaer.
Biologische Strukturen werden nicht automatisch personifiziert.

## Reference-First ist Pflicht – normale Szenen nur mit textfreier Referenz

Fuer normale Szenen gilt diese Referenzreihenfolge:
1. `assets/channel/STYLE_REFERENCE.png` – textfrei
2. projektspezifische `EPISODE_STYLE_REFERENCE.png` – textfrei
3. wiederkehrende Objekt-/Character-Referenzen
4. konkreter Szenenprompt

`Bild_01.png` ist ein Cover mit Hook und darf **nicht** als Stilreferenz fuer `Bild_02+` angehaengt werden.

Wenn keine kanalweite STYLE_REFERENCE vorhanden ist, wird vor dem Cover eine textfreie Episode-Style-Referenz erzeugt. Sie ist kein finales nummeriertes Szenenbild.

Referenzen liefern Stil, Farben, Material- und Formensprache – nicht Text oder Cover-Komposition.

## Cover-Hook ist exklusiv

Die exakte Cover-Hook darf nur auf `Bild_01` sichtbar sein.

Fuer `Bild_02` bis `Bild_NN` ist die Cover-Hook immer verboten, auch:
- als erneute grosse Ueberschrift
- als Kapiteltrenner
- als dekorativer Hintergrundtext
- als nahezu identische Kurzfassung
- wenn Flow sie aus einer Referenz kopiert

Kapiteltexte oder kurze Labels duerfen nur verwendet werden, wenn sie explizit im Flow-Textplan stehen und klar anders als die Cover-Hook sind.

## Sichtbarer Text kommt aus Google Flow – nicht aus Remotion

Ab sofort gilt fuer diesen Kanal hart:
- sichtbarer Text wird in Google Flow erzeugt und gegen `label-plan.json` geprueft
- Cover-Titel kommt aus Google Flow
- normale Labels kommen aus Google Flow
- Kapiteltexte, falls geplant, kommen ebenfalls aus Google Flow
- **Remotion darf keinen sichtbaren Text erzeugen**
- keine Remotion-Kapitelueberschriften
- keine Remotion-Keywords
- keine Remotion-Callouts
- keine Remotion-Label-Fallbacks

Wenn Flow einen Text falsch schreibt:
1. Bild in Flow neu erzeugen oder dort korrigieren
2. erst akzeptieren, wenn Text stimmt
3. nicht mit Remotion nachtraeglich reparieren

Remotion ist nur fuer Timing, leichte Kamerabewegung, Schnitt, Audio und nicht-textliche Uebergaenge zustaendig.

`overlay-plan.json` muss fuer neue Projekte leer sein bzw. keine Text-Overlays enthalten.

## Asset-Hygiene / keine doppelten Bilder

Finale Bildsets sind kanonisch und eindeutig.

Cover-Ausnahme:
- nur `Bild_01` darf vor Nutzerwahl bis zu 3 Varianten haben
- Nutzer waehlt genau 1
- alle nicht gewaehlten Covervarianten werden geloescht/verworfen
- im finalen Set existiert genau ein `Bild_01.png`

Normale Szenen:
- pro Bildnummer genau ein retained asset
- ein FAIL wird durch eine neue Version derselben Nummer ERSETZT
- FAIL-Version nicht zusaetzlich sammeln
- keine `_A`, `_B`, `v2`, `final2`, `copy`, `new`
- dasselbe Bildasset darf nicht fuer zwei Szenen benutzt werden

Finaler Ordner:
- jede erwartete `Bild_XX.png` exakt einmal
- keine Luecken
- keine Duplikate
- keine Temp-/FAIL-Dateien
- Style-Referenzen liegen ausserhalb des finalen nummerierten Sets

## Sichtbarer Text ist Whitelist-basiert

### Cover / Bild_01
- sichtbar ist nur die exakte geplante deutsche Hook
- keine Anatomie-Zusatzlabels
- Cover ohne Hook = FAIL

### Normale Bilder
- sichtbar sind nur die exakt fuer diese Szene in `label-plan.json` geplanten Labels oder explizit geplante einzigartige Flow-Kapitelueberschrift
- 0 Eintraege bedeutet: kein sichtbares Wort
- 0–2 Labels bevorzugt, maximal 3 bei echtem Bedarf
- die Cover-Hook darf niemals in der normalen Whitelist stehen

Immer verboten:
- Cover-Hook nach Bild_01
- `Bild_19`, `Bild 19`, `IMAGE 19`, `Scene 19`
- Dateinamen / Asset-IDs
- Prompt-Ueberschriften wie `BILD_12 – O2 BINDET`
- erfundene Szenentitel
- englischer sichtbarer Text
- KI-Gibberish
- zusaetzliche nicht geplante Anatomie-Labels

JEDES sichtbare Wort ausserhalb der Whitelist = Hard FAIL.

## Google-Flow-Ablauf

### A – Style-Referenz
1. `STYLE_REFERENCE.png` anhaengen, falls vorhanden
2. falls nicht vorhanden: textfreie `EPISODE_STYLE_REFERENCE.png` erzeugen
3. Referenz auf Stil/Klarheit pruefen

### B – Cover
1. ausschliesslich `Bild_01` erzeugen
2. bis zu 3 Cover-Richtungen erlaubt
3. Nutzer waehlt eine
4. unselektierte Covervarianten entfernen
5. genau ein `Bild_01.png` behalten
6. Cover danach NICHT als normale Szenenreferenz verwenden

### C – Produktion
Nach Freigabe:
- jede Szene einzeln erzeugen
- textfreie Style-Referenz wirklich anhaengen
- genau ein retained asset pro normale Bildnummer
- semantische Farben stabil halten
- sichtbaren Text gegen Whitelist pruefen
- Cover-Hook nach Bild_01 explizit pruefen und verbieten
- bei langem Speech-Beat neue Bildnummer planen statt Bild zu wiederholen
- bei zu vielen aehnlichen Einzelobjektbildern neue Prozess-/Beziehungsdarstellung planen
- vor jedem Bild pruefen, wie es sich sichtbar vom vorherigen UND naechsten Bild unterscheidet

### D – Recovery
Fehlerhafte Bilder behalten ihre Nummer. Recovery bedeutet Ersetzen, nicht Sammeln.

## Echte Bild-QA

`image-review.json` darf erst nach Sichtpruefung des tatsaechlichen Bildes aktualisiert werden.

Pflicht:
- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- visual_novelty >= 8/10
- information_value >= 8/10
- visible_text_whitelist = PASS
- cover_hook_isolated = PASS
- no_visible_asset_id = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10

## Drei Phasen

### Phase 1 – Creative Director
Erstellt Recherche, Claim-Check, Script, Szenenplan, Label-Plan, Flow-Prompts und Metadaten.

Muss zusaetzlich:
- neugiergetriebenen Hook nach `engine/SCRIPT-STANDARD.md` schreiben
- Opening auf Hook → Wendung → Payoff aufbauen
- lange oder mehrteilige Speech-Beats in genuegend eindeutige Bilder teilen
- Sequenzen aus drei oder mehr isolierten Einzelobjektbildern vermeiden
- fuer jede Szene einen sichtbaren Erklaerwert definieren
- alle sichtbaren Texte bereits fuer Google Flow planen
- keine spaeteren Remotion-Texte einplanen

### Phase 2 – Nutzer + Voice-KI + Google Flow
1. rohes Voiceover erzeugen
2. textfreie Style-Referenz bereitstellen
3. Bild_01 erzeugen / eine Variante auswaehlen / Alternativen loeschen
4. restliche Bilder einzeln auf Basis der textfreien Referenz erzeugen
5. echte Einzelbild-QA inkl. Hook-Leak-, Novelty-, Information-Value- und Text-Check
6. finale ZIP mit eindeutigen Bildnummern

### Phase 3 – Antigravity + Tools + Remotion
1. Voice auf 1.10x + Pausenkompression kanonisieren
2. Bilder importieren und validieren
3. Whisper auf finalem verarbeiteten Audio
4. Timeline aus echten Worttimings erzeugen
5. FAIL wenn ein Bild >7s stehen muesste
6. Remotion nur fuer Timing, Zoom/Pan, Schnitt, Audio und nicht-textliche Uebergaenge verwenden
7. FAIL wenn ein Remotion-Textoverlay geplant oder gerendert wird
8. Final-QA inkl. Voice-Speed, Pausen-Audit und sichtbarem Hook-Audit

## Autoritative Reihenfolge

1. aktuelle ausdrueckliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `PROJECT_STATE.md`
4. `config/*.json`
5. `engine/*.md`
6. `bildwelt/*.md`
7. `THEMEN-GEHIRN.md`
8. projektspezifische Dateien

## Fail-closed

Stoppen bei:
- Script startet ohne starken Neugier-Hook
- Script/Audio stimmen nicht ueberein
- Voice nicht mit kanonischem Tempo/Pausenprozess vorbereitet
- stille Voice-Pause >=0.50s im finalen verarbeiteten Voiceover
- einzelnes Standbild >7s
- dasselbe Bildasset mehrfach in der Timeline
- fehlenden oder doppelten finalen Bildnummern
- Cover-Hook sichtbar nach Bild_01
- texttragendem Cover als Folge-Szenenreferenz
- sichtbarem Asset-/Szenennamen oder Prompt-Titel
- sichtbarem Text ausserhalb der Whitelist
- **jedem Remotion-Textoverlay**
- unselektierten Covervarianten im finalen Set
- zu vielen nahezu identischen Szenen ohne neuen Lehrzweck
- mehr als zwei isolierten Einzelobjektbildern hintereinander
- falschem Seitenverhaeltnis
- unklarer Szenenzuordnung
- wissenschaftlich ungeklaerten Kernbehauptungen
- sichtbar falscher biologischer Darstellung
- behaupteter Referenznutzung ohne angehaengte Referenz
- Photorealismus / Medical-CGI-Stil-Drift
