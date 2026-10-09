# Google Flow – EIN Prompt und EIN ZIP-Ordner

**KANONISCHER PRODUKTIONSSTANDARD** für alle neuen Object-Talk-Videos.

## Nutzeroberfläche – genau zwei Einträge
Im jeweiligen Videoordner `02_bildprompts/` stehen:
```text
02_bildprompts/
├── GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
└── bilder-zip/
    └── README.md
```
Die README liegt **innerhalb** des ZIP-Ordners, nicht daneben. Dort genau **eine fertige Bilder-ZIP** ablegen. Der Ordner wird von `tools/prepare_phase3.py` direkt gelesen. Entpackte Bilder gehören intern unter `03_pipeline/images/`. Interne Label-/QA-Daten liegen in `05_info/label-plan.json` und `05_info/image-review.json`, nie sichtbar neben dem Nutzerprompt. Alte Projekte dürfen historische Pfade behalten.

## Referenz-Gate VOR dem ersten Cover

Der Nutzer stellt 2–4 **echte Original-008-Bildreferenzen** aus `bildwelt/008-ORIGINAL-VIDEO-STYLE-REFERENCE.md` bereit. Diese müssen Google Flow als Bildinput vorliegen; reiner GitHub-Link/Stilname reicht nicht. Ohne Bilder die Ausgabe als nicht stilverifiziert markieren und zuerst um die Bildreferenzen bitten.

**Nach der Coverwahl:** das ausgewählte Cover als SEKUNDÄRE Stilreferenz gemeinsam mit den echten 008-JPGs weiterverwenden. Die 008-JPGs bleiben Hauptanker für biologische Konturen, Organ-/Zellkontexte und Schattierung. Kein Cover-Titel in Folgebildern.

## Ein Prompt steuert drei Phasen
Der Prompt ist **eine einzige vollständig ausgefüllte Textdatei** mit den 3 konkreten Cover-Varianten und dem gesamten, konkreten Szenenregister von Bild 02 bis Bild NN. Keine 17 separaten Textprompts oder Batchdateien.

**Phase 1:** Flow erzeugt zuerst tatsächlich drei unterschiedliche Cover EINZELN (niemals eine Collage). Alle tragen nur exakt denselben Titel mit starkem Textkontrast. Danach alle drei zeigen, die Frage stellen: „Welches Cover wählst du – 1, 2 oder 3?“ **STOP bis zur Nutzerwahl**. Keine normalen Bilder vor Auswahl.

**Phase 2:** Ausgewähltes Cover wird finale `Bild_01.png`. Die anderen zwei werden nicht in Endpaket übernommen. **Sofort**, ohne weitere Freigabe, fünf eigenständige Bilder 02–06 generieren; anschließend intern fortfahren 07–11 usw., jeweils maximal fünf einzelne Bilder pro Arbeitsschritt. Die Szenenbeschreibungen stehen alle im SELBEN Prompt. Kein neuer Prompt nötig, keine generische Frage nach jedem Batch. Wenn Google Flow stoppt oder auf eine weitere Nutzeraktion wartet, exakte nächste Bildnummer nennen; Nutzer sagt „weiter“, Agent fährt mit demselben Prompt fort. Keine unbegrenzte Hintergrundarbeit behaupten.

**Phase 3:** Exakt alle genehmigten Bilder `Bild_01.png … Bild_NN.png` ohne Doppelungen, Lücken oder zusätzliche Cover zu EINER ZIP zusammenfassen. Der Nutzer legt die ZIP unter `02_bildprompts/bilder-zip/` ab. ZIP bleibt lokal und wird per `.gitignore` nicht automatisch nach GitHub eingecheckt.

## Bildwelt und QA
Klarer, sanft plastischer Clean-Animated-Biology-Illustration-Look des freigegebenen Videos 008: saubere Konturen, weiche organische Formen, verständliche Anatomie, helle harmonische Farben, passend dunklere Akzente. Kein generischer flacher Nacht-Silhouettenlook. Ein dominanter Lehrpunkt/Bild; nur 0–2 notwendige kurze Labels. Heller Hintergrund → dunkle Schrift, dunkler Hintergrund → helle Schrift. Cover nur Titel. **Bildnummern und Dateinamen niemals sichtbar**. Fehlerhafte Bilder vor Aufnahme in ZIP regenerieren.

## Kein Falschabschluss
Die Promptdatei und ZIP-Ablage sind die VORBEREITUNG, keine tatsächlich produzierten Bilder. Fehlende Medien, ZIP oder Nutzer-Coverwahl offen als Status kennzeichnen; nicht „fertig“ melden.

## Safety-First / Google-Flow-Richtlinien

Google Flow kann bestimmte Bildanfragen ablehnen. Halte die Bildaufträge klar bildungsbezogen, freundlich und **nicht-grafisch**. Normaler Schlaf und leicht verständliche isolierte Illustrationen von Organen/Zellen sind passend; keine invasiven Körperdarstellungen, verletzten Personen, sexualisierten Motive, täuschenden Nachahmungen realer Personen oder medizinische Heilsversprechen verlangen.

**Wenn Flow eine Anfrage ablehnt:** Nicht versuchen, Filter/Sicherheitsmechanismen zu umgehen oder Schutzregeln zu überschreiben. Stattdessen den betroffenen Bildauftrag kennzeichnen, die Ursache nicht als Gewissheit behaupten und nur eine sachlich zulässige, vereinfachte Illustration vorschlagen. Bei fortdauernder Ablehnung die Generation abbrechen und Feedback/Support der Plattform nutzen.

Lange komplette Szenenpläne können technisch oder durch Moderation scheitern; die einzelne Promptdatei bleibt erhalten, aber im Chat zuerst nur die 3 Coverbilder als konkrete Bildgenerierung anfordern. Keine Zusage, dass jedes externe Tool alle Cover oder ZIPs automatisch erzeugt.

Richtlinien: https://policies.google.com/terms/generative-ai/use-policy?hl=de-DE und https://support.google.com/flow/answer/16353333.
