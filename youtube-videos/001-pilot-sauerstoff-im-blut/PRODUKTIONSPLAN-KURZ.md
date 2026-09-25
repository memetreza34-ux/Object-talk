# Produktionsplan – Pilot 001 Sauerstoff

Ziel: schneller, klarer Object-Talk-Erklaerpilot mit hoher visueller Dichte.

## 1. Verbindliche Stilbasis

Vor Produktion gelten immer:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/FLOW-PRODUCTION-STANDARD.md
```

Grundregel:

**Anschaulich erklaeren, nicht medizinisch-realistisch darstellen.**

## 2. Voice erzeugen und VOR Timeline korrigieren

Script:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Rohes TTS-Audio niemals direkt verwenden.

Zwingend:

```bash
python tools/prepare_audio.py RAW_AUDIO \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --speed 1.10
```

Verbindlich:
- Voice-Speed 1.10x
- lange TTS-Pausen komprimieren
- kurze natuerliche Mikro-Pausen behalten
- `final-voiceover.wav` ist einzige Timing-Quelle
- Whisper + Timeline erst NACH dieser Verarbeitung

## 3. Google Flow

Datei:

```text
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Der aktuelle Pilot plant **35 eindeutige Bilder**.

Zuerst ausschließlich `Bild_01`.

Bild_01 ist:
- Cover
- Hook
- erster Shot
- Master Style Frame

Nur Bild_01 darf bis zu 3 Varianten haben.
Nach Nutzerwahl:
- genau eine Coverdatei behalten
- alle anderen Cover-Kandidaten loeschen/verwerfen
- erst dann Bild_02 starten

## 4. Normale Bilder genau einmal behalten

Fuer Bild_02–Bild_35:
- jeweils nur einen Kandidaten pro Versuch
- genau ein retained asset pro Bildnummer
- FAIL-Version ersetzen, nicht sammeln
- keine `v2`, `A`, `B`, `final2`, `copy`
- kein Bild fuer eine andere Szene wiederverwenden

## 5. Sichtbarer Text

Whitelist-Regel:
- Cover: nur die exakte Hook
- normale Bilder: nur die explizit geplanten Labels
- kein anderes Wort erlaubt

Immer verboten:
- `Bild 19`
- `Bild_19`
- `BILD_12 – O2 BINDET`
- `Scene 19`
- `IMAGE 19`
- Dateinamen
- Prompt-Ueberschriften
- erfundene Szenentitel

## 6. Informationsdichte

Nicht jedes Bild muss leer sein.

Standard:
- ein dominanter Lehrpunkt
- wenige Objekte
- 0–2 Labels

Bei wichtigen Mechanismus-/Zusammenfassungsbildern darf EIN zusaetzlicher sinnvoller Detailpunkt vorkommen.

Wenn ein Speech-Beat mehr als ca. 7 Sekunden Bildzeit braucht oder zwei echte Lehrbeats enthaelt:
- in zwei eindeutige Szenen teilen
- neue fortlaufende Bildnummern verwenden
- nie dasselbe Bild doppeln

## 7. Finale Bildausgabe

Finaler Ordner:

```text
001-pilot-sauerstoff-im-blut_bilder/
```

Darin exakt:

```text
Bild_01.png
Bild_02.png
...
Bild_35.png
```

Jede Nummer exakt einmal.
Keine Varianten, keine Luecken, keine Alternativcover, keine FAIL-Dateien.

## 8. Phase 3 / Video

Nach finaler Voice + 35 finalen Bildern:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut --phase2
python tools/prepare_phase3.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Dann:

```text
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Remotion/Antigravity uebernimmt:
- nur `final-voiceover.wav`
- Whisper-Worttimings aus verarbeitetem Audio
- dynamische Timeline
- maximale Bildhaltezeit 7s
- dezente Kamerabewegung
- sparsame Overlays
- Render + QA

## 9. Final-QA

```bash
python tools/qa_final.py \
  youtube-videos/001-pilot-sauerstoff-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 100 \
  --expected-speed 1.10 \
  --max-voice-pause 0.50
```

Hard FAIL bei:
- Voice nicht 1.10x vorbereitet
- lange stille Voice-Pause >=0.50s
- Standbild >7s
- Bildasset doppelt in Timeline
- Bildnummer fehlt/doppelt
- sichtbare interne Bild-/Szenennummer
- Text ausserhalb der Whitelist
- unselektierte Covervarianten vorhanden

## 10. Ergebnis

```text
04_export/fertiges-video/final-video.mp4
```
