# Object-Talk – Project State

Letzte Aktualisierung: 26.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/003-pilot-muskelwachstum/
```

Thema:

**Wie wächst ein Muskel?**

Cover-Hook:

**„So wächst dein Muskel“**

## Zweck von Pilot 003

Pilot 003 ist der nächste End-to-End-Test nach dem echten Review von Pilot 002.

Er prüft insbesondere die neuen Schutzregeln gegen:
- wiederholte Cover-Hooks in normalen Szenen
- texttragende Cover als Style-Referenz
- zu ähnliche Bildfolgen
- zu leere Mechanismusbilder
- doppelte/coverartige Übersichtsframes

## Produktionsziel

- 35 eindeutige Bilder
- ca. 329 Wörter Voiceover
- Voice 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- erwartete Endlänge ca. 2:05–2:30
- kein Bild länger als 7 Sekunden
- kein Bildasset doppelt

## Inhaltliche Reise

`Widerstand → mechanische Spannung → Zell-Signal → Proteinsynthese → Aminosäuren → Myofibrillen → Querschnitt/Hypertrophie → Satellitenzellen → Ernährung/Erholung/Schlaf → Muskelkater-Mythos → Anpassung → Progression → Zusammenfassung`

## Fachliche Leitplanken

- Muskelwachstum NICHT als simples „Mikrorisse entstehen und werden größer repariert“-Modell erklären.
- Muskelkater ist kein zuverlässiges Maß für Muskelwachstum.
- Protein ist Baustoff, aber nicht alleinige Ursache von Muskelwachstum.
- keine individuellen Mengen-, Supplement-, Therapie- oder Trainingsplan-Empfehlungen.

## Bildwelt

Verbindlich bleibt:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Pilot-003-Farben:
- Muskel/Muskelfaser = Coral / Salmon / Rot-Orange
- Spannung = warmes Orange-Rot
- Zell-Signale = Cyan / Blau
- Aminosäuren = Türkis / Cyan
- Proteinaufbau = warmes Gold
- Myofibrillen = tieferes Rot / Burgunder
- Erholung = Soft-Blau / Teal
- Progression = Gold / Orange
- Hintergrund = Creme / Beige / helles Blau

## Cover-Hook-Hard-Lock

Die Hook **„So wächst dein Muskel“** darf exakt nur auf `Bild_01` erscheinen.

Für Bild_02–Bild_35 ist sie Hard FAIL:
- kein Titel mit derselben Hook
- keine Kapitelüberschrift mit derselben Hook
- keine dekorative Hintergrundschrift
- keine nahezu identische Kurzfassung

## Referenzlogik

1. Bild_01 als Cover erzeugen, bis zu 3 Varianten.
2. Nutzer wählt exakt 1 Cover; Rest löschen/verwerfen.
3. Danach eine **textfreie** `EPISODE_STYLE_REFERENCE.png` mit `STYLE-REFERENCE-PROMPT.txt` erzeugen.
4. Bild_02–Bild_35 nur mit dieser textfreien Referenz erzeugen.
5. Das texttragende Cover niemals als Follow-up-Style-Referenz verwenden.

## Visuelle Dichte / Abwechslung

- ein dominanter Lehrpunkt pro Bild
- ca. 20–35 % wichtiger Mechanismusbilder dürfen einen sinnvollen Zusatzdetailpunkt enthalten
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander
- danach Prozess / Weg / Ursache-Wirkung / Vorher-Nachher / Kontext
- gleiche Übersichtskomposition nicht wiederholen
- Nachbarszenen müssen Perspektive, Maßstab oder Informationsfunktion klar ändern

Bild-QA prüft:
- `visual_novelty >= 8/10`
- `information_value >= 8/10`
- `cover_hook_isolated = PASS`
- für Bild_02+ `text_free_reference_used = PASS`
- Text-Whitelist / keine Asset-IDs / genau ein retained Asset

## Kapiteloverlays

Sparsam und jeweils nur einmal:
- Im Muskel beginnt die Anpassung
- Jetzt beginnt der Aufbau
- Training allein reicht nicht
- Muskelkater ist kein Wachstums-Messer
- Der Reiz muss mitwachsen

Keine dieser Formulierungen darf die Cover-Hook wiederholen.

## Wichtige Dateien

```text
youtube-videos/003-pilot-muskelwachstum/01_script/VOICEOVER-ZUM-KOPIEREN.txt
youtube-videos/003-pilot-muskelwachstum/05_info/mechanism-map.md
youtube-videos/003-pilot-muskelwachstum/05_info/phase1-scenes.json
youtube-videos/003-pilot-muskelwachstum/05_info/sentence-visual-plan.json
youtube-videos/003-pilot-muskelwachstum/02_bildprompts/STYLE-REFERENCE-PROMPT.txt
youtube-videos/003-pilot-muskelwachstum/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
youtube-videos/003-pilot-muskelwachstum/02_bildprompts/label-plan.json
youtube-videos/003-pilot-muskelwachstum/02_bildprompts/image-review.json
youtube-videos/003-pilot-muskelwachstum/03_pipeline/overlay-plan.json
youtube-videos/003-pilot-muskelwachstum/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

## Nächster Testablauf

1. Voice aus `VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. Bild_01: bis zu 3 Coverrichtungen, genau 1 auswählen.
3. ungewählte Cover löschen.
4. textfreie Episode-Style-Referenz erzeugen.
5. Bild_02–Bild_35 jeweils einzeln produzieren.
6. jedes Bild gegen Hook-Leak, Whitelist, Novelty und Informationswert prüfen.
7. Phase 3 mit 1.10x-Audio und Overlay-Plan rendern.
8. finalen Render erneut vollständig prüfen.
