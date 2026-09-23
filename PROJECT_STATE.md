# Object-Talk – Project State

Letzte Aktualisierung: 23.09.2026

## Aktiver Produktionspilot

Aktiv ist jetzt wieder:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Der 10-Bilder-Mini-Test `002-mini-test-sauerstoff` wird vorerst übersprungen. Die freigegebene Bildwelt ist inzwischen stabil genug, deshalb gehen wir direkt auf einen echten kleinen 2–3-Minuten-Pilotfilm.

## Ziel des ersten echten Kleinpiloten

- ungefähr 2–2,5 Minuten
- akzeptabler Testbereich 115–160 Sekunden
- 28 Erklärbilder
- hohe visuelle Dichte
- stark stilisierte hochwertige 3D-Animationsfilm-Welt
- kein medizinischer Fotorealismus
- Bild_01 = Cover + Hook + Master Style Frame
- Folgeproduktion in 5er-Blöcken

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

## Produktionsablauf 001

```text
Voice erzeugen
→ Flow nur Bild_01
→ Bild_01 prüfen und freigeben
→ Bild_02–06 einzeln
→ Block-QA
→ Bild_07–11 einzeln
→ Block-QA
→ Bild_12–16 einzeln
→ Block-QA
→ Bild_17–21 einzeln
→ Block-QA
→ Bild_22–26 einzeln
→ Block-QA
→ Bild_27–28 einzeln
→ Fehlerliste + Recovery
→ Audio + Bilder ins Projekt
→ Whisper / Timeline
→ Remotion
→ final-video.mp4
→ Test-QA
```

## Nutzerdateien

Voice:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Flow:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Antigravity:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Kurzplan:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/PRODUKTIONSPLAN-KURZ.md
```

## Was noch fehlt

Phase 1 ist vorbereitet. Für den echten Render fehlen nur die Medien:

1. finales Voice-Audio
2. akzeptierte Flow-Bilder `Bild_01.png` bis `Bild_28.png`
3. ausgefüllte Einzelbild-Reviews nach echter Bildauswahl

## Nächster Schritt

1. Voiceover erzeugen.
2. Flow-Prompt öffnen.
3. Zuerst ausschließlich `Bild_01` erzeugen.
4. Bild_01 als Master Style Frame freigeben.
5. Danach direkt mit den 5er-Blöcken weitermachen.
