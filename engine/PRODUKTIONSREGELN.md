# Produktionsregeln – Object-Talk Longform

Diese Regeln gelten für **jedes** lange YouTube-Video im Repository.

## 1. Videolänge

- harte Mindestlänge final: **5:00 Minuten**
- normaler Zielbereich: **5:30–8:00 Minuten**
- länger nur, wenn zusätzliche Tiefe echten Mehrwert bringt
- kein künstliches Strecken
- trägt ein Thema keine 5 Minuten sinnvoll, Thema größer formulieren oder verwerfen

Nach der Voice-Erzeugung entscheidet die echte Audiodauer. Unter 300 Sekunden = FAIL.

## 2. Script

`01_script/script.txt` enthält ausschließlich den **final tatsächlich gesprochenen Text**.

Verboten in `script.txt`:

- Szenennummern
- Zeitcodes
- Regieanweisungen
- Klammerbefehle für Editor/Voice
- alternative Formulierungen

Das Script muss 1:1 in die Voice-KI kopierbar sein.

Richtwert für 5–7 Minuten: ungefähr 850–1100 deutsche Wörter, abhängig vom tatsächlichen Sprechtempo. Die Wortzahl ist kein Ersatz für die echte Audiodauer.

Sprachstil:

- kurze verständliche Sätze
- Fachbegriffe direkt erklären
- konkrete Beispiele
- keine unnötigen Wiederholungen
- neugierig und klar, nicht babyhaft

## 3. Semantische Szenen statt Satz-für-Satz

Die Bildanzahl wird **nicht vorher künstlich festgelegt**.

Ablauf:

```text
finales script.txt
→ echte visuelle Sinnwechsel bestimmen
→ daraus Szenen bilden
→ erst danach Anzahl der Bilder kennen
```

Regeln:

- ein Satz darf mehrere Bilder bekommen, wenn die visuelle Aussage wechselt
- mehrere Sätze dürfen ein Bild teilen, wenn dieselbe visuelle Aussage gilt
- keine Füllbilder nur um eine Quote zu erfüllen
- kein Bildwechsel nur weil ein Satzzeichen kommt

## 4. Bildrhythmus als QA

Weil das Video ausschließlich aus Standbildern besteht, muss die visuelle Erzählung lebendig bleiben.

Typische Richtwerte nach der Szenenplanung:

- normale Szene: ca. 6–10 Sekunden
- komplexe biologische Erklärung: ca. 4–8 Sekunden
- ruhige Übersicht: ca. 8–12 Sekunden
- Cover-/Hook-Szene: ca. 4–7 Sekunden
- über 12 Sekunden nur mit bewusstem Grund

Diese Werte sind **Qualitätsprüfung**, keine starre Formel für die Szenenanzahl.

Wenn ein sinnvoller Abschnitt 13 Sekunden braucht, ist das besser als zwei inhaltsleere Bilder. Wenn innerhalb von 5 Sekunden zwei völlig verschiedene visuelle Aussagen kommen, können zwei Bilder nötig sein.

## 5. Bildformat

- 16:9 horizontal
- Ziel: mindestens 1920×1080
- keine vertikalen Reel-Kompositionen
- Hauptmotive und Labels nicht direkt an den Rand
- genug visueller Rand für dezente Pan-/Zoom-Bewegung

## 6. Szenennummerierung

Jede visuelle Szene besitzt genau ein Bild:

```text
Szene 01 = Bild_01
Szene 02 = Bild_02
Szene 03 = Bild_03
...
```

Keine Lücke, keine doppelte Nummer.

`Bild_01` ist immer:

- erster sichtbarer Shot
- Cover-/Hook-Szene
- Grundlage des YouTube-Thumbnails
- Master Style Frame für die konkrete Episode

## 7. Faceless Explainer als visuelle Hauptsprache

Der Kanal ist kein Mascot-/Presenter-Format.

Die Bilder sollen den gesprochenen Mechanismus direkt sichtbar machen.

Bevorzugte Bildtypen:

- anatomische Cutaways
- transparente Körperansichten
- Prozessdarstellungen
- Organ-, Gewebe- und Zellvisualisierungen
- Mikro-/Makro-Übergänge
- Vergleiche und Transformationen
- Ursache→Prozess→Folge-Kompositionen

Personifizierte Lebensmittel oder andere Object-Talk-Figuren sind nur erlaubt, wenn sie einen echten didaktischen Mehrwert haben. Sie dürfen nicht automatisch als dauerhafte Sprecherfigur vor den biologischen Inhalt gesetzt werden.

