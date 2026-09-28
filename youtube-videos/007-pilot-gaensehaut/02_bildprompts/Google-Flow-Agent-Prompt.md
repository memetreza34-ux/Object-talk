# Google Flow Agent – Pilot 007 Gänsehaut

## Rolle
Erzeuge die finalen 16:9-Standbilder für `007-pilot-gaensehaut` einzeln und in Reihenfolge.

## Verbindliche Bildwelt
Nutze ausschließlich **Clean Animated Biology Illustration** nach:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Kurzfassung: clean animated biology illustration, simplified recognizable anatomy, smooth organic forms, clean outlines, soft gradients, subtle depth, bright calm background, clear biological colors, simple composition.

## Harte Textregel
Produktionsnamen sind nur Metadaten.

**Nie sichtbar rendern:**
- `Bild_01`, `Bild 01`, `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Asset-IDs
- Promptüberschriften

Sichtbarer Text darf ausschließlich aus `label-plan.json` kommen. Falsche oder zusätzliche Schrift = Bild regenerieren.

## Produktion
Jedes Bild einzeln erzeugen und danach unter dem vorgesehenen Dateinamen speichern. Der Dateiname selbst darf niemals im Artwork erscheinen.

Die vollständigen kurzen Szenenprompts stehen in:
`02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

## Bildprinzip
- 2–5 zentrale sichtbare Elemente
- ein klarer biologischer Prozess oder Zusammenhang
- 0–3 kurze deutsche Labels
- starke visuelle Unterschiede zwischen Nachbarbildern
- Hautoberfläche, Cutaway, Nervensignal, Haarfollikel, Tierfell und Vergleich sinnvoll mischen

## Harte Stil-Fails
- fotorealistisches Medizinbild
- Medical-CGI
- glossy 3D
- Feature-Animation/Kinderbuch
- überladene Infografik
- random Icons
- sichtbare Produktionsnummern
- falscher deutscher Text
- Ausschlag-/Krankheitsoptik statt normaler Gänsehaut

## QA pro Bild
- 16:9
- Voiceover-Match
- wissenschaftlich plausibel
- Hauptidee sofort erkennbar
- niedrige Komplexität
- Labels exakt aus Whitelist
- keine sichtbaren Produktions-IDs
- keine unnötigen Kleinteile
- keine Duplikat-Komposition

Final exakt 20 akzeptierte Dateien behalten.