# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widerspruechen gilt zuerst eine ausdrueckliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert deutschsprachige YouTube-Erklaervideos zu Ernaehrung, Gesundheit und Biologie.

Harte Grundregeln:
- normale Kanalvideos mindestens 5:00 Minuten, sofern der Nutzer nicht bewusst einen kuerzeren Testpilot bestellt
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- generierte Standbilder bleiben die visuelle Basis, sofern fuer ein Projekt nichts anderes beschlossen wird
- hohe visuelle Dichte statt langer statischer Bildhaltezeiten
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wissenschaftlich relevante Aussagen pruefen

## Script-Standard – Neugier zuerst

Die ersten 5–10 Sekunden muessen sofort Neugier erzeugen.

Bevorzugt:
- direkte Zuschauerfrage
- ueberraschende Aussage
- Mythos / Fehlannahme
- Alltagsraetsel
- klarer Kontrast

Opening:
1. Hook
2. unerwartete Antwort / Wendung
3. klares Payoff-Versprechen innerhalb der ersten ca. 15 Sekunden

Vermeiden:
- `In diesem Video ...`
- `Heute erklaeren wir ...`
- Definition-first ohne Neugier
- lange Einleitung vor der eigentlichen Frage

Autoritativ: `engine/SCRIPT-STANDARD.md`

## Audio-/Pacing-Standard

Sofern nichts anderes beschlossen wird:
- finales Voiceover 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- finales verarbeitetes `final-voiceover.wav` ist die Timing-Quelle
- Video nicht durch Pausen oder lange Bild-Holds kuenstlich strecken

## Visuelle Dichte / Bildwechsel

Diese Regeln sind STYLE-UNABHAENGIG:
- ein Standbild normalerweise etwa 3–6 Sekunden
- harte Obergrenze 7.0 Sekunden
- bei mehreren Lehrbeats neue eindeutige Szene planen
- dasselbe Bild nicht wiederverwenden, um Zeit zu fuellen
- ein dominanter Lehrpunkt pro Bild
- Prozesse, Beziehung, Ursache/Wirkung, Wege, Vergleiche, Vorher/Nachher und Kontext bevorzugen
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander
- benachbarte Szenen sollen sich in mindestens zwei visuellen Dimensionen unterscheiden

## KRITISCH: BILDWELT IST OFFEN

Am 27.09.2026 wurden alle bisherigen kanalweiten Bildwelt-Definitionen bewusst verworfen.

Aktuell gibt es KEINE verbindliche Vorgabe fuer:
- 2.5D / Soft-3D
- Premium-3D / Feature-Animation
- Character-Stil
- Explainer-Stil
- Farben
- Materialien
- Beleuchtung
- Rendergrad
- Kameraaesthetik
- Style-Reference-System
- Flow-vs-Editor-Typografie als Stilentscheidung

Historische Pilotdateien sind keine Stilautoritaet.
Kein Agent darf aus alten Piloten automatisch eine neue Kanalbildwelt ableiten.

## Style-Gate

Bevor neue finale Kanalbilder produziert werden:
1. mehrere geeignete Bildwelt-Richtungen recherchieren
2. Richtungen gegeneinander vergleichen
3. mit identischen Testmotiven testen
4. Nutzer waehlt eine Richtung
5. neue Bildwelt schriftlich definieren
6. erst dann Referenzsystem, Flow-Prompts und Style-QA neu aufbauen

Bis Schritt 4/5 abgeschlossen ist, ist finale Bildproduktion gesperrt.

## Menschen / Figuren / Personifizierung

Aktuell keine kanalweite Stilregel. Ob und wie Menschen, Objekte, Lebensmittel oder biologische Strukturen personifiziert werden, wird mit der neuen Bildwelt entschieden.

Wissenschaftliche Klarheit hat Vorrang vor dekorativer Personifizierung.

## Sichtbarer Text

Weiterhin gilt:
- viewer-facing Text nur auf Deutsch
- interne Assetnamen, Szenennummern und Promptueberschriften niemals sichtbar
- keine Textwaende

Ob finaler Text in Flow oder im Editor erzeugt wird, wird zusammen mit der neuen Bildwelt neu entschieden. Alte Flow-only-/Remotion-only-Stilregeln sind nicht automatisch verbindlich.

## Asset-Hygiene

- pro finaler Bildnummer genau ein retained Asset
- FAIL wird ersetzt, nicht dauerhaft als Variantensammlung behalten
- keine Bildduplikate fuer mehrere Szenen
- keine Luecken im finalen nummerierten Set

## Drei Phasen

### Phase 1 – Creative Director
Recherche → Claim-Check → Script → Mechanism Map → Satz-Visual-Plan → Szenenplan → Label-/Textplan.

### Phase 2 – Medienproduktion
Aktuell Style-Gate. Nach Freigabe der neuen Bildwelt: Referenztest → Cover → Einzelbilder → Bild-QA → finale Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio kanonisieren → Whisper → Timeline → Bildbewegung/Schnitt → Render → Final-QA.

## Autoritative Reihenfolge

1. aktuelle ausdrueckliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `PROJECT_STATE.md`
4. `config/channel.json`
5. aktuelle Engine-Regeln
6. aktuelles Projekt
7. historische Piloten nur als Lern-/Fehlerhistorie

## Goldene Regel waehrend des Style-Resets

**Keine alte Bildwelt wiederbeleben. Erst neu suchen, testen, auswaehlen und danach festschreiben.**
