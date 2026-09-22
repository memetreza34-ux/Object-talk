# Visual Quality Gate

Vor dem finalen Render muss Antigravity jedes Bild, jede Overlay-Ebene und die gesamte Timeline prüfen.

## Pflichtprüfung pro Bild

- korrektes Seitenverhältnis 16:9
- ausreichende Auflösung
- richtige Dateinummer
- keine fehlenden oder doppelten Szenennummern
- keine sichtbaren schweren KI-Artefakte
- keine ungewollten zusätzlichen Figuren
- anatomische Darstellung verständlich und plausibel
- **stark stilisierte hochwertige 3D-Animationsfilm-Welt**, kein Drift in Fotorealismus
- weiche, klare Formensprache und konsistente Materialien/Lichtwelt
- wichtigste sichtbare Strukturen/Prozesse sinnvoll beschriftet
- normalerweise 1–3 kurze deutsche Labels
- deutsche Beschriftungen korrekt geschrieben
- Pfeile/Labels zeigen eindeutig auf die richtige Struktur
- kein englischer sichtbarer Text
- keine unnötigen Textblöcke
- keine eklige medizinische Realistik, kein Gore

## Pflichtprüfung Bild_01

`Bild_01` muss zusätzlich bestehen:

- funktioniert als Cover und erster Shot
- Thema auf einen Blick verständlich
- enthält eine kurze starke deutsche Hook-Zeile zum Thema
- Hook ist korrekt geschrieben und nicht irreführend
- Hook bleibt auch als Cover lesbar
- definiert klar den gewünschten Renderstil für alle späteren Bilder
- spätere Bilder wirken sichtbar wie dieselbe Welt

## Pflichtprüfung der Overlays

Wenn `03_pipeline/overlay-plan.json` vorhanden ist:

- Vollbild bleibt dominant; kein PowerPoint-/Dashboard-Look
- Overlay-Text ist auf Deutsch
- keine unnötige Wiederholung bereits sichtbarer Flow-Labels
- kein zweiter Cover-Hook über Bild_01
- Überschrift möglichst 2–5 Wörter, maximal ungefähr 6 Wörter
- keine kompletten Voice-over-Sätze als eingebrannter Text
- kein Overlay verdeckt das entscheidende Organ oder die zentrale Bildaussage
- keine Anime-/Comic-/Meme-Typografie oder hektische Popup-Animation
- Overlay-Timing liegt innerhalb der passenden Szene
- Text bleibt maximal zwei Zeilen

## Pflichtprüfung der Timeline

- Szene 01 beginnt bei 0 Sekunden
- keine Lücken zwischen Szenen
- keine Überlappungen
- letztes Bild endet mit dem Voiceover
- Zielrhythmus überwiegend 3–6 Sekunden pro Bild
- über 8 Sekunden nur mit bewusstem Grund
- lange Standzeiten werden nicht nur durch Zoom/Pan kaschiert
- wichtige neue Aussage bekommt das passende Bild
- Bildwechsel erfolgen nicht mitten in einer zusammengehörigen Aussage, wenn vermeidbar

## Pflichtprüfung des fertigen Videos

- normales Kanalvideo mindestens 5:00 Minuten; dokumentierter Testmodus darf die definierte Ausnahme verwenden
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

Wenn eine Pflichtprüfung fehlschlägt, darf nicht einfach final exportiert werden. Der Fehler wird zuerst behoben.
