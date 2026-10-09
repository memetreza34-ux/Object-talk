# Object-Talk – Video 008 als verbindliche Longform-Produktionsreferenz

## Goldstandard
**Referenzvideo:** `youtube-videos/008-longform-verdauung/`
**Referenzinhalt:** „Was passiert mit Essen in deinem Körper?“; erster positiv bewerteter 6–7-Minuten-Film.
**Adaptionsbeispiel:** `youtube-videos/009-longform-schlaf/` mit dem Thema Schlaf.

Bei einer neuen regulären Longform-Episode **kopiere die bewährten Herstellungsprinzipien 1:1** und ersetze NUR Script, Recherche, biologische Aussagen/Prozesse, Cover-Titel und die zugehörigen Visuals. NICHT jedes Mal die Bildwelt, Promptstruktur, Dramaturgie, Timing oder Technik neu erfinden.

## 1. Script/Dramaturgie – genau die bewährte Bauform
- ca. 6:00–7:00 nach echter 1.10x-Voice, niemals durch lange Standbilder erzwingen.
- Hook mit offener Zuschauerfrage und unmittelbar folgender überraschender biologischer Wendung.
- Einleitung mit klarem Payoff, dann zusammenhängende Mechanismuskette statt lose Fakten.
- **Beispiel 008: 77 einzigartige Visual-Beats, 13 logische Mechanismusabschnitte.**
- Pro Beat ein Voice-Abschnitt, ein eindeutiges Bild, 3–6 Sekunden üblich, maximal 7 Sekunden. Für 009 exakt 77.
- Schluss erklärt die Ausgangsfrage und fügt keine unvorbereitete Nebenfrage hinzu.

## 2. Originaler 008-Flow-Stil (wortgetreu)
```text
Clean Animated Biology Illustration: simplified but recognizable anatomy, smooth organic forms, clean outlines, soft gradients, subtle depth, bright calm backgrounds, clear biological colors, low complexity, one dominant biological idea per frame.
```
Originale 008-Negativregel:
```text
No photoreal medical imagery, no medical CGI, no glossy 3D, no feature-animation/Pixar look, no toy/kids-book look, no corporate infographic, no clutter, no gore, no random icons, no unnecessary text.
```
- Mehrheit helle beruhigte Hintergründe (hellblau, mint, creme), klare biologische Formen und Korall-/Türkis-/Rottöne.
- Biologische Vorgänge im Vordergrund: 2–4 erkennbare Elemente, 0–2 Labels, korrekter Schriftkontrast.
- Kamera wechseln: Alltag → Körperroute → Organ-Cutaway → Gewebe → Zelle → Mechanismus → Ergebnis.
- Verbot: eigenständiger dunkler Nacht-/Anime-/Neon-Stil nur wegen Schlafthema; glühende Gehirne als Wiederholungsmotiv.
- **Gewähltes Cover NIEMALS als Stilreferenz für Innenbilder verwenden.** Es ist nur Bild_01.

## 3. Identische Struktur des ausführlichen Flow-Prompts
Ab `youtube-videos/008-longform-verdauung/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`:
1. ROLE
2. CANONICAL STYLE (wortgetreu)
3. HARD TEXT RULES
4. INFORMATION DENSITY
5. STYLE FAILS (wortgetreu)
6. Szenenregister, je Bild eine konkrete biologische Hauptaktion, sichtbare Labels nur aus Whitelist
7. FINAL QA PER IMAGE und FINAL SET.

Zusatz aus Nutzerwunsch für neue Produktionen: **im selben EINEN Prompt** zunächst drei getrennte Cover generieren und 1/2/3 wählen lassen, dann Bilder ab 02 in internen Fünfergruppen; keine weitere Promptdatei an Nutzer. Unter `02_bildprompts/` gibt es genau `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` und `bilder-zip/`.

## 4. Identische Planungsdateien, nur intern
- `01_script/script.txt` und `VOICEOVER-ZUM-KOPIEREN.txt` sind identisch.
- `05_info/phase1-scenes.json`: genau 1 Scene je finalem Bild, Script-Abdeckung ohne Lücke.
- `05_info/sentence-visual-plan.json`: 13 Mechanismusabschnitte als Navigationsindex wie 008; echte Sprachbeats separat in phase1-scenes.
- Recherche, Claim-Matrix, Mechanism-Map und Label-Plan mit konkreten wissenschaftlichen Behauptungen.
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`: genau die zugehörige Bildanzahl, numerierte Namen nur als interne Produktionsdaten.

## 5. Gleicher vollständiger Antigravity/Remotion-Auftrag
Kopiere die technische Detailtiefe aus `008/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt`, nicht nur ein paar Stichpunkte.
- Audio canonisieren 1.10x, natürliche Pausen; Whisper echte Wortzeitcodes.
- 100 % Vollbild-Illustration, 0 sichtbarer Remotion-Text, 1920x1080/30fps, leichte Pans/Zooms.
- kein Hold über 7s, keine Bilder duplizieren, keine Voice-Script-Lücken.
- `overlay-plan.json` disabled / leer.

## 6. YouTube-Export identisch vollständig
`04_export/fertiges-video/Object-Talk-XXX-THEMA-YOUTUBE.mp4`, fertige individuelle Copy-Paste-Caption, Beschreibung, Hashtags, komplettes zeitcodiertes Script, externe SRT, Renderbericht, Quality-Scorecard, Postmortem, Upload-Paket. Zeitcodes nur aus echter finaler Timeline. Keine fehlenden Medien als fertig melden.

## 7. Qualitätsübernahme 008
- 0 sichtbare interne Bildnummern
- Cover exakt ein Titelblock
- 0–2 kurze Beschriftungen mit hohem Kontrast
- 1 Hauptidee/Bild, mehr Einzelbilder statt überfüllter Mehrfachgrafiken
- neue Perspektive oder biologischer Maßstab in jedem Bild
- alle Einzelbilder wissenschaftlich und gestalterisch prüfen, Fehler neu generieren
- vor Abschluss komplettes MP4 visuell/technisch kontrollieren.

## Formatfreiheit
77 Bilder sind der **freigegebene konkrete Standard von 008 und 009**, nicht eine starre wissenschaftliche Notwendigkeit für jede denkbare Video-Länge. Nur mit begründeter dramaturgischer Notwendigkeit und erhaltener Bildzeit-Regel davon abweichen. 6–7 Minuten werden erst nach echtem Voice-Timing sicher bestätigt.
