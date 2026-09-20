# Audio-Regeln

Diese Regeln gelten für jedes Object-Talk-Longform-Video.

## Stimme

Die konkrete Voice-KI kann gewechselt werden. Sobald der Nutzer eine Stimme als Kanalstimme freigibt, soll dieselbe Stimme möglichst über alle Longform-Videos beibehalten werden.

Ziel:

- Deutsch
- klar und natürlich
- freundlich und neugierig
- verständlich für jüngere Zuschauer, aber nicht babyhaft
- ruhig genug für Biologie-Erklärungen
- lebendig genug für Object-Talk
- keine übertriebene Werbestimme

## Sprechtempo

Zielbereich ungefähr **135–155 Wörter pro Minute**.

Wichtiger als eine starre Zahl ist gute Verständlichkeit. Die echte Videodauer wird immer am finalen Audio geprüft.

## Aussprache

Fachbegriffe müssen vor der Voice-Erzeugung auf sprechfreundliche Formulierung geprüft werden.

`script.txt` muss exakt dem gesprochenen Text entsprechen. Keine alternative Audiofassung verwenden, ohne anschließend `script.txt` ebenfalls anzupassen und Phase 1 neu zu validieren.

## Keine künstliche Longform-Streckung

- kein Speed-down, um 5 Minuten zu erreichen
- keine künstlich langen Pausen
- keine unnötigen Wiederholungen

Wenn das finale Voiceover unter 300 Sekunden liegt:

1. Script sinnvoll erweitern
2. Szenenplanung aktualisieren
3. Voice neu erzeugen
4. erst danach Phase 2 erneut prüfen

## Rohes Audio und kanonisches Audio

Die Voice-KI-Datei ist zunächst nur das Rohasset.

Vor Whisper wird daraus immer erzeugt:

```text
01_script/audio/final-voiceover.wav
```

mit:

```bash
python tools/prepare_audio.py RAW_AUDIO 01_script/audio/final-voiceover.wav
```

## Kanonische Audioeigenschaften

Interner Produktionsstandard:

- WAV
- 48 kHz
- PCM 16-bit
- Geschwindigkeit: exakt `1.0×`
- keine Kompression interner Sprechpausen
- Ziel-Lautheit ungefähr `-16 LUFS`
- Ziel True Peak maximal ungefähr `-1 dB`

Diese Werte sind unser **Pipeline-Standard**, nicht die Behauptung einer zwingenden YouTube-Vorgabe.

`prepare_audio.py` verwendet dafür FFmpeg `loudnorm` und verändert die Sprechgeschwindigkeit nicht.

## Wichtig für Timing

Whisper läuft ausschließlich auf `final-voiceover.wav`.

Nach Erstellung von Wort-Zeitstempeln darf diese Audiodatei nicht mehr verändert werden.

Jede Audioänderung macht folgende Dateien ungültig und sie müssen neu erzeugt werden:

- `whisper-raw.json`
- `word-timings.json`
- `timeline.json`
- `subtitles.srt`
- Renderer-Runtime

## Musik und SFX

- Hintergrundmusik optional und sehr leise
- Voiceover immer dominant
- Soundeffekte sparsam und nur mit echtem inhaltlichem Nutzen
- keine dauernden Cartoon-Sounds
- keine zweite narrative Stimme

Für den ersten Pilot ist **Voiceover ohne zusätzliche Musik/SFX technisch völlig ausreichend**. Erst nach stabiler Bild-/Timing-Pipeline sollen zusätzliche Audio-Layer optimiert werden.
