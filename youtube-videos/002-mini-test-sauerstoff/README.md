# 002 – Mini-Test Sauerstoff

Zweck: kleines internes Beispiel für einen sehr kurzen Produktions- und Stiltest.

## Status

**Der Mini-Test wird aktuell übersprungen.**

Der aktive echte Kleinpilot ist stattdessen:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Dieser Ordner bleibt nur als internes Beispiel/Template im Repo bestehen und ist aktuell nicht der nächste Produktionsschritt.

## Eckdaten
- 10 Bilder
- Ziel ca. 50 Sekunden
- akzeptabler Bereich 40–70 Sekunden
- stark stilisierte 3D-Animationsfilm-Welt
- Bild_01 = Cover + Hook + Master Style Frame
- Flow-Prompts auf Englisch
- sichtbarer Text nur Deutsch
- Produktion in 5er-Blöcken

## Dateien
- `01_script/VOICEOVER-ZUM-KOPIEREN.txt`
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
- `03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt`
- `04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt`
- `05_info/phase1-scenes.json`
- `05_info/test-mode.json`

## Ablauf, falls später genutzt
1. Voiceover erzeugen.
2. In Flow zuerst nur Bild_01 erzeugen und freigeben.
3. Bild_02–06 einzeln mit Bild_01 als Referenz erzeugen.
4. Bild_07–10 einzeln mit Bild_01 als Referenz erzeugen.
5. Fehlerhafte Bilder im Recovery-Pass neu erzeugen.
6. Audio + Bilder ins Projekt legen.
7. Antigravity-/Remotion-Pipeline ausführen.
8. Finales Testvideo rendern und prüfen.

Dieser Test zählt nicht als veröffentlichtes Kanalthema.