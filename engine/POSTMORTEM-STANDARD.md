# Verbindliches Post-Video-Review – höchste Priorität

Gilt **nach jedem tatsächlich fertig produzierten Video**. Zusammen mit `engine/CONTINUOUS-IMPROVEMENT.md` ist diese Prüfung Pflicht, bevor das nächste Video freigegeben wird. Ein leeres Postmortem mit drei Listen ist kein Review; ein nur ausgefülltes Postmortem ohne tatsächliche globale Änderungen ist keine Verbesserung.

## Interne Review-Datei
`VIDEOORDNER/.intern/05_info/improvement-review.json`, nie in `03_export/`. Vorlage unter `youtube-videos/_TEMPLATE/.intern/05_info/`.

Für historische Videos 000–009 werden keine leeren Altpostmortems ohne reale Sichtung nachträglich als geprüft erklärt.

## Vollständige echte Sichtung
- finales MP4 (Laufzeit und Abschnitte), separates Titelcover, fertiges Audio und die tatsächlich angezeigten Bilder ansehen
- Hook, Hauptteil, Schluss, Erklärungstiefe, Informationsbudget, sichtbare Labels, Abwechslung, Flow-Stabilität, Flow-Anatomie, Voice↔Bild-Verhältnis, Textkontrast, 16:9-Render, Qualitäts- und Exportfehler untersuchen
- Nutzerfeedback wörtlich bzw. sinngemäß erfassen; nicht verfügbare YouTube-Zuschauerdaten als unbekannt markieren
- mindestens zwei konkrete Stärken, **mindestens drei mit Zeitstelle/Bild-ID verortete Schwächen**, zu jeder Schwäche eine überprüfbare Ursache
- die stärksten 2–5 dauerhaften Fehlerquellen beheben, nicht bloß beschreiben; jede Implementierung belegt betroffene globale Dateien und einen echten Test mit PASS
- vorheriges Video nur mit tatsächlich vorliegenden Daten vergleichen; qualitative Bewertung von objektiver Metrik trennen
- neue Regeln und Prompts möglichst in bestehende globale Dateien und Tools integrieren; keine neue Bildwelt erfinden, keine Altfilme umschreiben

## Harte Vererbung
Nach bestandener inhaltlicher und technischer Prüfung:

```bash
python tools/improvement_loop.py register youtube-videos/VIDEOORDNER
```

Dadurch wird `engine/IMPROVEMENT-LEDGER.json` ergänzt und die 2–5 gerade behobenen Probleme werden zur verbindlichen Aufgabe für das nächste Video.

Das nächste Projekt belegt vor Phase 1 in `.intern/05_info/improvement-applied.json` für jede vorgeschriebene Lesson die konkrete Anpassung, die verwendete echte Datei und deren Überprüfung. `tools/validate_planning_v2.py` setzt diesen Prüfpunkt automatisch durch.

## Ehrlichkeit und Freigabe
- keine Behauptung tatsächlicher Medienprüfungen ohne Sichtung
- keine erfundenen Zeitstellen, Scores oder YouTube-Analytics
- wenn der Film noch nicht fertig ist, Review-Status `PENDING_FINAL_MEDIA` lassen
- falls Fix nicht bestanden: Test nicht PASS nennen, Fehler weiter untersuchen
- vollständige Evidenz ist wichtiger als kosmetische Verbesserungspunkte
- sichtbarer Export für neue Produktionen bleibt bei **genau vier Dateien** gemäß `engine/EXPORT-STANDARD.md`
