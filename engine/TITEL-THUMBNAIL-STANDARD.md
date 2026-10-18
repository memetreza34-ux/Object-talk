# Titel-, Cover- und Beschreibungs-Standard – Lebenslogik

Gilt ab Video 011. Begründung: `engine/KANAL-ANALYSE-2026-10.md` §4–5.

## Kanalname
Für Zuschauer heißt der Kanal immer **Lebenslogik**. „Object-Talk“ ist nur der technische Repo-Name, „FoodSpricht“ ist nicht mehr aktiv. In Captions, Hashtags und Skripten nie „Object-Talk“ schreiben.

## Titel (YouTube)
- 40–60 Zeichen, wichtigster Suchbegriff in der ersten Hälfte (z. B. „Hunger“, „Verdauung“, „Pizza“).
- Eine der Formen: **konkretes Objekt + Reise** („Die Reise einer Pizza durch deinen Körper“), **Du-Problem** („Warum du kurz nach dem Essen schon wieder Hunger hast“), **Behauptung/Mythos** („Warum dein Magen sich nicht selbst verdaut“), **Vergleich** („Croissant vs. Kartoffel: Was dich wirklich satt macht“).
- Kein „einfach erklärt“ als Standardanhang, keine Clickbait-Lüge: Der Einstieg des Videos muss das Versprechen in den ersten 15 Sekunden einlösen.
- Im Storyboard immer drei Alternativen in `youtube.title_alternatives` hinterlegen (landen in `.intern/05_info/TITEL-UND-COVER-OPTIONEN.md`).

## Cover-Text (einziger Textblock)
- 2–4 Wörter, höchstens 5. Er **ergänzt** den Titel und wiederholt ihn nicht.
  - gut: Titel „Warum du kurz nach dem Essen schon wieder Hunger hast“ + Cover „Hunger trotz Essen?“
  - gut: Titel „Die Reise einer Pizza durch deinen Körper“ + Cover „Wohin verschwindet sie?“
  - schlecht: Titel „Warum du nach dem Essen so schnell wieder Hunger hast“ + Cover „Warum bist du wieder hungrig?“
- Alle drei Cover-Optionen tragen denselben Text, damit nur die Bildidee verglichen wird.

## Cover-Bild
- Ein großes Hauptmotiv (mindestens 60 % der Fläche), maximal 3 Elemente, starker Hell-Dunkel-Kontrast, auf dem Handy in Daumengröße lesbar.
- Zeigt das Paradox oder das Objekt der Reise (Croissant vs. Kartoffel, Pizza im Körper), nicht eine ratlose Person.
- Die zwei nicht gewählten Cover lokal behalten und mit YouTube „Testen und vergleichen“ testen, sobald die Funktion im Kanal verfügbar ist.

## Beschreibung (`CAPTION-YOUTUBE.txt`)
1. **Erste zwei Zeilen = Hook** (erscheinen in der Suche): Paradox oder Frage plus Versprechen.
2. Was der Zuschauer lernt, mit den konkreten Highlights (Zahlen, Mythos, Experiment).
3. **KAPITEL**: werden nach dem Render automatisch mit echten Zeiten eingesetzt (`tools/export_chapters.py`). Kapitelnamen sind die Storyboard-Kapiteltitel, also zuschauerfreundlich formulieren.
4. **Quellen (Auswahl)**: Studien kurz nennen (Autor, Jahr, Thema).
5. Ein Satz Bildungshinweis (keine medizinische Beratung).
6. **HASHTAGS:** genau 3–5, der letzte ist `#Lebenslogik`.

## Endscreen
Jedes Video endet mit einer Brücke zu einem Partnervideo. Dieses Video im YouTube-Endscreen verlinken, damit Zuschauer im Kanal bleiben.
