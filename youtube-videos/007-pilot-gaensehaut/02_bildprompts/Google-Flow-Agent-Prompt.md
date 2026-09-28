# Google Flow Agent – Pilot 007 Gänsehaut

## Rolle
Erzeuge die finalen 16:9-Standbilder für `007-pilot-gaensehaut` einzeln und in Reihenfolge.

## Verbindliche Bildwelt
Nutze ausschließlich **Clean Animated Biology Illustration** nach:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

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

## Cover – HARD RULE

`Bild_01`:
- exakt ein sichtbarer Textblock
- nur `Warum Gänsehaut?`
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Pfeiltexte
- heller Hintergrund → dunkler Titel

Jeder weitere sichtbare Text auf dem Cover = REGENERATE.

## Produktion
Jedes Bild einzeln erzeugen und danach unter dem vorgesehenen Dateinamen speichern. Der Dateiname selbst darf niemals im Artwork erscheinen.

Die vollständigen kurzen Szenenprompts stehen in:
`02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

## Bildprinzip
- genau eine Hauptidee / ein Hauptprozess pro Bild
- bevorzugt 2–4 zentrale sichtbare Elemente
- normale Bilder 0–2 kurze deutsche Labels, maximal 2
- wenn das Bild selbsterklärend ist: kein Label
- Label bevorzugt 1–2 Wörter, maximal 3
- keine Anführungszeichen im finalen Artwork
- unnötige Strukturen und Informationen weglassen
- wenn ein Frame zu dicht wird: lieber zusätzlichen Frame planen als Text/Details hinzufügen
- starke visuelle Unterschiede zwischen Nachbarbildern
- Hautoberfläche, Cutaway, Nervensignal, Haarfollikel, Tierfell und Vergleich sinnvoll mischen

## Textkontrast – HARD RULE

- heller / blasser Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- kein hell-auf-hell
- kein dunkel-auf-dunkel
- Text bevorzugt in ruhiger negativer Fläche

Schlecht lesbarer Text = REGENERATE.

## Harte Stil-Fails
- fotorealistisches Medizinbild
- Medical-CGI
- glossy 3D
- Feature-Animation/Kinderbuch
- überladene Infografik
- random Icons
- sichtbare Produktionsnummern
- falscher deutscher Text
- mehr als 2 Labels auf einem normalen Bild
- Zusatztext auf dem Cover
- schwacher Textkontrast
- unnötiger Text
- Ausschlag-/Krankheitsoptik statt normaler Gänsehaut

## QA pro Bild
- 16:9
- Voiceover-Match
- wissenschaftlich plausibel
- genau eine dominante Hauptidee
- niedrige Komplexität
- Labels exakt aus Whitelist
- Label-Anzahl <= 2
- Labels maximal 3 Wörter
- starker Textkontrast
- keine unnötigen Texte
- Cover = title-only
- keine sichtbaren Produktions-IDs
- keine unnötigen Kleinteile
- keine Duplikat-Komposition

Final exakt 20 akzeptierte Dateien behalten.