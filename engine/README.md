# Engine

Dieser Ordner enthält die **globalen Produktionsregeln und technischen Hilfen** für alle langen Object-Talk-YouTube-Videos.

## Aufgabe des Engines

Der Engine sorgt dafür, dass jedes Video gleich aufgebaut wird und Antigravity nicht jedes Mal neu raten muss.

Er übernimmt bzw. definiert:

- Mindestlänge und Bildrhythmus
- Audio-Synchronisierung
- Whisper-Transkription mit Wort-Zeitstempeln
- Zuordnung von `Bild_XX` zu exakten Audio-Zeiten
- 16:9-Longform-Regeln
- Kamera-Bewegungen auf Standbildern
- Exportregeln
- Qualitätskontrolle

## Wichtige Dateien

- `PRODUKTIONSREGELN.md` – feste Regeln für alle Videos
- `SYNC-WHISPER.md` – exakte Audio-/Bild-Synchronisierung
- `VISUAL-QUALITY-GATE.md` – Prüfung vor dem finalen Export

## Grundprinzip

Antigravity ist der ausführende Agent. Die technische Render-Pipeline soll möglichst reproduzierbar sein:

`Script -> Voice-Audio -> Whisper-Wortzeiten -> Szenen-Timeline -> nummerierte Bilder -> Render -> Export`

Die Bilder selbst werden weiterhin über den Google-Flow-Agenten erzeugt.