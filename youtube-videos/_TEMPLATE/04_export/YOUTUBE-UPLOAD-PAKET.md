# YouTube Upload-Paket – TEMPLATE

## Finaler Videodateiname

`[VIDEO-ID]-YOUTUBE.mp4`

Ablage:
`04_export/fertiges-video/[VIDEO-ID]-YOUTUBE.mp4`

## YouTube-Titel

[Individueller finaler Titel für genau dieses Video]

## YouTube-Beschreibung

[Individuelle finale Beschreibung für genau dieses Video. Sie muss den echten Inhalt korrekt zusammenfassen, wichtige Suchbegriffe natürlich enthalten und darf nichts versprechen, was im Video nicht vorkommt.]

## Kurze Caption

[Kurze individuelle Caption für Veröffentlichung/Sharing.]

## Hashtags

[Maximal 5 passende Hashtags]

## Direkt kopierbare Caption-Datei

`04_export/CAPTION-YOUTUBE.txt`

Pflichtinhalt:
- finaler Titel
- finale Beschreibung
- maximal 5 Hashtags

## Untertitel-Dateien

`04_export/UNTERTITEL-MIT-ZEITEN.txt`
- komplettes tatsächlich gesprochenes Script
- echte Zeitabschnitte aus finaler Timeline

`04_export/UNTERTITEL-YOUTUBE.srt`
- direkt bei YouTube hochladbar
- externe Untertitel, nicht ins Video eingebrannt

Erzeugung nach finaler Timeline:

```bash
python tools/export_subtitles.py youtube-videos/VIDEOORDNER
```

Zeitcodes niemals schätzen.

## Upload-Checkliste

- [ ] finale MP4 liegt im Ordner `fertiges-video/`
- [ ] Zielauflösung/FPS bestanden
- [ ] Audio vollständig
- [ ] keine sichtbaren Produktionsnummern/Dateinamen
- [ ] kein sichtbarer Remotion-Text
- [ ] Cover-Regeln bestanden
- [ ] Flow-Labels korrekt und lesbar
- [ ] finaler Sichtcheck vollständig bestanden
- [ ] `CAPTION-YOUTUBE.txt` vollständig und individuell
- [ ] `UNTERTITEL-MIT-ZEITEN.txt` vollständig aus finaler Timeline erzeugt
- [ ] `UNTERTITEL-YOUTUBE.srt` nicht leer und hochladbar
- [ ] Untertitel decken das komplette gesprochene Script ab
- [ ] `quality-scorecard.md` ausgefüllt
- [ ] `render-report.md` ausgefüllt
- [ ] Titel/Beschreibung/Caption gegen den echten Finalrender geprüft

Erst nach allen Checks gilt die MP4 als **YouTube-ready**.
