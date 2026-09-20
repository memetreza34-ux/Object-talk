# Fixed Remotion Renderer

Dieser Renderer ist die feste technische Runtime für Object-Talk-Longform. Antigravity soll **nicht pro Video einen neuen Editor erfinden**.

## Prinzip

Die kreative Planung endet vor Phase 3. Der Renderer bekommt nur:

- kanonisches `final-voiceover.wav`
- kanonische `Bild_XX.png`
- bereits aufgelöste `timeline.json`

`tools/build_renderer_runtime.py` kopiert die Assets nach `renderer/public/current/` und erzeugt `src/project.generated.ts`.

## Installation

```bash
cd renderer
npm install
```

## Runtime bauen

Vom Repository-Root:

```bash
python tools/build_renderer_runtime.py \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json \
  youtube-videos/THEMA/02_bildprompts/images \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav
```

## Preview

```bash
cd renderer
npm run studio
```

## Render

```bash
cd renderer
npm run render -- ../youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4
```

## Unterstützte Bewegungen

- `static`
- `slow-push-in`
- `slow-pull-out`
- `pan-left`
- `pan-right`

Die Bewegungen werden über Remotion-Frames und `interpolate()` erzeugt. Keine CSS-Keyframe-Animationen.

## Feste Regeln

- 1920×1080
- 30 fps
- Voiceover unverändert als Master-Timeline
- harte Schnitte zwischen Bildern als Standard
- keine automatisch erfundenen Übergänge
- keine Änderung der Szenenreihenfolge
- kein Looping von Bildern nötig
- Bildbewegung bleibt dezent

Nach Render immer `tools/qa_final.py` ausführen.
