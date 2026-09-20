# Engine

Dieser Ordner enthält die globalen Regeln für alle langen Object-Talk-YouTube-Videos.

## Zweck

Der Engine sorgt dafür, dass ChatGPT, Google Flow und Antigravity nicht bei jedem Video neue Regeln erfinden.

Er definiert:

- Themenauswahl und Abgrenzung
- Hook, Einleitung, Hauptteil, rhetorische Mittel und Schluss
- Visual-First-Scriptwriting
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
- Export- und Qualitätsregeln

## Dateien

- `SCRIPT-STANDARD.md` – Visual-First-Scriptwriting, Hook, Einleitung, Hauptteil, rhetorische Mittel, Schluss und Script-QA
- `THEMEN-STRATEGIE.md` – welche Gesundheits-/Biologie-/Ernährungsthemen besonders gut funktionieren und wie Themen bewertet werden
- `PRODUKTIONSREGELN.md` – globale Longform-Regeln
- `FLOW-PRODUCTION-STANDARD.md` – faceless Explainer-Bildwelt, Bild_01 als Master Style Frame, 5er-Blöcke, Fehlerliste und Recovery
- `AUDIO-REGELN.md` – Voice und kanonische Audioaufbereitung
- `SYNC-WHISPER.md` – strikte Audio-/Script-/Szenen-Synchronisierung
- `STYLE-REFERENCE-SYSTEM.md` – dauerhafter visueller Kanalanker
- `FACT-CHECK-STANDARD.md` – Gesundheit/Biologie/Ernährung prüfen
- `PHASE-GATES.md` – verbindliche PASS/FAIL-Gates
- `VISUAL-QUALITY-GATE.md` – visueller und finaler Qualitätscheck

## Produktionsablauf

```text
Themen-Gehirn + Themen-Score
→ Recherche + Claim-Matrix
→ Visual-First-Script
→ semantische Phase-1-Szenen
→ PHASE-1-PASS
→ Voice
→ Flow zuerst nur Bild_01
→ Bild_01 als Master Style Frame
→ restliche Bilder in 5er-Blöcken, einzeln generiert
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
→ PHASE-3-PASS
```

## Wichtig

Die technische Pipeline ist **fail-closed**: Ein unbekannter oder widersprüchlicher Zustand wird nicht durch Raten repariert.

Eine einzelne technisch fehlgeschlagene Google-Flow-Generation ist dagegen kein globaler Blocker. Sie wird in Phase 2 auf die Recovery-Liste gesetzt und am Ende gezielt erneut erzeugt.

Die finalen Szenenbilder erzeugt weiterhin der Nutzer mit Google Flow.
