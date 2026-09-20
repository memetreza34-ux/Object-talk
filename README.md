# Object-Talk

Zentrale Produktionsbasis für den YouTube-Kanal **Object-Talk / FoodSpricht**.

## Exaktes Ziel

Wir produzieren **lange YouTube-Erklärvideos über Ernährung, Gesundheit und Biologie**.

Jedes Video muss:

- **mindestens 5 Minuten lang** sein
- visuell **nur aus generierten Standbildern** bestehen
- ein klar abgegrenztes Thema verständlich erklären
- fachlich sinnvoll und für Zuschauer leicht nachvollziehbar aufgebaut sein
- visuell durchgehend in derselben wiedererkennbaren 3D-Bildwelt bleiben
- Object-Talk-Szenen und biologische Inside-the-Body-Szenen sinnvoll miteinander verbinden
- nur die wichtigsten biologischen Strukturen zeigen und beschriften
- wichtige Beschriftungen **auf Deutsch** enthalten
- keine unnötigen Wiederholungen früherer Videos enthalten

## Themen

ChatGPT wählt geeignete Themen aus den Bereichen:

- Ernährung
- Gesundheit
- menschlicher Körper
- Verdauung
- Gehirn und Nervensystem
- Zellen und Zellbiologie
- Blut und Kreislauf
- Immunsystem
- Muskeln und Knochen
- Stoffwechsel
- Schlaf
- Hormone
- Vitamine und Mineralstoffe
- Lebensmittel und ihre Wirkung im Körper

Themen sollen genug Inhalt für **mindestens 5 Minuten** bieten und sich visuell gut mit Bildern erklären lassen.

Vor jeder neuen Produktion muss zuerst das [Themen-Gehirn](THEMEN-GEHIRN.md) geprüft werden. Bereits verwendete oder zu ähnliche Themen dürfen nicht erneut ausgewählt werden.

Nach Auswahl oder Fertigstellung eines Videos wird das Thema dort eingetragen, damit wir langfristig keine Videos doppelt produzieren.

## Visuelles Kernprinzip

Die Bildwelt verbindet zwei Ebenen:

1. **Viral Object-Talk** – sprechende Lebensmittel und Objekte mit großen Augen, klarer Mimik und starker Persönlichkeit.
2. **Inside-the-Body** – verständliche, kindgerechte 3D-Darstellungen von Organen, Zellen, Blut, Nervensystem und biologischen Prozessen.

Beide Ebenen müssen wie **dieselbe Animationsserie** wirken: semi-realistisch, klar animiert, warm, hochwertig und nicht fotorealistisch.

## Produktionsprinzip

Ein Video wird grundsätzlich so entwickelt:

1. Themen-Gehirn prüfen
2. neues, nicht doppelt vorhandenes Thema auswählen
3. recherchieren und Fakten prüfen
4. Thema in sinnvolle Kapitel gliedern
5. Sprechertext für mindestens 5 Minuten entwickeln
6. alle benötigten Standbilder planen
7. Google Flow erzeugt jedes Bild einzeln und nummeriert es als `Bild_01`, `Bild_02` usw.
8. Nutzer erzeugt das finale Voiceover aus `script.txt`
9. `faster-whisper` analysiert das fertige Voiceover und erstellt Wort-Zeitstempel
10. die Textanker der Szenen werden automatisch in echte Sekundenwerte umgerechnet
11. Antigravity/Renderer setzt Bilder und Voiceover exakt synchron zusammen
12. dezente Zooms, Schwenks und Übergänge erzeugen Bewegung aus den Standbildern
13. Video, YouTube-Caption und Untertitel werden exportiert
14. Thema im Themen-Gehirn als produziert markieren

## Repository-Bereiche

- `THEMEN-GEHIRN.md` – verhindert doppelte Themen
- `bildwelt/` – feste visuelle Welt und Fach-Bildwelten
- `youtube-videos/` – alle einzelnen Longform-Produktionen
- `engine/` – globale Produktions-, Timing- und Qualitätsregeln
- `tools/` – Whisper-/Timeline-Hilfstools für Phase 3

## Technischer Kern

Die Synchronisierung folgt:

```text
Script
  -> Voice-KI
  -> finales Voiceover
  -> faster-whisper Wort-Zeitstempel
  -> scene-map.json
  -> timeline.json
  -> Antigravity / Renderer
  -> final-video.mp4
```

Dadurch werden Bildwechsel nicht anhand geschätzter Zeitpunkte gesetzt, sondern anhand des tatsächlich gesprochenen Audios.

## Wichtige Regeln

Siehe:

- [Produktionsregeln](engine/PRODUKTIONSREGELN.md)
- [Whisper-Synchronisierung](engine/SYNC-WHISPER.md)
- [Visual Quality Gate](engine/VISUAL-QUALITY-GATE.md)
- [YouTube-Video-Struktur](youtube-videos/README.md)

## Bildwelten

- [Gehirn & Nervensystem](bildwelt/gehirn.md)

Weitere Bildwelten folgen für Verdauung, Blutkreislauf, Immunsystem, Zellen, Muskeln, Knochen und Ernährung.
