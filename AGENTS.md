# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap fuer ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `config/channel.json`
4. `config/video.json`
5. `THEMEN-GEHIRN.md`
6. `engine/README.md`
7. `engine/SCRIPT-STANDARD.md`
8. `engine/FLOW-AGENT-INSTRUCTIONS.md` bei Flow-/Bildarbeit
9. `engine/FLOW-PRODUCTION-STANDARD.md`
10. `engine/PLANNING-V2.md`
11. relevante `bildwelt/*.md`
12. Dateien des aktuellen YouTube-Projekts

Aktiver Testpilot steht in `PROJECT_STATE.md`.

## Phase 1 – Creative Director

Darf:
- recherchieren und Fakten pruefen
- Mechanism Map erstellen
- Skript schreiben
- Satz-Visual-Plan und Szenen festlegen
- Label-Plan erstellen
- Flow-Szenenprompts schreiben
- Metadaten schreiben

Muss:
- `engine/SCRIPT-STANDARD.md` einhalten
- Satz 1 als starken Neugier-Hook schreiben
- Hook bevorzugt als direkte Zuschauerfrage, ueberraschende Aussage, Mythos, Alltagsraetsel oder Kontrast bauen
- innerhalb der ersten ca. 15 Sekunden Hook → Wendung → Payoff liefern
- jeden Speech-Beat als echtes Erklaerbild planen
- mindestens etwa 60 % der normalen Explainerframes als Prozess, Beziehung, Ursache/Wirkung, Weg, Vergleich, Vorher/Nachher oder Kontext planen
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander zulassen
- fuer jedes Bild sichtbaren Erklaerwert und Unterschied zu Nachbarbildern definieren
- Flow-Anweisungen auf Englisch schreiben
- sichtbaren Text ausschliesslich auf Deutsch planen
- alle final sichtbaren Texte direkt fuer Google Flow planen
- textfreie Style-Referenzen vor texttragenden Referenzen priorisieren

Darf nicht:
- Schulbuch-Einstiege schreiben
- `In diesem Video ...` / `Heute erklaeren wir ...` als Standardopening nutzen
- sichtbare Texte fuer Remotion einplanen
- drei oder mehr aehnliche Objektportraits hintereinander planen
- ein schwaches Bild mit spaeterem Overlay retten
- finale Flow-Bilder vortaeuschen

## Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt die von Phase 1 vorgegebenen Bilder.

Verbindlich:
- dauerhafte Regeln aus `engine/FLOW-AGENT-INSTRUCTIONS.md` verwenden
- textfreie `STYLE_REFERENCE.png` oder `EPISODE_STYLE_REFERENCE.png` als echte Referenz anhaengen
- `Bild_01` ist Cover und darf Text tragen, wird aber NICHT als Follow-up-Style-Referenz benutzt
- nur `Bild_01` darf bis zu 3 Covervarianten haben
- nach Nutzerwahl unselektierte Covervarianten verwerfen
- jedes normale Bild einzeln erzeugen und genau eine finale Version behalten
- alle sichtbaren Texte kommen aus Google Flow
- normale Bilder enthalten nur die in `label-plan.json` freigegebenen deutschen Begriffe
- Cover-Hook darf nach `Bild_01` nie wieder sichtbar sein
- falsche Flow-Schrift in Flow regenerieren/korrigieren, nicht spaeter in Remotion ersetzen
- jede Szene auf Novelty, Information Value und Nachbarschaftsunterschied pruefen

## Phase 3 – Editor / Antigravity / Remotion

Remotion ist nur fuer:
- Audio
- Timing
- leichte Zoom-/Pan-Bewegungen
- Schnitte
- nicht-textliche Uebergaenge
- Rendering

Remotion darf NICHT:
- sichtbaren Text erzeugen
- Kapitelueberschriften einblenden
- Keywords einblenden
- Callouts/Labels einblenden
- Flow-Schrift ersetzen
- Script umschreiben
- Bildideen austauschen

Jedes nicht-leere Text-Overlay ist ein Hard FAIL.

## Bildwelt

Educational Explainer:
- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- ca. 80 % animierte Illustration / 20 % Soft-3D-Tiefe
- klar animiert, nicht fotorealistisch
- helle ruhige Hintergruende
- weiche gerundete Formen
- wenige klare Objekte
- ein dominanter Lehrpunkt pro Bild
- ca. 20–35 % wichtiger Mechanismusbilder duerfen einen sinnvollen Zusatzdetailpunkt tragen

Nicht erlaubt:
- Medical-CGI
- nasses realistisches Gewebe
- kosmische / Sci-Fi-Mikrowelt
- Anatomie-Mannequins
- ueberladene Infografik
- billiger Toy-Look

## Text

Google Flow ist die einzige Quelle fuer sichtbaren Text.

Cover:
- nur exakte deutsche Hook

Normale Szenen:
- 0–2 kurze deutsche Labels bevorzugt
- max. 3 bei echtem Bedarf
- exakt nach `label-plan.json`

Immer verboten:
- `Bild_XX`, `Scene XX`, Dateinamen, Prompttitel
- Cover-Hook nach Bild_01
- englischer sichtbarer Text
- KI-Gibberish
- Remotion-Text

## Timing

Finale Zeitbasis:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Standard:
- Voice 1.10x
- lange Pausen komprimieren
- kein Standbild ueber 7 Sekunden
- kein Bildasset doppelt verwenden

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

## Fail-closed

STOP bei:
- schwachem Script-Hook
- Script/Audio-Mismatch
- sichtbarem Text ausserhalb der Flow-Whitelist
- Remotion-Textoverlay
- Cover-Hook nach Bild_01
- texttragendem Cover als Follow-up-Referenz
- fehlenden/doppelten Bildern
- zu aehnlichen Szenen ohne neuen Lehrzweck
- drei oder mehr isolierten Objektportraits hintereinander
- wissenschaftlich falscher Kernaussage
- Photorealismus / Medical-CGI-Stildrift
