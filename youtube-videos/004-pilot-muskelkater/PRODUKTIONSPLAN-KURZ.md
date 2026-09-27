# Produktionsplan – Pilot 004 Muskelkater

## Thema
**Warum kommt Muskelkater so spaet?**

## Ziel
End-to-End-Test mit der neuen freigegebenen Kanalbildwelt:
- starke Frage-Hook im ersten Satz
- klare animierte Biologie-Illustrationen
- einfache statt komplexe Bilder
- wichtige Strukturen direkt auf Deutsch beschriften
- mehr anschauliche Prozess-/Vergleichsbilder
- keine fast identischen Muskelbilder hintereinander

## Umfang
- 35 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- ca. 380 Woerter Voiceover
- Voice-Verarbeitung 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- erwartete Endlaenge ungefähr 2:05–2:30, abhängig vom Roh-TTS

## 1. Voice
`01_script/VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die Voice-KI uebernehmen.

Phase 3 verarbeitet das Roh-Audio mit `tools/prepare_audio.py --speed 1.10`.
`final-voiceover.wav` ist die einzige Timing-Quelle.

## 2. Verbindliche Bildwelt

**Clean Animated Biology Illustration**

Autoritativ:
- `../../bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `../../bildwelt/FLOW-STYLE-BLOCK.txt`

Fuer jedes Bild:
- vereinfachte erkennbare Biologie
- saubere Illustrationsformen und Konturen
- weiche Verlaeufe, subtile Schatten und leichte Tiefe
- heller ruhiger Hintergrund
- wenige wichtige Elemente
- ein dominanter Prozess/Zusammenhang
- normalerweise 1–3 kurze deutsche Labels

Nicht verwenden:
- alte 2.5D-/Soft-3D-Regeln
- Premium-3D/Feature-Animation
- Medical-CGI
- glossy Plastik-3D
- ueberladene Infografik

## 3. Google Flow

1. jedes Bild einzeln erzeugen
2. den kurzen kanonischen Styleblock verwenden
3. Szene und Prozess konkret beschreiben
4. nur die fuer die Szene geplanten 1–3 deutschen Labels erzeugen
5. falsche Schreibweise oder falsche Label-Zuordnung regenerieren/korrigieren
6. pro Bildnummer genau 1 finales Bild behalten
7. keine sichtbaren Bildnummern, Dateinamen, Prompttitel oder Asset-IDs
8. keine alte Pilot-Style-Reference verwenden
9. Cover-Hook nur auf Bild_01
10. `Bild_01` nicht automatisch als Master-Stilanker fuer alle Folgebilder verwenden

Eine `assets/channel/STYLE_REFERENCE.png` wird erst genutzt, wenn spaeter ein einzelnes sauberes Referenzbild vom Nutzer freigegeben wurde.

## 4. Prompt-Schema

Prompts bewusst kurz:

```text
[CANONICAL STYLE BLOCK]
[SCENE]
[PROCESS]
Add only these German labels: "...", "...", "..."
No clutter, no realistic tissue, no unnecessary details or extra text.
```

## 5. Visuelle Vielfalt

- mindestens ca. 60% der normalen Frames zeigen Prozess, Beziehung, Route, Ursache/Wirkung, Vergleich, Vorher/Nachher oder Kontextaenderung
- Cutaway, Querschnitt, Makro, Muskel-/Gewebeansicht, Nerven-/Signalansicht und Vergleich abwechseln
- maximal zwei isolierte Objektbilder hintereinander
- Nachbarszenen unterscheiden sich in mindestens zwei Punkten
- kein Bild wird doppelt verwendet
- kein Standbild laenger als 7 Sekunden
- nicht jedes Bild als zentriertes Objekt mit drei Labels bauen

## 6. Komplexitaet

Pro Bild bevorzugt:
- 2–5 zentrale Elemente
- 1 Hauptprozess
- 1–3 Labels

Wenn mehr Inhalt noetig ist: neues Bild statt mehr Kleinteile.

## 7. Remotion

Remotion darf standardmaessig nur:
- Timing
- Audio
- Bildwechsel
- dezente Push/Pull/Pan-Bewegung
- saubere Schnitte/Ueberblendungen

Sichtbare Labels kommen aus Flow.

## 8. Erfolgskriterien

- Frage-Hook funktioniert sofort
- kein Schulbuch-Einstieg
- neue Bildwelt klar erkennbar
- Biologie schnell verstaendlich
- Bilder nicht ueberladen
- Labels kurz, korrekt und eindeutig
- keine alten 2.5D-/3D-Stilreste
- keine doppelten oder nahezu identischen Bilder
- Laktat-Mythos korrekt erklaert
- Muskelkater nicht als Trainingsqualitaets- oder Wachstums-Messer dargestellt
- 1.10x Voice und keine langen Pausen
- Abschlussbild ist neu und kein Cover-Recycling
