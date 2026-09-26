# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik fuer Google Flow.

## 1. Referenz zuerst – aber textfrei

Normale Szenen duerfen keine Typografie vom Cover erben.

Referenzreihenfolge fuer `Bild_02` bis `Bild_NN`:
1. `assets/channel/STYLE_REFERENCE.png` – textfrei
2. projektspezifisches `EPISODE_STYLE_REFERENCE.png` – textfrei
3. Objekt-/Character-Referenzen – textfrei, sofern moeglich
4. konkreter Szenenprompt

`Bild_01.png` ist ein texttragendes Cover und wird NICHT als normale Szenenreferenz angehaengt.

Wenn `STYLE_REFERENCE.png` fehlt:
- vor dem Cover eine separate textfreie `EPISODE_STYLE_REFERENCE.png` erzeugen
- diese Datei ist nur Produktionsreferenz und keine nummerierte Videoszene
- Cover und normale Szenen orientieren sich an dieser textfreien Referenz

Eine textliche Erwaehnung einer Referenz ersetzt niemals das echte Attachment.

## 2. Verbindliche Explainer-Bildwelt

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
- wenige Objekte
- Klarheit wichtiger als Detailreichtum

## 3. Visuelle Dichte und Abwechslung

Der Kanal soll nicht wie eine Diashow wirken und nicht aus einer Reihe fast identischer Objektportraits bestehen.

Harte Regeln:
- normale Bildhaltezeit meistens 3–6 Sekunden
- harte Obergrenze pro Standbild: 7 Sekunden
- lange oder mehrteilige Speech-Beats werden in neue Szenen mit neuen Bildnummern geteilt
- dasselbe Bild nie zweimal benutzen, um Zeit zu fuellen
- lieber mehrere eindeutige Bilder als ein Bild zu lange halten

Visual-Mix:
- mindestens etwa **60 %** der normalen Explainerframes zeigen Prozess, Beziehung, Weg, Ursache/Wirkung, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander
- danach Prozess-, Beziehungs-, Weg-, Ursache/Wirkung-, Vergleichs- oder Kontextbild
- ca. **20–35 %** wichtiger Mechanismus-/Summary-Frames duerfen EINEN sinnvollen Zusatzdetailpunkt enthalten

Nachbarschaftsregel:
- benachbarte Szenen unterscheiden sich in mindestens ZWEI Punkten:
  - Kameramassstab
  - raeumliches Layout
  - Hauptmotiv
  - Prozessrichtung
  - Hintergrundkontext
  - Visual-Typ

Nicht erlaubt:
- gleiche Uebersichtskomposition spaeter einfach wiederholen
- gleiche Muskelquerschnitt-/Zell-/Gefäss-/Myofibrillen-Komposition mehrfach fast identisch verwenden
- schwaches/zu leeres Bild spaeter mit Textoverlay retten

## 4. Cover-Hook ist einmalig

Die exakte Cover-Hook darf ausschliesslich auf `Bild_01` erscheinen.

Fuer `Bild_02` bis `Bild_NN` ist sie ein Hard FAIL.

Verboten nach Bild_01:
- Cover-Hook als erneute Ueberschrift
- Cover-Hook als Kapiteltrenner
- Cover-Hook als dekorativer Hintergrundtext
- gekuerzte oder nahezu identische Wiederholung

## 5. Asset-IDs sind nur Metadaten

`Bild_01`, `Bild_19`, `Scene 19`, `IMAGE 19`, Dateinamen und Produktionsnummern duerfen niemals sichtbar im Bild erscheinen.

Hard FAIL:
- `Bild 19`
- `Bild_19`
- `BILD_12 – ...`
- `Scene 19` / `IMAGE 19`
- Dateiname / Asset-ID / Prompttitel

## 6. Sichtbarer Text – nur Google Flow

Vor jeder Generation muss eine `ALLOWED_VISIBLE_TEXT`-Liste feststehen.

Cover:
- nur die exakte deutsche Hook

Normale Szene:
- exakt die fuer diese Szene geplanten Labels oder explizit geplanten kurzen Flow-Kapitelbegriffe
- bei 0 Eintraegen: kein sichtbares Wort
- Cover-Hook niemals in normaler Szene

Alles andere = FAIL.

Bei falscher Flow-Schreibweise:
1. Bild ablehnen
2. in Flow regenerieren oder korrigieren
3. erst akzeptieren, wenn Text stimmt

**Kein Remotion-Fallback.**

Remotion darf fuer neue Object-Talk-Videos keinen sichtbaren Text erzeugen.

## 7. Object-Talk Character Mode

Fuer sprechende Lebensmittel / Alltagsobjekte bleibt der hochwertige stilisierte 3D-Character-Look erlaubt.
Dieser Modus darf nicht automatisch auf Organe, Molekuele und Zellen uebertragen werden.

