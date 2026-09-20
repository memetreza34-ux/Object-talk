# Bild-Timing-Pipeline – Video 001

## Thema

**Was passiert mit deinem Essen im Körper?**

Die eigentliche Sekunden-Timeline wird erst nach dem finalen Voiceover aus Whisper-Wortzeiten erzeugt.

Die Szenengrenzen sind **jetzt schon kreativ festgelegt** und dürfen in Phase 3 nicht neu erfunden werden. Die vollständigen 1:1-Sprachabschnitte stehen in `../../05_info/phase1-scenes.json`.

`scene-map.json` wird technisch und deterministisch daraus erzeugt mit:

```bash
python tools/generate_scene_map.py \
  youtube-videos/001-was-passiert-mit-essen-im-koerper/05_info/phase1-scenes.json \
  youtube-videos/001-was-passiert-mit-essen-im-koerper/03_pipeline/scene-map.json
```

## Szenen

| Szene | Bild | START bei gesprochenen Worten | ENDE bei gesprochenen Worten | Visuelle Aufgabe | Bewegung |
|---:|---|---|---|---|---|
| 01 | Bild_01 | „Du nimmst einen Bissen, kaust ein paarmal und“ | „und schluckst. Für dich dauert das nur Sekunden.“ | Hook: Ein Bissen startet eine unerwartete Reise | slow-push-in |
| 02 | Bild_02 | „Für deinen Körper beginnt jetzt eine Reise durch“ | „Magen ist dabei gar nicht der wichtigste Ort.“ | Verdauung als Reise; Reveal, dass der Magen nicht die Haupt-Aufnahmestation ist | slow-push-in |
| 03 | Bild_03 | „Schon im Mund startet die Verdauung. Deine Zähne“ | „die Verdauung. Deine Zähne zerkleinern das Essen mechanisch.“ | Mund: mechanisches Zerkleinern | pan-right |
| 04 | Bild_04 | „Gleichzeitig mischt Speichel es mit Flüssigkeit, damit daraus“ | „weicher Bissen wird, den du leichter schlucken kannst.“ | Speichel macht den Bissen schluckbar | slow-push-in |
| 05 | Bild_05 | „Im Speichel steckt außerdem ein Enzym, das bei“ | „stärkehaltigen Lebensmitteln bereits beginnt, lange Kohlenhydratketten zu zerlegen.“ | Speichelenzym beginnt Stärkeabbau | slow-push-in |
| 06 | Bild_06 | „Dann kommt der Moment, den du kaum noch“ | „Essen in die Speiseröhre statt in die Atemwege.“ | Schlucken + Kehldeckel | pan-right |
| 07 | Bild_07 | „Aber wie kommt der Bissen von dort bis“ | „Speiseröhre erzeugt wellenförmige Muskelbewegungen. Diese Bewegung heißt Peristaltik.“ | Frage + Peristaltik erklären | pan-right |
| 08 | Bild_08 | „Hinter dem Bissen zieht sich die Muskulatur zusammen,“ | „das Essen Stück für Stück nach unten geschoben.“ | Muskelwelle schiebt Bissen | slow-push-in |
| 09 | Bild_09 | „Am Ende der Speiseröhre öffnet sich ein ringförmiger“ | „den Magen. Jetzt beginnt eine deutlich aggressivere Phase.“ | Übergang Speiseröhre → Magen | slow-push-in |
| 10 | Bild_10 | „Der Magen knetet und mischt den Nahrungsbrei. Gleichzeitig“ | „von Proteinen wird hier weiter in Gang gesetzt.“ | Magen, Säure, Enzyme, Proteinverdauung | slow-push-in |
| 11 | Bild_11 | „Der Magen ist also wichtig. Aber er ist“ | „er in den ersten Abschnitt des Dünndarms weitergegeben.“ | Magen als Vorbereitung; Chymus zum Dünndarm | pan-right |
| 12 | Bild_12 | „Und hier passiert der entscheidende Teil. Der erste“ | „aus dem Magen ist dort noch stark sauer.“ | Reveal Zwölffingerdarm | slow-push-in |
| 13 | Bild_13 | „Deshalb gibt die Bauchspeicheldrüse nicht nur Enzyme ab,“ | „neutralisiert. Das schafft bessere Bedingungen für viele Verdauungsenzyme.“ | Pankreas-Bicarbonat | slow-push-in |
| 14 | Bild_14 | „Im Dünndarm treffen mehrere Helfer zusammen. Die Bauchspeicheldrüse“ | „Verdauungsenzyme, die Kohlenhydrate, Fette und Proteine weiter zerlegen.“ | Pankreasenzyme | pan-right |
| 15 | Bild_15 | „Die Leber produziert Galle. Sie wird in der“ | „gespeichert und bei Bedarf in den Dünndarm abgegeben.“ | Leber, Gallenblase, Galle | pan-right |
| 16 | Bild_16 | „Galle hilft dabei, Fette in kleine Tröpfchen zu“ | „zu verteilen, damit Enzyme besser an sie herankommen.“ | Fett-Emulgierung verständlich zeigen | slow-push-in |
| 17 | Bild_17 | „Aus großen Nährstoffen werden jetzt immer kleinere Bausteine.“ | „zu Aminosäuren. Fette werden in kleinere Bestandteile zerlegt.“ | Makronährstoffe → kleinere Bausteine | slow-push-in |
| 18 | Bild_18 | „Erst in dieser Form kann dein Körper einen“ | „ihre Bausteine klein genug für den Transport sind.“ | Zerlege-/Sortieranlagen-Analogie | pan-right |
| 19 | Bild_19 | „Warum ist der Dünndarm dafür so gut gebaut?“ | „viele Falten und winzige fingerartige Ausstülpungen, die Darmzotten.“ | Dünndarmfalten + Darmzotten | slow-push-in |
| 20 | Bild_20 | „Dadurch entsteht eine riesige Oberfläche auf kleinem Raum.“ | „diese Oberfläche gelangen viele Nährstoffe durch die Darmwand.“ | große Oberfläche + Aufnahme | slow-push-in |
| 21 | Bild_21 | „Ein großer Teil der einfachen Zucker und Aminosäuren“ | „und Aminosäuren gelangt von dort in kleine Blutgefäße.“ | Darmzotte → Blutgefäß | slow-push-in |
| 22 | Bild_22 | „Das Blut transportiert sie weiter, unter anderem zur“ | „verarbeitet, speichert und verteilt viele dieser Stoffe weiter.“ | Blut → Leber | pan-right |
| 23 | Bild_23 | „Fette nehmen teilweise einen anderen Weg und gelangen“ | „gelangen zunächst über das Lymphsystem in den Kreislauf.“ | Fettaufnahme → Lymphe | pan-right |
| 24 | Bild_24 | „Das bedeutet: Dein Essen verschwindet nicht einfach im“ | „Bissen tatsächlich Baustoffe und Energiequellen für deinen Körper.“ | Kerngedanke: Nahrung → aufnehmbare Moleküle | slow-push-in |
| 25 | Bild_25 | „Doch die Reise ist noch nicht vorbei. Was“ | „den Dickdarm. Dort wird vor allem Wasser zurückgewonnen.“ | Dünndarm → Dickdarm + Wasseraufnahme | pan-right |
| 26 | Bild_26 | „Gleichzeitig lebt hier ein großer Teil deines Darmmikrobioms:“ | „Teil deines Darmmikrobioms: eine riesige Gemeinschaft aus Mikroorganismen.“ | Mikrobiom zeigen | slow-push-in |
| 27 | Bild_27 | „Einige dieser Bakterien können Bestandteile verwerten, die deine“ | „können. Dazu gehören bestimmte unverdauliche Kohlenhydrate und Ballaststoffe.“ | Bakterien + Ballaststoffe | slow-push-in |
| 28 | Bild_28 | „Dabei entstehen Stoffwechselprodukte, die wiederum mit deinem Darm“ | „nicht einfach nur der letzte Abfluss des Systems.“ | Stoffwechselprodukte + Darmwand | slow-push-in |
| 29 | Bild_29 | „Seine Mikroorganismen können unter anderem bestimmte unverdauliche Kohlenhydrate“ | „die von Zellen im Darm genutzt werden können.“ | Fermentation → nutzbare Stoffe | pan-right |
| 30 | Bild_30 | „Gleichzeitig ist das Mikrobiom von Mensch zu Mensch“ | „komplexer, als ein einzelnes Video vollständig erklären könnte.“ | Unterschiedliche Mikrobiome, Komplexität | slow-pull-out |
| 31 | Bild_31 | „Während Wasser entzogen wird, wird der verbleibende Inhalt“ | „als Stuhl im Enddarm gespeichert und später ausgeschieden.“ | Wasserentzug, Stuhlbildung, Enddarm | slow-push-in |
| 32 | Bild_32 | „Und während all das passiert, arbeitet dein Verdauungssystem“ | „ausgeschüttet werden und wie schnell Nahrung weitertransportiert wird.“ | Nerven + Hormone steuern Verdauung | pan-right |
| 33 | Bild_33 | „Sogar der Anblick oder Geruch von Essen kann“ | „kann deinen Körper schon auf die Verdauung vorbereiten.“ | Sinneseindruck → Speicheldrüsen | slow-push-in |
| 34 | Bild_34 | „Wenn du also das nächste Mal einen Bissen“ | „Mund zerkleinert. Deine Speiseröhre transportiert. Dein Magen mischt.“ | Recap Mund → Speiseröhre → Magen | pan-right |
| 35 | Bild_35 | „Der Dünndarm zerlegt weiter und nimmt Nährstoffe auf.“ | „mit Hilfe von Mikroorganismen einen Teil der Reste.“ | Recap Dünndarm → Blut/Lymphe → Dickdarm | pan-right |
| 36 | Bild_36 | „Aus einem einzigen Bissen wird so eine ganze“ | „Körper für Energie, Wachstum und Reparatur verwenden kann.“ | Finale Gesamtbild | slow-pull-out |

## Phase-3-Regel

Die echten Start-/Endsekunden kommen ausschließlich aus dem finalen Voiceover:

```text
finales Audio
→ faster-whisper + strikte Script-Ausrichtung
→ word-timings.json
→ scene-map.json
→ timeline.json
```

Keine Szene nach Gefühl verschieben. Wenn Script und Audio nicht exakt zusammenpassen: FAIL statt Raten.