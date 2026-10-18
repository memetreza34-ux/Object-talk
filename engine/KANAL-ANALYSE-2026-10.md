# Kanal-Analyse Lebenslogik – Oktober 2026

Stand 18.10.2026. Grundlage: komplettes Repository (Regeln, Engine, Tools, alle Videoordner 000–010), Skripte und Flow-Prompts von 008 (Verdauung), 009 (Schlaf) und 010 (Hunger), Recherche zu vergleichbaren Kanälen. **Nicht geprüft:** die gerenderten MP4-Dateien selbst und echte YouTube-Statistiken (CTR, Retention). Sie liegen nicht im Repository.

## Kurzfassung

1. **Die Technik ist stark, die Inhalte sind zu vorsichtig.** Pipeline, Untertitel-Abgleich und Exportregeln sind sauber. Die Skripte lesen sich aber wie ein vorsichtiges Schulbuch: fast keine Zahlen, keine Experimente, keine Spannungsbögen, viele Absicherungen.
2. **Die Bilder illustrieren Sätze statt Mechanismen.** In 010 zeigen 34 von 72 Szenen Menschen oder Hände, 32 spielen an Tisch, Küche, Markt oder Café. Nur 21 zeigen Organ, Zelle oder Signalweg.
3. **Das Regelwerk prüft Format, nicht Wirkung.** Es gibt viele Regeln zu Ordnern, Labels und IDs, aber keine messbare Regel für Unterhaltung oder Zuschauerbindung. Die Planungsdateien von 010 wurden mechanisch befüllt und enthalten Fehler, die das Rendern blockiert hätten.
4. **Titel und Cover verschenken Neugier.** Der Covertext wiederholt den Titel. 008 und 009 enden auf „… einfach erklärt“. Der Kanalname ist uneinheitlich (Object-Talk, FoodSpricht, Lebenslogik).
5. **Umgesetzt:** vier neue Tools mit Tests und neue Pflichtregeln für Skript, Bild und Titel, die für jedes **zukünftige** Video gelten. Dazu kommen zwei vollständige Musterbeispiele (Hunger, Verdauung) unter `examples/storyboard-v2/`. Sie zeigen, wie ein Storyboard nach den neuen Regeln aussieht, und werden nicht produziert. Die veröffentlichten Videos 008 und 010 bleiben unverändert und werden nicht neu aufgelegt.

## 1. Was gut ist und bleibt

- **Bildwelt 008** („Clean Animated Biology Illustration“) ist eine gute, wiedererkennbare Basis.
- Die stärksten Bilder in 010 sind laut Nutzer-Sichtung die Mechanismusbilder: Magendehnung (00:49), Darm-Botenstoffe (01:04), lösliche Ballaststoffe (02:24).
- **Saubere Produktion:** Whisper-Abgleich ohne geschätzte Zeiten, kein Remotion-Text, nur vier sichtbare Exportdateien, separates Cover.
- **Wissenschaftliche Sorgfalt:** keine Heilversprechen, keine Diätlügen. Das ist ein echter Vorteil gegenüber vielen Gesundheitskanälen.

## 2. Skripte – Diagnose mit Messwerten

Gemessen mit dem neuen `tools/script_quality.py` (Stand nach Review-Korrekturen; gezählt werden nur echte Zahlwörter und Zahlen):

| Video | Wörter | Konkrete Zahlen | Fragen | Absicherungen pro 1000 Wörter | Disclaimer-Floskeln | Open Loops |
|---|---:|---:|---:|---:|---:|---:|
| 008 Verdauung | 1111 | **1** | 2 | **20,7** | 0 | 0 |
| 009 Schlaf | 986 | 4 | 1 | **29,4** | 4 | 0 |
| 010 Hunger | 1044 | **0** | 5 | **30,7** | **6** | 0 |
| **Musterbeispiel Hunger** | 1095 | **25** | 5 | **12,8** | **0** | **2** |
| **Musterbeispiel Verdauung** | 1144 | **19** | 5 | **1,7** | **0** | **3** |

### Konkrete Schwächen

