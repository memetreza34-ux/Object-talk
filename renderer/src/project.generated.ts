export type MotionType =
  | 'static'
  | 'slow-push-in'
  | 'slow-pull-out'
  | 'pan-left'
  | 'pan-right';

export type OverlayKind = 'heading' | 'keyword' | 'callout';
export type OverlayPosition = 'top-left' | 'top-center' | 'bottom-left' | 'center';
export type OverlayAnimation = 'fade-slide' | 'pop' | 'underline';

export type OverlayRuntime = {
  kind: OverlayKind;
  text: string;
  position: OverlayPosition;
  animation: OverlayAnimation;
  startFraction: number;
  durationFraction: number;
};

export type SceneRuntime = {
  scene: number;
  file: string;
  startFrame: number;
  durationInFrames: number;
  motion: MotionType;
  overlays?: OverlayRuntime[];
};

export type ObjectTalkProject = {
  fps: number;
  width: number;
  height: number;
  durationSeconds: number;
  audioFile: string;
  scenes: SceneRuntime[];
};

// This placeholder is replaced by tools/build_renderer_runtime.py.
export const project: ObjectTalkProject = {
  fps: 30,
  width: 1920,
  height: 1080,
  durationSeconds: 1,
  audioFile: '',
  scenes: [],
};
