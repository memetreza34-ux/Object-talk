import React from 'react';
import {Audio} from '@remotion/media';
import {
  AbsoluteFill,
  CanvasImage,
  Easing,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {
  project,
  type MotionType,
  type SceneRuntime,
} from './project.generated';

const smoothEase = Easing.inOut(Easing.ease);

const SceneImage: React.FC<{scene: SceneRuntime}> = ({scene}) => {
  const frame = useCurrentFrame();
  const duration = Math.max(1, scene.durationInFrames - 1);

  let scale = 1;
  let translate = '0px 0px';

  const motion: MotionType = scene.motion ?? 'slow-push-in';

  if (motion === 'slow-push-in') {
    scale = interpolate(frame, [0, duration], [1, 1.038], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
      easing: smoothEase,
    });
  } else if (motion === 'slow-pull-out') {
    scale = interpolate(frame, [0, duration], [1.038, 1], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
      easing: smoothEase,
    });
  } else if (motion === 'pan-left') {
    scale = 1.03;
    translate = interpolate(frame, [0, duration], ['24px 0px', '-24px 0px'], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
      easing: smoothEase,
    });
  } else if (motion === 'pan-right') {
    scale = 1.03;
    translate = interpolate(frame, [0, duration], ['-24px 0px', '24px 0px'], {
      extrapolateLeft: 'clamp',
      extrapolateRight: 'clamp',
      easing: smoothEase,
    });
  }

  return (
    <AbsoluteFill style={{overflow: 'hidden', backgroundColor: '#000'}}>
      <CanvasImage
        src={staticFile(scene.file)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          scale,
          translate,
        }}
      />
    </AbsoluteFill>
  );
};

export const ObjectTalkVideo: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {project.audioFile ? <Audio src={staticFile(project.audioFile)} /> : null}

      {project.scenes.map((scene) => (
        <Sequence
          key={scene.scene}
          from={scene.startFrame}
          durationInFrames={scene.durationInFrames}
          layout="absolute-fill"
        >
          <SceneImage scene={scene} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