- **Lehrbuch-Ton und Dauer-Absicherung.** Schon das Intro von 010 endet mit: „Dabei geht es nicht ums Hungern oder darum, einzelne Lebensmittel als schlecht abzustempeln.“ Dazu kommen „Das bedeutet nicht, dass jede Suppe …“, „Aber Vorsicht: …“ und „Ein einzelner Nährstoff löst nicht jedes Hungerproblem.“ Jede Einschränkung ist für sich richtig. Zusammen nehmen sie aber jede Spannung raus.
- **Keine Zahlen, keine Experimente.** 008 hat eine einzige Zahl in 1111 Wörtern. Es gibt starke, gut belegte Fakten, die Zuschauer weitererzählen würden: Darmoberfläche ein halbes Badmintonfeld statt Tennisplatz, 9 Liter Flüssigkeit pro Tag, 38 Billionen Bakterien, Croissant vs. Kartoffel siebenmal, +500 kcal bei stark verarbeitetem Essen, Ghrelin +28 % nach kurzer Nacht. Keine davon kommt in den Skripten vor.
- **Keine Spannungsbögen.** Das Intro von 010 zählt alle Themen auf (Eiweiß, Ballaststoffe, Getränke, Schlaf). Damit sind die Antworten vorweggenommen, und es gibt keinen Grund, bis zum Ende zu bleiben.
- **Keine benannten Akteure.** 010 nennt kein einziges Hormon, weder Ghrelin noch Leptin noch GLP-1. Dabei ist GLP-1 durch die Abnehmspritzen gerade eines der Wörter mit der größten Neugier.
- **Schwache Schlüsse.** Am Ende steht eine Wiederholung oder eine Moral („Hunger ist ein Signal, kein Fehler …“), aber keine Brücke zum nächsten Video.
- **009:** doppelte Aussagen direkt hintereinander („Du liegst ganz still im Bett. Doch unter der Oberfläche passiert erstaunlich viel. Von außen wirkt alles still.“).

### Ursachen im System

1. `engine/SCRIPT-STANDARD.md` prüfte praktisch nur Satz 1. Für den Mittelteil gab es keine messbaren Regeln.
2. Die Vorsichtsregeln („keine ungesicherten Aussagen“) wurden als „lieber gar keine Zahl“ gelesen. Die richtige Lesart ist: Zahl nennen, Quelle prüfen, kurz einordnen.
3. **Ein technischer Grund gegen Zahlen:** Der Whisper-Abgleich verglich Wörter streng. Schreibt Whisper „15 Prozent“, steht im Skript aber „fünfzehn Prozent“, bricht die Pipeline ab. Konkrete Zahlen wurden damit faktisch bestraft. Das ist jetzt behoben (`tools/text_normalize.py`).

## 3. Bilder – Diagnose

- **Personenlastig:** In 010 zeigen 34 von 72 Szenen Menschen oder Hände (47 %) und 32 Szenen Tisch, Küche, Markt, Café oder Schreibtisch. Im Musterbeispiel Hunger sind es 14 von 94 Szenen mit Menschen im Alltag, nur als Hände oder Ausschnitt, und null Ganzkörper.
- **Unpassende oder überladene Motive in 010:**
  - Bild_05 zeigt „Joghurt, Bohnen, Saft, **Schlafkissen**“ auf einer Küchenarbeitsplatte.
  - Bild_16 zeigt zwei Szenen in einem Bild (Hunger und Appetit) und verletzt damit die Regel „eine Idee pro Bild“.
  - Bei Bild_50 („Schlaf“ auf einer wachen Person) und Bild_52 („Stress“) wirkt das Label wie eine Bildunterschrift statt wie eine Erklärung.
  - Bild_64 zeigt „Energiebilanz“ mit Laufschuhen.
- **Mechanisch befüllte Planung:** In `sentence-visual-plan.json` von 010 rotiert `visual_type` exakt 9-mal durch 8 Werte, und `learning_goal` lautet immer „Zuschauer versteht: <Satz>“. Szene 2 (Esszimmer) ist als „organ-cutaway“ markiert.
- **Render-Blocker in 010:** 24 Szenen nutzen die Kamerabewegungen `slow-pull-back` oder `gentle-up-pan`. Der Renderer kennt sie nicht, `tools/validate_phase1.py` hätte Phase 3 gestoppt. Der Antigravity-Prompt von 010 ist noch die unveränderte Vorlage und nennt den alten Export mit zehn Dateien.
- **Kein Farbcode und keine Leitmotive:** Hormone und Nährstoffe hatten in jedem Bild andere Farben. Zuschauer konnten also nicht „mitlesen“. Erfolgreiche Erklärkanäle halten Farben und Metaphern über das ganze Video konstant.

## 4. Titel, Cover, Beschreibung

