import React from 'react';
import {Composition} from 'remotion';
import {ObjectTalkVideo} from './ObjectTalkVideo';
import {project} from './project.generated';

export const Root: React.FC = () => {
  const durationInFrames = Math.max(1, Math.ceil(project.durationSeconds * project.fps));

  return (
    <Composition
      id="ObjectTalk"
      component={ObjectTalkVideo}
      durationInFrames={durationInFrames}
      fps={project.fps}
      width={project.width}
      height={project.height}
    />
  );
};
