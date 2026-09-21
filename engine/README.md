# Engine

Dieser Ordner enthält die globalen Regeln für alle langen Object-Talk-YouTube-Videos.

## Zweck

Der Engine sorgt dafür, dass ChatGPT, Google Flow und Antigravity nicht bei jedem Video neue Regeln erfinden.

Er definiert:

- Themenauswahl und Abgrenzung
- Hook, Einleitung, Hauptteil, rhetorische Mittel und Schluss
- Visual-First-Scriptwriting
- Mechanism Map und Satz-Visual-Planung
- Longform-Länge und semantischen Bildrhythmus
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
- `THEMEN-STRATEGIE.md` – welche Gesundheits-/Biologie-/Ernährungsthemen besonders gut funktionieren und wie Themen bewertet werden
- `PRODUKTIONSREGELN.md` – globale Longform-Regeln
- `PLANNING-V2.md` – Mechanism Map, Satz-Visual-Plan, stabile Bild-IDs, Label-Plan und Einzelbildreview für neue Projekte
- `VISUAL-EXPLANATION-SYSTEM.md` – Beobachtung/Auslöser/Weg/Vergleich/Schwelle/Wirkung und Maßstabskette für echte Erklärbilder
- `FLOW-PRODUCTION-STANDARD.md` – faceless Explainer-Bildwelt, Bild_01 als Master Style Frame, 5er-Blöcke, Fehlerliste und Recovery
- `AUDIO-REGELN.md` – Voice und kanonische Audioaufbereitung
- `SYNC-WHISPER.md` – strikte Audio-/Script-/Szenen-Synchronisierung
- `STYLE-REFERENCE-SYSTEM.md` – dauerhafter visueller Kanalanker
- `FACT-CHECK-STANDARD.md` – Gesundheit/Biologie/Ernährung prüfen
- `PHASE-GATES.md` – verbindliche PASS/FAIL-Gates
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

## V2-Kompatibilität

Video 001 und andere bereits bestehende Projekte bleiben kompatibel. Die neuen V2-Planungsdateien werden nicht rückwirkend erzwungen.

Neue Projekte, die aus `youtube-videos/_TEMPLATE` erstellt werden, erhalten die V2-Dateien automatisch und können geprüft werden mit:

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

Der V2-Validator verändert keine Dateien und ist bewusst nicht in die bestehende Phase-3-Pipeline eingehängt.

## Wichtig

Die technische Pipeline ist **fail-closed**: Ein unbekannter oder widersprüchlicher Zustand wird nicht durch Raten repariert.

Eine einzelne technisch fehlgeschlagene Google-Flow-Generation ist dagegen kein globaler Blocker. Sie wird in Phase 2 auf die Recovery-Liste gesetzt und am Ende gezielt erneut erzeugt.

Die finalen Szenenbilder erzeugt weiterhin der Nutzer mit Google Flow.
