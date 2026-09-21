# Engine

Dieser Ordner enthält die globalen Regeln für Object-Talk-YouTube-Videos.

## Zweck

Der Engine sorgt dafür, dass ChatGPT, Google Flow und Antigravity nicht bei jedem Video neue Regeln erfinden.

Er definiert:

- Themenauswahl und Abgrenzung
- Hook, Einleitung, Hauptteil, rhetorische Mittel und Schluss
- Visual-First-Scriptwriting
- Mechanism Map und Satz-Visual-Planung
- Longform-Länge und ausdrücklich markierte interne Testausnahmen
- semantischen Bildrhythmus
- faceless Explainer-Bildsprache
- Google-Flow-Masterframe, 5er-Blöcke und Recovery
- wissenschaftliche Prüfung
- kanalweite Style-Konsistenz
- Voice-/Audio-Standard
- harte Phase-Gates
- Whisper-/Script-Synchronisierung
- Bild-/Audio-Zuordnung
- Standbild-Motion
- Einzelbild-Review, Gesamt-Scorecard und Postmortem
- Export- und Qualitätsregeln

## Dateien

- `SCRIPT-STANDARD.md` – Visual-First-Scriptwriting, Hook, Einleitung, Hauptteil, rhetorische Mittel, Schluss und Script-QA
- `THEMEN-STRATEGIE.md` – Themenauswahl und Bewertung
- `PRODUKTIONSREGELN.md` – globale Produktionsregeln
- `PLANNING-V2.md` – Mechanism Map, Satz-Visual-Plan, stabile Bild-IDs, Label-Plan und Einzelbildreview
- `VISUAL-EXPLANATION-SYSTEM.md` – Beobachtung/Auslöser/Weg/Vergleich/Schwelle/Wirkung und Maßstabskette
- `FLOW-PRODUCTION-STANDARD.md` – faceless Explainer-Bildwelt, Bild_01 als Master Style Frame, 5er-Blöcke, Fehlerliste und Recovery
- `AUDIO-REGELN.md` – Voice und kanonische Audioaufbereitung
- `SYNC-WHISPER.md` – strikte Audio-/Script-/Szenen-Synchronisierung
- `STYLE-REFERENCE-SYSTEM.md` – visueller Kanalanker
- `FACT-CHECK-STANDARD.md` – Gesundheit/Biologie/Ernährung prüfen
- `PHASE-GATES.md` – verbindliche PASS/FAIL-Gates inklusive dokumentierter Testmodus-Regel
- `VISUAL-QUALITY-GATE.md` – visueller und finaler Qualitätscheck
- `QUALITY-SCORECARD.md` – gewichtete Freigabe mit hartem Wissenschaftsblocker
- `POSTMORTEM-STANDARD.md` – Lernschleife nach jedem echten Finalrender

## Produktionsablauf

```text
Themen-Gehirn + Themen-Score
→ Recherche + Claim-Matrix
→ Mechanism Map
→ Visual-First-Script
→ Satz-Visual-Plan
→ semantische Phase-1-Szenen
→ Label-Plan
→ PHASE-1-PASS
→ Voice
→ Flow zuerst nur Bild_01
→ Bild_01 als Master Style Frame
→ restliche Bilder in 5er-Blöcken, einzeln generiert
→ Einzelbild-Review
→ Flow-Fehlerliste + Recovery-Pass
→ vollständige Bilder-ZIP
→ kanonisches Audio + sichere ZIP-Übernahme
→ PHASE-2-PASS
→ faster-whisper
→ strikte vollständige Script↔Audio-Ausrichtung
→ exakte Szenen-Timeline
→ feste Remotion-Runtime
→ Render
→ technischer + visueller Final-QA
→ Qualitäts-Scorecard
→ PHASE-3-PASS
→ Postmortem + dauerhafte Lehren
```

## Aktueller Testpilot

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Dieser Pilot ist mit `05_info/test-mode.json` ausdrücklich als interner ca. 2-Minuten-Test markiert.

Nur seine Laufzeitregel weicht ab. Alle anderen V2-, Wissenschafts-, Visual-, Sync- und QA-Regeln bleiben vollständig aktiv.

Normale Kanalvideos bleiben mindestens 300 Sekunden lang.

## V2-Prüfung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

Der V2-Validator verändert keine Dateien und ist bewusst separat von der Phase-3-Pipeline.

## Wichtig

Die technische Pipeline ist **fail-closed**: Ein unbekannter oder widersprüchlicher Zustand wird nicht durch Raten repariert.

Eine einzelne technisch fehlgeschlagene Google-Flow-Generation ist dagegen kein globaler Blocker. Sie wird in Phase 2 auf die Recovery-Liste gesetzt und am Ende gezielt erneut erzeugt.

Die finalen Szenenbilder erzeugt weiterhin der Nutzer mit Google Flow.
