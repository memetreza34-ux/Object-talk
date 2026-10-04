# 04_export – Veröffentlichungsbereich

Jedes reguläre Video besitzt diesen Ordner als finale Veröffentlichungsschicht.

## Pflichtstruktur

```text
04_export/
├── YOUTUBE-UPLOAD-PAKET.md
├── YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
├── YouTube-Caption.md
├── quality-scorecard.md
├── render-report.md
├── postmortem.md
└── fertiges-video/
    └── [VIDEO-ID]-YOUTUBE.mp4
```

## Regeln

- `fertiges-video/` enthält nur die finale veröffentlichungsfertige Master-MP4.
- Keine Preview-, Draft- oder Testexports dort behalten.
- Titel, Beschreibung und Caption werden individuell für das konkrete Video geschrieben.
- Metadaten müssen exakt zum tatsächlichen finalen Inhalt passen.
- Erst nach bestandenem Renderbericht und Quality-Score gilt die MP4 als `YouTube-ready`.
