# Object-Talk – Project State

Letzte Aktualisierung: 23.09.2026

## Aktiver Kurztest

Aktiv ist jetzt:

```text
youtube-videos/002-mini-test-sauerstoff/
```

Zweck: ein sehr kleiner kompletter Testfilm, bevor ein längeres Video gebaut wird.

Eckdaten:
- ca. 50 Sekunden Ziel
- akzeptabler Bereich 40–70 Sekunden
- genau 10 Bilder
- Test zählt nicht als veröffentlichtes Kanalthema
- Bild_01 = Cover + erster Shot + Master Style Frame
- Produktion danach in 5er-Blöcken: Bild_02–06, dann Bild_07–10

Der frühere `001-pilot-sauerstoff-im-blut` bleibt vollständig im Repo und dient als längerer 28-Bilder-Pilot.

## Freigegebene Bildwelt

Verbindlich ist:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

Kanal-DNA:
- stark stilisierte hochwertige 3D-Animationsfilm-Welt
- klar animiert statt fotorealistisch
- weiche gerundete Formen
- warme Creme-/Apricot-/Amber-/Orange-Grundwelt
- tiefe Rot-/Burgundertöne für Blut und Gefäße
- blass Cyan/Türkis als O2-Kontrast
- glatte hochwertige Materialien
- starke filmische Tiefenwirkung
- vereinfachte, erkennbare Anatomie
- kein Anime, kein Comic, kein medizinischer Fotorealismus, kein Gore

Ein sauber exportiertes kanalweites `assets/channel/STYLE_REFERENCE.png` fehlt noch. Bis dahin gelten die schriftliche Bildwelt und Bild_01 der jeweiligen Episode als Referenz.

## Prompt- und Textregel

- Flow-Anweisungen: Englisch
- sichtbarer Text im Bild: nur Deutsch
- wichtige Dinge kurz beschriften
- normalerweise 1–3 Labels pro Bild
- keine langen Textblöcke
- falsches oder englisches Label = Regeneration oder sauberer Remotion-Fallback

## 002 – vorhandene Dateien

Voice:
```text
youtube-videos/002-mini-test-sauerstoff/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Flow:
```text
youtube-videos/002-mini-test-sauerstoff/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Antigravity:
```text
youtube-videos/002-mini-test-sauerstoff/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

YouTube-Metadaten:
```text
youtube-videos/002-mini-test-sauerstoff/04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Szenenplan:
```text
youtube-videos/002-mini-test-sauerstoff/05_info/phase1-scenes.json
```

## Produktionsablauf 002

```text
Voice erzeugen
→ Flow nur Bild_01
→ Bild_01 prüfen und freigeben
→ Bild_02–06 einzeln
→ Block-QA
→ Bild_07–10 einzeln
→ Fehlerliste + Recovery
→ Audio + Bilder ins Projekt
→ Whisper / Timeline
→ Remotion
→ final-video.mp4
→ Test-QA
```

## Was noch fehlt

Der Test ist geplant und produktionsbereit, aber noch nicht gerendert.

Es fehlen nur die echten Medien:
1. finales Voice-Audio
2. akzeptierte Flow-Bilder `Bild_01.png` bis `Bild_10.png`

Danach kann Phase 3 direkt starten.

## Nächster Schritt

`GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` in Flow verwenden und zuerst ausschließlich `Bild_01` erzeugen. Nach Freigabe folgen die restlichen 9 Bilder.