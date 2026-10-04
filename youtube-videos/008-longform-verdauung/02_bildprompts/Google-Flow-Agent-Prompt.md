# Google Flow Agent – 008 Longform Verdauung

## Auftrag
Erzeuge die **77 finalen 16:9-Bilder** für `008-longform-verdauung` einzeln und in Reihenfolge.

Nutze als Szenenquelle:
- `05_info/phase1-scenes.json`
- `02_bildprompts/label-plan.json`
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

## Bildwelt
Ausschließlich **Clean Animated Biology Illustration** nach:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

## Harte Regeln
- jedes Bild einzeln erzeugen
- 16:9
- ein dominanter biologischer Lehrpunkt pro Bild
- bevorzugt 2–4 zentrale sichtbare Elemente
- bei zu viel Inhalt vereinfachen, niemals mehr Text hineinpressen
- 0–2 Labels pro normales Bild, nur exakt aus `label-plan.json`
- wenn ein Bild ohne Label verständlich ist, kein Label hinzufügen
- keine Zusatztexte, keine englischen Texte
- keine dekorativen Anführungszeichen im Artwork

## Cover
`Bild_01` ist das Cover.

Es darf **exakt einen sichtbaren Textblock** enthalten:
`Was passiert mit Essen?`

Sonst nichts:
- keine anatomischen Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Produktionsnummer

## Kontrast
- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- Text und Hinweislinie müssen sofort lesbar sein
- schwacher Kontrast = REGENERATE

## Produktions-IDs
Interne Namen sind ausschließlich Metadaten.

Niemals sichtbar rendern:
- `Bild_01` bis `Bild_77`
- Szenennummern
- Dateinamen
- Asset-IDs
- Promptüberschriften
- Produktionshinweise

## Wissenschaftliche Hard-Fails
- Speiseröhre nicht als reines Fallrohr darstellen
- Magen nicht als Hauptort der Nährstoffaufnahme darstellen
- Galle nicht als Enzym darstellen
- Zucker/Aminosäuren und viele Fette nicht als identischen Aufnahmeweg darstellen
- Chylomikronen/Fettweg zuerst über Lymphgefäße darstellen
- Darmzotten/Mikrovilli nicht als separate Organe darstellen
- Dickdarm nicht als Hauptort der Makronährstoffaufnahme zeigen
- Mikrobiom nicht vermenschlichen oder als Allheilmittel darstellen

## Stil-Fails
Regenerieren bei:
- Medical-CGI
- Fotorealismus
- glossy 3D
- Pixar-/Feature-Animation
- Kinderbuch-/Spielzeuglook
- Corporate-Infografik
- UI-Karten
- überladenen anatomischen Details
- Gore
- zufälligen Icons
- unnötigem Text

## QA nach jedem Bild
1. exakte Szene getroffen
2. wissenschaftlich plausibel
3. Hauptidee in ca. 1 Sekunde erkennbar
4. niedrige Informationsdichte
5. Text nur aus Whitelist
6. Textkontrast stark
7. keine Produktions-ID sichtbar
8. kein schwerer KI-Artefakt
9. klarer Unterschied zu Nachbarbildern
10. nur ein retained Finalbild pro Asset

Final exakt `Bild_01.png` bis `Bild_77.png` behalten.