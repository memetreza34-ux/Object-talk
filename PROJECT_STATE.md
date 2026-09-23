# Object-Talk – Project State

Letzte Aktualisierung: 23.09.2026

## Aktiver Produktionspilot

Aktiv:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Der 10-Bilder-Mini-Test `002-mini-test-sauerstoff` wird übersprungen. Pilot 001 ist der erste echte 2–3-Minuten-Pilotfilm.

## Ziel

- ungefähr 2–2,5 Minuten
- 28 Erklärbilder
- hohe visuelle Dichte
- **stark animierte Premium-3D-Animationsfilm-Welt**
- 85–90 % Stilisierung, nur wenig Realismus zur Erkennbarkeit
- kein medizinischer CGI-Look
- Bild_01 = Cover + Hook + Master Style Frame

## Verbindliche Bildwelt

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

Kanal-DNA:
- eindeutig animierter 3D-Feature-Film-Look
- weiche gerundete skulptierte Formen
- glatte Premium-Materialien
- vereinfachte Anatomie
- keine realistische Haut, Poren oder Gewebetexturen
- Coral/Apricot/Rot/Burgunder + tiefe Navy/Pflaume
- blass Cyan/Türkis als O₂-Kontrast
- starke filmische Tiefe
- keine medizinische CGI, kein Stock-3D, kein Toy-Look

## Flow-Regel – nur eine Freigabe

Flow darf den Nutzer normal nur **ein einziges Mal** stoppen:

```text
Bild_01 erzeugen
→ Bild_01 intern prüfen
→ Bild_01 zeigen
→ einmalige Nutzerfreigabe
```

Nach dieser Freigabe:

```text
Bild_02–06
→ interne QA
→ Bild_07–11
→ interne QA
→ Bild_12–16
→ interne QA
→ Bild_17–21
→ interne QA
→ Bild_22–26
→ interne QA
→ Bild_27–28
→ Recovery-Pass
→ finaler Ordner
→ ZIP
```

**Keine weiteren Fragen zwischen den Blöcken.**

Flow darf nicht mehr fragen:
- „Soll ich weitermachen?“
- „Soll ich den nächsten Block erstellen?“
- „Bist du zufrieden?“

Nur ein echter technischer Blocker nach mehreren automatischen Versuchen darf den Lauf stoppen.

## Finale Bildausgabe

Am Ende muss vorhanden sein:

```text
001-pilot-sauerstoff-im-blut_bilder/
├── Bild_01.png
├── Bild_02.png
├── ...
└── Bild_28.png
```

Zusätzlich:

```text
001-pilot-sauerstoff-im-blut_bilder.zip
```

Keine Varianten, keine Lücken, keine falschen Dateinamen.

## Prompt- und Textregel

- Flow-Anweisungen: Englisch
- sichtbarer Text: nur Deutsch
- normale Szenen: 1–3 wichtige Labels
- Cover: nur Hook, keine kleinen Labels
- falsches/englisches Label = Regeneration oder Remotion-Fallback

## Nutzerdateien

Voice:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Flow:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Antigravity:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Kurzplan:
```text
youtube-videos/001-pilot-sauerstoff-im-blut/PRODUKTIONSPLAN-KURZ.md
```

## Was noch fehlt

Für den echten Render fehlen:

1. finales Voice-Audio
2. finale Flow-Bilder `Bild_01.png` bis `Bild_28.png`
3. Bild-QA/Reviews

## Nächster Schritt

Den aktualisierten Flow-Prompt verwenden und `Bild_01` neu erzeugen. Es muss **klar wie hochwertige 3D-Animation** aussehen und nicht wie medizinische Anatomie. Nach einmaliger Freigabe läuft Flow selbstständig bis zum fertigen 28-Bilder-Ordner und ZIP weiter.