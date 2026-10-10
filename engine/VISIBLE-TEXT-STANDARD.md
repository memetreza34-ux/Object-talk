# Visible Text & Information Density Standard – Object-Talk

Status: **KANONISCH / VERBINDLICH**

Diese Datei regelt allen sichtbaren Text und die Informationsdichte in finalen Google-Flow-Bildern.

## 1. Grundsatz

Das Bild erklaert zuerst visuell. Text ist nur eine Orientierungshilfe.

**Wenn ein Bild ohne Label verstaendlich ist, wird kein Label hinzugefuegt.**

## 2. Cover – harte Sonderregel

Das Cover (separate PNG-Datei; Bild_01 ist erste normale Szene) darf genau **einen sichtbaren Textblock** enthalten:

- nur den geplanten deutschen Titel / Hook
- bevorzugt 3–7 Woerter
- keine Anatomie-Labels
- keine Pfeiltexte
- keine Unterzeile
- keine Zusatzinfo
- keine Bild-/Szenennummer
- keine Dateinamen oder Produktionshinweise

Wenn neben dem Titel irgendein weiterer Text sichtbar ist: **FAIL → neu generieren.**

## 3. Normale Bilder

Standard:
- **0–2 kurze Labels pro Bild**
- maximal **2 Labels**
- bevorzugt 0 oder 1, wenn das Bild bereits eindeutig ist
- jedes Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- keine ganzen Saetze
- keine dekorativen Anfuehrungszeichen um Labels
- keine Wiederholung von Begriffen, die visuell offensichtlich sind

## 4. Kontrast / Lesbarkeit

Jeder sichtbare Text muss sofort lesbar sein.

Harte Regeln:
- heller / sehr heller Hintergrund → **dunkle Schrift** (z. B. dunkles Grau, Navy, dunkles Blau)
- dunkler Hintergrund → **helle Schrift**
- niemals helle Schrift auf hellem Hintergrund
- niemals dunkle Schrift auf dunklem Hintergrund
- Text bevorzugt in ruhiger negativer Flaeche platzieren
- falls der Hintergrund hinter dem Text unruhig ist: Textposition verschieben statt Lesbarkeit zu opfern
- Hinweislinie und Text muessen beide klar sichtbar sein

Schwacher Kontrast oder schwer lesbarer Text: **FAIL → neu generieren.**

## 5. Informationsbudget pro Bild

Ein Bild soll in etwa einer Sekunde grob verstanden werden koennen.

Standard:
- **1 Hauptaussage / 1 Hauptprozess**
- bevorzugt 2–4 zentrale sichtbare Elemente
- maximal 2 Labels
- nur Details zeigen, die fuer den aktuellen Voice-over-Beat gebraucht werden

Wenn ein Bild mehrere Erklaerziele, viele Strukturen oder mehrere Textgruppen braucht:
1. unwichtige Information weglassen, oder
2. den Beat auf **mehrere Bilder** aufteilen.

**Mehr Bilder sind besser als ein ueberladenes Bild.**

## 6. Was weggelassen werden soll

Nicht beschriften oder darstellen, wenn es fuer den aktuellen Lehrpunkt nicht notwendig ist:
- offensichtliche Objekte
- Nebenstrukturen ohne Erklaerfunktion
- zusaetzliche Fachbegriffe nur weil sie anatomisch vorhanden sind
- redundante Pfeile
- dekorative Icons
- Wiederholungen des Voice-over als Text

## 7. Label-Stil

- Deutsch
- kurze einfache Begriffe
- klare Sans-Serif-Schrift
- keine Anfuehrungszeichen im finalen Artwork
- duenne klare Hinweislinie nur wenn noetig
- eindeutige Zuordnung zur Struktur
- Fachwort nur wenn es wirklich gelehrt wird; sonst einfacheren Begriff bevorzugen

## 8. QA – harte Freigabe

Jedes Bild muss vor ACCEPT bestehen:

- `text_contrast = PASS`
- `information_density = PASS`
- `label_count = PASS`
- `label_readability = PASS`
- `no_unnecessary_text = PASS`

Cover zusaetzlich:
- `cover_title_only = PASS`
- exakt ein sichtbarer Textblock

Bei einem FAIL wird das Bild nicht repariert oder per Remotion ueberdeckt, sondern in Flow neu erzeugt.

## Goldene Regel

**So wenig Text wie moeglich, so viel wie noetig. Cover nur Titel. Ein Bild = eine Hauptidee. Gute Lesbarkeit vor Dekoration.**

## Neue 3-Ordner-Regel ab Video 009 (verbindlich)

Sichtbar nur `01_script/`, `02_bildprompts/`, `03_export/`. Technische Planungs- und Renderdateien unter verstecktem `.intern/`. Das Google-Flow-Cover ist ein **eigenes YouTube-Thumbnail `03_export/COVER.png` und KEINE Szene `Bild_01`**. Bild_01 ist sofort die erste normale biologische Illustration, nur die normal nummerierten Bilder in die Bilder-ZIP und das MP4. Nach Coverwahl Bilder 01–05, danach 06–10 usw. Untertitel aus echter Audioausrichtung nach `03_export/UNTERTITEL-MIT-ZEITEN.txt`. Alle Labels sollen häufig dann erscheinen, wenn sie einen Vorgang verständlicher machen, ansonsten textfrei; höchstens 2 kurze Wörter/Gruppen pro Bild. Keine Vorlagen-Uploads, keine Remotion-Textlayer, keine überfüllten Szenen.
