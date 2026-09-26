# Postmortem – Pilot 003 Render 1

## Gesamturteil

Der Render ist ein klarer Fortschritt gegenüber den früheren Piloten, aber noch nicht finaler Kanalstandard.

Bildwelt und Tempo funktionieren grundsätzlich. Die größten Restprobleme lagen bei Script-Hook, Remotion-Text und visueller Wiederholung.

## Was funktioniert

- 2.5D / Soft-3D-Bildwelt ist passend
- nicht zu realistisch / nicht Medical-CGI
- Voice mit 1.10x wirkt deutlich besser
- lange Pausen sind stark reduziert
- Thema Muskelwachstum ist grundsätzlich verständlich
- Mythos Muskelkater / Mikroriss wird sinnvoll korrigiert

## Problem 1 – Script-Einstieg zu flach

Alter Einstieg:

`Warum wird ein Muskel nach Wochen Training größer?`

Problem:
- sachlich
- klingt eher nach Schulbuchfrage
- wenig direkte Zuschaueransprache
- keine sofortige Überraschung

Neue Regel:

`Hast du dich schon mal gefragt, warum ...?`

oder eine starke überraschende Aussage / Mythos / Kontrast.

Neuer Pilot-003-Einstieg:

`Hast du dich schon mal gefragt, warum deine Muskeln durch Training überhaupt größer werden?`

Direkt danach:

`Das Überraschende: Sie wachsen nicht während der Wiederholung selbst – das Training setzt zuerst nur einen Reiz.`

## Problem 2 – Remotion-Text passt optisch nicht

Beobachtung:
- nachträgliche Kapiteltexte wirken wie eine zweite Designschicht
- Flow-Typografie und Remotion-Typografie wirken nicht aus einem Guss
- Text kann die Bildidee künstlich retten, statt dass das Bild selbst stärker wird

Neue harte Regel:
- alle sichtbaren Texte kommen aus Google Flow
- Remotion erzeugt keinen Text
- Flow-Schreibfehler werden in Flow korrigiert/regeneriert
- `overlay-plan.json` bleibt leer
- Renderer bricht bei nicht-leeren Textoverlays ab

## Problem 3 – ähnliche Bilder hintereinander

Beobachtet wurden mehrfach ähnliche:
- Muskelquerschnitte
- Zell-Cutaways
- Myofibrillen-Darstellungen
- Anpassungsbilder

Neue harte Regeln:
- mindestens ca. 60 % Prozess-/Beziehungs-/Vergleichs-/Kontextbilder
- maximal zwei isolierte Objektportraits hintereinander
- benachbarte Szenen ändern mindestens zwei visuelle Dimensionen
- gleiche Komposition nicht erneut ohne neuen Lehrzweck verwenden

## Problem 4 – manche Mechanismusbilder zu leer

Neue Regel:
- 20–35 % wichtiger Mechanismusframes dürfen einen zusätzlichen sinnvollen Detailpunkt tragen
- lieber Ursache + Folge sichtbar machen als nur ein einzelnes Organ/Objekt zeigen
- schwaches Bild in Flow verbessern statt mit Textoverlay zu erklären

## Konkrete Pilot-003-Fixes

Besonders geschärft wurden:
- Bild 05 vs. 06: Membran-Sensorik vs. Signalkette im Zellinneren
- Bild 13 vs. 14: Aminosäure-Einbau vs. Myofibrillen-Mechanik
- Bild 15 vs. 16 vs. 17: Myofibrillen-Anpassung vs. Faserquerschnitt vs. Hypertrophie
- Bild 27 vs. 28: Gewöhnung im Kontext vs. direkter gleicher-Reiz-Vergleich
- Bild 31–33: Zusammenfassung in drei klar verschiedenen Maßstäben/Layouttypen

## Regeln, die aus diesem Postmortem global wurden

Autoritativ aktualisiert:
- `PROJECT_CONTRACT.md`
- `AGENTS.md`
- `config/channel.json`
- `engine/SCRIPT-STANDARD.md`
- `engine/PLANNING-V2.md`
- `engine/FLOW-AGENT-INSTRUCTIONS.md`
- `engine/PRESENTATION-OVERLAY-SYSTEM.md`
- `tools/build_renderer_runtime.py`

## Ziel für den nächsten Render

- Hook sofort neugierig
- keine Remotion-Texte
- Flow-Texte sauber und konsistent
- keine fast identischen Bildfolgen
- mehr echte Ursache-Wirkung-Bilder
- Tempo weiterhin schnell und sauber
