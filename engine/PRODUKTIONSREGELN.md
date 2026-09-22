# Produktionsregeln – Object-Talk Longform

Diese Regeln gelten für **jedes** lange YouTube-Video im Repository.

## 1. Videolänge

- harte Mindestlänge final: **5:00 Minuten**
- normaler Zielbereich: **5:30–8:00 Minuten**
- länger nur, wenn zusätzliche Tiefe echten Mehrwert bringt
- kein künstliches Strecken
- trägt ein Thema keine 5 Minuten sinnvoll, Thema größer formulieren oder verwerfen

Nach der Voice-Erzeugung entscheidet die echte Audiodauer. Unter 300 Sekunden = FAIL, außer dokumentierter Testmodus.

## 2. Script

`01_script/script.txt` enthält ausschließlich den final tatsächlich gesprochenen Text.

Verboten:

- Szenennummern
- Zeitcodes
- Regieanweisungen
- Klammerbefehle für Editor/Voice
- alternative Formulierungen

Das Script muss 1:1 in die Voice-KI kopierbar sein.

Sprachstil:

- kurze verständliche Sätze
- Fachbegriffe direkt erklären
- konkrete Beispiele
- keine unnötigen Wiederholungen
- neugierig und klar, nicht babyhaft

## 3. Semantische Szenen statt Satz-für-Satz

Die Bildanzahl wird nicht künstlich vorher festgelegt.

```text
finales script.txt
→ echte visuelle Sinnwechsel bestimmen
→ daraus Szenen bilden
→ erst danach Anzahl der Bilder kennen
```

- ein Satz darf mehrere Bilder bekommen, wenn die visuelle Aussage wechselt
- mehrere Sätze dürfen ein Bild teilen, wenn dieselbe visuelle Aussage gilt
- keine Füllbilder
- kein Bildwechsel nur wegen eines Satzzeichens

## 4. Bildrhythmus als QA

Das Format lebt von hoher visueller Dichte.

Richtwerte:

- Hook / schneller Einstieg: **2–4 Sekunden**
- normale Erklärszene: **4–6 Sekunden**
- komplexer biologischer Mikroschritt: **3–5 Sekunden**
- ruhige Übersicht / Zusammenfassung: **6–8 Sekunden**
- über **8 Sekunden** nur mit bewusstem Grund

Ein neues Bild ist sinnvoll, wenn sich mindestens eines ändert:

- Ort
- Maßstab
- Organ/Struktur
- Zustand
- Prozessschritt
- Vergleich
- zentrale visuelle Aussage

Lange Standzeiten dürfen nicht allein durch Zoom/Pan kaschiert werden.

Bei einem ca. 2-Minuten-Test können 24–30 echte Erklärbilder sinnvoll sein. Bei Longform ergibt sich die Bildzahl aus dem Script.

## 5. Bildformat

- 16:9 horizontal
- mindestens 1920×1080
- Hauptmotive, Hook und Labels nicht direkt an den Rand
- genug visueller Rand für dezente Bewegung

## 6. Szenennummerierung und Bild_01

```text
Szene 01 = Bild_01
Szene 02 = Bild_02
Szene 03 = Bild_03
...
```

Keine Lücke, keine doppelte Nummer.

`Bild_01` ist immer gleichzeitig:

- Cover
- erster sichtbarer Shot
- Hook-Szene
- Master Style Frame der Episode
- Stilvorlage für alle späteren Bilder

Bild_01 wird besonders ausführlich beschrieben und enthält eine **kurze starke deutsche Hook-Zeile**, die sofort zeigt, worum es im Video/Reel geht.

Hook-Regel:

- normalerweise 3–7 Wörter
- maximal zwei kurze Zeilen
- kein irreführender Clickbait
- auch als Cover lesbar

## 7. Verbindliche visuelle Hauptsprache

Der Kanal ist kein Mascot-/Presenter-Format.

Die Welt ist:

- **stark stilisierte hochwertige 3D-Animationsfilm-Optik**
- deutlich animiert statt fotorealistisch
- weiche gerundete Formen
- vereinfachte, aber fachlich erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige Materialien und klare Tiefenwirkung
- familienfreundlich und modern, aber nicht babyhaft
- kein medizinischer Fotorealismus
- kein Anime, Comic, Gore oder Horror-Look

Bevorzugte Bildtypen:

- anatomische Cutaways
- transparente Körperansichten
- Prozessdarstellungen
- Organ-, Gewebe-, Zell- und Organellvisualisierungen
- Mikro-/Makro-Übergänge
- Vergleiche und Transformationen
- Ursache→Prozess→Folge-Kompositionen

Personifizierte Figuren sind nur erlaubt, wenn sie echten didaktischen Mehrwert haben.

Biologische Strukturen bekommen normalerweise keine Gesichter.

## 8. Google-Flow-Prompt-Sprache

- Flow-Prompt-Anweisungen immer **Englisch**
- jeder sichtbare Text im Bild immer **Deutsch**
- kein englischer sichtbarer Text
- kein KI-Gibberish

