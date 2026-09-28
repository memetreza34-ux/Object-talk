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
- sehr klares Cover mit nur einem Titel
- starke Textkontraste
- sinnvolle textfreie Bilder

### 3. Gemessene Schwächen

Mindestens drei konkrete Punkte, z. B.:

- Szene zu lang
- zwei Bilder zu ähnlich
- falscher Maßstab
- KI-Schrift unbrauchbar
- schwacher Textkontrast
- heller Text auf hellem Hintergrund
- unnötiges Label
- zu viele Labels
- Cover enthält Zusatztext
- Frame wirkt informationsüberladen
- Bild erklärt nur das Thema, nicht den Prozess
- schwache Hook-Komposition
- Voice-over und Visual wechseln zu spät

### 4. Cover-Check

Explizit dokumentieren:

- exakt ein sichtbarer Textblock? PASS / FAIL
- nur Titel/Hook? PASS / FAIL
- Zusatzlabels/Unterzeile vorhanden? JA / NEIN
- Titelkontrast stark? PASS / FAIL
- Titel sofort lesbar? PASS / FAIL

### 5. Text-/Informationsdichte-Check

Explizit dokumentieren:

- normale Bilder maximal 2 Labels? PASS / FAIL
- Labels maximal 3 Wörter? PASS / FAIL
- unnötige Labels gefunden? JA / NEIN
- heller Text auf hellem Hintergrund? JA / NEIN
- dunkler Text auf dunklem Hintergrund? JA / NEIN
- überladene Frames gefunden? JA / NEIN
- hätte ein Frame besser auf zwei Bilder verteilt werden sollen? JA / NEIN

### 6. Bildfehler

Für jedes problematische Bild:

```text
Bild-ID:
Problem:
Ursache im Prompt/Workflow:
Wie es künftig verhindert wird:
```

### 7. Prompt-Lernen

Festhalten:

- welche Promptformulierungen besonders zuverlässig waren
- welche Formulierungen zu Stil- oder Anatomiefehlern führten
- welche Labels häufig falsch gerendert wurden
- welche Kontrastformulierungen gut funktioniert haben
- welche Szenen ohne Text besser funktionierten
- welche Visualtypen Google Flow besonders gut oder schlecht umgesetzt hat

### 8. Pipeline-Lernen

Prüfen:

- Cover title-only eingehalten?
- Textkontrast-Gate zuverlässig?
- Informationsdichte-Gate zuverlässig?
- funktionierte die Script↔Audio-Ausrichtung korrekt?
- waren Szenengrenzen logisch?
- wurden überladene Beats früh genug auf mehrere Bilder geteilt?
- gab es Probleme beim ZIP-Import oder bei Dateinummern?
- war Remotion ruhig genug, aber nicht statisch/langweilig?
- erzeugte Remotion garantiert keinen sichtbaren Text?

### 9. Konkrete Änderungen

Maximal fünf konkrete Änderungen, die beim nächsten Video umgesetzt werden.

Keine vagen Punkte wie „besser machen“. Jede Änderung muss ausführbar sein.

### 10. Dauerhafte Regeln

Nur Erkenntnisse, die sich über dieses einzelne Video hinaus verallgemeinern lassen, werden anschließend in eine bestehende globale Regeldatei übernommen.

Dabei gilt:

- keine neue Lock-Datei für jede Kleinigkeit
- zuerst bestehende Datei aktualisieren
- `PROJECT_CONTRACT.md` nur bei wirklich dauerhaften Grundregeln ändern
- Widersprüche zu älteren Regeln vermeiden

## Scorecard

Das Postmortem übernimmt den finalen Gesamtwert aus `engine/QUALITY-SCORECARD.md`.

Ein Video mit weniger als 8,0/10 darf zwar analysiert werden, aber nicht als Goldstandard oder Referenzvideo markiert werden.
