# Export-Standard – Object-Talk

Status: **KANONISCH / VERBINDLICH**

Jedes reguläre Video muss am Ende ein vollständiges Veröffentlichungs-Paket unter `04_export/` besitzen.

## Pflichtstruktur

```text
04_export/
├── CAPTION-YOUTUBE.txt
├── YOUTUBE-UPLOAD-PAKET.md
├── YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
├── YouTube-Caption.md
├── UNTERTITEL-MIT-ZEITEN.txt
├── UNTERTITEL-YOUTUBE.srt
├── render-report.md
├── quality-scorecard.md
├── postmortem.md
└── fertiges-video/
    └── [VIDEO-ID]-YOUTUBE.mp4
```

## 1. CAPTION-YOUTUBE.txt

Direkt kopierbare Veröffentlichungsdatei mit:
- individuellem YouTube-Titel
- individueller YouTube-Beschreibung
- maximal 5 passenden Hashtags

Titel und Beschreibung müssen nach dem echten Finalrender nochmals gegen den Inhalt geprüft werden.

## 2. Komplettes Script mit Zeitabschnitten

`UNTERTITEL-MIT-ZEITEN.txt` enthält das **komplette tatsächlich gesprochene Script** mit echten Zeitfenstern aus dem finalen Voiceover.

Beispiel:

```text
00:00–00:06  Hast du dich schon mal gefragt, ...
00:06–00:12  Danach passiert ...
```

Die Abschnitte müssen zusammen den gesamten gesprochenen Inhalt abdecken.

## 3. YouTube-Untertitel

`UNTERTITEL-YOUTUBE.srt` ist die direkt hochladbare SRT-Datei.

Pflicht:
- gleiche finale Sprachfassung wie im Video
- echte Zeitcodes
- keine geschätzten Zeiten
- keine fehlenden gesprochenen Abschnitte
- keine Produktionshinweise, Bildnummern oder Szenennummern im Untertiteltext

## 4. Timing-Quelle

**Zeitcodes dürfen niemals manuell geschätzt werden.**

Autoritative Reihenfolge:

```text
final-voiceover.wav
→ Whisper / word-timings.json
→ timeline.json
→ tools/export_subtitles.py
→ UNTERTITEL-MIT-ZEITEN.txt + UNTERTITEL-YOUTUBE.srt
```

Befehl:

```bash
python tools/export_subtitles.py youtube-videos/VIDEOORDNER
```

Wenn `timeline.json` fehlt oder nicht valide ist: **FAIL**, keine Untertitel erzeugen.

## 5. Finales Video

`fertiges-video/` enthält nur die finale YouTube-Masterdatei.
Keine Preview-, Draft- oder Testexports dort behalten.

## 6. YouTube-ready Gate

Ein Video ist erst `YouTube-ready`, wenn:
- finale MP4 vorhanden und geprüft
- `CAPTION-YOUTUBE.txt` individuell ausgefüllt
- `UNTERTITEL-MIT-ZEITEN.txt` aus finaler Timeline erzeugt
- `UNTERTITEL-YOUTUBE.srt` aus finaler Timeline erzeugt
- SRT nicht leer ist
- Titel/Beschreibung gegen Finalrender geprüft
- Renderbericht ausgefüllt
- Quality-Scorecard bestanden
- Postmortem vorbereitet/ausgefüllt nach Finalrender

## Goldene Regel

**Export bedeutet nicht nur MP4. Export = fertiges Video + YouTube-Metadaten + vollständige zeitcodierte Untertitel + QA.**
