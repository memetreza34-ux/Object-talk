# 04_export – Veröffentlichungsfertiges Paket

Dieser Ordner enthält ausschließlich die finalen Ausgaben für die Veröffentlichung von **008 – Was passiert mit Essen in deinem Körper?**

Verbindlicher Standard: `engine/EXPORT-STANDARD.md`

## Pflichtinhalt nach Phase 3

```text
04_export/
├── CAPTION-YOUTUBE.txt
├── YOUTUBE-UPLOAD-PAKET.md
├── YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
├── YouTube-Caption.md
├── UNTERTITEL-MIT-ZEITEN.txt
├── UNTERTITEL-YOUTUBE.srt
├── quality-scorecard.md
├── render-report.md
├── postmortem.md
└── fertiges-video/
    └── Object-Talk-008-Verdauung-YOUTUBE.mp4
```

## Finales Video

Das Video in `fertiges-video/` ist die **einzige veröffentlichungsfertige Masterdatei**.

Sie muss:
- 1920×1080 sein
- 30 fps haben
- vollständiges finales Voice-over enthalten
- 6:00–7:00 Minuten Zielbereich einhalten
- alle final akzeptierten Bilder enthalten
- keine sichtbaren Produktionsnummern enthalten
- keinen von Remotion erzeugten sichtbaren Text enthalten
- den vollständigen Final-QA bestanden haben

Zwischenrenders, Testexports und Preview-Dateien gehören **nicht** in diesen Ordner.

## Caption / YouTube-Metadaten

`CAPTION-YOUTUBE.txt` ist die einfachste Copy/Paste-Datei und enthält:
- finalen YouTube-Titel
- finale YouTube-Beschreibung
- maximal 5 Hashtags

`YOUTUBE-UPLOAD-PAKET.md` enthält zusätzlich Upload-Checkliste und finalen MP4-Dateinamen.

`YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt` und `YouTube-Caption.md` bleiben als alternative lesbare Exportformen erhalten.

## Komplettes Script mit Zeitabschnitten

`UNTERTITEL-MIT-ZEITEN.txt` enthält das komplette tatsächlich gesprochene Script mit echten Zeitfenstern, zum Beispiel:

```text
00:00–00:06  Hast du dich schon mal gefragt, ...
00:06–00:12  Danach passiert ...
```

`UNTERTITEL-YOUTUBE.srt` ist die direkt bei YouTube hochladbare Untertiteldatei.

Beide Dateien werden **nicht manuell geschätzt**, sondern nach der finalen Timeline erzeugt:

```bash
python tools/export_subtitles.py youtube-videos/008-longform-verdauung
```

Timing-Quelle:
`final-voiceover.wav → Whisper → word-timings.json → timeline.json → Untertitel-Export`

Solange die `.srt` leer ist oder `UNTERTITEL-MIT-ZEITEN.txt` noch den PENDING-Hinweis enthält, ist der Export **nicht YouTube-ready**.
