# Pilot 001 – 2:30-Minuten-Produktionsplan

## Ziel

Ein fertiger 16:9-Erklaerpilot mit exakt ca. **2:30 Minuten** Laufzeit.

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

## Format

- 1920×1080
- 16:9
- 30 fps
- ca. 150 Sekunden
- 28 visuelle Szenen
- Voiceover: `01_script/VOICEOVER-ZUM-KOPIEREN.txt`
- Voice-Ziel: 137 Woerter/Minute
- Timeline: `05_info/timeline-2m30.json`
- Bildwelt: `bildwelt/EXPLAINER-STYLE-LOCK.md`

## Bildwelt

Explainer-Szenen:

- moderne stilisierte 2.5D / Soft-3D-Erklaerillustration
- ca. 80 % Illustration / 20 % Soft-3D-Tiefe
- kein Medical-CGI
- keine realistischen nassen Gewebetexturen
- klare weiche Formen
- helle Hintergruende
- eine Hauptaussage pro Frame
- O2 immer Cyan/Tuerkis
- CO2 immer Violett
- rote Blutkoerperchen Dunkelrot
- Gefaesse Coral/Rot
- ATP Gelb/Gold

## Phase A – Voice

1. `VOICEOVER-ZUM-KOPIEREN.txt` 1:1 verwenden.
2. Stimme auf etwa 137 WPM einstellen.
3. Ziel-Audiolaenge: 145–155 Sekunden.
4. Keine Textaenderung fuer Timing; nur Tempo/Pausen anpassen.

## Phase B – Bilder in Google Flow

1. Agent Instructions aus `engine/FLOW-AGENT-INSTRUCTIONS.md` setzen.
2. `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` verwenden.
3. Zuerst nur `Bild_01` erzeugen.
4. Bild_01 muss Cover + Master-Style-Frame sein.
5. Nutzer gibt Bild_01 genau einmal frei.
6. Danach Bild_01 als echtes Flow-Reference/Ingredient an jede Folgegeneration anhaengen.
7. Bild_02–Bild_28 einzeln erzeugen.
8. Jedes Bild gegen `phase1-scenes.json`, `label-plan.json` und den Style-Lock pruefen.
9. Schlechte Bilder regenerieren; keine Ersatznummern erfinden.

## Phase C – Bewegung in Remotion

Bewegung bleibt dezent. Keine KI-Video-Clips sind fuer diesen Pilot zwingend erforderlich.

Erlaubte Standardbewegungen:

- slow-push-in: 3–6 % Zoom ueber die Szene
- slow-pull-out: 3–6 % Zoom-out
- pan-right / pan-left: langsame horizontale Bewegung
- micro-hold: fast statisch, maximal 1–2 % Drift
- final pull-out: 5–8 % langsamer Zoom-out

Wichtig:

- keine hektischen Ken-Burns-Bewegungen
- Bewegung muss Prozessrichtung unterstuetzen
- O2/CO2-Partikel koennen zusaetzlich subtil animiert werden, wenn die Szene dadurch klarer wird
- Labels nicht mitskalieren, wenn dadurch Lesbarkeit leidet

## Phase D – Text / Labels

Cover:

- nur Hook: `So reist Sauerstoff durch deinen Körper`
- keine Zusatzlabels

Normale Szenen:

- bevorzugt 0–2 kurze Labels
- nur Deutsch
- Begriffe aus `label-plan.json`
- Flow-Text nutzen, wenn korrekt
- bei wiederholtem Schreibfehler sauberes Bild ohne falschen Text nehmen und Label exakt in Remotion setzen

## Phase E – Audio + SFX

Voice steht klar im Vordergrund.

SFX nur dezent:

- sanfter Einatem-/Luftstrom bei Szenen 1–4
- subtiler weicher Übergangston bei O2-Diffusion Szenen 7–8
- sehr dezenter Herzschlag bei Szenen 13–14
- weiche Flow-/Whoosh-SFX bei Gefaessbewegung
- dezentes Energie-SFX bei ATP Szenen 22–24
- sanfter Ausatem bei Szene 27

Keine lauten Cartoon-SFX. Keine Musik ist fuer den Pilot erforderlich.

## Exakte Dauer

`05_info/timeline-2m30.json` ist autoritativ.

Gesamtdauer:

**150.0 Sekunden**

Szenen:

- Szene 01: 0:00–0:04
- Szene 02: 0:04–0:10
- Szene 03: 0:10–0:15
- Szene 04: 0:15–0:21
- Szene 05: 0:21–0:25.5
- Szene 06: 0:25.5–0:30.5
- Szene 07: 0:30.5–0:34.5
- Szene 08: 0:34.5–0:40.5
- Szene 09: 0:40.5–0:44.5
- Szene 10: 0:44.5–0:48.5
- Szene 11: 0:48.5–0:52.5
- Szene 12: 0:52.5–0:59.5
- Szene 13: 0:59.5–1:05.5
- Szene 14: 1:05.5–1:10.5
- Szene 15: 1:10.5–1:14.5
- Szene 16: 1:14.5–1:18
- Szene 17: 1:18–1:21.5
- Szene 18: 1:21.5–1:29
- Szene 19: 1:29–1:32.5
- Szene 20: 1:32.5–1:38.5
- Szene 21: 1:38.5–1:42
- Szene 22: 1:42–1:48
- Szene 23: 1:48–1:51.5
- Szene 24: 1:51.5–1:55
- Szene 25: 1:55–1:58.5
- Szene 26: 1:58.5–2:02
- Szene 27: 2:02–2:10
- Szene 28: 2:10–2:30

## Final-QA

Vor Export pruefen:

- Dauer 145–155 Sekunden, Ziel 150
- alle 28 Bilder vorhanden
- keine Bildnummer doppelt oder fehlend
- Cover nur Titel
- normale Labels korrekt und Deutsch
- kein Medical-CGI / Photorealismus
- O2/CO2-Farbcode konsistent
- keine Menschen-Presenter oder Torso-Mannequins
- Voice und Bild passen semantisch zusammen
- keine Szene erklaert mehr als einen Hauptpunkt gleichzeitig
- alle sichtbaren Texte fehlerfrei
- Audio ohne Clipping
- 1920×1080 / 30 fps

## Produktionsstatus

Der Inhalt, das Voiceover und die 150-Sekunden-Timeline sind produktionsbereit.

Der eigentliche finale MP4-Render kann erst erfolgen, sobald die 28 freigegebenen Bildassets und das finale Voice-Audio vorliegen.
