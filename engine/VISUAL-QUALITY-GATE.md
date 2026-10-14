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

## Zusätzlicher visueller Director-Check ab Video 011

- Kann ein Zuschauer den zentralen Vorgang im Bild in etwa 1 Sekunde erkennen? Wenn nein: klare Vergrößerung oder weniger Bildelemente.
- Ist das Motiv selbst ein erklärendes Bild statt nur „Person schaut/isst/steht“? Wenn nein: ersetzen, sofern nicht wirklich eine Alltagshandlung erklärt wird.
- Zeigt der Film überwiegend hochwertige lehrreiche Cutaways/Prozesse/Vergleiche und nur punktuell Ganzkörper-Personen?
- Farben und Perspektiven variieren sinnvoll, ohne den durchgehenden gezeichneten Stil zu verlieren.
- Wenn eine Szene anschaulicher mit einem beschrifteten Querschnitt oder Diagramm wäre, wird nicht automatisch eine Person verwendet.
- Bei wiederholtem Menschen-/Küchenmotiv trotz unterschiedlichen Sätzen: visuelles Konzept vor Flow-Regeneration ändern, nicht nur Seed austauschen.
- Aus Meta-Plan-Feldern darf NICHT auf echte Bildqualität geschlossen werden: jedes generierte Bild nach Produktion gesondert prüfen.

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
