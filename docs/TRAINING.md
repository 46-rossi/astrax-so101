
# AstraX SO-101 — Training Workflow

## Overview

AstraX was developed for the NWaves Physical AI
Buildathon 2026 by Team Vayu Astra.

The project explores simulation-to-real learning
for an SO-101 robotic arm performing a cube
pick-and-place task.

## Technology Stack

- NVIDIA Isaac Sim — robotic simulation
- NVIDIA Isaac Lab — task environments
- Python and YAML — scripts and configuration
- LeRobot — robot learning dataset framework
- ACT — Action Chunking Transformer
- NWaves GPU Workspace — training and evaluation

## Demonstration Data

The project presentation records:

| Data source | Demonstrations |
|---|---:|
| Successful simulated demonstrations | 20 |
| Uploaded physical demonstrations | 30 |

Each demonstration uses:

- Fixed scene camera
- Wrist-mounted camera
- Six-channel robot state
- Six-channel target action
- Timestamps and episode metadata

Camera resolution: 640 x 480
Control frequency: 30 Hz

## Simulation Workflow

The documented NWaves commands were:

```bash
nwaves-generate --config configs/station.yaml --episodes 20 --name sim20
```

Convert recorded demonstrations:

```bash
nwaves-dataset sim20 my_team/sim20
```

Train the ACT policy:

```bash
nwaves-train my_team/sim20 --policy act --steps 2000 --name sim_baseline
```

These commands describe the original NWaves
environment. They are not expected to run in
a standard local Python installation.

## Physical Demonstrations

The original workflow used:

```bash
nwaves-realdata pull real
nwaves-realdata check real
nwaves-dataset real my_team/real
```

Calibration and joint conventions must be
checked before combining real and simulated
demonstrations.

The final winning checkpoint's exact
training-data mixture is unverified.

## Evaluation

The project presentation reports:

| Evaluation | Successful trials |
|---|---:|
| Early run | 2 / 10 |
| Later run | 5 / 10 |

Success rate increased from 20% to 50%
in these recorded practice evaluations.

These are historical project results,
not results reproduced by this repository.

## Deployment Workflow

The documented evaluation command:

```bash
nwaves-eval --policy ~/workspace/outputs/RUN
```

The documented submission command:

```bash
nwaves-submit ~/workspace/outputs/RUN
```

The submitted policy was selected on the
robot laptop for supervised testing.

A motors-off dry run and camera/start-pose
checks were part of the deployment procedure.

## Competition Outcome

Physical AI Buildathon, Bengaluru, 2026

Team: Vayu Astra

- Round 1: Fifth place
- Round 2: Second place
- Team prize: INR 1,50,000

## Repository Limitations

The original NWaves GPU workspace, recorded
datasets, policy checkpoints, and complete
Isaac Lab environment are not included.

Some Python modules in this repository are
reconstructed reference implementations.

They should not be represented as the
original competition source code.
