# Visual Quality Gate

Vor dem finalen Render muss Antigravity jedes Bild, jede Overlay-Ebene und die gesamte Timeline prüfen.

## Pflichtprüfung pro Bild

- korrektes Seitenverhältnis 16:9
- ausreichende Auflösung
- richtige Dateinummer
- keine fehlenden oder doppelten Szenennummern
- keine sichtbaren KI-Artefakte an Augen, Händen, Armen, Lebensmitteln oder Organen
- keine ungewollten zusätzlichen Figuren
- anatomische Darstellung verständlich und plausibel
- deutsche Beschriftungen korrekt geschrieben
- Pfeile/Labels zeigen auf die richtige Struktur
- keine unnötigen Textblöcke
- keine fotorealistisch-grafischen oder ekligen medizinischen Darstellungen
- Look passt zur einheitlichen Object-Talk-/Inside-the-Body-Welt

## Pflichtprüfung der Overlays

Wenn `03_pipeline/overlay-plan.json` vorhanden ist:

- Vollbild bleibt dominant; kein PowerPoint-/Dashboard-Look
- Overlay-Text ist auf Deutsch
- Überschrift möglichst 2–5 Wörter, maximal ungefähr 6 Wörter
- keine kompletten Voice-over-Sätze als eingebrannter Text
- keine unnötige Wiederholung von sichtbaren Labels
- kein Overlay verdeckt das entscheidende Organ, die relevante Zellstruktur oder die zentrale Bildaussage
- keine Anime-/Comic-/Meme-Typografie oder hektische Popup-Animation
- Überschrift/Schlüsselwort erscheint nur, wenn es Orientierung oder Verständnis verbessert
- Overlay-Timing liegt innerhalb der passenden Szene
- Text bleibt maximal zwei Zeilen
- Flow-Gibberish wird nicht durch zusätzlichen falschen Text verstärkt; wichtige Begriffe werden stattdessen sauber in Remotion gesetzt

## Pflichtprüfung der Timeline

- Szene 01 beginnt bei 0 Sekunden
- keine Lücken zwischen Szenen
- keine Überlappungen
- letztes Bild endet mit dem Voiceover
- Zielrhythmus überwiegend 3–6 Sekunden pro Bild
- über 8 Sekunden nur mit bewusstem Grund
- lange Standzeiten werden nicht nur durch Zoom/Pan kaschiert
- wichtige neue Aussage bekommt das passende Bild
- Bildwechsel erfolgen nicht mitten in einer zusammengehörigen Aussage, wenn das vermeidbar ist

## Pflichtprüfung des fertigen Videos

- normales Kanalvideo mindestens 5:00 Minuten; dokumentierter Testmodus darf die in `test-mode.json` definierte Ausnahme verwenden
- Audio vollständig und verständlich
- Bilder synchron zur Aussage
- Zooms/Schwenks ruhig und sauber
- Overlays ruhig, lesbar und gezielt
- keine schwarzen Frames
- keine falschen Bildreihenfolgen
- kein Bild fehlt
- 1920×1080, 30 fps
- `final-video.mp4` erfolgreich erzeugt
- `YouTube-Caption.md` vollständig
- optional `subtitles.srt` vorhanden

Wenn eine Pflichtprüfung fehlschlägt, darf nicht einfach final exportiert werden. Der Fehler wird zuerst behoben.
