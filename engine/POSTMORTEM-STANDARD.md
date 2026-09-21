# Postmortem-Standard – Object-Talk

## Zweck

Nach jedem echten Finalrender wird dokumentiert, was funktioniert hat und was beim nächsten Video anders gemacht werden muss. Dadurch wird das Repository schrittweise besser, statt bekannte Fehler zu wiederholen.

## Datei pro Video

```text
04_export/postmortem.md
```

Das Postmortem wird erst nach Sichtung des echten finalen Videos ausgefüllt. Keine erfundenen Bewertungen ohne Render.

## Pflichtinhalt

### 1. Technische Daten

- Videodauer
- Auflösung / FPS
- Audioformat
- verwendete Bildanzahl
- fehlgeschlagene Flow-Generierungen
- Recovery-Anzahl
- finale Bildanzahl

### 2. Gemessene Stärken

Mindestens drei konkrete Punkte, z. B.:

- besonders verständlicher Mechanismusschritt
- sehr gutes Bild↔Voice-over-Matching
- starke Maßstabsüberleitung
- gute Label-Lesbarkeit
- konsistenter Stil

### 3. Gemessene Schwächen

Mindestens drei konkrete Punkte, z. B.:

- Szene zu lang
- zwei Bilder zu ähnlich
- falscher Maßstab
- KI-Schrift unbrauchbar
- Bild erklärt nur das Thema, nicht den Prozess
- schwache Hook-Komposition
- Voice-over und Visual wechseln zu spät

### 4. Bildfehler

Für jedes problematische Bild:

```text
Bild-ID:
Problem:
Ursache im Prompt/Workflow:
Wie es künftig verhindert wird:
```

### 5. Prompt-Lernen

Festhalten:

- welche Promptformulierungen besonders zuverlässig waren
- welche Formulierungen zu Stil- oder Anatomiefehlern führten
- welche Labels häufig falsch gerendert wurden
- welche Visualtypen Google Flow besonders gut oder schlecht umgesetzt hat

### 6. Pipeline-Lernen

Prüfen:

- funktionierte Bild_01 als Style-Anker?
- funktionierten 5er-Blöcke und Recovery?
- war die Script↔Audio-Ausrichtung korrekt?
- waren Szenengrenzen logisch?
- gab es Probleme beim ZIP-Import oder bei Dateinummern?
- war Remotion ruhig genug, aber nicht statisch/langweilig?

### 7. Konkrete Änderungen

Maximal fünf konkrete Änderungen, die beim nächsten Video umgesetzt werden.

Keine vagen Punkte wie „besser machen“. Jede Änderung muss ausführbar sein.

### 8. Dauerhafte Regeln

Nur Erkenntnisse, die sich über dieses einzelne Video hinaus verallgemeinern lassen, werden anschließend in eine bestehende globale Regeldatei übernommen.

Dabei gilt:

- keine neue Lock-Datei für jede Kleinigkeit
- zuerst bestehende Datei aktualisieren
- `PROJECT_CONTRACT.md` nur bei wirklich dauerhaften Grundregeln ändern
- Widersprüche zu älteren Regeln vermeiden

## Scorecard

Das Postmortem übernimmt den finalen Gesamtwert aus `engine/QUALITY-SCORECARD.md`.

Ein Video mit weniger als 8,0/10 darf zwar analysiert werden, aber nicht als Goldstandard oder Referenzvideo markiert werden.