Prompt-Länge:

- Bild_01 bewusst ausführlich und präzise
- Folgeprompts so kurz wie möglich, so genau wie nötig
- Folgeprompt normalerweise 2–5 Sätze
- globalen Stilblock nicht in jedem Szenenprompt vollständig wiederholen

Jeder Folgeprompt nennt nur:

1. konkrete Szene
2. sichtbaren Prozess
3. wichtige Komposition/Perspektive
4. deutsche Labels

## 9. Style Anchor und Flow-Produktion

Stilanker:

```text
assets/channel/STYLE_REFERENCE.png = langfristige Kanal-DNA, falls freigegeben
Bild_01.png = Master Style Frame der aktuellen Episode
```

Produktionsablauf:

1. kompletten Flow-Auftrag lesen
2. nur Bild_01 erzeugen
3. Bild_01 prüfen
4. Nutzerfreigabe abwarten
5. Bild_01 für jede spätere Generation als Style-/Continuity-Referenz verwenden
6. restliche Bilder in 5er-Blöcken erzeugen

Blöcke:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
Bild_22–26
Bild_27–31
...
```

Innerhalb jedes Blocks jedes Bild einzeln erzeugen und prüfen. Nach jedem Block Stil-/Nummerierungscheck.

Fehlgeschlagene Generierungen kommen auf eine Recovery-Liste und werden am Ende gezielt erneut erzeugt.

Details: `FLOW-PRODUCTION-STANDARD.md` und `STYLE-REFERENCE-SYSTEM.md`.

## 10. Beschriftungen

**Jedes Bild beschriftet die wichtigsten sichtbaren Dinge.**

Richtwert:

- normalerweise 1–3 kurze deutsche Labels
- nur Schlüsselstrukturen oder Schlüsselprozesse
- eindeutige Pfeile/Linien bzw. klare räumliche Zuordnung
- keine unnötigen Fließtexte
- Rechtschreibung und Zuordnung müssen stimmen
- keine englischen Labels

Beispiele:

- `Lunge`
- `Lungenbläschen`
- `Sauerstoff`
- `Rote Blutkörperchen`
- `Hämoglobin`
- `Mitochondrium`

Falsches oder unlesbares Label = Bild FAIL. Bei wiederholtem Flow-Schriftfehler saubere Bildvariante erzeugen und exakt denselben deutschen Begriff später in Remotion setzen.

## 11. Bewegung auf Standbildern

Erlaubt:

- `static`
- `slow-push-in`
- `slow-pull-out`
- `pan-left`
- `pan-right`

Kein hektischer Zoom, Wackeln oder Verzerren. Labels dürfen durch Bewegung nicht abgeschnitten werden.

## 12. Übergänge

Standard ist ein sauberer harter Schnitt. Keine auffälligen Übergangseffekte ohne inhaltlichen Grund.

## 13. Audio

Das Voiceover ist die Master-Timeline.

Vor Whisper wird es als `final-voiceover.wav` vorbereitet.

- Geschwindigkeit 1.0×
- keine künstliche Verlängerung
- keine spätere Änderung nach Wort-Timing-Erzeugung

Details: `AUDIO-REGELN.md`.

## 14. Synchronisierung

Finale Sekundenwerte werden niemals in Phase 1 geschätzt.

```text
final-voiceover.wav
→ faster-whisper Wortzeiten
→ strikte vollständige Ausrichtung gegen script.txt
→ word-timings.json
→ exakte speech_section-Zuordnung
→ timeline.json
```

Details: `SYNC-WHISPER.md`.

## 15. Gesundheit und Biologie

- Kernclaims vor Produktion prüfen
- Claim-Matrix pro Video führen
- keine erfundenen Wirkungen
- keine individuellen Diagnosen oder Behandlungsempfehlungen
- Korrelation nicht als Kausalität ausgeben
- Prozesse vereinfachen, aber nicht fachlich verfälschen
- Recherche in `05_info/`

Details: `FACT-CHECK-STANDARD.md`.

## 16. Export

- MP4
- 1920×1080
- 30 fps
- H.264
- AAC-Audio
- finaler Dateiname `final-video.mp4`
- Untertitel zusätzlich als SRT

## 17. Qualitätsregel

Ein Video ist erst fertig, wenn:

- Phase 1 PASS
- Phase 2 PASS
- Phase 3 PASS
- normales finales Voiceover mindestens 300 Sekunden oder dokumentierte Testausnahme
- jedes Bild vorhanden
- gesamte Sprache lückenlos einer Szene zugeordnet
- Bild_01 als Cover/Hook/Style-Anker funktioniert
- wichtige Dinge in jedem Bild korrekt auf Deutsch beschriftet
- kein englischer sichtbarer Text
- keine groben KI-Fehler
- stark stilisierte 3D-Welt konsistent
- kein unbeabsichtigter Mascot-/Presenter-Schwerpunkt
- finaler technischer QA-Check PASS
- finaler visueller Sichtcheck PASS
- Thema im Themen-Gehirn korrekt aktualisiert
