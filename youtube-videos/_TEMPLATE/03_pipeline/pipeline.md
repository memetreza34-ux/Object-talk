# Bild-Timing-Pipeline

Diese Datei ist die verbindliche Zuordnung zwischen Voiceover und Bildern.

## Grundregel

Jedes Bild beginnt **genau bei dem gesprochenen Wort**, das in `START` steht, und bleibt sichtbar, bis das in `ENDE` definierte Wort gesprochen wurde. Danach beginnt sofort das nächste Bild.

Die Zuordnung erfolgt nach **Wortgrenzen im finalen Skript**, nicht nach geschätzten Sekunden. Dadurch funktioniert die Pipeline auch dann sauber, wenn die Voice-KI etwas schneller oder langsamer spricht.

## Format

| Szene | Bild | START – ab diesem Wort | ENDE – bis zu diesem Wort | Inhalt / Zweck |
|---|---|---|---|---|
| 01 | Bild_01 | „[erstes Wort / erste eindeutige Wortgruppe]“ | „[letztes Wort / letzte eindeutige Wortgruppe]“ | Cover / Einstieg |
| 02 | Bild_02 | „[...]“ | „[...]“ | [...] |
| 03 | Bild_03 | „[...]“ | „[...]“ | [...] |

## Regeln für ChatGPT

Beim Erstellen der finalen Pipeline:
- ausschließlich Wörter verwenden, die **1:1 in `01_script/script.txt` vorkommen**
- für START und ENDE möglichst eindeutige kurze Wortgruppen verwenden, nicht einzelne häufige Wörter wie „und“ oder „der“
- keine Textlücken zwischen zwei Bildern
- keine Überlappungen
- jede Szene aus `02_bildprompts/Google-Flow-Agent-Prompt.md` muss genau einmal vorkommen
- Reihenfolge der Bilder darf nicht verändert werden
- `Bild_01` beginnt mit dem Video und ist die Cover-/Einstiegsszene
- Bildwechsel immer an einer inhaltlich sinnvollen Stelle
- ein Bild nicht so lange stehen lassen, dass der gesprochene Inhalt bereits ein neues Thema behandelt
- ein Bild nicht zu früh wechseln, solange der aktuelle Gedanke noch erklärt wird

## Finale Pipeline

ChatGPT ersetzt diesen Bereich bei jedem Video vollständig.

### Szene 01 / Bild_01
- **START:** „[...]“
- **ENDE:** „[...]“
- **Zeigt:** [...]
- **Bewegung:** [z. B. langsamer Push-in / leichter Pan / statisch]

### Szene 02 / Bild_02
- **START:** „[...]“
- **ENDE:** „[...]“
- **Zeigt:** [...]
- **Bewegung:** [...]

[Fortsetzen bis zur letzten Szene.]

## Abschlussprüfung

Vor Freigabe prüfen:
1. Deckt die Pipeline das Skript vom ersten bis zum letzten gesprochenen Wort vollständig ab?
2. Existiert jede Bildnummer genau einmal?
3. Stimmen Bildnummern und Szenennummern exakt überein?
4. Ist jeder Wechsel inhaltlich sinnvoll?
5. Beginnt kein Bild zu früh oder zu spät?
6. Sind alle START-/ENDE-Wortgruppen exakt im Skript vorhanden?
