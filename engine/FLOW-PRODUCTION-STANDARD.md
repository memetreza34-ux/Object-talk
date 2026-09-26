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
- Cover und alle normalen Szenen orientieren sich an dieser textfreien Referenz

Eine textliche Erwaehnung einer Referenz ersetzt niemals das echte Attachment.
Eine Referenz liefert Stil, Farben, Material- und Formensprache – nicht automatisch Text oder Komposition.

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

## 4. Visuelle Dichte und Abwechslung

Der Kanal soll nicht wie eine Diashow wirken und nicht aus einer Reihe fast identischer Einzelobjekt-Portraits bestehen.

Darum gilt:
- normale Bildhaltezeit meistens 3–6 Sekunden
- harte Obergrenze fuer ein einzelnes Standbild: 7 Sekunden
- ist ein Sprachabschnitt laenger oder enthaelt zwei echte Lehrbeats, wird er in mehrere NEUE Szenen mit NEUEN Bildnummern geteilt
- dasselbe Bild darf niemals als Loesung fuer einen langen Abschnitt zweimal verwendet werden
- lieber 1–3 zusaetzliche eindeutige Bilder als ein Bild 10–20 Sekunden stehen lassen

Informationsdichte:
- ein DOMINANTER Lehrpunkt pro Bild
- ca. 20–35 % wichtiger Mechanismus-/Zusammenfassungsbilder duerfen EINEN zusaetzlichen sinnvollen Detailpunkt enthalten
- wenn mehr Information noetig ist: neues Bild statt Textwand oder ueberladener Infografik

Abwechslung:
- maximal zwei isolierte Einzelobjekt-Szenen direkt hintereinander
- danach bevorzugt Prozess-, Ursache/Wirkung-, Weg-, Vergleichs- oder Kontextbild
- gleiche Uebersichtskomposition spaeter im Video nicht einfach wiederholen
- wiederkehrendes Thema muss einen neuen visuellen Zweck haben: anderer Massstab, andere Richtung, anderer Zustand oder andere Beziehung
- `scene_difference` ist eine echte QA-Anforderung, keine Formalitaet

## 5. Cover-Hook ist einmalig

Die exakte Cover-Hook darf ausschliesslich auf `Bild_01` erscheinen.

Fuer `Bild_02` bis `Bild_NN` ist sie ein Hard FAIL – auch dann, wenn Flow sie aus einer Referenz kopiert.

Verboten nach Bild_01:
- Cover-Hook als erneute Ueberschrift
- Cover-Hook als Kapiteltrenner
- Cover-Hook als dekorativer Hintergrundtext
- gekuerzte oder nahezu identische Wiederholung des Cover-Titels

Kapitelueberschriften duerfen nur erscheinen, wenn sie explizit im Szenen-Whitelist-Plan stehen und klar anders als die Cover-Hook sind.

## 6. Asset-IDs sind nur Metadaten

`Bild_01`, `Bild_19`, `Scene 19`, `IMAGE 19`, Dateinamen und Produktionsnummern duerfen niemals als sichtbarer Bildtext interpretiert werden.

Hard FAIL:
- `Bild 19` sichtbar im Bild
- `Bild_19` sichtbar im Bild
- `BILD_12 – O2 BINDET` sichtbar im Bild
- `Scene 19` / `IMAGE 19` sichtbar im Bild
- Dateiname oder sonstige interne Produktionskennung sichtbar im Bild

## 7. Sichtbarer Text ist Whitelist-basiert

Vor jeder Generation muss eine `ALLOWED_VISIBLE_TEXT`-Liste feststehen.

Cover:
- Whitelist = nur die exakte deutsche Hook

Normale Szene:
- Whitelist = exakt die fuer diese Szene geplanten Labels oder explizit geplante einzigartige Kapitelueberschrift
- bei 0 Eintraegen darf kein Wort sichtbar sein
- Cover-Hook darf niemals in einer normalen Szenen-Whitelist stehen

Nicht auf der Whitelist = FAIL. Dazu gehoeren insbesondere:
- Cover-Hook nach Bild_01
- Bild-/Szenennummern
- Prompt-Ueberschriften
- erfundene Szenentitel
- erfundene Erklaertexte
- englische Woerter
- zusaetzliche Anatomie-Labels
- KI-Gibberish

Bei falscher Flow-Schreibweise:
1. regenerieren
2. maximal einen weiteren Text-Versuch
3. danach exakter Remotion-Fallback

## 8. Object-Talk Character Mode

Fuer sprechende Lebensmittel / Alltagsobjekte bleibt der hochwertige stilisierte 3D-Character-Look erlaubt.
Dieser Modus darf nicht automatisch auf Organe, Molekuele und Zellen uebertragen werden.

## 9. Bild_01 – einzige nummerierte Varianten-Ausnahme

`Bild_01` ist Cover und erster Shot.

Nur fuer Bild_01 sind mehrere kreative Varianten erlaubt.

Ablauf:
1. textfreie Style-Referenz bereitstellen
2. bis zu 3 klar unterschiedliche Cover-Kandidaten erzeugen
3. Nutzer waehlt genau einen Cover-Kandidaten
4. dieser Kandidat wird `Bild_01.png`
5. alle nicht gewaehlten Cover-Kandidaten loeschen/verwerfen
6. Cover NICHT als normale Szenenreferenz verwenden
7. mit `Bild_02` auf Basis der textfreien Style-Referenz fortfahren

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

## 10. Folgegenerationen – genau ein Output pro Bildnummer

Fuer `Bild_02` bis `Bild_NN` gilt strikt:
- textfreie Style-Referenz wirklich anhaengen
- texttragendes Cover nicht anhaengen
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

Wenn Flow technisch mehrere Outputs liefert:
- nur den besten PASS-Kandidaten behalten
- alle anderen sofort verwerfen
- erst danach zur naechsten Bildnummer wechseln

## 11. Szenenprompt-Schema

```text
1. DOMINANT TEACHING IDEA
2. OPTIONAL SUPPORTING DETAIL
3. MAIN SUBJECT
4. START / END
5. MOVEMENT / CHANGE
6. SIMPLE SPATIAL LAYOUT
7. COMPOSITION DIFFERENCE VS PREVIOUS SCENES
8. SOFT-3D STYLE CONTINUITY
9. ALLOWED_VISIBLE_TEXT
10. FORBIDDEN ELEMENTS
11. COVER_HOOK_FORBIDDEN = true for Bild_02+
```

Eine Ueberschrift wie `BILD_19 – HAEMOGLOBIN GIBT O2 AB` ist reine Prompt-Struktur und darf nie gerendert werden.

## 12. QA

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

Fuer `Bild_02+` bedeutet `cover_hook_isolated = PASS`: Die Cover-Hook ist nirgendwo sichtbar.

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

Textfreie Referenzen liegen ausserhalb dieses finalen nummerierten Sets.

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
- nach Bild_01 weitere Freigaben verlangen
