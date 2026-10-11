# Export-Standard – Object-Talk

Status: **VERBINDLICH FÜR ALLE KÜNFTIGEN VIDEOS (ab der neuen 3-Ordner-Struktur)**

## Oberste Regel: Der sichtbare Export muss sauber bleiben

In `03_export/` liegen nach vollständig abgeschlossener Produktion **genau vier Dateien** – weder mehr noch weniger:

```text
03_export/
├── VIDEO.mp4
├── COVER.png
├── CAPTION-YOUTUBE.txt
└── UNTERTITEL-MIT-ZEITEN.txt
```

1. **VIDEO.mp4:** einziges fertiges YouTube-Video; keine Previews oder Testversionen. Das Cover ist NICHT im Video; die erste Szene ist `Bild_01`.
2. **COVER.png:** genau das vom Nutzer ausgewählte, separat gespeicherte YouTube-Vorschaubild. Kein Bild aus der normalen Videoszenen-ZIP und kein Videostart.
3. **CAPTION-YOUTUBE.txt:** *ein* individuell formulierter und komplett kopierbarer YouTube-Titel und *eine* Beschreibung inklusive bis zu fünf passenden Hashtags. Keine zusätzlichen Titel-/Caption-/Metadaten-Dateien.
4. **UNTERTITEL-MIT-ZEITEN.txt:** der komplette tatsächlich gesprochene Sprechertext, in gut kopierbaren Abschnitten mit **echten** Start-/Endzeitstempeln aus dem finalen Audio, z. B. `00:00–00:10  Tatsächlich gesprochener Text`. Keine erfundenen Zeiten, keine ausgelassenen Sätze.

Diese vier Namen sind fest. Nicht mehr `final-video.mp4`, `fertiges-video/`, zusätzliche Caption-Versionen oder `YOUTUBE-UPLOAD-PAKET.md` im sichtbaren Export anlegen.

## Technischer Bereich – nicht im sichtbaren Export

Sämtliche internen Dateien wie `render-report.md`, `quality-scorecard.md`, `postmortem.md`, `final-video.qa.json`, `UNTERTITEL-YOUTUBE.srt`, `timeline.json`, `word-timings.json`, Audio-Zwischenstände und Prüfprotokolle gehören **nur nach `.intern/`** (jeweils passende Unterordner). Die technische QA bleibt verbindlich, aber darf den Nutzerexport nicht auffüllen. Kein technischer README, PLACEHOLDER, Zwischenordner oder JSON in `03_export/`.

**Ausnahme nach Status, nicht nach Inhalt:** Vor Abschluss der Produktion existieren `VIDEO.mp4` und `COVER.png` möglicherweise noch gar nicht; keine leeren oder erfundenen Mediendateien anlegen. Die zwei Textdateien können vorläufige Entwürfe sein und dürfen erst als fertig bezeichnet werden, wenn die Inhalte geprüft wurden.

## Zeitcode-Regel

```text
final-voiceover.wav
→ Whisper / word-timings.json
→ timeline.json
→ tools/export_subtitles.py
→ 03_export/UNTERTITEL-MIT-ZEITEN.txt
→ .intern/UNTERTITEL-YOUTUBE.srt (internes optionales Zusatzformat)
```

`python tools/export_subtitles.py youtube-videos/VIDEOORDNER` verwendet die finale Timeline. Fehlt sie oder ist sie ungültig, keine fertigen Untertitel und keine geratenen Zeitfenster behaupten.

## Finalfreigabe

Erst nach echtem MP4-Render und Prüfung: Videodauer, 16:9, Ton, passende normale Szenen ohne Cover-Einblendung, korrekte Titel-/Beschreibungsdatei, vollständiges zeitgestempeltes Skript sowie technische QA in `.intern/`. Dann besteht der sichtbare Export aus genau den vier festgelegten Dateien.

## Bestandsschutz

Die historische Verdauungsproduktion `008-longform-verdauung` und andere bestehende Videoordner werden **NICHT verändert oder rückwirkend migriert**. Ihre bisherigen `04_export/`-Strukturen sind ausschließlich historisch. Neue Videos richten sich immer nach diesem 3-Ordner-Standard; `03_export/` ist für fertige Nutzerdateien reserviert.
