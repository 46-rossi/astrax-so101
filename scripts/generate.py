
"""
AstraX SO-101 - Demonstration Sequence

Reconstructed reference implementation.
This script describes the pick-and-place stages.
It does not connect to Isaac Sim or control motors.
"""

from dataclasses import dataclass
from pathlib import Path
import argparse
import json

from nwaves_hackathon import layout as L


@dataclass
class DemonstrationStep:
    phase: str
    description: str
    duration_s: float


def build_sequence():
    """Build the conceptual pick-and-place sequence."""
    return [
        DemonstrationStep(
            "approach",
            f"Move above cube by {L.APPROACH_HEIGHT_M} m",
            1.0,
        ),
        DemonstrationStep(
            "descend",
            "Lower gripper toward cube",
            1.0,
        ),
        DemonstrationStep(
            "close",
            "Close gripper around cube",
            0.5,
        ),
        DemonstrationStep(
            "lift",
            "Lift cube clear of starting surface",
            1.0,
        ),
        DemonstrationStep(
            "carry",
            f"Move toward tray with {L.CARRY_CLEARANCE_M} m clearance",
            1.5,
        ),
        DemonstrationStep(
            "release",
            f"Release near tray floor with {L.RELEASE_GAP_M} m gap",
            0.5,
        ),
        DemonstrationStep(
            "settle",
            "Hold after release",
            L.POST_RELEASE_HOLD_S,
        ),
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="outputs/demo_plan.json",
    )
    args = parser.parse_args()

    steps = build_sequence()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "project": "AstraX SO-101",
        "mode": "reference_plan_only",
        "control_hz": L.CONTROL_HZ,
        "steps": [step.__dict__ for step in steps],
    }

    output.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )

    print(f"Saved reference plan to {output}")
    print("No simulation or robot execution performed.")


if __name__ == "__main__":
    main()
