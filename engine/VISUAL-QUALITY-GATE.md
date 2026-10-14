# Visuelle Qualitätsprüfung – keine Rückkehr zum alten 3D-System

Aktuelle autoritative Regeln: `PROJECT_CONTRACT.md`, `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`, `engine/VISIBLE-TEXT-STANDARD.md` und `engine/CONTINUOUS-IMPROVEMENT.md`.

## Jedes NORMAL nummerierte Bild prüfen
- 16:9 und korrekte Bildnummer als **Dateimetadatum**, niemals sichtbar ins Bild gerendert
- Clean Animated Biology Illustration: organische lesbare Formensprache, leichte Schattentiefe, keine glossy CGI-, Medizinsoftware- oder überladene Infografik-Welt
- ein eindeutig verständlicher biologischer Lehrvorgang; ausreichend große relevante Elemente, keine Detail-Labyrinthe
- wissenschaftlich plausible Ursache/Wirkung, richtige Strukturen und Pfeile
- 0–2 kurze deutsche Beschriftungen nur wenn sie der Erklärung dienen, korrekter Kontrast dunkel auf hell bzw. hell auf dunkel
- keine englischen Flow-Labels, Produktionsnummern, zusätzlichen Figuren oder Textblöcke
- erkennbare Abwechslung in Motiv, Maßstab, Kamerawinkel und Lehrziel; keine Duplikate

## Cover separat prüfen
- `03_export/COVER.png` ist das ausgewählte YouTube-Thumbnail, nicht das Videoszenenbild `Bild_01`
- exakt ein sichtbarer Titeltext; kein Untertitel, kein Anatomie-Label, keine Dateinummer
- auf Smartphonegröße kontrastreich und klar lesbar; Cover nicht in der Video-Timeline

## Timeline und fertiges Video
- erste Szene startet mit `Bild_01` als eigenständigem Video-Hook, nicht mit dem Cover
- Voice↔Bild passt ohne fehlende Sätze oder Umstellungen
- bevorzugt 3–6 Sekunden pro Standbild, niemals über 7 Sekunden
- Remotion nur für Audio, Timing, dezente Pans/Zooms und Schnitt, kein sichtbarer Editor-Text
- 1920×1080 bei 30 fps, Ton vollständig, keine schwarzen Bildabschnitte
- sichtbarer Endexport nur vier Dateien, technische QA verborgen unter `.intern/`

## Nach jedem Video: Lernen ist Pflicht
Problematische Bild-IDs / Zeitstellen zusammen mit der konkreten Fehlerursache im tatsächlichen Video festhalten. Mindestens zwei umgesetzte und getestete global gültige Verbesserungen ins Ledger übernehmen, nicht nur „guter Stil“ behaupten. `engine/CONTINUOUS-IMPROVEMENT.md` ist verbindlich.
