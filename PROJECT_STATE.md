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

## Review des echten Pilot-003-Renders

Der Render wurde vollständig angesehen.

Was funktioniert:
- 2.5D / Soft-3D-Bildwelt bleibt bestehen
- Tempo mit 1.10x ist deutlich besser
- Cover-Hook-Leak wurde weitgehend verbessert
- Muskelthema ist grundsätzlich verständlich visualisiert

Neue Hauptprobleme aus dem echten Render:
1. Script-Einstieg war noch zu sachlich/flach.
2. Mehrere Muskelquerschnitt-/Zell-/Myofibrillenbilder wirkten zu ähnlich.
3. Einige Mechanismusbilder waren zu leer bzw. hätten mehr inhaltliche Erklärung im Bild gebraucht.
4. Remotion-Text wirkte optisch fremd zur Flow-Bildwelt.
5. Sichtbarer Text soll künftig ausschließlich aus Google Flow kommen.

Diese Punkte sind jetzt als globale Repo-Regeln gehärtet.

## Neuer Script-Hard-Lock

Neue Videos starten nicht mehr mit einer sachlichen Definition oder einer flachen Fachfrage.

Pflicht:
- Satz 1 erzeugt sofort Neugier
- bevorzugt direkte Zuschauerfrage wie `Hast du dich schon mal gefragt, warum ...?`
- alternativ überraschende Aussage, Mythos, Alltagsraetsel oder Kontrast
- innerhalb von 1–2 Saetzen folgt eine Wendung / unerwartete Antwort
- innerhalb von ca. 15 Sekunden ist der Payoff klar

Autoritativ:

```text
engine/SCRIPT-STANDARD.md
```

Pilot 003 wurde entsprechend umgeschrieben. Neuer Einstieg:

`Hast du dich schon mal gefragt, warum deine Muskeln durch Training überhaupt größer werden?`

Danach direkt:

`Das Überraschende: Sie wachsen nicht während der Wiederholung selbst – das Training setzt zuerst nur einen Reiz.`

## Sichtbarer Text – nur Google Flow

Neue harte Regel:
- Cover-Titel kommt aus Google Flow
- normale Labels kommen aus Google Flow
- eventuell geplante Kapitelbegriffe kommen aus Google Flow
- Remotion erzeugt **keinen** sichtbaren Text
- keine Remotion-Kapitelüberschriften
- keine Remotion-Keywords
- keine Remotion-Callouts
- keine Remotion-Label-Fallbacks

Wenn Flow Text falsch schreibt:
- Bild in Flow regenerieren/korrigieren
- nicht in Remotion reparieren

`tools/build_renderer_runtime.py` bricht jetzt hart ab, wenn `overlay-plan.json` nicht-leere Textoverlays enthält.

Pilot 003:

```text
youtube-videos/003-pilot-muskelwachstum/03_pipeline/overlay-plan.json
```

ist jetzt deaktiviert/leer.

## Visuelle Vielfalt / Informationswert

Neue harte Regeln:
- mindestens etwa 60 % der normalen Explainerbilder zeigen Prozess, Beziehung, Ursache/Wirkung, Weg, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander
- benachbarte Szenen unterscheiden sich in mindestens zwei Dimensionen: Kameramassstab, Layout, Hauptmotiv, Prozessrichtung, Kontext oder Visual-Typ
- gleiche Muskelquerschnitt-/Zell-/Myofibrillen-Komposition nicht mehrfach nahezu identisch verwenden
- ca. 20–35 % wichtiger Mechanismusbilder duerfen einen sinnvollen Zusatzdetailpunkt enthalten
- ein schwaches Bild wird nicht durch Editor-Text gerettet; es wird in Flow besser erzeugt

Der Pilot-003-Flow-Prompt wurde besonders bei den aehnlichen Szenen geschaerft:
- Membran-Sensorik vs. intrazellulaere Signalkette
- Aminosaeure-Einbau vs. Myofibrillen-Mechanik
- Myofibrillen-Anpassung vs. Faserquerschnitt vs. Hypertrophie
- Gewoehnung vs. gleicher Reiz mit kleinerer Herausforderung
- Zusammenfassungsbilder in unterschiedlichen Massstaeben

## Produktionsziel Pilot 003

- 35 eindeutige Bilder
- Voice 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- kein Bild länger als 7 Sekunden
- kein Bildasset doppelt
- alle sichtbaren Texte direkt in Flow
- Remotion nur Timing / Audio / Zoom-Pan / Schnitt / nicht-textliche Uebergaenge

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

## Cover-Hook-Hard-Lock

Die Hook **„So wächst dein Muskel“** darf exakt nur auf `Bild_01` erscheinen.

Für Bild_02–Bild_35 ist sie Hard FAIL.

## Referenzlogik

1. textfreie `EPISODE_STYLE_REFERENCE.png` erzeugen bzw. kanalweite textfreie Style-Reference verwenden
2. Bild_01 als Cover erzeugen, bis zu 3 Varianten
3. Nutzer wählt exakt 1 Cover; Rest löschen/verwerfen
4. Bild_02–Bild_35 nur mit textfreier Referenz erzeugen
5. texttragendes Cover niemals als Follow-up-Style-Referenz verwenden

## Wichtige Dateien

```text
PROJECT_CONTRACT.md
AGENTS.md
config/channel.json
engine/SCRIPT-STANDARD.md
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/PLANNING-V2.md
engine/PRESENTATION-OVERLAY-SYSTEM.md
tools/build_renderer_runtime.py
youtube-videos/003-pilot-muskelwachstum/01_script/VOICEOVER-ZUM-KOPIEREN.txt
youtube-videos/003-pilot-muskelwachstum/05_info/phase1-scenes.json
youtube-videos/003-pilot-muskelwachstum/05_info/sentence-visual-plan.json
youtube-videos/003-pilot-muskelwachstum/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
youtube-videos/003-pilot-muskelwachstum/02_bildprompts/label-plan.json
youtube-videos/003-pilot-muskelwachstum/03_pipeline/overlay-plan.json
youtube-videos/003-pilot-muskelwachstum/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

## Nächster echter Test

Beim naechsten Render insbesondere pruefen:
1. Hook klingt wie ein echter neugieriger Einstieg.
2. Remotion-Textoverlays = 0.
3. Flow-Texte sind korrekt und stilistisch einheitlich.
4. keine Sequenz aus fast identischen Muskelquerschnitten.
5. wichtige Mechanismen zeigen Ursache und Folge sichtbar.
6. Tempo bleibt schnell und ohne lange Pausen.
