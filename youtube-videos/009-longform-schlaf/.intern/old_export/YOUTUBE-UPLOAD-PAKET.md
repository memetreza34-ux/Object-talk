# YouTube Upload-Paket – 009 Schlaf

## Finaler Videodateiname

`Object-Talk-009-Schlaf-YOUTUBE.mp4`

Ablage:
`04_export/fertiges-video/Object-Talk-009-Schlaf-YOUTUBE.mp4`

## YouTube-Titel

**Was passiert in deinem Körper, während du schläfst? | Schlaf einfach erklärt**

## YouTube-Beschreibung

Was macht dein Gehirn, während du schläfst – und warum ist Schlaf viel mehr als eine Pause?

Wir folgen einer Nacht durch deinen Körper: Zuerst erklären wir Schlafdruck, Adenosin und die innere Uhr. Danach geht es durch die leichteren Schlafstufen bis in den Tiefschlaf. Du siehst, was mit Herzschlag, Atmung und Hormonen passiert und weshalb Schlaf für Lernen, Gedächtnis und das Immunsystem wichtig ist.

Anschließend zeigen wir die REM-Phase mit Träumen und schnellen Augenbewegungen – und erklären, warum sich Tiefschlaf und REM im Lauf der Nacht abwechseln.

Eine verständliche Biologie-Erklärung mit klaren Illustrationen, ohne übertriebene Gesundheitsversprechen.

## Kurze Caption

Warum bleibt dein Gehirn aktiv, während du schläfst? Wir folgen Schlafdruck, innerer Uhr, Tiefschlaf, Gedächtnis, Immunzellen und REM durch eine Nacht.

## Hashtags

`#Schlaf #Biologie #Gehirn #Gesundheit #ObjectTalk`

## Direkt kopierbare Caption-Datei

`04_export/CAPTION-YOUTUBE.txt`

Enthält denselben finalen Titel, dieselbe Beschreibung und die Hashtags in einer einfachen Copy/Paste-Datei.

## Untertitel-Dateien

### Lesbare Komplettfassung
`04_export/UNTERTITEL-MIT-ZEITEN.txt`

Enthält das komplette tatsächlich gesprochene Script mit echten Zeitabschnitten.

### YouTube-SRT
`04_export/UNTERTITEL-YOUTUBE.srt`

Direkt als externe Untertiteldatei bei YouTube hochladbar. Nicht ins Video eingebrannt.

Zeitcodes werden ausschließlich aus der finalen `timeline.json` erzeugt:

```bash
python tools/export_subtitles.py youtube-videos/009-longform-schlaf
```

## Upload-Checkliste

- [ ] finale MP4 liegt im Ordner `fertiges-video/`
- [ ] exakt 77 eigenständige akzeptierte Bilder aus der freigegebenen 008-Bildwelt
- [ ] Laufzeit 6:00–7:00 Minuten
- [ ] 1920×1080 / 30 fps
- [ ] Audio vollständig und sauber
- [ ] keine sichtbaren Bild-/Szenennummern oder Dateinamen
- [ ] kein sichtbarer Remotion-Text
- [ ] Coverbild im Video enthält nur den geplanten Titel
- [ ] Flow-Labels korrekt und gut lesbar
- [ ] finaler Sichtcheck vollständig bestanden
- [ ] `CAPTION-YOUTUBE.txt` vollständig und gegen Finalrender geprüft
- [ ] `UNTERTITEL-MIT-ZEITEN.txt` enthält das komplette Script mit echten Zeitabschnitten
- [ ] `UNTERTITEL-YOUTUBE.srt` ist nicht leer und direkt hochladbar
- [ ] Untertitel-Zeitcodes stammen aus finaler Timeline und wurden nicht geschätzt
- [ ] `quality-scorecard.md` ausgefüllt
- [ ] `render-report.md` ausgefüllt
- [ ] Titel und Beschreibung gegen den finalen Render gegengeprüft

## Veröffentlichungsregel

Erst wenn alle Upload-Checks bestanden sind, gilt die MP4 als **YouTube-ready**.
