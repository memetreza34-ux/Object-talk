# Verbindliche Phasen-Gates – Object-Talk

Priorität vor neuer Produktion: `PROJECT_CONTRACT.md` und `engine/CONTINUOUS-IMPROVEMENT.md`; für Export `engine/EXPORT-STANDARD.md`, für Sichtbarkeit `engine/VISIBLE-TEXT-STANDARD.md`.

## GATE 0 – Verbesserung vor der NÄCHSTEN Phase 1

- nach jedem **tatsächlich fertig gerenderten** vorherigen Video echtes Finale, Cover und Audio anschauen und `.intern/05_info/improvement-review.json` vollständig ausfüllen
- Probleme mit Zeit-/Bildbeleg und Ursachen analysieren, zwei bis fünf globale Korrekturen umsetzen und testen, im zentralen Ledger registrieren
- beim neuen Video `.intern/05_info/improvement-applied.json` ausfüllen: permanente und zuletzt registrierte Lessons in konkret sichtbare Verbesserungen überführen
- `python tools/improvement_loop.py check-next VIDEOORDNER` muss bestehen; wird automatisch durch den Phase-1-Validator aufgerufen
- Historische Projekte bis einschließlich 009 bleiben ohne rückwirkende Pflichtdateien und werden nicht als geprüft ausgegeben

## PHASE 1 – Recherche und Produktion vorbereiten

- Faktenquellen, Claim-Matrix und Script prüfen; neugierig machender Hook, klarer Aufbau, korrekte Gesundheitstipps
- vollständiges `01_script/script.txt`, EINE `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
- Mechanism-, Szenen-, Satz-Visual- und Labelpläne nur intern unter `.intern/05_info/`
- erste Videoszene `Bild_01` ist **normale Erklärungsszene**; separates Cover zeigt exakt einen lesbaren Titel und ist nicht im Video
- einfache, in 1–2 Sekunden verständliche biologisch korrekte Illustrationen: eine Hauptidee, normalerweise 2–4 wichtige Formen und höchstens zwei relevante deutsche Labels
- Projekt und alle vererbten Verbesserungen bestehen `python tools/validate_planning_v2.py VIDEOORDNER`
- **Nach PASS zwei anklickbare Direktlinks** in der Chat-Antwort: Flow-Prompt und Sprecher-Script
- bei FAIL keine Freigabe als Phase-1-fertig

## FLOW-COVER-GATE

- genau drei echte eigenständige Covervarianten erstellen und anzeigen; Nutzer wählt 1/2/3
- das gewählte Cover ist **ausschließlich** `03_export/COVER.png`, nicht `Bild_01`, nicht in der Bilder-ZIP oder der Remotion-Timeline
- ohne weitere Startfrage normale `Bild_01`–`Bild_05` und danach fünf Szenen je Batch
- ein textbasierter kompletter Google-Flow-Prompt, keine verlangten Bild-Referenz-Uploads
- interne Produktionsnummern erscheinen NIEMALS auf den Bildern

## PHASE 2 – Bilder und Audio

- echte Flow-Bilder vor Freigabe sichten; falsche Anatomy, Stilbrüche, unlesbare/unnötige Labels, zu komplizierte Strukturen oder Duplikate ersetzen
- wissenschaftliche Genauigkeit, Flow-Bildwelt, Prozessverständnis, Bild-Unterschiede, deutsche korrekte 0–2 Labels und Kontrast PASS
- Bilder-ZIP vollständig; erstes normales Asset `Bild_01`, separates Cover nicht enthalten
- Voice-Datei vollständig, final verarbeitet und Script↔Voice korrekt
- `python tools/validate_planning_v2.py VIDEOORDNER --phase2` muss bestehen, bevor gerendert wird

## PHASE 3 – Video, Export und Qualitätsfreigabe

- echtes final verarbeitetes Voiceover nach Whisper-Wortzeiten ausrichten
- normale Videobilder mit ruhigen Schnitten/leichter Kamerabewegung, maximal 7 Sekunden pro Standbild, keine erzwungenen Wiederholungen
- Remotion erzeugt **keinen** sichtbaren Text, Cover nicht im Video
- fertig gerendertes MP4 1920×1080, 30fps, vollständiger Ton, keine schwarzen Lücken
- `03_export/` enthält nach Abschluss **genau** `VIDEO.mp4`, `COVER.png`, `CAPTION-YOUTUBE.txt`, `UNTERTITEL-MIT-ZEITEN.txt`
- echte Audiotimestamps (keine Schätzungen); technisch notwendige SRT, Bericht, Scorecard und Postmortem bleiben in `.intern/`
- Quality-Scorecard >= 8.0/10 und harte QA-Blocker bestanden, **erst dann** YouTube-ready behaupten

## GATE 4 – Ohne Abschlussreview kein nachweisbarer Fortschritt

Nach dem echten Video Final-Review wie Gate 0 durchführen, `tools/improvement_loop.py register` bestehen lassen und die Lehren in die nächste Produktion übernehmen. **Ein Repo-Commit allein beweist keine Videobildqualität.** Für echte Verbesserungsbehauptungen tatsächliche Ergebnisse prüfen; unbekannte Ergebnisse ehrlich als noch nicht geprüft deklarieren.

FAIL blockiert die jeweils folgende Freigabe. WARN darf nur begründet und dokumentiert weiterlaufen.
