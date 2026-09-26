# Produktionsplan – Pilot 004 Muskelkater

## Thema
**Warum kommt Muskelkater so spät?**

## Ziel
Nächster End-to-End-Test nach Pilot 003 mit den neuen harten Regeln:
- stärkere Frage-Hook im ersten Satz
- sichtbarer Text ausschließlich aus Google Flow
- Remotion = motion-only, kein Text
- mehr anschauliche Prozess-/Vergleichsbilder
- keine fast identischen Muskelbilder hintereinander

## Umfang
- 35 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- ca. 380 Wörter Voiceover
- Voice-Verarbeitung 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- erwartete Endlänge ungefähr 2:05–2:30, abhängig vom Roh-TTS

## 1. Voice
`01_script/VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die Voice-KI übernehmen.

Phase 3 verarbeitet das Roh-Audio mit `tools/prepare_audio.py --speed 1.10`.
`final-voiceover.wav` ist die einzige Timing-Quelle.

## 2. Google Flow
1. textfreie `EPISODE_STYLE_REFERENCE.png` mit `STYLE-REFERENCE-PROMPT.txt` erzeugen.
2. nur Bild_01 als Cover erzeugen; bis zu 3 klar verschiedene Varianten erlaubt.
3. genau 1 Cover auswählen und alle anderen verwerfen.
4. Bild_02–Bild_35 jeweils einzeln mit der textfreien Style-Referenz erzeugen.
5. texttragendes Cover niemals als Follow-up-Referenz anhängen.
6. pro normale Bildnummer genau 1 finales Bild behalten.
7. keine sichtbaren Bildnummern, Dateinamen, Prompttitel oder Asset-IDs.
8. sichtbarer Text ausschließlich aus `label-plan.json`.
9. Cover-Hook „Warum kommt Muskelkater so spät?“ nur auf Bild_01.
10. falsche Flow-Schrift in Flow regenerieren/korrigieren; kein Remotion-Text-Fallback.

## 3. Bildwelt
- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- ca. 80% animierte Illustration / 20% Soft-3D-Tiefe / 0% Medical-CGI
- hell, klar, nicht kindisch, nicht realistisch-medizinisch
- Muskel = Coral/Salmon/Rot-Orange
- Signale/Botenstoffe = Cyan/Blau
- Erholung = Teal/Soft-Blau
- Warnung = gedämpftes Orange-Rot

## 4. Visuelle Vielfalt
- mindestens ca. 60% der normalen Frames zeigen Prozess, Beziehung, Route, Ursache/Wirkung, Vergleich, Vorher/Nachher oder Kontextänderung
- maximal zwei isolierte Objektbilder hintereinander
- Nachbarszenen unterscheiden sich in mindestens zwei Punkten: Komposition, Maßstab, Subjekt, Richtung, Zustand oder Visual-Typ
- wichtige Mechanismusbilder dürfen einen sinnvollen Zusatzdetailpunkt zeigen
- kein Bild wird doppelt verwendet
- kein Standbild länger als 7 Sekunden

## 5. Remotion
Remotion darf nur:
- Timing
- Audio
- Bildwechsel
- dezente Push/Pull/Pan-Bewegung
- saubere Schnitte/Überblendungen

Remotion darf NICHT:
- Text
- Labels
- Kapitelüberschriften
- Keywords
- Callouts
- Captions
- UI-Overlays

`03_pipeline/overlay-plan.json` bleibt DISABLED und leer.

## 6. Erfolgskriterien
- Frage-Hook funktioniert sofort
- überraschende Wendung innerhalb der ersten Sekunden
- kein Schulbuch-Einstieg
- Cover-Hook nur einmal
- keine doppelten oder nahezu identischen Bilder
- sichtbarer Text vollständig aus Flow
- 0 Remotion-Textelemente
- Laktat-Mythos korrekt erklärt
- Muskelkater nicht als Trainingsqualitäts- oder Wachstums-Messer dargestellt
- 1.10x Voice und keine langen Pausen
- Abschlussbild ist neu und kein Cover-Recycling