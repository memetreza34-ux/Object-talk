# Google Flow – einfacher Drei-Ordner-Ablauf

## Sichtbar für den Nutzer: genau drei Ordner
```text
VIDEOORDNER/
├── 01_script/
│   ├── script.txt                  ← einziger Fließtext des Sprechers
│   └── audio/                      ← hier die Sprachdatei einlegen
├── 02_bildprompts/
│   ├── GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
│   └── bilder-zip/                 ← nur fertige NORMALEN Szenenbilder
└── 03_export/
    ├── VIDEO.mp4                   ← entsteht erst nach Render
    ├── COVER.png                   ← separates YouTube-Thumbnail
    ├── CAPTION-YOUTUBE.txt         ← individueller Titel/Beschreibung
    └── UNTERTITEL-MIT-ZEITEN.txt   ← exakte Audio-Zeitabschnitte
```
Alle weiteren Forschungs-, QA- und Pipeline-Dateien liegen versteckt in `.intern/`. Die 008-Verdauungsproduktion bleibt als historisches Altformat unverändert.

## Reihenfolge – KEINE visuellen Vorlagen
1. Ein einziger ausführlicher Flow-TEXTPROMPT enthält drei Coverkandidaten plus alle nummerierten Videoszenen. Keine hochgeladenen JPG-Referenzen und keine zusätzlichen Promptdateien.
2. Flow erzeugt **drei separate Coverbilder**, jedes mit nur exakt dem einen YouTube-Titel. Nutzer wählt 1/2/3. Bis dahin keine normalen Bilder erzeugen.
3. Das gewählte Cover ist **nur** `03_export/COVER.png`, **NICHT Bild_01 und nicht Teil der Videotimeline**. Kein Cover in die Bilder-ZIP.
4. Ab Auswahl unverzüglich **Bild_01 bis Bild_05** als fünf einfache 16:9-Videoszenen erzeugen. Danach Bild_06–10 usw. in max. Fünfergruppen, letzter Batch ggf. kleiner. Kein zweites Startsignal. Flow-Limits transparent angeben und auf „weiter“ fortsetzen.
5. Jedes Bild: **ein einfach erkennbarer biologischer Vorgang**, große klare Strukturen, ruhige freundliche organische Illustration, wechselnde Maßstäbe, mit deutschen Labels (0–2) immer dann, wenn sie helfen. Keine komplizierten Neuronen-Labyrinthe, generischen Schaubild-Poster oder dekorativen Angaben. Sichtbare Produktionsnummern verboten.
6. Alle NORMALEN Videoszenen in die eine ZIP unter `02_bildprompts/bilder-zip/`. Cover separat als PNG.
7. Render nur die normalen Szenen zu `03_export/VIDEO.mp4`, ohne Cover und ohne jeglichen Remotion-Text. Das finale Audio bestimmt den Schnitt.
8. Erst nach Audio-/Whisper-Alignment das gesprochene Skript aus `.intern/03_pipeline/timing/timeline.json` nach `03_export/UNTERTITEL-MIT-ZEITEN.txt` schreiben. Keine geschätzten Zeiten. Optionales SRT liegt intern unter `.intern/`.

## Bildregie nach Feedback aus Video 010

Lesen und konsequent anwenden: `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`, Abschnitt „Neue verbindliche Bildregie ab Video 011“. Mechanismen, Cutaways, Makros und echte Erklärung statt weiterer voller Menschenfiguren als Standard. Mehr kontrollierte Farben und bessere Komposition. Das reine Textprompt-Prinzip, die 3 Cover und die Fünfergruppen bleiben unverändert.

## QA
Die Datei `COVER.png` gehört nicht in das MP4. `Bild_01` ist die erste echte Szene, nicht das Cover. 0–2 wirklich notwendige Kurzlabels, gut lesbar, korrekte deutsche Worte, 16:9. Fehlende Bilder oder Medien nicht als fertig ausgeben.

## Technische Kompatibilität
`tools/prepare_phase3.py`, `tools/export_subtitles.py` und Validatoren erkennen neue `.intern/`-Projekte automatisch. Alte 008-Projekte dürfen ihren historischen 5-Ordner-Aufbau weiterverwenden, ohne rückwirkende Migration.


## Phase-1-Handoff – ZWEI DIREKTLINKS ANTWORTEN (verbindlich)

**Sobald Phase 1 eines Videos nach tatsächlicher Erstellung und Prüfung erfolgreich abgeschlossen ist, MUSS die Antwort von ChatGPT oder einem anderen Chat-Agenten sofort diese zwei ANKLICKBAREN Links zum AKTUELLEN Video enthalten** (wie die zwei Aktionslinks im Beispiel des Nutzers):

- **Google-Flow-Prompt öffnen** → `https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/<VIDEOORDNER>/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
- **Voice-over-Skript öffnen** → `https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/<VIDEOORDNER>/01_script/script.txt`

`<VIDEOORDNER>` zwingend durch den tatsächlich gerade erstellten Videoordner ersetzen; echte Pfade/Dateiinhalte vor dem Link überprüfen. Niemals die Template-Platzhalter oder Links eines älteren Videos ausgeben. Links als Markdown-Klicklinks oder als zwei bedienbare Öffnen-Schaltflächen in der Chat-Antwort präsentieren, **nicht nur Dateipfade, einen allgemeinen Repository-Link oder eine Erklärung**. Beide Dateien öffnen die komplette Datei in GitHub und sind auch im mobilen Browser/Tablet zugänglich (bei privaten Repos mit GitHub-Anmeldung). Nutzer kann Text von dort 1:1 in Google Flow bzw. seine Voice-KI kopieren. Ein GitHub-Dateilink öffnet **nicht automatisch** Google Flow selbst; nichts anderes behaupten.

Die Übergabe darf KEINE zusätzliche Bestätigung abfragen und soll direkt nach dem Phase-1-Abschluss erfolgen. Keine weiteren sichtbaren Dateien im Videoordner erzeugen; `01_script/script.txt` und der eine Flow-TXT reichen. Wenn eine der Dateien fehlt, unvollständig oder ein Template ist, Phase 1 NICHT als fertig behaupten und keine falschen Links ausgeben. Nach erfolgreichem `python tools/validate_planning_v2.py youtube-videos/<VIDEOORDNER>` druckt der Validator exakt diese zwei Links als Handoff-Vorlage.

