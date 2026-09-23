# Produktionsplan – Pilot 001 Sauerstoff

Ziel: erster echter kleiner Object-Talk-Pilot mit ungefähr 2–2,5 Minuten Laufzeit und 28 Bildern.

## 1. Verbindliche Stilbasis

Vor Produktion gelten immer:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/OBJECT-TALK-STYLE-EXAMPLE.md
02_bildprompts/STYLE-LOCK-BEISPIEL.md
```

Grundregel:

**Object-Talk-Welt zuerst, Thema danach.**

Der O₂-Guide, Augenstil, Materialien, Farbwelt und Lichtlogik bleiben im ganzen Video identisch.

## 2. Voice erzeugen

Datei:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Text 1:1 in die Voice-KI übernehmen. Finales Audio in:

```text
01_script/audio/
```

## 3. Google Flow starten

Datei:

```text
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Den kompletten Prompt verwenden.

Zuerst ausschließlich:

```text
Bild_01
```

Bild_01 ist:
- Cover
- Hook
- erster Shot
- Master Style Frame
- verbindliche Referenz für alle 27 Folgeframes

Bild_01 muss klar wie die festgelegte virale Object-Talk-3D-Animationswelt aussehen. Kein medizinischer CGI-Look, keine realistische Haut, keine realistischen Gewebetexturen, kein Stock-3D, kein Toy-Look.

## 4. Genau eine Freigabe

Flow darf nur nach `Bild_01` auf die Nutzerfreigabe warten.

Nach Freigabe von Bild_01 arbeitet Flow **ohne weitere Rückfragen** bis zum Ende.

Nicht erlaubt:
- nach einem 5er-Block fragen, ob weitergemacht werden soll
- zwischen Bildern zusätzliche Freigaben verlangen
- den Lauf freiwillig pausieren

## 5. Restliche Bilder automatisch produzieren

Reihenfolge:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
Bild_22–26
Bild_27–28
Recovery-Pass
```

Die Blöcke sind nur interne QA-Schritte. Nach jedem Block automatisch weiter.

Jedes Bild:
- einzeln generieren
- `Bild_01` als exakte Style-/Continuity-Referenz verwenden
- denselben O₂-Guide und dieselbe Character-DNA beibehalten
- auf Object-Talk-Animationsstil prüfen
- auf korrekte deutsche Labels prüfen
- bei Fehler auf Recovery-Liste setzen

Fehlerhafte Bilder automatisch bis zu 3-mal neu versuchen.

## 6. Finale Bildausgabe

Am Ende einen finalen Ordner erstellen:

```text
001-pilot-sauerstoff-im-blut_bilder/
```

Darin exakt:

```text
Bild_01.png
Bild_02.png
...
Bild_28.png
```

Keine Varianten, keine Lücken, keine Zusätze wie `neu`, `final2`, `v3` oder `copy`.

Zusätzlich:

```text
001-pilot-sauerstoff-im-blut_bilder.zip
```

Die ZIP enthält exakt denselben finalen Ordner.

Repo-Ziel für die ZIP:

```text
02_bildprompts/bilder-zip/001-pilot-sauerstoff-im-blut_bilder.zip
```

## 7. Phase 3 / Video

Sobald Voice + alle 28 Bilder vorhanden sind:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut --phase2
python tools/prepare_phase3.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Dann verwenden:

```text
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Antigravity/Remotion übernimmt jetzt ausdrücklich:
- Audioaufbereitung
- Whisper-Worttimings
- exakte Szenen-Timeline
- Bildimport
- O₂-Guide als visuellen roten Faden
- Bewegungsrichtung entlang der Sauerstoffreise
- dezente hochwertige Kamerabewegung
- sparsame deutsche Overlays
- Render
- QA

Ziel: **ein zusammenhängender Object-Talk-Animationsfilm statt einer Diashow.**

## 8. Ergebnis

```text
04_export/fertiges-video/final-video.mp4
```

Der 10-Bilder-Mini-Test 002 wird übersprungen.
