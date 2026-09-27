# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap fuer ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `config/channel.json`
4. `config/video.json`
5. `THEMEN-GEHIRN.md`
6. `engine/README.md`
7. `engine/SCRIPT-STANDARD.md`
8. `engine/PLANNING-V2.md`
9. relevante Dateien des aktuellen YouTube-Projekts

Aktiver Testpilot steht in `PROJECT_STATE.md`.

## KRITISCH: VISUELLE BILDWELT IST NOCH NICHT FESTGELEGT

Alle frueheren kanalweiten Bildwelten wurden am 27.09.2026 bewusst entfernt.

Bis der Nutzer eine neue Bildwelt ausdruecklich auswaehlt und freigibt:
- keine alte 2.5D-/Soft-3D-Regel verwenden
- keine alte Premium-3D-/Feature-Animation-Regel verwenden
- keine alte semantische Farbpalette als Kanalstandard verwenden
- keine historische Pilot-Bildwelt kopieren
- keine historische Style-Reference als neue Kanalreferenz behandeln
- keine finale Flow-Bildproduktion starten

Historische Pilotdateien duerfen zur Analyse der damaligen Fehler gelesen werden, aber nicht als Stilautoritaet.

## Phase 1 – Creative Director

Darf:
- recherchieren und Fakten pruefen
- Mechanism Map erstellen
- Skript schreiben
- Satz-Visual-Plan und Szenen festlegen
- Label-Plan erstellen
- Metadaten schreiben

Muss:
- `engine/SCRIPT-STANDARD.md` einhalten
- Satz 1 als starken Neugier-Hook schreiben
- innerhalb der ersten ca. 15 Sekunden Hook → Wendung → Payoff liefern
- jeden Speech-Beat als echtes Erklaerbild planen
- Prozesse, Beziehungen, Ursache/Wirkung, Wege, Vergleiche und Kontext bevorzugen
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander zulassen
- fuer jedes Bild sichtbaren Erklaerwert und Unterschied zu Nachbarbildern definieren
- Flow-Anweisungen spaeter auf Englisch schreiben
- sichtbaren Text ausschliesslich auf Deutsch planen

## Phase 2 – Nutzer + Medienerzeugung

Aktuell PAUSIERT, bis die neue Bildwelt freigegeben ist.

Nach Freigabe wird ein neues Referenz- und Produktionssystem definiert. Alte Style-Regeln duerfen nicht automatisch wieder aktiviert werden.

## Phase 3 – Editor / Antigravity / Remotion

Remotion ist fuer:
- Audio
- Timing
- leichte Zoom-/Pan-Bewegungen
- Schnitte
- nicht-textliche Uebergaenge
- Rendering

Die genaue Text-/Overlay-Strategie wird zusammen mit der neuen Bildwelt erneut festgelegt. Historische Textregeln sind nicht automatisch Stilstandard.

## Timing

Finale Zeitbasis:
`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Standard:
- Voice 1.10x
- lange Pausen komprimieren
- kein Standbild ueber 7 Sekunden
- kein Bildasset doppelt verwenden

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

## Fail-closed

STOP bei:
- schwachem Script-Hook
- Script/Audio-Mismatch
- fehlenden/doppelten Bildern
- zu aehnlichen Szenen ohne neuen Lehrzweck
- drei oder mehr isolierten Objektportraits hintereinander
- wissenschaftlich falscher Kernaussage
- Versuch, vor der neuen Style-Freigabe eine alte Bildwelt zum Kanalstandard zu machen
