# Produktionsplan – Pilot 007 Gänsehaut

## Thema
**Warum bekommst du Gänsehaut?**

## Ziel
Kurzer End-to-End-Test der **Clean Animated Biology Illustration** mit Haut, Nerven, Haarfollikel, kleinem glatten Muskel und Tierfell.

## Umfang
- maximal 2:00 Minuten final
- ca. 190 Wörter Voiceover
- 20 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice-Verarbeitung 1.10x
- bevorzugte Laufzeit ungefähr 1:20–1:55
- über 120 Sekunden = Hard FAIL

## Biologische Reise
`Kälte → Temperatursignal → Nervensystem → sympathisches Signal → Haaraufrichtemuskel → Haar richtet sich auf → Haut hebt sich → Gänsehaut`

Zusatz:
`starkes Gefühl → sympathische Aktivierung → gleicher lokaler Haarmuskel-Mechanismus`

## Bildwelt
Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Pflicht:
- saubere animierte Biologie-Illustration
- vereinfachte erkennbare Anatomie
- helle ruhige Hintergründe
- **eine Hauptidee pro Bild**
- bevorzugt 2–4 wichtige Elemente
- normale Bilder **0–2 kurze deutsche Labels**, nur wenn nötig
- keine alte 2.5D-/Premium-3D-/Medical-CGI-Welt

## Cover

`Bild_01`:
- genau ein sichtbarer Textblock
- nur `Warum Gänsehaut?`
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- Titel auf hellem Hintergrund in dunkler Schrift

Zusatztext = Hard FAIL / regenerieren.

## Text / Lesbarkeit

- helle Fläche → dunkle Schrift
- dunkle Fläche → helle Schrift
- keine Anführungszeichen um Labels
- Label bevorzugt 1–2 Wörter, maximal 3 Wörter
- wenn das Bild selbsterklärend ist: kein Label
- schwacher Textkontrast = regenerieren

## Informationsdichte

- ein dominanter Lehrpunkt pro Bild
- unnötige Nebeninformation weglassen
- wenn ein Beat zu viel Inhalt braucht: lieber mehr Bilder als einen überladenen Frame

## Google Flow
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` verwenden
- jedes Bild einzeln erzeugen
- intern exakt `Bild_01` bis `Bild_20`
- **Dateiname/Bildnummer/Szenennummer niemals sichtbar rendern**
- sichtbare Texte ausschließlich aus `label-plan.json`
- falsche Schrift/Zuordnung/Kontrast = regenerieren
- keine Bildduplikate

## Remotion
**Kein sichtbarer Text.**

Remotion nur für:
- Audio
- Timing
- sanfte Push/Pull/Pan-Bewegungen
- Schnitte
- dezente nicht-textliche Übergänge
- Render

`03_pipeline/overlay-plan.json` bleibt deaktiviert und leer.

## Audio / Timing
1. Voice aus `VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. `tools/prepare_audio.py --speed 1.10`.
3. finales `final-voiceover.wav` ist Master-Timeline.
4. Whisper-Wortzeiten aus finalem Audio.
5. keine Szene länger als 7 Sekunden.

## Erfolgskriterien
- Video <= 120 Sekunden
- Hook sofort verständlich
- Cover enthält ausschließlich den Titel
- Text auf allen Bildern sofort lesbar
- kein light-on-light / dark-on-dark
- maximal 2 Labels pro normalem Bild
- keine unnötigen Labels
- Haaraufrichtemuskel und Haarfollikel klar erkennbar
- Kälte → Nerv → Muskel → Gänsehaut visuell klar
- Tierfell-Nutzen einfach und nicht übertrieben
- emotionale Gänsehaut als zweiter Auslöser verständlich
- 20 unterschiedliche Illustrationen
- keine sichtbaren Produktionsnummern
- kein Remotion-Text
- keine überladenen Bilder
