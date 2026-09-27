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
  type OverlayRuntime,
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

const positionStyle = (position: OverlayRuntime['position']): React.CSSProperties => {
  if (position === 'top-center') {
    return {top: 70, left: '50%', transform: 'translateX(-50%)', alignItems: 'center'};
  }
  if (position === 'bottom-left') {
    return {bottom: 72, left: 78, alignItems: 'flex-start'};
  }
  if (position === 'center') {
    return {top: '50%', left: '50%', transform: 'translate(-50%, -50%)', alignItems: 'center'};
  }
  return {top: 72, left: 78, alignItems: 'flex-start'};
};

const OverlayItem: React.FC<{overlay: OverlayRuntime; scene: SceneRuntime}> = ({
  overlay,
  scene,
}) => {
  const frame = useCurrentFrame();
  const sceneDuration = Math.max(1, scene.durationInFrames);
  const start = Math.round(sceneDuration * overlay.startFraction);
  const duration = Math.max(1, Math.round(sceneDuration * overlay.durationFraction));
  const end = Math.min(sceneDuration - 1, start + duration);
  const fadeFrames = Math.max(4, Math.min(10, Math.round(sceneDuration * 0.08)));

  const opacityIn = interpolate(frame, [start, start + fadeFrames], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: smoothEase,
  });
  const opacityOut = interpolate(frame, [Math.max(start, end - fadeFrames), end], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: smoothEase,
  });
  const opacity = Math.min(opacityIn, opacityOut);

  if (frame < start || frame > end) return null;

  const enter = interpolate(frame, [start, start + fadeFrames], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: smoothEase,
  });

  const translateY = overlay.animation === 'fade-slide' ? interpolate(enter, [0, 1], [12, 0]) : 0;
  const scale = overlay.animation === 'pop' ? interpolate(enter, [0, 1], [0.975, 1]) : 1;
  const accentWidth = overlay.animation === 'underline' ? `${Math.round(enter * 100)}%` : '28%';

  const fontSize = overlay.kind === 'heading' ? 54 : overlay.kind === 'keyword' ? 43 : 38;
  const fontWeight = overlay.kind === 'heading' ? 800 : 700;
  const padding = overlay.kind === 'heading' ? '18px 26px 16px' : '15px 22px 14px';

  return (
    <div
      style={{
        position: 'absolute',
        zIndex: 10,
        display: 'flex',
        flexDirection: 'column',
        pointerEvents: 'none',
        opacity,
        ...positionStyle(overlay.position),
      }}
    >
      <div
        style={{
          transform: `translateY(${translateY}px) scale(${scale})`,
          transformOrigin: overlay.position.includes('left') ? 'left center' : 'center center',
          color: '#18364f',
          fontFamily: 'Inter, Arial, Helvetica, sans-serif',
          fontSize,
          fontWeight,
          lineHeight: 1.04,
          letterSpacing: '-0.025em',
          maxWidth: 760,
          padding,
          borderRadius: 20,
          background: 'rgba(248, 252, 255, 0.94)',
          border: '1px solid rgba(24, 54, 79, 0.10)',
          boxShadow: '0 10px 30px rgba(23, 55, 80, 0.16)',
        }}
      >
        {overlay.text}
        <div
          style={{
            marginTop: 10,
            height: 4,
            width: accentWidth,
            maxWidth: '100%',
            borderRadius: 999,
            background: '#49b6d6',
          }}
        />
      </div>
    </div>
  );
};

const SceneOverlays: React.FC<{scene: SceneRuntime}> = ({scene}) => {
  const overlays = scene.overlays ?? [];
  if (overlays.length === 0) return null;

  return (
    <AbsoluteFill>
      {overlays.map((overlay, index) => (
        <OverlayItem key={`${scene.scene}-${index}-${overlay.text}`} overlay={overlay} scene={scene} />
      ))}
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
          <SceneOverlays scene={scene} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
