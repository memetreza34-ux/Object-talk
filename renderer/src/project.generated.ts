export type MotionType =
  | 'static'
  | 'slow-push-in'
  | 'slow-pull-out'
  | 'pan-left'
  | 'pan-right';

export type SceneRuntime = {
  scene: number;
  file: string;
  startFrame: number;
  durationInFrames: number;
  motion: MotionType;
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
