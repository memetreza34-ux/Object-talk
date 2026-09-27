# Google Flow Agent – Pilot 006 Wundheilung

## Rolle
Erzeuge die finalen 16:9-Standbilder fuer `006-pilot-wundheilung` einzeln und in Reihenfolge.

## Verbindliche Bildwelt
Nutze ausschliesslich **Clean Animated Biology Illustration** nach:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Kurzfassung: clean animated biology illustration, simplified recognizable anatomy, smooth organic forms, clean outlines, soft gradients, subtle depth, bright calm background, clear biological colors, simple composition.

Pro Bild bevorzugt 2–5 zentrale Elemente und genau ein Hauptprozess. Sichtbarer Text nur Deutsch und nur aus `label-plan.json`. Keine Zusatztexte, keine alte 2.5D-/Premium-3D-/Medical-CGI-Optik.

## HARTE REGEL: PRODUKTIONSNUMMERN SIND UNSICHTBAR

`Bild_01`, `Bild_02`, `BILD 01`, Szenennummern, Dateinamen, Asset-IDs und Prompttitel sind ausschliesslich interne Produktionsmetadaten.

**Sie duerfen niemals im erzeugten Bild sichtbar sein.**

Die Bezeichnung `Bild_XX` dient nur zum Speichern der Datei. Sichtbar sein duerfen ausschliesslich die explizit fuer die jeweilige Szene genannten deutschen Labels bzw. der geplante Cover-Titel.

Wenn eine interne Bild-/Szenennummer, ein Dateiname oder ein Prompttitel sichtbar erscheint: Bild verwerfen und neu erzeugen.

## Produktion
Jedes Bild einzeln erzeugen, pruefen und als `Bild_XX.png` speichern. Fehlgeschlagene Version ersetzen, nicht sammeln.

1. **Bild_01:** skin cutaway with a small fresh cut and tiny damaged vessel. Visible title only: `Wie heilt eine Wunde?`. Never show `Bild_01` or any production number.
2. **Bild_02:** wound as start of a simple repair journey. Visible label only: `Reparatur startet`.
3. **Bild_03:** skin cross-section with one small damaged vessel. Visible label only: `Blutgefäß`.
4. **Bild_04:** before/after of the same vessel becoming narrower. Visible label only: `Verengung`.
5. **Bild_05:** platelets attach to the injured vessel wall and gather. Visible labels: `Blutplättchen`, `verletzte Stelle`.
6. **Bild_06:** thin fibrin strands appear between platelets. Visible label only: `Fibrin`.
7. **Bild_07:** fibrin strands form a mesh across the injury. Visible label only: `Fibrinnetz`.
8. **Bild_08:** a few platelets and red blood cells caught in the fibrin mesh. Visible labels: `Blutplättchen`, `Fibrinnetz`.
9. **Bild_09:** clot seals the damaged vessel opening. Visible label only: `Gerinnsel`.
10. **Bild_10:** clot above, first immune cells arriving below. No visible text.
11. **Bild_11:** a few immune cells move toward injured tissue. Visible label only: `Immunzellen`.
12. **Bild_12:** one immune cell removes a few bacteria and damaged cell fragments. Visible labels: `Bakterien`, `Zellreste`.
13. **Bild_13:** before/after skin cross-section showing mild redness and slight swelling. Visible labels: `Rötung`, `Schwellung`.
14. **Bild_14:** cleaned wound space beginning to fill with new repair tissue. Visible label only: `Wiederaufbau`.
15. **Bild_15:** one fibroblast lays down a few collagen fibers. Visible labels: `Fibroblast`, `Kollagen`.
16. **Bild_16:** a small new capillary grows into repair tissue. Visible label only: `neue Blutgefäße`.
17. **Bild_17:** skin cells move from both wound edges toward the center. Visible labels: `Hautzellen`, `Wundrand`.
18. **Bild_18:** skin surface nearly closed with a tiny remaining gap. Visible label only: `neue Haut`.
19. **Bild_19:** repaired tissue changes over time as fibers become more organized. Visible label only: `Umbau`.
20. **Bild_20:** before/after of disorganized collagen becoming more organized. Visible labels: `Kollagenfasern`, `stabiler`.
21. **Bild_21:** shallow healed injury compared with a deeper injury leaving a small scar. Visible label only on the deeper result: `Narbe`.
22. **Bild_22:** four connected mini-illustrations: clot stops bleeding → immune cell cleans → new tissue grows → stable healed skin. No visible text at all.

## QA pro Bild
- 16:9
- richtige Szene
- gleiche Illustrationswelt
- Hauptprozess innerhalb etwa einer Sekunde verstaendlich
- Labels exakt und korrekt
- keine unnoetigen Kleinteile
- keine zusaetzlichen Woerter
- **keine sichtbare Bild-/Szenennummer, Asset-ID, Dateiname oder Promptueberschrift**
- kein fotorealistisches Gewebe, CGI, glossy 3D oder Gore
- keine Duplikat-Komposition zum Nachbarbild

Final exakt als Dateien `Bild_01.png` bis `Bild_22.png` speichern. Diese Dateinamen duerfen niemals im Bild selbst sichtbar sein.
