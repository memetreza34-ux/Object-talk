# Postmortem 008 → 009: Warum trotz gleichem Stilnamen andere Bilder entstanden

## Beobachtung
Der Nutzer hat die **fertige Original-MP4 von Video 008 Verdauung** erneut hochgeladen (6:54.208, 1920x1080, 30fps). Aus ihr wurden echte Frames bei 00:18, 01:24, 01:48, 03:24, 03:48, 04:12, 04:24, 05:36 analysiert. Die Screenshots aus Video 009 zeigen in Flow hingegen sterile freigestellte Synapsen/Gehirne, teilweise neonartig-dunkle Bilder und posterartige Motive.

## Dateivergleich – konkret

**008 Originalprompt:** `youtube-videos/008-longform-verdauung/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

**009 umgebauter Prompt:** `youtube-videos/009-longform-schlaf/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

1. **Gleiche Worte sind keine gleiche Bildwelt.** Der 008-Prompt hat nur den generischen Satz `Clean Animated Biology Illustration...`, aber das **fertige Video** enthält spezifische Farb-/Linien-/Volumeneigenschaften, die nicht in diesem Satz codiert sind.
2. **009-Szenen waren zu repetitiv und isoliert.** Mehrfach gab es freigestellte Gehirne/Neuronen und sanfte Schlafwellen statt bildfüllender ORGANISCH VERBUNDENER anatomischer Prozesse mit Gewebe-/Gefäßkontext wie 008.
3. **Widerspruch im Repo:** Frühere Style-Regeln verboten `Bild_01` als Stilreferenz. Der Nutzer wünscht aber die gewählte Cover-Gestaltung als zusätzliche Vorlage. Korrigiert: echtes 008-Referenzset primär, ausgewähltes Cover sekundär.
4. **Kein tatsächlich importiertes 008-Bildset:** `config/channel.json` hatte `style_reference_image = null`. Weder die bloße Erwähnung eines Videonamens noch ein lokaler Dateiname macht Google Flow reale Frames zugänglich.
5. **Nachtmotiv als eigenständiger Stil:** Schlaf induzierte wiederholt dunkle/schwebende/Neon-Bildsprache. Nacht ist biologischer Kontext, nicht ein neuer Kanal-Renderstil.
6. **Too many negatives, too little exact visual evidence:** Wiederholtes Verbieten von Comic, Neon etc. kann die positive plastisch-organische Referenz aus dem 008-Video nicht ersetzen.

## Korrektur
- **008 wird NICHT umgestaltet oder neu generiert.** Der Original-Prompt bleibt die historische Referenz.
- Achte zusätzlich auf die **echten Frames** aus dem Originalvideo: `bildwelt/008-ORIGINAL-VIDEO-STYLE-REFERENCE.md`.
- Eine ZIP mit acht tatsächlichen JPG-Frames aus dem Originalvideo wurde im aktuellen Chat erstellt; sie muss in Google Flow als Bildquelle verwendet werden (Dateinamen allein sind nutzlos).
- Vor erstem Cover: Original-008-Bildreferenzen hochladen. Dann 3 Cover → Nutzer wählt. Danach 008-Originalframes + gewähltes Cover **gemeinsam** für Bilder 02–77.
- Jeder Shot: visueller Körper-/Organ-/Gewebe-/Zellkontext, ein sichtbarer Mechanismus; bildfüllende organische Formen, weiche warme Konturen, pastellige lebendige Lichtumgebung; nicht nur ein Icon vor Weiß.
- Phase-2-Validator prüft nun eine dokumentierte tatsächliche Nutzung der Original-008-Frames, Coverfreigabe und visuelle Abnahme. Prompttexte allein ergeben kein PASS.
- **Keine Pixelidentitätsgarantie:** Google Flow ist stochastisch. Die gleiche Bildwelt muss über Referenzen + begutachtete Endframes abgesichert werden.

## Noch offen (ehrlicher Produktionsstatus)
- Die acht JPGs sind **nicht automatisch als GitHub-Binärdateien eingecheckt**. Repo enthält Extraktionsskript/Manifest, der Nutzer erhält separat die herunterladbare ZIP und kann sie in Flow hochladen.
- Die generierten alten 009-Szenen müssen anhand der echten 008-Frames erneut geprüft und bei Bruch ersetzt werden. Ein GitHub-Prompt-Commit repariert alte Flow-Bilder nicht rückwirkend.
- Es liegen in diesem neuen Chat **keine neu erzeugten/abgenommenen 009-Bilder oder MP4** vor, folglich bleibt `style-reference-review.json` auf PENDING.