Richtwert:

- etwa 70 % direkte Erklärbilder
- etwa 20 % Prozess-/Vergleichsbilder
- maximal etwa 10 % optionale Character-/Guide-Momente

Die Werte sind keine starre Quote. Verständlichkeit geht vor.

Biologische Strukturen bekommen normalerweise keine Gesichter.

## 8. Style Anchor und Flow-Produktion

Es gibt zwei mögliche Stilanker:

```text
assets/channel/STYLE_REFERENCE.png = langfristige Kanal-DNA, falls freigegeben
Bild_01.png = Master Style Frame der aktuellen Episode
```

Für jede weitere Bildgeneration wird `Bild_01` als Style-/Continuity-Referenz verwendet, soweit Google Flow dies technisch unterstützt.

Die restlichen Bilder werden in 5er-Blöcken produziert, aber weiterhin einzeln generiert und geprüft.

Fehlgeschlagene Flow-Generationen werden nicht zum globalen Blocker. Sie kommen auf eine Recovery-Liste und werden nach dem regulären Durchlauf gezielt erneut erzeugt.

Details: `FLOW-PRODUCTION-STANDARD.md` und `STYLE-REFERENCE-SYSTEM.md`.

## 9. Beschriftungen

- wichtige Lernstrukturen auf Deutsch
- nur Begriffe, die zum Verständnis helfen
- kurze, lesbare Labels
- eindeutige Pfeile/Linien
- keine unnötigen Fließtexte
- Rechtschreibung und Zuordnung müssen stimmen

Beispiele:

- Zellkern
- Mitochondrium
- Dünndarm
- rote Blutkörperchen
- Nervenzelle

Falsches Label = Bild FAIL; im Flow-Hauptdurchlauf auf Recovery-Liste setzen und später neu erzeugen.

## 10. Bewegung auf Standbildern

Der Renderer darf ausschließlich dezente Bildbewegung verwenden:

- `static`
- `slow-push-in`
- `slow-pull-out`
- `pan-left`
- `pan-right`

Kein hektischer Zoom, kein Wackeln, keine Bildverzerrung.

Ein Bild mit wichtigen Labels darf nicht so bewegt werden, dass Labels abgeschnitten werden.

## 11. Übergänge

Standard ist ein sauberer harter Schnitt.

Keine auffälligen Übergangseffekte ohne inhaltlichen Grund.

## 12. Audio

Das Voiceover ist die Master-Timeline.

Vor Whisper wird es kanonisch als `final-voiceover.wav` vorbereitet.

- Geschwindigkeit 1.0×
- keine künstliche Verlängerung
- keine spätere Änderung nach Wort-Timing-Erzeugung

Details: `AUDIO-REGELN.md`.

## 13. Synchronisierung

Finale Sekundenwerte werden niemals in Phase 1 geschätzt.

Ablauf:

```text
final-voiceover.wav
→ faster-whisper Wortzeiten
→ strikte vollständige Ausrichtung gegen script.txt
→ word-timings.json
→ exakte speech_section-Zuordnung
→ timeline.json
```

Details: `SYNC-WHISPER.md`.

## 14. Gesundheit und Biologie

- Kernclaims vor Produktion prüfen
- Claim-Matrix pro Video führen
- keine erfundenen Wirkungen von Lebensmitteln
- keine individuellen Diagnosen oder Behandlungsempfehlungen
- Korrelation nicht als Kausalität ausgeben
- biologische Prozesse vereinfachen, aber nicht fachlich verfälschen
- Recherche in `05_info/`

Details: `FACT-CHECK-STANDARD.md`.

## 15. Export

Standard:

- MP4
- 1920×1080
- 30 fps
- H.264
- AAC-Audio
- finaler Dateiname `final-video.mp4`
- Untertitel zusätzlich als SRT

## 16. Qualitätsregel

Ein Video ist erst fertig, wenn:

- Phase 1 PASS
- Phase 2 PASS
- Phase 3 PASS
- finales Voiceover mindestens 300 Sekunden
- jedes Bild vorhanden
- gesamte Sprache lückenlos einer Szene zugeordnet
- keine falschen Labels
- keine groben KI-Fehler
- Stil konsistent
- kein unbeabsichtigter Mascot-/Presenter-Schwerpunkt
- finaler technischer QA-Check PASS
- finaler visueller Sichtcheck PASS
- Thema im Themen-Gehirn korrekt aktualisiert