- **010:** Titel „Warum du nach dem Essen so schnell wieder Hunger hast“, Covertext „Warum bist du wieder hungrig?“. Der Covertext sagt dasselbe wie der Titel. Besser ist ein Covertext, der den Titel ergänzt, z. B. „Hunger trotz Essen?“.
- **008/009:** „… | Verdauung einfach erklärt“ und „… | Schlaf einfach erklärt“ sind gute Suchbegriffe, aber auch ein Schulbuch-Signal ohne Neugier.
- **Beschreibungen** ohne Kapitelmarken und ohne Quellen. Kapitel helfen Zuschauern beim Springen und in der Suche. Quellen schaffen bei Gesundheitsthemen Vertrauen.
- **Kanalname uneinheitlich:** 008/009 schreiben „Object-Talk“, 010 „Lebenslogik“, README „Object-Talk / FoodSpricht“. Für Zuschauer sollte es nur **Lebenslogik** geben.

## 5. Was vergleichbare Kanäle anders machen

| Kanal | Was auffällt | Was wir übernehmen |
|---|---|---|
| Kurzgesagt / „Dinge Erklärt – Kurzgesagt“ (funk) | Titel als klare Behauptung oder Gegenposition („Vergiss alles, was du über Sport weißt!“, „Die Wahrheit über Milch – So ungesund ist sie wirklich“, „Dein Körper bekämpft täglich Krebs!“); feste Farben und wiederkehrende Bildmetaphern | Covertext als Behauptung oder Paradox; Farbcode und Leitmotiv pro Video |
| TED-Ed („How does your body know you're full?“) | eine einzige klare Frage; benannte Hormone (Leptin, CCK) über ihre Wirkung erklärt | Akteure benennen und sofort erklären |
| Zack D. Films (laut Drittanbietern ca. 28 Mio. Abos, Okt. 2026) | sehr kurzer Cold Open; die Konsequenz ist im ersten Bild sichtbar | erste 3 Bilder in 1–3 Sekunden schneiden, Paradox sofort zeigen |
| Doktor Whatson, Quarks, Galileo („Weg des Essens“) | Experimente, Alltagstests, eine Reise mit roter Linie | echte Studien als Mini-Experiment erzählen; „Reise einer Pizza“ |
| DoktorWeigl (1 Mio. Abos) | Arzt-Autorität schafft Vertrauen | ohne Gesicht: Vertrauen über Quellen in der Beschreibung und genaue Formulierungen |

**Retention-Praxis** (Erfahrungswerte von Creator-Tools, keine harte Forschung): Der größte Absprung passiert in den ersten 30 Sekunden. Der Einstieg muss das Versprechen von Titel und Cover sofort einlösen, und Open Loops halten Zuschauer in der Mitte. Wir behandeln das als Arbeitshypothese und messen es an den echten YouTube-Kurven der nächsten Videos.

Quellen: [onlinemarketing.de – Top-10 deutsche Kanäle](https://onlinemarketing.de/?p=143072), [giga.de – Wissenskanäle](https://www.giga.de/entertainment/11-geniale-youtube-kanaele-die-besser-sind-als-jede-netflix-doku--01K4Q2DM62NMR878WC81V92MEC), [LingQ-Liste Dinge Erklärt](https://www.lingq.com/en/learn-german-online/courses/739836/), [TED-Ed Lesson](https://www.ted.com/talks/hilary_coller_how_does_your_body_know_you_re_full), [CreatorDB Zack D. Films](https://creatordb.app/creatorstats/zackdfilms/), [YouTube-Blog DoktorWeigl](https://blog.youtube/intl/de-de/creator-and-artist-stories/als-arzt-erfolgreich-auf-youtube-doktorweigl-ermutigt-medizinerinnen-online-aufzuklaren/), [Galileo „Weg des Essens“](https://www.youtube.com/watch?v=8QCg9-w3X7o), [vidIQ Retention](https://vidiq.com/blog/post/increase-audience-retention-youtube/).

## 6. Was umgesetzt wurde

### Zwei Musterbeispiele (validiert, keine Produktion)
- `examples/storyboard-v2/901-beispiel-hunger/` – Hunger-Thema, 94 Bilder, Titel-/Coverbeispiel „Warum du kurz nach dem Essen schon wieder Hunger hast“ / „Hunger trotz Essen?“.
- `examples/storyboard-v2/902-beispiel-verdauung/` – Verdauungs-Thema „Die Reise einer Pizza“, 99 Bilder, Coverbeispiel „Wohin verschwindet sie?“.
- Die Themen sind mit 008 und 010 bereits veröffentlicht, deshalb werden die Beispiele **nicht** produziert. Sie zeigen nur Aufbau, Zahlendichte, Open Loops, Bildregie und Titel nach den neuen Regeln. Der CI-Lauf prüft sie bei jeder Änderung, damit Regeln und Werkzeuge zusammenpassen.
- Vor dem Pull Request wurden alle Änderungen unabhängig gegengeprüft (fünf Prüfer, ein skeptischer Gegenprüfer). 39 bestätigte Punkte wurden behoben, darunter „Zellwände“ → „Zellmembranen“, ein anatomisch falsch beschriebenes Schluckbild, ein Warnhinweis ohne „ungewollt“ und zu großzügige Zahlenerkennung im Prüfwerkzeug.

### Neue Tools (getestet, in CI)
- `tools/text_normalize.py`: Zahlen werden beim Whisper-Abgleich automatisch erkannt („15“ = „fünfzehn“, „15 %“ = „fünfzehn Prozent“, „2-3“ = „zwei bis drei“, „1.500“ = „tausendfünfhundert“, „GLP-1“ = „GLP eins“); `transcribe_audio.py`, `build_timeline.py` und `validate_phase1.py` nutzen dieselbe Normalisierung.
- `tools/script_quality.py`: misst Zahlen, Fragen, Absicherungen, Disclaimer, Satzlänge, Open Loops und die geschätzte Sprechzeit pro Bild. Pflicht ab Video 011.
- `tools/build_phase1_package.py`: Eine Storyboard-Datei erzeugt Skript, Flow-Prompt, Szenen-, Satz- und Labelplan, Caption-Entwurf und Antigravity-Auftrag. Damit kann nichts mehr auseinanderlaufen.
- `tools/export_chapters.py`: setzt nach dem Render YouTube-Kapitel mit echten Zeiten in die Caption (läuft automatisch in `prepare_phase3.py`).
- `tools/validate_planning_v2.py`: prüft jetzt auch Kamerabewegungen und Skriptqualität (ab 011).

### Neue Pflichtregeln
- `engine/SCRIPT-STANDARD.md` §13 Retention-Handwerk
- `engine/TITEL-THUMBNAIL-STANDARD.md`
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`: Farbcode, Leitmotiv, Orientierungskarte
- `engine/PLANNING-V2.md`: Storyboard-v2 als einzige Quelle
- `engine/IMPROVEMENT-LEDGER.json`: zwei neue dauerhafte Lessons (BASE-RETENTION-SCRIPT, BASE-STORYBOARD-SOURCE)

## 7. Empfehlungen für die nächsten Schritte

1. **Nächstes neues Thema mit dem neuen Workflow:** `python tools/create_video.py 011-longform-THEMA`, Storyboard nach dem Vorbild der Musterbeispiele schreiben, `build_phase1_package.py`, Validator PASS, dann Flow, Voice und Phase 3. Am Ende auf ein bereits veröffentlichtes Video (z. B. 008 oder 010) als Endscreen verweisen.
2. **Cover-Test:** Die zwei nicht gewählten Cover behalten und mit YouTube „Testen und vergleichen“ gegen das Hauptcover laufen lassen, sobald die Funktion im Kanal verfügbar ist.
3. **Nach 7 Tagen messen:** CTR, durchschnittliche Wiedergabedauer, Retention bei 0:30 und 1:00. Diese Werte zusammen mit einer echten Sichtung in `.intern/05_info/improvement-review.json` eintragen und mit `tools/improvement_loop.py register` registrieren.
4. **Shorts als Zubringer** (Idee, noch nicht umgesetzt; braucht ein 9:16-Format in der Pipeline): Aus jedem Longform lassen sich 2–3 Shorts schneiden, z. B. „Warum dein Magen sich nicht selbst verdaut“, „Tennisplatz-Mythos“, „Croissant vs. Kartoffel“.
5. **Themen mit starkem Hook** (Vorschläge, vor Produktion in `THEMEN-GEHIRN.md` prüfen):
   - „Was Kaffee in deinem Körper macht – Minute für Minute“ (Cover: „Wach durch Betrug?“; Adenosin-Blockade)
   - „Was passiert, wenn du 24 Stunden nichts isst?“ (Cover: „24 h ohne Essen“; Glykogen → Fettverbrennung)
   - „Warum Zucker dich erst wach und dann müde macht?“ (Vorsicht: Mythen sauber trennen)
   - „Was Alkohol in deinem Körper macht“ (Leber, Schlaf, Durst)
   - „Wie dein Körper Fett verbrennt – und wo es hingeht“ (Cover: „Fett wird ausgeatmet?“; CO₂-Fakt)
   - „Warum du nach dem Essen müde wirst“ (Food-Koma)
