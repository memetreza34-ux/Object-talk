# Bildkontrolle des hochgeladenen Schlafvideos 009 – 10.10.2026

**Quellvideo:** `Object-Talk-009-Schlaf-YOUTUBE.mp4` aus Chat-Upload, 358,741 Sekunden (5:58,741), 1920×1080, 30 fps. Dies sind Sichtungsnotizen, nicht die Behauptung, das Binärvideo liege bereits in GitHub.

## Unterschied zum Verdauungsfilm 008 (Standbilder bei 00:10, 00:35, 01:05, ...)

008 zeichnet die einzelnen Prozesse meist mit breiten, leicht lesbaren, bildfüllenden organischen Schnittansichten. Die sichtbaren Labels sind oft entscheidend (z. B. Mageneingang, Verdauungsenzyme, Mikrovilli, Blutgefäß, Glukose, Aminosäuren, Ballaststoffe); pro Bild sind die Handlungen einfach und die Kamerastufen variieren.

009 enthält viele schöne weich illustrierte Organe/Signale, aber ein Teil der neuronalen Makrobilder ist sehr filigran und visuell überfrachtet, die Bedeutung ist ohne Erklärung schwer zu lesen. Beispiele: verzweigte Neuro-Szenen bei ca. 00:35, leuchtende Verbindungssignale bei ca. 01:35, komplexes Synapsen-/Proteinbild ca. 02:35, komplexere REM-Struktur bei ca. 05:05. Zwischen vielen Makros fehlen teilweise gut nachvollziehbare Körper-/Alltagsbezüge. Im Vergleich werden Begriffe nur selten im Bild benannt (alter Plan: 7/77 Szenen).

## Neue Regeln ab dieser Revision
- Cover = eigenes YouTube-Thumbnail unter `03_export/COVER.png`, nicht Bild_01 und nicht in der Timeline.
- Video beginnt mit einer echten, einfachen Erklärungsszene zum ersten Voice-Satz; 77 normale Szenen.
- Nur **ein** deutlicher biologischer Vorgang pro Illustration, 2–4 erkennbare Hauptbestandteile; höchstens 2 kurze Labels, wenn sie konkret helfen (aktueller 009-Plan: 33 Szenen mit mindestens einem Label, vorbehaltlich tatsächlicher Prüfung).
- Wechsel Alltag/Körper → Organ → Zellprozess → sichtbares Resultat; keine Serien leerer Gehirn-/Neuronen-Tafeln.
- Labels müssen genau an einer sichtbaren Struktur sitzen, korrekte deutsche Fachwörter, dunkel auf hell und hell auf dunkel. Keinerlei Remotion-Textlayer.
- Bei Überladung vereinfachen, vergrößern oder Bild in einen neuen, fachlich passenden Beat aufteilen.
- Der alte bereits gerenderte MP4-Upload beginnt mit dem Cover. **Die geänderte Regel ist erst beim nächsten echten Render gültig.** Ein GitHub-Promptcommit verändert bereits exportierte MP4-Dateien nicht.

## Export
Visible: `03_export/VIDEO.mp4`, `COVER.png`, `CAPTION-YOUTUBE.txt`, `UNTERTITEL-MIT-ZEITEN.txt`.
Keine erfundenen Untertitelzeiten: Das Render-Audio muss noch streng per Whisper/Worttimings ausgerichtet werden. `.intern/UNTERTITEL-YOUTUBE.srt` optional für maschinischen YouTube-Upload.
