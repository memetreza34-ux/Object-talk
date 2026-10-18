# Musterbeispiele Storyboard-v2 – nur Vorlage, keine Produktion

Diese zwei Ordner zeigen, wie ein Video nach den Regeln ab Video 011 geplant wird: eine Storyboard-Datei mit konkretem Hook, belegten Zahlen, Open Loops, nummerierten Stationen, illustrationsstarker Bildregie, Farbcode und Titel/Cover.

- `901-beispiel-hunger/` – Hunger und Sättigung
- `902-beispiel-verdauung/` – „Die Reise einer Pizza“

**Nicht produzieren.** Beide Themen sind mit 008 (Verdauung) und 010 (Hunger) bereits veröffentlicht. Keine Handoff-Links ausgeben, keine Bilder oder Voice dafür erzeugen.

So nutzt du sie:
1. `.intern/05_info/storyboard-source.json` als Vorbild für Aufbau und Ton lesen.
2. Für ein neues Thema `python tools/create_video.py 011-longform-THEMA` ausführen und dort ein eigenes Storyboard schreiben.
3. `python tools/build_phase1_package.py youtube-videos/011-longform-THEMA` und `python tools/validate_planning_v2.py youtube-videos/011-longform-THEMA`.

CI baut und prüft beide Beispiele bei jeder Änderung, damit Regeln und Werkzeuge zusammenpassen.
