
"""
AstraX SO-101 - Dataset Validation

Checks recorded episode metadata before conversion
to the LeRobot dataset format.

Reference implementation only.
Does not create a LeRobot dataset.
"""

import argparse
import json
from pathlib import Path

from nwaves_hackathon.layout import STATE_DIM, ACTION_DIM


def validate_episode(path):
    with open(path, encoding="utf-8") as file:
        episode = json.load(file)

    frames = episode.get("frames", [])

    if not frames:
        raise ValueError(f"{path}: No frames found")

    previous_time = None

    for index, frame in enumerate(frames):
        if len(frame["state"]) != STATE_DIM:
            raise ValueError(
                f"Frame {index}: Invalid state dimension"
            )

        if len(frame["action"]) != ACTION_DIM:
            raise ValueError(
                f"Frame {index}: Invalid action dimension"
            )

        for camera in ("scene_image", "wrist_image"):
            image_path = Path(frame[camera])
            if not image_path.is_file():
                raise FileNotFoundError(
                    f"Missing {camera}: {image_path}"
                )

        timestamp = float(frame["timestamp"])

        if previous_time is not None:
            if timestamp <= previous_time:
                raise ValueError(
                    "Timestamps must be increasing"
                )

        previous_time = timestamp

    return len(frames)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data/episodes",
    )
    args = parser.parse_args()

    directory = Path(args.input)
    episodes = sorted(directory.glob("episode_*.json"))

    if not episodes:
        print("No recorded episodes found.")
        return

    total_frames = 0

    for episode in episodes:
        count = validate_episode(episode)
        total_frames += count
        print(f"Validated {episode.name}: {count} frames")

    print(f"Episodes validated: {len(episodes)}")
    print(f"Total frames: {total_frames}")
    print("Ready for a separate LeRobot conversion step.")


if __name__ == "__main__":
    main()
