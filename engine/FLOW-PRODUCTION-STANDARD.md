# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik fuer Google Flow.

## 1. Referenz zuerst

Referenzreihenfolge:
1. `assets/channel/STYLE_REFERENCE.png`
2. `Bild_01.png`
3. Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Ein Satz wie `Using Bild_01 as reference` ersetzt niemals das echte Anhaengen von `Bild_01.png`.

Solange `STYLE_REFERENCE.png` fehlt:
- nur `Bild_01` darf ohne kanalweite Bildreferenz entstehen
- Bild_01 wird besonders streng geprueft
- danach muss das eine ausgewaehlte Bild_01 bei jeder Folgegeneration wirklich angehaengt werden

## 2. Dauerhafte Flow-Regeln

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
```

## 3. Verbindliche Explainer-Bildwelt

Fuer Biologie-/Erklaerszenen gilt:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:
**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Verbindlich:
- klar animiert / illustriert
- nicht fotorealistisch
- weich gerundete vereinfachte Formen
- matte bis leicht satinierte Oberflaechen
- weiche Farbverlaeufe
- subtile Schatten
- leichte Tiefenstaffelung
- ruhige helle Hintergruende
- eine DOMINANTE Hauptaussage pro Bild
- gelegentlich ein sinnvoller Zusatzdetailpunkt
- wenige Objekte
- Klarheit wichtiger als Detailreichtum

Semantische Farben:
- O2 = Cyan / Tuerkis
- rote Blutkoerperchen = tiefes warmes Rot
- Blutgefaesse = Coral / Rot
- Organe = Peach / Coral
- Muskelzellen = Orange / Apricot
- CO2 = weiches Violett
- ATP = warmes Gelb / Gold
- Hintergrund = Creme / helles Blau / weiches Beige

Harte Stilverbote:
- Photorealismus
- Medical-CGI / Anatomiesoftware
- nasses Fleisch / Gewebe
- Mikroskop-Fotorealismus
- dunkle violette Sci-Fi-Mikrowelt
- Weltraum / Galaxy
- Human-Presenter
- Torso-Mannequin
- ueberladene Infografik
- billiger Toy-Look

## 4. Visuelle Dichte

Der Kanal soll nicht wie eine Diashow wirken.

Darum gilt:
- normale Bildhaltezeit im fertigen Schnitt meistens 3–6 Sekunden
- harte Obergrenze fuer ein einzelnes Standbild: 7 Sekunden
- ist ein Sprachabschnitt laenger oder enthaelt zwei echte Lehrbeats, wird er in mehrere NEUE Szenen mit NEUEN Bildnummern geteilt
- dasselbe Bild darf niemals als Loesung fuer einen langen Abschnitt zweimal verwendet werden
- lieber 1–3 zusaetzliche eindeutige Bilder als ein Bild 10–20 Sekunden stehen lassen

Etwa 20–30 % der Szenen duerfen etwas informativer sein, wenn der Hauptpunkt klar bleibt. Erlaubt ist genau ein sinnvoller Zusatzdetailpunkt, z. B. ein Zielobjekt, ein Vorher/Nachher-Hinweis oder ein kleines Detailfenster. Keine Dashboard- oder Posteroptik.

## 5. Asset-IDs sind nur Metadaten

`Bild_01`, `Bild_19`, `Scene 19`, `IMAGE 19`, Dateinamen und Produktionsnummern duerfen niemals als sichtbarer Bildtext interpretiert werden.

Hard FAIL:
- `Bild 19` sichtbar im Bild
- `Bild_19` sichtbar im Bild
- `BILD_12 – O2 BINDET` sichtbar im Bild
- `Scene 19` / `IMAGE 19` sichtbar im Bild
- Dateiname oder sonstige interne Produktionskennung sichtbar im Bild

## 6. Sichtbarer Text ist Whitelist-basiert

Vor jeder Generation muss eine `ALLOWED_VISIBLE_TEXT`-Liste feststehen.

Cover:
- Whitelist = nur die exakte deutsche Hook

Normale Szene:
- Whitelist = exakt die fuer diese Szene geplanten Labels
- bei 0 Labels darf kein Wort sichtbar sein

Nicht auf der Whitelist = FAIL. Dazu gehoeren insbesondere:
- Bild-/Szenennummern
- Prompt-Ueberschriften
- Szenentitel
- erfundene Erklaertexte
- englische Woerter
- zusaetzliche Anatomie-Labels
- KI-Gibberish

Bei falscher Flow-Schreibweise:
1. regenerieren
2. maximal einen weiteren Text-Versuch
3. danach exakter Remotion-Fallback

## 7. Object-Talk Character Mode

Fuer sprechende Lebensmittel / Alltagsobjekte bleibt der hochwertige stilisierte 3D-Character-Look erlaubt.
Dieser Modus darf nicht automatisch auf Organe, Molekuele und Zellen uebertragen werden.

## 8. Bild_01 – einzige Varianten-Ausnahme

`Bild_01` ist Cover, erster Shot, Episode-Master-Frame und Referenz fuer Folgebilder.

Nur fuer Bild_01 sind mehrere kreative Varianten erlaubt.

Ablauf:
1. Agent Instructions laden
2. STYLE_REFERENCE anhaengen, falls vorhanden
3. nur Bild_01 bearbeiten
4. bis zu 3 klar unterschiedliche Cover-Kandidaten erzeugen
5. ungeeignete Varianten automatisch verwerfen
6. verbleibende gute Kandidaten dem Nutzer zeigen
7. Nutzer waehlt genau einen Cover-Kandidaten
8. dieser Kandidat wird `Bild_01.png`
9. alle nicht gewaehlten Cover-Kandidaten werden geloescht/verworfen
10. erst danach mit Bild_02 fortfahren

Im finalen Set darf genau EIN `Bild_01.png` existieren.

Bild_01 Hard FAIL:
- Hook fehlt / falsch
- Zusatzlabels auf Cover
- sichtbare Bild-/Szenennummer oder Prompt-Ueberschrift
- photorealistisch / medizinisch
- Mensch / Presenter / Torso-Mannequin
- kosmisch / Sci-Fi
- ueberladen
- Thema nicht sofort erkennbar

## 9. Folgegenerationen – genau ein Output pro Bildnummer

Fuer `Bild_02` bis `Bild_NN` gilt strikt:
- jede Szene einzeln bearbeiten
- genau EINEN Kandidaten pro Generierungsversuch anfordern
- keine kreativen Mehrfachvarianten anlegen
- niemals zwei Versionen derselben Bildnummer behalten
- kein `Bild_05_A`, `Bild_05_B`, `Bild_05_v2`, `Bild_05_final2`

Wenn ein Bild FAIL ist:
1. gleiche Bildnummer behalten
2. Fehler notieren
3. Prompt gezielt korrigieren
4. neue Version derselben Bildnummer erzeugen
5. alte FAIL-Version verwerfen
6. nur die akzeptierte Version behalten

Wenn Flow technisch mehrere Outputs fuer einen Request liefert:
- nur den besten PASS-Kandidaten behalten
- alle anderen sofort verwerfen
- erst danach zur naechsten Bildnummer wechseln

## 10. Szenenprompt-Schema

```text
1. DOMINANT TEACHING IDEA
2. OPTIONAL SUPPORTING DETAIL
3. MAIN SUBJECT
4. START / END
5. MOVEMENT / CHANGE
6. SIMPLE SPATIAL LAYOUT
7. SOFT-3D STYLE CONTINUITY
8. ALLOWED_VISIBLE_TEXT
9. FORBIDDEN ELEMENTS
```

Eine Ueberschrift wie `BILD_19 – HAEMOGLOBIN GIBT O2 AB` ist reine Prompt-Struktur und darf nie gerendert werden.

## 11. Wiederkehrende Elemente Pilot 001

- O2 = Cyan / Tuerkis
- CO2 = weiches Violett
- rote Blutkoerperchen = tiefes warmes Rot
- Haemoglobin = Burgunder
- Gefaesse = Coral / Rot
- Organe = Peach / Coral
- Muskelzellen = Apricot / Orange
- ATP = Gelb / Gold

## 12. QA

`image-review.json` erst nach Sichtpruefung des echten Bildes aktualisieren.

Pflichtkriterien:
- scientific_accuracy
- voiceover_match
- immediate_clarity
- style_continuity
- composition
- label_accuracy, wenn Labels vorgesehen
- visible_text_whitelist = PASS
- no_visible_asset_id = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check
- scene_difference
- overall_score

Jeder zentrale Score mindestens 8/10.
Hard FAIL kann nicht durch Durchschnittsscore ausgeglichen werden.

## 13. Recovery

Bei FAIL:
1. gleiche Bildnummer behalten
2. konkreten Fehler notieren
3. nur diesen Fehler im Prompt korrigieren
4. bis zu 3 Neuversuche
5. vorherige FAIL-Versionen nicht im finalen Set behalten

Recovery bedeutet ERSETZEN, nicht ZUSAETZLICH SAMMELN.

## 14. Finaler Bilderordner

```text
<video-id>_bilder/
```

Finaler Ordner muss exakt enthalten:
- `Bild_01.png` bis `Bild_NN.png`
- jede Nummer exakt einmal
- keine Luecken
- keine Duplikate
- keine Cover-Alternativen
- keine FAIL-Versionen
- keine Temp-Dateien

Vor ZIP/Export:
1. erwartete Bildanzahl bestimmen
2. Dateien zaehlen
3. Nummern auf Luecken pruefen
4. Nummern auf Duplikate pruefen
5. Cover-Alternativen loeschen
6. Temp-/FAIL-Dateien loeschen
7. erst danach ZIP erzeugen

## 15. Harte Verbote

Flow darf niemals:
- Asset-/Bild-/Szenennummern sichtbar rendern
- Prompt-Ueberschriften sichtbar rendern
- Text ausserhalb der Whitelist erzeugen
- nur erwaehnte Referenzen als angehaengt behandeln
- mehrere retained Varianten einer normalen Szene behalten
- unselektierte Covervarianten im finalen Set behalten
- dasselbe Bild zweimal fuer verschiedene Zeitabschnitte benutzen
- ein Standbild laenger als 7 Sekunden einplanen
- Explainer-Szenen in Medical-CGI oder Photorealismus driften lassen
- semantische Farben grundlos aendern
- Cover-Zusatzlabels erzeugen
- nach Bild_01 weitere Freigaben verlangen
