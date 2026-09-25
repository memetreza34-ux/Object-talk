# Object-Talk – Project State

Letzte Aktualisierung: 25.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/002-zucker-im-koerper/
```

Thema:

**Was passiert mit Zucker in deinem Körper?**

Cover-Hook:

**„So verarbeitet dein Körper Zucker“**

## Zweck von Pilot 002

Pilot 002 ist der erste neue Test nach dem echten Render-Review von Pilot 001.

Er soll prüfen, ob die korrigierte Pipeline allgemein funktioniert:
- Voice standardmäßig 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- keine künstliche Streckung auf feste Laufzeit
- maximal 7 Sekunden pro Standbild
- 35 eindeutige Bilder
- kein Bildasset zweimal in der Timeline
- sichtbarer Text strikt Whitelist-basiert
- keine internen Bild-/Szenennummern im Artwork
- nur Cover darf vor Auswahl mehrere Varianten haben
- nach Coverwahl alle ungewählten Varianten löschen/verwerfen
- normale Szenen jeweils genau ein retained asset
- Finale ist neue Zusammenfassung statt Cover-Wiederholung

## Pilot 002 – Inhalt

Reise:

`Nahrung → Mund/Magen → Dünndarm → Glukose → Blut → Pfortader/Leber → Bauchspeicheldrüse/Insulin → Zellaufnahme → ATP → Glykogen → längerfristiger Energieüberschuss/Fett → Glukagon → Leber gibt Glukose frei`

Voiceover:
- 352 Wörter
- 35 Sprach-/Visual-Beats
- Zielverarbeitung 1.10x
- erwartete finale Laufzeit ungefähr 125–145 Sekunden, abhängig vom Roh-TTS und der Pausenkompression

## Aktuelle Bildwelt

Verbindliche Richtung:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Eigenschaften:
- klar animiert / illustriert
- nicht fotorealistisch
- hell und freundlich
- weich gerundete vereinfachte Formen
- matte bis leicht satinierte Oberflächen
- wenige klare Objekte
- ein dominanter Lehrpunkt pro Bild
- etwa 20–30 % wichtiger Mechanismus-/Summary-Frames dürfen einen zusätzlichen sinnvollen Detailpunkt enthalten

## Semantische Farben Pilot 002

- Glukose = Türkis/Cyan mit warm-goldenem Akzent
- Insulin = Blau
- Glukagon = Violett
- Blutgefäße = Coral-Rot
- Organe = Peach/Coral/Orange
- Glykogen = Amber/Gold
- ATP = warmes Gelb/Gold
- Fettzelle = Apricot/Gelb
- Hintergrund = Creme / helles Blau / weiches Beige

## Cover-Regel

`Bild_01` ist Cover, erster Shot und Episode-Master-Frame.

Nur bei Bild_01:
- bis zu 3 unterschiedliche Covervarianten erlaubt
- Nutzer wählt genau 1
- alle anderen Covervarianten danach löschen/verwerfen
- final existiert genau ein `Bild_01.png`

Cover sichtbarer Text:
- nur **„So verarbeitet dein Körper Zucker“**
- keine Anatomie-Labels
- keine interne Bildnummer

## Normale Bilder

Bild_02–Bild_35:
- jedes Bild genau einmal final behalten
- FAIL ersetzt dieselbe Nummer
- keine Alternativversionen sammeln
- kein Asset doppelt verwenden
- sichtbarer Text nur aus `02_bildprompts/label-plan.json`

Hard FAIL sichtbarer Text:
- `Bild 19`
- `Bild_19`
- `BILD_12 – ...`
- `Scene 19`
- `IMAGE 19`
- Dateiname / Asset-ID
- Promptüberschrift
- erfundener Szenentitel

## Autoritative Dateien Pilot 002

```text
youtube-videos/002-zucker-im-koerper/01_script/script.txt
youtube-videos/002-zucker-im-koerper/01_script/VOICEOVER-ZUM-KOPIEREN.txt
youtube-videos/002-zucker-im-koerper/05_info/mechanism-map.md
youtube-videos/002-zucker-im-koerper/05_info/phase1-scenes.json
youtube-videos/002-zucker-im-koerper/02_bildprompts/label-plan.json
youtube-videos/002-zucker-im-koerper/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
youtube-videos/002-zucker-im-koerper/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
youtube-videos/002-zucker-im-koerper/PRODUKTIONSPLAN-KURZ.md
```

## Produktionsstatus

Bereit:
- Thema
- Voiceover
- Mechanism Map
- 35-Szenen-Plan
- Cover-Hook
- Text-Whitelist
- Google-Flow-Masterprompt
- 1.10x-/Pausenregeln
- Antigravity-/Remotion-Anweisung

Nächster Schritt:
1. Voice aus `VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. Google Flow mit dem Masterprompt starten.
3. drei Coverrichtungen erzeugen.
4. genau ein Cover auswählen und Alternativen entfernen.
5. Bild_02–Bild_35 jeweils einzeln produzieren.
6. erst danach Phase 3 ausführen.
