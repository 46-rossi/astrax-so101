
"""
AstraX SO-101 - Reference Episode Recorder

Stores synchronized observation metadata and
six-channel robot state/action data.

Reconstructed implementation, not the original
NWaves recorder or a LeRobot dataset exporter.
"""

import json
from pathlib import Path

from nwaves_hackathon.layout import STATE_DIM, ACTION_DIM


class EpisodeRecorder:
    def __init__(self, output_dir="data/episodes"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.frames = []

    def record(
        self,
        timestamp,
        state,
        action,
        scene_image,
        wrist_image,
    ):
        if len(state) != STATE_DIM:
            raise ValueError("Expected six state values")

        if len(action) != ACTION_DIM:
            raise ValueError("Expected six action values")

        self.frames.append({
            "timestamp": float(timestamp),
            "state": [float(x) for x in state],
            "action": [float(x) for x in action],
            "scene_image": str(scene_image),
            "wrist_image": str(wrist_image),
        })

    def save(self, episode_id, success, task):
        output = self.output_dir / (
            f"episode_{episode_id:04d}.json"
        )

        payload = {
            "episode_id": episode_id,
            "task": task,
            "success": bool(success),
            "frame_count": len(self.frames),
            "frames": self.frames,
        }

        output.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )

        self.frames.clear()
        return output
