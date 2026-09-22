# Engine

Dieser Ordner enthält die globalen Regeln für Object-Talk-YouTube-Videos.

## Zweck

Der Engine sorgt dafür, dass ChatGPT, Google Flow und Antigravity nicht bei jedem Video neue Regeln erfinden.

Er definiert:

- Themenauswahl und Abgrenzung
- Visual-First-Scriptwriting
- Mechanism Map und Satz-Visual-Planung
- Longform-Länge und interne Testausnahmen
- semantischen Bildrhythmus
- stark stilisierte 3D-Animationsfilm-Bildsprache
- deutsche Schlüsselbeschriftungen in jedem Bild
- Bild_01 als Cover + Hook + Master Style Frame
- englische Flow-Prompts bei ausschließlich deutschem sichtbaren Text
- Google-Flow-5er-Blöcke und Recovery
- selektive Remotion-Überschriften/Callouts
- wissenschaftliche Prüfung
- kanalweite Style-Konsistenz
- Voice-/Audio-Standard
- Phase-Gates
- Whisper-/Script-Synchronisierung
- Einzelbild-Review, Gesamt-Scorecard und Postmortem

## Dateien

- `SCRIPT-STANDARD.md` – Visual-First-Scriptwriting
- `THEMEN-STRATEGIE.md` – Themenauswahl und Bewertung
- `PRODUKTIONSREGELN.md` – globale Produktionsregeln
- `PLANNING-V2.md` – Mechanism Map, Satz-Visual-Plan, stabile Bild-IDs, Label-Plan und Einzelbildreview
- `VISUAL-EXPLANATION-SYSTEM.md` – visuelle Erklärfunktionen und Maßstabskette
- `PRESENTATION-OVERLAY-SYSTEM.md` – deutsche Labels plus gezielte Remotion-Überschriften/Callouts
- `FLOW-PRODUCTION-STANDARD.md` – Bildwelt, Bild_01, Prompt-Sprache, Labels, 5er-Blöcke, Fehlerliste und Recovery
- `AUDIO-REGELN.md` – Voice und Audioaufbereitung
- `SYNC-WHISPER.md` – Script-/Audio-/Szenen-Synchronisierung
- `STYLE-REFERENCE-SYSTEM.md` – langfristige Kanal-DNA + Episode-Style-Anker
- `FACT-CHECK-STANDARD.md` – Gesundheit/Biologie/Ernährung prüfen
- `PHASE-GATES.md` – verbindliche PASS/FAIL-Gates
- `VISUAL-QUALITY-GATE.md` – visueller und finaler Qualitätscheck
- `QUALITY-SCORECARD.md` – gewichtete Freigabe
- `POSTMORTEM-STANDARD.md` – Lernschleife nach Finalrender

## Produktionsablauf

```text
Themen-Gehirn + Themen-Score
→ Recherche + Claim-Matrix
→ Mechanism Map
→ Visual-First-Script
→ Satz-Visual-Plan
→ semantische Szenen
→ Label-Plan
→ Flow-Prompt: Bild_01 besonders ausführlich
→ PHASE-1-PASS
→ Voice
→ Flow erzeugt nur Bild_01
→ Bild_01 = Cover + deutscher Hook + Master Style Frame
→ Nutzerfreigabe
→ restliche Bilder in 5er-Blöcken
→ jedes Bild einzeln mit wichtigen deutschen Labels
→ Einzelbild-Review
→ Fehlerliste + Recovery
→ vollständige Bilder-ZIP
→ Audio + Whisper
→ Script↔Audio-Ausrichtung
→ exakte Szenen-Timeline
→ Remotion + selektive Overlay-Ebene
→ Render
→ technischer + visueller Final-QA
→ Qualitäts-Scorecard
→ Postmortem
```

## Aktueller Testpilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Der Pilot ist mit `05_info/test-mode.json` als interner ca. 2–2,5-Minuten-Test markiert. Nur seine Laufzeitregel weicht ab.

Er testet aktuell besonders:

- neue stark stilisierte 3D-Animationsfilm-Welt
- Cover-Hook direkt in Bild_01
- wichtige deutsche Labels in jedem Bild
- englische Flow-Prompts
- Bild_01 als konkrete Vorlage für alle restlichen Bilder
- kurze Folgeprompts
- 5er-Block-Produktion
- feste O₂-/CO₂-/RBC-/Hämoglobin-Symbolik

## V2-Prüfung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

## Wichtig

Die technische Pipeline ist fail-closed: Bei echtem Widerspruch nicht raten. Einzelne Flow-Generierungsfehler werden dagegen über Fehlerliste + Recovery behandelt.
