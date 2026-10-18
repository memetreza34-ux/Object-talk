# Object-Talk / Lebenslogik – Aktueller Projektstand

Letzte Aktualisierung: 18.10.2026

## AKTIVE PRODUKTION – NEUAUFLAGEN 011 UND 012 (Nutzerwunsch 18.10.2026)

Der Nutzer wünscht deutlich unterhaltsamere Skripte, passendere Bilder sowie bessere Titel und Cover. Die alten Videos 008 und 010 bleiben unverändert. Die Neuauflagen sind eigene Projekte nach den neuen Regeln (`engine/KANAL-ANALYSE-2026-10.md`).

| Projekt | Titel | Cover-Text | Bilder | Wörter | Status |
|---|---|---|---:|---:|---|
| `youtube-videos/011-longform-hunger-v2/` | Warum du kurz nach dem Essen schon wieder Hunger hast | Hunger trotz Essen? | 94 | 1095 | Phase 1 PASS, Medien ausstehend |
| `youtube-videos/012-longform-verdauung-v2/` | Die Reise einer Pizza durch deinen Körper | Wohin verschwindet sie? | 99 | 1144 | Phase 1 PASS, Medien ausstehend |

**Offen und bewusst benannt:** Die formale Lernrunde für das gerenderte Video 010 (`tools/improvement_loop.py register`) ist nicht registriert, weil die MP4 nicht im Repository liegt und keine vollständige Sichtung stattfand. Phase 1 von 011/012 entstand auf ausdrücklichen Nutzerauftrag; die Lehren stammen aus `engine/KANAL-ANALYSE-2026-10.md` (Skript- und Planungsanalyse, 21 Nutzer-Standbilder zu 010) und sind als dauerhafte Lessons im Ledger hinterlegt. Vor der Bilderzeugung wurden beide Pakete unabhängig gegengeprüft; 39 bestätigte Punkte sind behoben.

- Quelle für alles: `.intern/05_info/storyboard-source.json` → `python tools/build_phase1_package.py`.
- Geschätzte Länge nach 1,10x-Voice: ca. 6:15–7:00 pro Video (an 010 geeicht, nicht gemessen).
- Beide Videos verweisen am Ende aufeinander (Endscreen verlinken).
- Nächster Schritt je Video: Flow-Prompt einfügen → drei Cover → Wahl → Bilder in Fünfergruppen → Voice → `tools/prepare_phase3.py` → Render → echte Sichtung → `improvement-review.json`.

**Handoff-Links 011:**
[Google-Flow-Prompt öffnen](https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/011-longform-hunger-v2/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt) · [Voice-over-Skript öffnen](https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/011-longform-hunger-v2/01_script/script.txt)

**Handoff-Links 012:**
[Google-Flow-Prompt öffnen](https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/012-longform-verdauung-v2/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt) · [Voice-over-Skript öffnen](https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/012-longform-verdauung-v2/01_script/script.txt)

(Die Links funktionieren, sobald der Branch nach `main` übernommen wurde.)

## Vorherige Produktion – VIDEO 010 (historisch, unverändert)

`youtube-videos/010-longform-hunger/`, gerendert und vom Nutzer hochgeladen (368,9 s). Bekannte Schwächen siehe `engine/KANAL-ANALYSE-2026-10.md`. Die Planungsdateien enthalten 24 ungültige Kamerabewegungen. Ein erneuter Render von 010 ist nicht vorgesehen, stattdessen 011.

## Bisherige Produktionsnotizen / Video 009

`youtube-videos/009-longform-schlaf/`

**Thema:** Was passiert in deinem Körper, während du schläfst?

**Status: PHASE 1 VORBEREITET / MEDIEN AUSSTEHEND; 008-PRODUKTIONSSTRUKTUR 1:1 ÜBERNOMMEN.** Es gibt noch keine finale Voice, keine akzeptierten Flow-Bilder und kein YouTube-MP4 im neuen Projekt.

## Referenz – Video 008 Verdauung

Das freigegebene erste Longform-Video 008 ist für 009 das strukturelle und visuelle Vorbild: 77 eindeutige Bilder, 13 Mechanismusabschnitte, dieselbe Flow-Promptgliederung/Zeichensprache, derselbe ausführliche Antigravity-Auftrag und Export/QA. Nur Thema, Script und biologische Motive wurden geändert. Eine einzige Flow-Promptdatei plus bilder-zip/ bleibt Nutzeroberfläche. Ein tatsächlicher neuer Flow-/MP4-Render ist noch NICHT geprüft.

## Ziel für Video 009

- Laufzeit: **6:00–7:00 Minuten** nach echter Audioverarbeitung bestätigen.
- Script: **986 Wörter**, 77 einzigartige semantische Bilder.
- 16:9, 1920×1080, 30fps; finales Voice 1.10×.
- Cover nur Titel `Was macht dein Körper nachts?` und zeitlich kurz.
- Starke Hook → Schlafdruck/innere Uhr → Schlafstadien → Tiefschlaf/Körper → Gedächtnis → Immunsystem → REM/Träume → Zyklen → Schluss.
- Jeder Frame: eine Hauptaussage, höchstens zwei kurze Labels, Kontrast Pflicht, keine Mehrfachtafeln.
- Mehr Licht-/Farbvariation (Dämmerung, Dunkelblau, warme Körperfarben, Morgenlicht).
- 0 sichtbarer Remotion-Text und 0 sichtbare Produktionsnummern.
- keine Bildduplikate; nie länger als 7 Sekunden pro Bild.

