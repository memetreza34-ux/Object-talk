# OBERSTE PRODUKTIONSPRIORITÄT: Nach jedem Video besser werden

**Qualitätsverbesserung hat Vorrang vor dem schnellen Start des nächsten Films.** Aktuelle ausdrückliche Nutzeranweisungen und wissenschaftliche Korrektheit haben weiterhin Vorrang.

## Verbindliche Lernschleife nach JEDEM echten Finalvideo, auch Testvideos

1. **Echtes Ergebnis prüfen:** finale MP4, gewähltes separates Cover, Voice-Ton, Bildfolge, Bild/Voice-Match, wissenschaftliche Aussagen, biologische Verständlichkeit, Labels, Hook/Schluss, Export und Nutzerfeedback. YouTube-CTR/Retention nur berücksichtigen, wenn echte Daten vorliegen. Kein erfundenes Review.
2. **Kritisch auseinandernehmen:** mindestens 3 konkrete Schwachstellen mit realer Zeitstelle/Bildnummer und Ursache im Skript, Flow-Prompt, Bildwelt, Voice, Schnitt oder Workflow; auch 2 Stärken nennen. Nicht „besser machen“ ohne Beispiel.
3. **Priorisieren:** wissenschaftliche Fehler, fehlende Inhalte und falsche Beschriftungen zuerst; dann Verständlichkeit, visuelle Vielfalt, Cover, Timing, Zuschauerbindung und Effizienz. Schwere, Häufigkeit, Wiederholungsrisiko und Zuschauerwirkung entscheiden.
4. **Tatsächliche Korrekturen:** 2–5 wirksame Änderungen an den **globalen** Regeln, der Vorlage oder den Tools umsetzen, soweit die Erkenntnisse auf andere Videos übertragbar sind. Eine Liste im Postmortem allein genügt nicht. Keine alten fertigen Videoordner ungefragt verändern.
5. **Nachweis:** für jede Änderung vorheriges Problem, Ursache, konkrete geänderte Datei und Test/Sichtprüfung mit Ergebnis dokumentieren. Bei fehlendem Test oder fehlender MP4 nicht „PASS“ bzw. „verbessert“ behaupten.
6. **Vererbung:** `.intern/05_info/improvement-review.json` des fertigen Films ausfüllen, mit `python tools/improvement_loop.py register youtube-videos/VIDEOORDNER` registrieren und so `engine/IMPROVEMENT-LEDGER.json` aktualisieren. Beim nächsten Video muss `.intern/05_info/improvement-applied.json` die permanenten und zuletzt gelernten Regeln konkret nachweisbar übernehmen. Der Phase-1-Validator prüft dies.
7. **Vergleich:** Fehler- und Regenerierungszahlen, Bildverständlichkeit, wiederholte Kompositionen, Label-Fehler, Voice-Sync, Zuschauerfeedback und – sofern vorhanden – echte Retention/CTR mit vorher vergleichen. Qualitative Einschätzungen von tatsächlichen Messungen unterscheiden. Nicht automatisch Steigerungen behaupten.

## Die zehn Prüffelder

Wissenschaft; Hook/Erzählstruktur; Bildverständlichkeit; Konsistenz & Abwechslung; Prompt/Flow-Fehlerrate; deutsche Labels/Textkontrast; Voice/Pausen; Bild-Ton-Timing; Cover/Uploadpaket; User-/YouTube-Feedback.

## Harte Regeln bleiben bestehen

- Google Flow: ein textbasierter Prompt ohne Vorlagen; drei Cover, Nutzerwahl, Fünfergruppen.
- Cover separat, keine Szene `Bild_01`. Normale Bilder: eine klare biologische Hauptaussage, maximal 2 sinnvolle kurze Labels.
- Nur drei sichtbare Arbeitsordner und nach Fertigstellung vier sichtbare Exportdateien. Alle Lernberichte und technischen Tests in `.intern/`.
- **Kein Hintergrund-Automatismus:** Erst wenn ein echtes fertiges Video vorliegt und geprüft wird, kann eine fundierte neue Lernrunde registriert werden.
- **Historische Videos bis 009** werden durch diese neue Regel nicht rückwirkend verändert oder automatisch als vollständig geprüft bezeichnet.

## Technische Befehle

```bash
# Nach Ansehen des echten finalen Videos und nach echten Repo-Korrekturen:
python tools/improvement_loop.py register youtube-videos/VIDEOORDNER

# Vor Freigabe von Phase 1 des NÄCHSTEN Videos:
python tools/improvement_loop.py check-next youtube-videos/NEUES-VIDEO
python tools/validate_planning_v2.py youtube-videos/NEUES-VIDEO
```

Fehlt ein Review, muss offen darauf hingewiesen werden, statt Verbesserung zu behaupten. Den Plan zur Nachbesserung dokumentieren und den neuen Film nicht allein als Fortschritt darstellen.

## Dokumentiertes aktuelles Lernsignal aus Video 010

Gezielte Sichtung des hochgeladenen `VIDEO.mp4` anhand 21 Zeitstichproben, **keine vollständige lückenlose Sichtung**: Nutzer fand Skript gut, Bildstil grundsätzlich passend, Illustrationserklärwert und Vielfalt aber zu schwach; zu viele ganze Menschen, Küche und Essen als rein dekorativer Hintergrund. Deshalb wurden vor Video 011 der globale Style-/Plan-/Promptmix, zusätzliche konkrete Art-Direction-Beispiele und ein neuer visueller Storyboard-Gate entwickelt. Primär ist das ein Fehler in der Bildplanung, nicht im Voice-Skript. Belege: `engine/VIDEO-010-VISUAL-FEEDBACK.md`, `bildwelt/ILLUSTRATION-FIRST-SCENE-EXAMPLES.md`. Die neue Qualität gilt erst als verifiziert, wenn die echten Bilder und das nächste fertige Video visuell verglichen wurden. Eine umfassende Postmortem-Registrierung von 010 wurde durch diese Stichproben **nicht** ersetzt.
