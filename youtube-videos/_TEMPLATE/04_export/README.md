# 04_export – Veröffentlichungsbereich

Jedes reguläre Video besitzt diesen Ordner als finale Veröffentlichungsschicht.

Verbindlicher Standard: `engine/EXPORT-STANDARD.md`

## Pflichtstruktur

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
    └── [VIDEO-ID]-YOUTUBE.mp4
```

## Regeln

- `fertiges-video/` enthält nur die finale veröffentlichungsfertige Master-MP4.
- Keine Preview-, Draft- oder Testexports dort behalten.
- `CAPTION-YOUTUBE.txt` enthält individuellen Titel, individuelle Beschreibung und maximal 5 Hashtags.
- `UNTERTITEL-MIT-ZEITEN.txt` enthält das komplette tatsächlich gesprochene Script mit echten Zeitabschnitten.
- `UNTERTITEL-YOUTUBE.srt` ist die direkt bei YouTube hochladbare Untertiteldatei.
- Untertitel-Zeitcodes werden nie geschätzt, sondern ausschließlich aus der finalen `timeline.json` erzeugt.
- Generierung: `python tools/export_subtitles.py youtube-videos/VIDEOORDNER`
- Titel, Beschreibung und Caption werden individuell für das konkrete Video geschrieben und nach dem Finalrender nochmals geprüft.
- Erst nach bestandenem Renderbericht, Quality-Score und vollständigem Untertitel-Export gilt die MP4 als `YouTube-ready`.
