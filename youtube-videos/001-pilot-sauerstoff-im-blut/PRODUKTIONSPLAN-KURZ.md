# Produktionsplan – Pilot 001 Sauerstoff

Ziel: erster echter kleiner Object-Talk-Pilot mit ungefähr 2–2,5 Minuten Laufzeit und 28 Bildern.

## 1. Voice erzeugen

Datei:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Text 1:1 in die Voice-KI übernehmen. Finales Audio in:

```text
01_script/audio/
```

## 2. Google Flow starten

Datei:

```text
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Den kompletten Prompt verwenden.

Zuerst ausschließlich:

```text
Bild_01
```

Bild_01 ist:
- Cover
- Hook
- erster Shot
- Master Style Frame

Bild_01 muss klar wie ein hochwertiger **stilisierter 3D-Animationsfilm** aussehen. Kein medizinischer CGI-Look, keine realistische Haut, keine realistischen Gewebetexturen.

## 3. Genau eine Freigabe

Flow darf nur nach `Bild_01` auf die Nutzerfreigabe warten.

Nach Freigabe von Bild_01 arbeitet Flow **ohne weitere Rückfragen** bis zum Ende.

Nicht erlaubt:
- nach einem 5er-Block fragen, ob weitergemacht werden soll
- zwischen Bildern zusätzliche Freigaben verlangen
- den Lauf freiwillig pausieren

## 4. Restliche Bilder automatisch produzieren

Reihenfolge:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
Bild_22–26
Bild_27–28
Recovery-Pass
```

Die Blöcke sind nur interne QA-Schritte. Nach jedem Block automatisch weiter.

Jedes Bild:
- einzeln generieren
- `Bild_01` als Style-/Continuity-Referenz verwenden
- auf Animationsstil prüfen
- auf korrekte deutsche Labels prüfen
- bei Fehler auf Recovery-Liste setzen

Fehlerhafte Bilder automatisch bis zu 3-mal neu versuchen.

## 5. Finale Bildausgabe

Am Ende einen finalen Ordner erstellen:

```text
001-pilot-sauerstoff-im-blut_bilder/
```

Darin exakt:

```text
Bild_01.png
Bild_02.png
...
Bild_28.png
```

Keine Varianten, keine Lücken, keine Zusätze wie `neu`, `final2`, `v3` oder `copy`.

Zusätzlich:

```text
001-pilot-sauerstoff-im-blut_bilder.zip
```

Die ZIP enthält exakt denselben finalen Ordner.

Repo-Ziel für die ZIP:

```text
02_bildprompts/bilder-zip/001-pilot-sauerstoff-im-blut_bilder.zip
```

## 6. Phase 3 starten

Sobald Voice + alle 28 Bilder vorhanden sind:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut --phase2
python tools/prepare_phase3.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Dann:

```text
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Antigravity/Remotion übernimmt:
- Audioaufbereitung
- Whisper-Worttimings
- exakte Szenen-Timeline
- Bildimport
- dezente Kamerabewegung
- Overlays
- Render
- QA

## 7. Ergebnis

```text
04_export/fertiges-video/final-video.mp4
```

Der 10-Bilder-Mini-Test 002 wird übersprungen.