
# AstraX — SO-101 Physical AI Robotics

### Simulation-to-Real Robotic Pick-and-Place

**Team Vayu Astra | Physical AI Buildathon 2026 | Bengaluru**

🏆 **2nd Place — Physical AI Buildathon 2026**

---

## Project Overview

AstraX is a robotics project developed by Team Vayu Astra
for the NWaves Physical AI Buildathon in Bengaluru.

The project explores how an SO-101 robotic arm can learn
a pick-and-place task using simulated demonstrations,
real-world demonstrations, and imitation learning.

The objective is to pick up a cube, transport it to a
designated tray, release it inside the tray walls,
and leave it at rest.

## Technology Stack

| Technology | Purpose |
|---|---|
| NVIDIA Isaac Sim | Physics-based robot simulation |
| NVIDIA Isaac Lab | Simulation task environments |
| Python | Robotics scripts and data processing |
| YAML | Scene and task configuration |
| LeRobot | Robot learning dataset framework |
| ACT | Action Chunking Transformer policy |
| NWaves GPU Workspace | Training and evaluation |

## Hardware

- SO-101 leader robotic arm
- SO-101 follower robotic arm
- Fixed laptop webcam
- Wrist-mounted gripper camera
- Cube and target tray
- Robot control laptop

## System Architecture

```text
Simulated SO-101 Environment
            |
            v
 Scripted Demonstrations
            |
            v
    Episode Recording
            |
            v
    LeRobot Dataset
            |
            v
     ACT Training
            |
            v
     Policy Evaluation
            |
            v
   Physical SO-101 Arm
```

## Task Specifications

| Parameter | Value |
|---|---|
| Cube width | 25 mm |
| Control frequency | 30 Hz |
| Camera resolution | 640 x 480 |
| Robot state | 6 channels |
| Robot action | 6 channels |
| Post-release hold | 0.5 seconds |
| Approach height | 7 cm |
| Carry clearance | 2 cm |
| Release gap | 3 mm |

## Demonstration Workflow

The scripted demonstration follows these stages:

1. Approach the cube.
2. Descend toward the object.
3. Close the gripper.
4. Lift the cube.
5. Carry it toward the tray.
6. Release the cube inside the tray.
7. Allow the object to settle.

## Dataset

The project presentation documents:

- 20 successful simulated demonstrations
- 30 uploaded physical demonstrations
- Two synchronized RGB camera views
- Six-channel observations and target actions
- Episode timestamps and metadata

The original datasets are not included in this repository.

## Model Training

The project used ACT (Action Chunking Transformer).

ACT predicts short sequences of future joint and
gripper targets from camera observations and the
current robot state.

The documented NWaves workflow included:

```bash
nwaves-generate --config configs/station.yaml --episodes 20 --name sim20
nwaves-dataset sim20 my_team/sim20
nwaves-train my_team/sim20 --policy act --steps 2000 --name sim_baseline
```

These commands belong to the original NWaves environment.

See [Training Documentation](docs/TRAINING.md).

## Evaluation Results

| Evaluation | Successful Trials | Success Rate |
|---|---|---|
| Early evaluation | 2 / 10 | 20% |
| Later evaluation | 5 / 10 | 50% |

The recorded practice success rate improved by
30 percentage points.

These results are from the hackathon presentation
and have not been reproduced using this repository.

## Competition Achievement

**Physical AI Buildathon — Bengaluru, November 2026**

Team: Vayu Astra

- Round 1: 5th place
- Round 2: 2nd place
- Team prize: INR 1,50,000

## Repository Structure

```text
astrax-so101/
├── README.md
├── .gitignore
├── configs/
│   └── station.yaml
├── docs/
│   └── TRAINING.md
├── nwaves_hackathon/
│   ├── __init__.py
│   ├── layout.py
│   ├── recorder.py
│   └── to_lerobot.py
└── scripts/
    └── generate.py
```

## Repository Status

This repository documents the hackathon workflow
and includes reconstructed reference Python modules.

The original NWaves simulator integration,
GPU workspace, complete training datasets,
trained model checkpoints, and physical robot
deployment environment are not included.

The reference generator describes motion phases
but does not execute an Isaac Lab simulation.

The recorder and dataset validator are educational
reference implementations rather than the original
NWaves recording and conversion tools.

## Team

**Team Vayu Astra**

Don Bosco Institute of Technology, Bengaluru

## Acknowledgements

- NWaves Physical AI Buildathon
- NVIDIA Isaac Sim and Isaac Lab
- Hugging Face LeRobot
- SO-101 open robotics ecosystem

---

**AstraX — Learning in Simulation, Acting in Reality**