## Recherche und Dateien

- NIH/NHLBI, NICHD, CDC als Quellen.
- `01_script/script.txt` und kopierbarer Voice-Text.
- `05_info/Recherche.md`, Claim-Matrix, Mechanism Map, 77 Szenen und 13 thematische Mechanismus-Indizes (wie 008).
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` für 77 Bilder mit deutscher Text-Whitelist.
- `03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt`, deaktivierter Overlayplan.
- `04_export/` mit Videoziel, individueller Caption, YouTube-SRT und komplettem zeitcodiertem Script.
- SRT und Zeit-Script bleiben bis zur finalen `timeline.json` ausdrücklich PENDING.

## Vorherige Produktion 008

`youtube-videos/008-longform-verdauung/` ist das vorherige Longform-Thema. Der Nutzer hat einen gerenderten Film zur Besprechung bereitgestellt. Im GitHub-Repo ist die finale Master-MP4 samt echten Zeitdaten noch nicht als geprüftes Exportpaket abgelegt. Nicht fälschlich als repo-seitig YouTube-ready deklarieren.

## Nächster Produktionsschritt (historisch, Video 009 – aktuell gilt die 011/012-Tabelle oben)

1. `python tools/validate_planning_v2.py youtube-videos/009-longform-schlaf`
2. Finale Voice aufnehmen/generieren und Laufzeit prüfen.
3. Alle 77 Flow-Bilder erstellen, einzeln wissenschaftlich und visuell reviewen.
4. `python tools/validate_planning_v2.py youtube-videos/009-longform-schlaf --phase2`
5. `python tools/prepare_phase3.py youtube-videos/009-longform-schlaf`.
6. MP4 rendern, komplette Sicht-/Tonprüfung, Untertitel aus echter Timeline, Export-QA.

## Historie

Pilotphase 000–007 abgeschlossen; Bildwelt: **Clean Animated Biology Illustration**.

## Produktionsentscheidung: keine Bildvorlagen (10.10.2026)
Wie beim erfolgreichen Verdauungsvideo 008 wird Google Flow **ausschließlich mit einem vollständigen Textprompt** bedient. Keine externen Stilbilder, 008-Frame-ZIP-Dateien oder Cover-als-Referenz. Erst genau drei separate Cover erstellen, Auswahl abwarten, dann Szenen 02–77 in Fünfergruppen. Die bekannte organisch-illustrative Bildwelt ist im Prompt positiv beschrieben. Bild-QA bleibt Pflicht; eine exakte Reproduktion ist mit generativer KI nicht garantiert.

## Tablet-Handoff nach Phase 1 (dauerhaft; Beispiel-Links unten stammen aus Video 009, aktuelle Links stehen oben bei 011/012)

Bei jeder abgeschlossenen Phase 1 direkt in der Chat-Antwort zwei anklickbare Dateilinks ausgeben, niemals nur einen Sammellink oder Ordnerpfade:

**Google-Flow-Prompt öffnen:** https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/009-longform-schlaf/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt

**Voice-over-Skript öffnen:** https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/009-longform-schlaf/01_script/script.txt

Diese URLs gelten NUR für das damalige Video 009. Bei späteren Videos immer den zugehörigen Projektordner einsetzen. Als Markdown-Klicklinks oder funktionierende Öffnen-Schaltflächen in der Antwort präsentieren. Die Dateien sind Text zum direkten Kopieren auf Tablet/PC; Login kann erforderlich sein. Details: `AGENTS.md`, `PROJECT_CONTRACT.md`.


## Verbindliches neues Bildfeedback (14.10.2026, ab Video 011)

Video 010 („Warum du nach dem Essen so schnell wieder Hunger hast“) wurde durch den Nutzer beim Skript gelobt; die Bildwelt passt grundsätzlich, aber die Illustrationen sind noch zu oft alltägliche Personen-/Küchen-/Markt-Szenen. Aus 21 gezielten Standbildern: erklärende Magen-/Darm-/Signal-Illustrationen sind anschaulicher als die wiederholten ganzen Menschen. **Kein Umschreiben des guten Skripts oder rückwirkender Exportumbau.** Globaler Fix in `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`, `bildwelt/ILLUSTRATION-FIRST-SCENE-EXAMPLES.md` und `engine/PLANNING-V2.md`: deutlich mehr Makros, anatomische Cutaways, biologisch erklärte Vergleiche, schönere detailbewusste organische Formen, mehr harmonisch kräftige Farben, deutlich weniger menschenzentrierte Bilder. Ab Video 011 verlangt die technische Phase-1-Prüfung passende Visual-Kategorien und einen nachvollziehbaren Mix (siehe `tools/visual_storyboard_gate.py`). Tatsächliche Qualitätssteigerung der generierten Folgebilder ist noch nicht nachgewiesen und wird im nächsten Finalvideo geprüft.