## 8. Bild_01 – einzige nummerierte Varianten-Ausnahme

Nur fuer Bild_01 sind mehrere kreative Varianten erlaubt.

Ablauf:
1. textfreie Style-Referenz bereitstellen
2. bis zu 3 klar unterschiedliche Cover-Kandidaten erzeugen
3. Nutzer waehlt genau einen
4. dieser Kandidat wird `Bild_01.png`
5. alle nicht gewaehlten Cover-Kandidaten loeschen/verwerfen
6. Cover NICHT als normale Szenenreferenz verwenden
7. mit `Bild_02` auf Basis der textfreien Style-Referenz fortfahren

Im finalen Set darf genau EIN `Bild_01.png` existieren.

## 9. Folgegenerationen – genau ein Output pro Bildnummer

Fuer `Bild_02` bis `Bild_NN` gilt strikt:
- textfreie Style-Referenz wirklich anhaengen
- texttragendes Cover nicht anhaengen
- jede Szene einzeln bearbeiten
- genau EINEN Kandidaten pro Generierungsversuch anfordern
- niemals zwei Versionen derselben Bildnummer behalten
- keine `_A`, `_B`, `v2`, `final2`, `copy`, `new`

Wenn ein Bild FAIL ist:
1. gleiche Bildnummer behalten
2. Fehler notieren
3. Prompt gezielt korrigieren
4. neue Version derselben Bildnummer erzeugen
5. alte FAIL-Version verwerfen
6. nur die akzeptierte Version behalten

## 10. Szenenprompt-Schema

```text
1. DOMINANT TEACHING IDEA
2. OPTIONAL SUPPORTING DETAIL
3. MAIN SUBJECT
4. START / END
5. MOVEMENT / CHANGE
6. SIMPLE SPATIAL LAYOUT
7. COMPOSITION DIFFERENCE VS PREVIOUS AND NEXT SCENE
8. AT LEAST TWO VISUAL DIMENSIONS CHANGED VS ADJACENT SCENE
9. SOFT-3D STYLE CONTINUITY
10. ALLOWED_VISIBLE_TEXT
11. FORBIDDEN ELEMENTS
12. COVER_HOOK_FORBIDDEN = true for Bild_02+
```

## 11. QA

`image-review.json` erst nach Sichtpruefung des echten Bildes aktualisieren.

Pflichtkriterien:
- scientific_accuracy
- voiceover_match
- immediate_clarity
- style_continuity
- composition
- visual_novelty
- information_value
- label_accuracy, wenn Labels vorgesehen
- visible_text_whitelist = PASS
- cover_hook_isolated = PASS
- no_visible_asset_id = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check
- scene_difference
- overall_score

Jeder zentrale Score mindestens 8/10.

Hard FAIL kann nicht durch Durchschnittsscore ausgeglichen werden.

## 12. Recovery

Bei FAIL:
1. gleiche Bildnummer behalten
2. konkreten Fehler notieren
3. nur diesen Fehler im Prompt korrigieren
4. bis zu 3 Neuversuche
5. vorherige FAIL-Versionen nicht im finalen Set behalten

Recovery bedeutet ERSETZEN, nicht ZUSAETZLICH SAMMELN.

## 13. Finaler Bilderordner

Finaler Ordner muss exakt enthalten:
- `Bild_01.png` bis `Bild_NN.png`
- jede Nummer exakt einmal
- keine Luecken
- keine Duplikate
- keine Cover-Alternativen
- keine FAIL-Versionen
- keine Temp-Dateien

Textfreie Referenzen liegen ausserhalb dieses Sets.

## 14. Harte Verbote

Flow darf niemals:
- Cover-Hook nach Bild_01 wiederholen
- texttragendes Cover als normale Szenenreferenz verwenden
- Asset-/Bild-/Szenennummern sichtbar rendern
- Prompt-Ueberschriften sichtbar rendern
- Text ausserhalb der Whitelist erzeugen
- nur erwaehnte Referenzen als angehaengt behandeln
- mehrere retained Varianten einer normalen Szene behalten
- unselektierte Covervarianten im finalen Set behalten
- dasselbe Bild zweimal fuer verschiedene Zeitabschnitte benutzen
- ein Standbild laenger als 7 Sekunden einplanen
- drei oder mehr isolierte Einzelobjekt-Portraits am Stueck produzieren, wenn ein Prozess-/Beziehungsbild moeglich ist
- Explainer-Szenen in Medical-CGI oder Photorealismus driften lassen
- semantische Farben grundlos aendern
- Cover-Zusatzlabels erzeugen

Remotion darf niemals:
- sichtbaren Text erzeugen
- Flow-Texte ersetzen
- Kapitelueberschriften / Keywords / Callouts einblenden
