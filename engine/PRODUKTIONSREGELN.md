# Produktionsregeln – Object-Talk Longform

Diese Regeln gelten für **jedes** lange YouTube-Video im Repository.

## 1. Videolänge

- Mindestlänge final: **5:00 Minuten**.
- Zielbereich für normale Videos: **5:30–8:00 Minuten**.
- Ein Thema wird nur länger, wenn der zusätzliche Inhalt echten Mehrwert bietet.
- Nach Erzeugung des Voiceovers wird die echte Audiodauer geprüft. Ist sie unter 5:00 Minuten, wird das Skript erweitert und das Audio neu erzeugt.

## 2. Skript

- `script.txt` enthält ausschließlich den gesprochenen Fließtext.
- Keine Regieanweisungen, keine Szenennummern, keine Zeitcodes, keine Klammerhinweise.
- Das Skript muss 1:1 in eine Voice-KI kopierbar sein.
- Ziel für ein normales 5–7-Minuten-Video: ungefähr **850–1100 deutsche Wörter**, abhängig von Sprechtempo und Thema.
- Kurze klare Sätze; schwierige Begriffe sofort einfach erklären.
- Erst erklären, dann vertiefen. Keine unnötigen Fachbegriffe.

## 3. Bildrhythmus

Da die Videos ausschließlich aus Standbildern bestehen, darf ein Bild nicht zu lange stehen.

Richtwerte:

- normale Szene: **6–10 Sekunden**
- komplexe biologische Erklärung: **4–8 Sekunden**
- ruhige Übersicht: **8–12 Sekunden**
- kein Bild länger als **12 Sekunden**, außer es gibt einen begründeten Sonderfall mit deutlicher Kamerabewegung
- Cover-/Hook-Szene `Bild_01`: etwa **4–7 Sekunden**

Grobe Zielmenge:

- 5 Minuten: ca. **35–50 Bilder**
- 7 Minuten: ca. **45–65 Bilder**
- 10 Minuten: ca. **65–90 Bilder**

Die tatsächliche Bildanzahl richtet sich nach dem Inhalt, nicht starr nach einer Quote.

## 4. Bildformat

- Format: **16:9**
- Zielauflösung: mindestens **1920 × 1080**
- keine vertikalen Reel-Kompositionen
- zentrale Motive nicht direkt an den Rand setzen
- genügend Raum für leichte Zooms und Schwenks lassen

## 5. Szenennummerierung

Jede visuelle Szene besitzt exakt eine Nummer und ein zugehöriges Bild:

- Szene 01 = `Bild_01`
- Szene 02 = `Bild_02`
- Szene 03 = `Bild_03`
- usw.

Keine Nummer darf fehlen oder doppelt vorkommen.

`Bild_01` ist immer die **Cover-/Hook-Szene** und gleichzeitig die visuelle Basis für das YouTube-Cover/Thumbnail.

## 6. Visuelle Ebenen

Jedes Video kann zwischen zwei Ebenen wechseln:

### A – Viral Object-Talk
Sprechende Lebensmittel oder passende Objekte mit:
- großen ausdrucksstarken Augen
- klarer Mimik
- kleinen Armen/Beinen, wenn sinnvoll
- starker, einfacher Pose
- semi-realistischen Materialien
- klar animiertem Look

### B – Inside-the-Body
Verständliche Darstellungen von:
- Organen
- Blutgefäßen
- Zellen
- Nervenzellen
- Molekülen
- Stoffwechselprozessen
- Verdauung
- Immunsystem

Beide Ebenen müssen wie dieselbe hochwertige 3D-Animationswelt wirken.

## 7. Beschriftungen

- wichtige Lerninhalte werden auf **Deutsch** beschriftet
- nur Begriffe, die zum Verständnis wirklich helfen
- klare Pfeile oder Verbindungslinien
- maximal wenige Labels gleichzeitig
- keine unnötigen Fließtexte im Bild
- Rechtschreibung muss korrekt sein

Beispiele:

- Zellkern
- Mitochondrium
- Dünndarm
- rote Blutkörperchen
- Nervenzelle

## 8. Kamerabewegung auf Standbildern

Antigravity darf aus den Standbildern Bewegung erzeugen durch:

- langsamen Push-in
- langsamen Pull-out
- leichte horizontale oder vertikale Schwenks
- Fokuswechsel durch Crop/Zoom
- sehr dezente Parallax-ähnliche Bewegung, sofern technisch sauber

Verboten:

- hektische Zooms
- dauerndes Wackeln
- starke Verzerrung
- künstliches Bewegen anatomischer Strukturen, wenn nur ein Standbild vorliegt

## 9. Übergänge

Standard ist ein sauberer harter Schnitt oder ein sehr kurzer weicher Übergang.

Keine auffälligen Effekt-Transitions ohne inhaltlichen Grund.

## 10. Synchronisierung

Die endgültige Szenenzeit wird **nicht geschätzt**.

Nach Erstellung des Voiceovers wird das Audio mit Whisper/faster-whisper transkribiert. Die Wort-Zeitstempel werden anschließend mit den von ChatGPT definierten Textankern der Szenen verbunden.

Dadurch erhält jede Szene echte Start- und Endzeiten in Sekunden.

Siehe `SYNC-WHISPER.md`.

## 11. Audio

- Voiceover ist die Hauptzeitbasis des Videos.
- Audio wird nicht beschleunigt oder verlangsamt, nur damit Bilder passen.
- Optional sehr leise Hintergrundmusik, wenn sie die Sprache nicht stört.
- Soundeffekte nur sparsam und passend.
- Ziel für finalen Export: verständliche Sprache, keine Übersteuerung.

## 12. Export

Standard:

- MP4
- 1920 × 1080
- 30 fps
- H.264
- AAC-Audio
- Voiceover vollständig enthalten
- finaler Dateiname: `final-video.mp4`

Zusätzlich kann aus Whisper `subtitles.srt` für YouTube exportiert werden.

## 13. Gesundheit und Biologie

- medizinische/biologische Aussagen müssen vor Produktion geprüft werden
- keine erfundenen Wirkungen von Lebensmitteln
- keine Diagnose oder individuelle Behandlungsempfehlung
- komplexe Prozesse vereinfachen, aber nicht fachlich verfälschen
- Recherche und Prüfnotizen kommen in `05_info/Recherche.md`

## 14. Qualitätsregel

Ein Video wird erst exportiert, wenn:

- Audio mindestens 5 Minuten lang ist
- jedes Bild vorhanden ist
- Bildnummern vollständig sind
- jede Szene einen Audio-Zeitraum besitzt
- keine sichtbaren KI-Fehler oder falschen Beschriftungen vorhanden sind
- keine langen unbeabsichtigten Standphasen bestehen
- das Thema im Themen-Gehirn korrekt eingetragen ist
