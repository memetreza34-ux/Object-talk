# Pilot 001 – Produktionsplan nach Video-Review

## Ziel

Ein fertiger 16:9-Erklaerpilot mit engem, modernen Erklaertempo.

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Die alte feste 150-Sekunden-Vorgabe ist aufgehoben. Die echte verarbeitete Voice bestimmt die Laufzeit.

## Format

- 1920×1080
- 16:9
- 30 fps
- erwartete Pilotdauer ca. 120–140 Sekunden
- 35 eindeutige visuelle Szenen
- Voiceover: `01_script/VOICEOVER-ZUM-KOPIEREN.txt`
- Voice-Speed: **1.10x**
- lange TTS-Pausen komprimieren
- maximale stille Voice-Pause nach Verarbeitung: **<0.50s**
- maximale Standbilddauer: **7.0s**
- Bildwelt: `bildwelt/EXPLAINER-STYLE-LOCK.md`

## Bildwelt

Explainer-Szenen:
- moderne stilisierte 2.5D / Soft-3D-Erklaerillustration
- ca. 80 % Illustration / 20 % Soft-3D-Tiefe
- kein Medical-CGI
- keine realistischen nassen Gewebetexturen
- klare weiche Formen
- helle Hintergruende
- ein dominanter Lehrpunkt pro Frame
- ca. 20–30 % der Szenen duerfen EIN zusaetzliches sinnvolles Detail tragen
- lieber mehr eindeutige Bilder als ein Bild zu lange halten

## Phase A – Voice

1. Rohes TTS-Audio erzeugen.
2. Danach zwingend `tools/prepare_audio.py` verwenden.
3. Produktionsstandard: `--speed 1.10`.
4. Lange interne Pausen werden automatisch komprimiert.
5. Erst `final-voiceover.wav` darf fuer Whisper, Timeline und Render verwendet werden.
6. Niemals Timings aus dem Roh-Audio bauen.

Beispiel:

```bash
python tools/prepare_audio.py RAW_AUDIO \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --speed 1.10
```

## Phase B – Bilder in Google Flow

1. Agent Instructions aus `engine/FLOW-AGENT-INSTRUCTIONS.md` setzen.
2. `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` verwenden.
3. Zuerst nur `Bild_01` erzeugen.
4. Nur beim Cover bis zu 3 Varianten.
5. Nutzer waehlt 1 Cover; alle anderen Cover loeschen/verwerfen.
6. Danach Bild_01 als echtes Flow-Reference/Ingredient an jede Folgegeneration anhaengen.
7. `Bild_02`–`Bild_35` einzeln erzeugen.
8. Normale Szene: genau ein retained asset pro Bildnummer.
9. Schlechte Version ersetzt dieselbe Nummer; FAIL-Version nicht behalten.
10. Kein Bild darf fuer zwei Szenen wiederverwendet werden.

### Sichtbarer Text

Whitelist-Regel:
- Cover: nur Hook
- normale Szene: nur exakt geplante Labels
- `Bild_19`, `BILD_12 – ...`, `Scene 19`, Dateinamen und Prompt-Ueberschriften sind immer verboten
- jedes nicht geplante Wort = FAIL

## Phase C – Timeline

Die Timeline wird dynamisch aus den Worttimings von `final-voiceover.wav` gebaut.

`tools/build_timeline.py` hat eine harte Standardgrenze von 7 Sekunden pro Bild.

Wenn ein Speech-Beat laenger ist:
- Speech-Beat semantisch teilen
- neue eindeutige Szene planen
- neue fortlaufende Bildnummer vergeben
- niemals dasselbe Bild duplizieren

## Phase D – Bewegung in Remotion

Bewegung bleibt dezent:
- slow-push-in: ca. 2–4 %
- slow-pull-out: ca. 2–4 %
- pan-right / pan-left: langsame horizontale Bewegung
- micro-hold: fast statisch

Keine hektischen Ken-Burns-Bewegungen.
Keine langen statischen Holds zum Strecken der Laufzeit.

## Phase E – Text / Labels

Cover:
- nur Hook: `So reist Sauerstoff durch deinen Körper`
- keine Zusatzlabels

Normale Szenen:
- bevorzugt 0–2 kurze Labels
- nur Deutsch
- Begriffe aus `label-plan.json`
- Flow-Text nur nutzen, wenn exakt korrekt und whitelist-konform
- bei wiederholtem Fehler Remotion-Fallback

## Phase F – Audio + SFX

Voice klar im Vordergrund.
SFX nur dezent und niemals als Ersatz fuer Pausen.

Moeglich:
- sanfter Luftstrom beim Einatmen
- subtiler O2-Uebergangston
- dezenter Herzschlag
- weicher Flow-/Whoosh bei Gefaessbewegung
- dezentes Energie-SFX bei ATP
- sanfter Ausatem

Keine Musik fuer den Pilot erforderlich.

## Final-QA

Vor Export pruefen:
- Dauer innerhalb der dokumentierten Testspanne
- Voice-Speed 1.10x laut Audio-Report
- Pausenkompression aktiv
- keine stille Voice-Pause >=0.50s
- 35 eindeutige Bilder vorhanden
- jede Bildnummer exakt einmal
- kein Bild doppelt in der Timeline
- kein Standbild >7.0s
- Cover nur einmal und nur Titel
- keine sichtbaren internen Bild-/Szenennummern
- sichtbarer Text nur aus Whitelist
- kein Medical-CGI / Photorealismus
- O2/CO2-Farbcode konsistent
- Voice und Bild semantisch passend
- Audio ohne Clipping
- 1920×1080 / 30 fps

QA-Aufruf:

```bash
python tools/qa_final.py \
  youtube-videos/001-pilot-sauerstoff-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 100 \
  --expected-speed 1.10 \
  --max-voice-pause 0.50
```

## Produktionsstatus

Das Script bleibt unveraendert. Der visuelle Plan wurde auf 35 eindeutige Bilder verdichtet, die Voice-Pipeline auf 1.10x + Pausenkompression umgestellt und die feste 2:30-Streckung entfernt.
