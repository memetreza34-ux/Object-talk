# Antigravity – Video 001 Phase 3

## Ziel

Baue aus dem finalen Voiceover und den 36 von Google Flow erzeugten Standbildern das vollständige YouTube-Video:

**Was passiert mit deinem Essen im Körper?**

Du arbeitest technisch. Du darfst Script, Fakten, Szenengrenzen, Bildreihenfolge oder Bildinhalte nicht kreativ verändern.

## Eingaben

Projektordner:

```text
youtube-videos/001-was-passiert-mit-essen-im-koerper/
```

Verwende:

```text
01_script/script.txt
01_script/audio/<vom Nutzer erzeugtes Voiceover>
02_bildprompts/bilder-zip/<Google-Flow-ZIP>
05_info/phase1-scenes.json
03_pipeline/pipeline.md
```

## Schnellster sicherer Ablauf

Vom Repo-Root:

```bash
python -m pip install -r tools/requirements.txt
python tools/prepare_phase3.py youtube-videos/001-was-passiert-mit-essen-im-koerper
```

Dieser Lauf muss:

1. `scene-map.json` deterministisch aus `phase1-scenes.json` erzeugen.
2. Phase 1 gegen das finale `script.txt` validieren.
3. Das Nutzer-Voiceover kanonisch vorbereiten.
4. Die Flow-ZIP sicher anhand von `Bild_01` bis `Bild_36` importieren.
5. alle Bilder technisch prüfen.
6. mit faster-whisper Wort-Zeitstempel aus dem **finalen** Audio erzeugen.
7. die Whisper-Wörter streng gegen `script.txt` ausrichten.
8. die 36 festgelegten `speech_section`-Bereiche auf echte Zeiten abbilden.
9. `timeline.json` erzeugen.
10. die Remotion-Runtime mit Audio und Bildern vorbereiten.

Bei einem Script↔Audio-Mismatch niemals raten. Stoppen und den konkreten Fehler melden.

## Timing-Wahrheit

Die finale Audiodatei ist die Master-Timeline.

Die kreative Zuordnung lautet bereits:

```text
Szene 01 = Bild_01
...
Szene 36 = Bild_36
```

Die exakten Sekunden werden erst aus dem tatsächlichen Voiceover bestimmt.

Kein Bildwechsel darf anhand geschätzter Durchschnittsdauer gesetzt werden.

## Bildbewegung

Verwende ausschließlich die in `phase1-scenes.json` bzw. `timeline.json` geplante Bewegung:

- `static`
- `slow-push-in`
- `slow-pull-out`
- `pan-left`
- `pan-right`

Regeln:

- Bewegung ruhig und subtil.
- Kein Wackeln.
- Keine schnellen Zooms.
- Keine 3D-Verformung der Anatomie.
- Deutsche Labels niemals aus dem Frame bewegen oder abschneiden.
- Wenn ein Bild komplexe Anatomie zeigt, Verständlichkeit vor Bewegung.

## Schnitte

Standard ist ein sauberer harter Schnitt genau an der aufgelösten Szenengrenze.

Kein Crossfade, wenn dadurch zwei unterschiedliche anatomische Zustände gleichzeitig verwirrend sichtbar werden.

## Audio

- Voiceover vollständig erhalten.
- Keine Wörter schneiden.
- Keine Geschwindigkeit ändern.
- Keine zusätzliche Erzählerstimme.
- Keine Musik automatisch erfinden.
- SFX nur dann ergänzen, wenn ein bereits freigegebener, unaufdringlicher Sound vorhanden ist und die Verständlichkeit nicht beeinträchtigt wird. Für Pilot 001 ist SFX nicht notwendig.

## Untertitel

Die automatisch aus dem finalen Audio erzeugte SRT nach:

```text
04_export/subtitles/subtitles.srt
```

kopieren.

Untertitel müssen nicht in das Video eingebrannt werden, sofern nicht ausdrücklich angefordert.

## Render

Nach erfolgreichem `prepare_phase3.py`:

```bash
cd renderer
npm install
```

Preview zuerst prüfen. Danach den finalen Render in:

```text
../youtube-videos/001-was-passiert-mit-essen-im-koerper/04_export/fertiges-video/final-video.mp4
```

Final:

- 1920×1080
- 30 fps
- H.264
- AAC
- 16:9

## Pflicht-QA

Vor Freigabe:

- finales Video mindestens 5:00 Minuten
- `Bild_01` startet bei 0:00
- exakt 36 Bilder verwendet
- Reihenfolge 01→36
- kein schwarzer Frame
- kein Bild fehlt
- keine Labels abgeschnitten
- jeder Bildwechsel stimmt mit `timeline.json` überein
- Voiceover vollständig
- Audio und Video enden korrekt
- Video abspielbar

Danach vom Repo-Root ausführen:

```bash
python tools/qa_final.py \
  youtube-videos/001-was-passiert-mit-essen-im-koerper/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-was-passiert-mit-essen-im-koerper/01_script/audio/final-voiceover.wav
```

Wenn QA fehlschlägt: nicht als fertig melden. Erst eindeutige technische Fehler beheben und neu rendern.