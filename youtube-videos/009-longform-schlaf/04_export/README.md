# Export 009 – Schlaf

Status: PENDING_MEDIA, nicht YouTube-ready.

Pflichtdateien:
- `CAPTION-YOUTUBE.txt` – individueller YouTube-Titel, Beschreibung, Hashtags.
- `YOUTUBE-UPLOAD-PAKET.md` – Upload-Checkliste und Dateiname.
- `UNTERTITEL-MIT-ZEITEN.txt` – komplettes gesprochenes Script mit exakten Zeitabschnitten nach Whisper.
- `UNTERTITEL-YOUTUBE.srt` – echte YouTube-Untertitel aus finaler Timeline, nicht ins Video eingebrannt.
- `fertiges-video/Object-Talk-009-Schlaf-YOUTUBE.mp4` – finale MP4 (fehlt aktuell).
- `render-report.md`, `quality-scorecard.md`, `postmortem.md` – nach QA ausfüllen.

Timing: `final-voiceover.wav` → Whisper → `word-timings.json` → `timeline.json` → `tools/export_subtitles.py`.
Keine geschätzten Zeiten oder erfundenen MP4s.
