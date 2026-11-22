
# AstraX — SO-101 Physical AI Robotics

### Simulation-to-Real Learning for Robotic Pick-and-Place

**Team Vayu Astra | NWaves Physical AI Buildathon 2026 | Bengaluru**

🏆 **2nd Place — Physical AI Buildathon 2026**

---

## About the Project

AstraX is a Physical AI robotics project developed by **Team Vayu Astra** from Don Bosco Institute of Technology, Bengaluru, for the NWaves Physical AI Buildathon 2026.

The project explores how an SO-101 robotic arm can learn a pick-and-place task using simulation, robotic demonstrations, and imitation learning.

Our approach combines NVIDIA Isaac Sim, Isaac Lab, LeRobot, and an Action Chunking Transformer (ACT) policy to study the transfer of learned robotic behavior from simulated environments to a physical robotic arm.

### Project Objective

The objective is to enable an SO-101 robotic arm to:

1. Locate a cube using camera observations.
2. Approach the cube with its gripper.
3. Grasp and lift the cube.
4. Transport it toward a target tray.
5. Release the cube inside the tray boundaries.
6. Complete the placement with the cube resting inside the tray.

The project focuses on simulation-to-real learning, robotic manipulation, demonstration-based training, and physical evaluation.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| NVIDIA Isaac Sim | Physics-based robotic simulation |
| NVIDIA Isaac Lab | Robot task environments and demonstrations |
| Python | Simulation scripting and data processing |
| YAML | Scene configuration and task parameters |
| Hugging Face LeRobot | Robotic learning dataset framework |
| ACT | Action Chunking Transformer policy |
| PyTorch | Deep learning framework |
| NWaves GPU Workspace | Model training and evaluation |

---

## Hardware Configuration

The physical setup used:

- SO-101 leader robotic arm
- SO-101 follower robotic arm
- Laptop webcam for the fixed scene view
- Wrist-mounted camera for gripper observations
- Cube for manipulation
- Target placement tray
- Robot control laptop

### Camera Configuration

Two camera views were used.

**Scene Camera**

A fixed camera observes the workspace, cube position, and target tray.

**Wrist Camera**

A camera mounted near the gripper provides observations for object alignment and grasping.

The recorded image resolution was 640 × 480 pixels.

---

## System Architecture

```text
          NVIDIA Isaac Sim
                  |
                  v
          NVIDIA Isaac Lab
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
       ACT Policy Training
                  |
                  v
         Policy Evaluation
                  |
                  v
        Physical SO-101 Arm
                  |
                  v
        Pick-and-Place Task
```

The workflow connects simulation-based demonstrations with robot learning and physical evaluation.

---

## Task Specifications

| Parameter | Value |
|---|---|
| Robot | SO-101 |
| Task | Cube pick-and-place |
| Cube width | 25 mm |
| Control frequency | 30 Hz |
| Camera resolution | 640 × 480 |
| State dimensions | 6 |
| Action dimensions | 6 |
| Approach height | 7 cm |
| Carry clearance | 2 cm |
| Release gap | 3 mm |
| Post-release hold | 0.5 seconds |

The task is considered successful when the cube is released inside the tray boundaries and remains at rest.

---

## Demonstration Generation

The original simulation workflow used scripted demonstrations to produce training examples.

### Motion Sequence

```text
Approach
   |
   v
Descend
   |
   v
Close Gripper
   |
   v
Lift Cube
   |
   v
Carry to Tray
   |
   v
Release Cube
   |
   v
Verify Placement
```

### Scene Randomization

The station configuration included randomized cube and tray positions.

Example configuration:

```yaml
randomization:
  cube_x: [0.14, 0.21]
  cube_y: [-0.16, -0.08]
  cube_yaw_deg: [-45, 45]
  tray_x: [0.20, 0.25]
  tray_y: [-0.01, 0.05]
  tray_yaw_deg: [-10, 10]
  surface: [white]
```

Randomization was used to provide demonstrations across different object placements and orientations.

---

## Dataset Collection

The project presentation documents:

| Dataset Source | Demonstrations |
|---|---:|
| Successful simulated demonstrations | 20 |
| Uploaded physical demonstrations | 30 |
| Total documented demonstrations | 50 |

Each recorded demonstration included:

- Fixed scene camera observations
- Wrist camera observations
- Six-channel robot state
- Six-channel commanded action
- Timestamps
- Episode metadata

The original dataset recordings are not included in this public repository.

---

## ACT — Action Chunking Transformer

ACT was used as the robot learning policy.

The model learns from recorded demonstrations to predict sequences of future robot actions.

### Learning Pipeline

```text
Camera Observations
         +
Current Robot State
         |
         v
   ACT Policy
         |
         v
Future Action Sequence
         |
         v
SO-101 Joint and Gripper Targets
         |
         v
New Observation
```

The robot repeatedly observes its environment, predicts actions, and updates its behavior using new observations.

---

## Original NWaves Training Workflow

The following commands are documented from the original NWaves hackathon environment.

### Generate Simulated Demonstrations

```bash
nwaves-generate --config configs/station.yaml --episodes 20 --name sim20
```

### Convert Demonstrations to Dataset

```bash
nwaves-dataset sim20 my_team/sim20
```

### Train ACT Policy

```bash
nwaves-train my_team/sim20 --policy act --steps 2000 --name sim_baseline
```

### Physical Dataset Workflow

```bash
nwaves-realdata pull real
nwaves-realdata check real
nwaves-dataset real my_team/real
```

### Evaluate Policy

```bash
nwaves-eval --policy ~/workspace/outputs/RUN
```

### Submit Policy

```bash
nwaves-submit ~/workspace/outputs/RUN
```

**Note:** These commands require the original NWaves environment and its tools. They are provided to document the competition workflow and are not expected to run in a standard local Python installation.

The exact training-data mixture used for the final competition checkpoint has not been independently verified.

For additional details, see [Training Documentation](docs/TRAINING.md).

---

## Evaluation Results

The project presentation documents an improvement in successful cube placements during practice evaluation.

| Evaluation | Successful Trials | Success Rate |
|---|---:|---:|
| Early evaluation | 2 / 10 | 20% |
| Later evaluation | 5 / 10 | 50% |

### Performance Improvement

**20% → 50%**

- Initial successful trials: 2 out of 10
- Later successful trials: 5 out of 10
- Improvement: 30 percentage points

These are recorded historical practice results from the hackathon, not results reproduced by the reconstructed code in this repository.

---

## Competition Achievement

### NWaves Physical AI Buildathon 2026

**Location:** Bengaluru, Karnataka, India

**Team:** Vayu Astra

**Institution:** Don Bosco Institute of Technology, Bengaluru

### Competition Results

| Round | Achievement |
|---|---|
| Round 1 | 5th Place — Qualified for final |
| Round 2 | 2nd Place |
| Final Achievement | Runner-Up |

🏆 **Second Place — Physical AI Buildathon 2026**

**Team Prize: ₹1,50,000**

---

## Repository Structure

```text
astrax-so101/
|
|-- .github/
|   `-- workflows/
|       `-- python-tests.yml
|
|-- configs/
|   `-- station.yaml
|
|-- docs/
|   `-- TRAINING.md
|
|-- nwaves_hackathon/
|   |-- __init__.py
|   |-- layout.py
|   |-- recorder.py
|   `-- to_lerobot.py
|
|-- scripts/
|   `-- generate.py
|
|-- tests/
|   `-- test_project.py
|
|-- .gitignore
|-- README.md
|-- requirements.txt
`-- Robotic-Arm.pdf
```

---

## Reference Code

This repository includes reconstructed Python reference implementations based on the documented project workflow.

### Available Modules

**layout.py**

Defines shared task parameters, robot state dimensions, camera settings, and demonstration constants.

**generate.py**

Creates a reference pick-and-place motion plan describing the demonstration stages.

**recorder.py**

Provides a basic structure for recording robot states, actions, timestamps, and camera image paths.

**to_lerobot.py**

Validates recorded episode metadata before a separate LeRobot conversion step.

### Important Limitations

The reference code is not a complete reproduction of the original NWaves simulator.

The repository does not currently include:

- The original Isaac Lab simulation environment
- Full robot motion controllers
- Original recorded datasets
- Trained ACT policy checkpoints
- Complete LeRobot dataset conversion
- Physical robot deployment integrations

The reconstructed scripts are intended for documentation, learning, and further development.

---

## Running the Reference Code

### Requirements

- Python 3.10 or newer
- Git
- A compatible operating system

The current reference scripts use Python standard-library modules.

### Clone the Repository

```bash
git clone https://github.com/46-rossi/astrax-so101.git
cd astrax-so101
```

### Run the Reference Demonstration Planner

From the repository root:

```bash
python -m scripts.generate
```

This creates:

```text
outputs/demo_plan.json
```

The output contains the reference motion stages.

It does not execute an Isaac Sim simulation or move a physical robot.

### Run the Unit Tests

```bash
python -m unittest discover -s tests -v
```

### Dataset Validation

If compatible episode metadata and image files are available:

```bash
python -m nwaves_hackathon.to_lerobot --input data/episodes
```

This validates the recorded metadata but does not export a complete LeRobot dataset.

---

## Automated Testing

The repository uses GitHub Actions to run Python syntax checks and unit tests.

The automated workflow checks:

- Python source syntax
- Shared task constants
- Robot state and action dimensions
- Demonstration sequence order
- Post-release timing

The automated tests validate the reference implementation only.

They do not test the original NWaves training environment or physical hardware.

---

## Project Presentation

The original project presentation is available here:

[View Vayu Astra SO-101 Robotic Arm Demonstration](Robotic-Arm.pdf)

The presentation covers:

- Software architecture
- Task specification
- Physical robot setup
- Demonstration generation
- Scene randomization
- Dataset collection
- ACT training
- Simulation-to-real adaptation
- Evaluation results
- Competition achievement

---

## Future Development

Potential future improvements include:

- Reconstructing the complete Isaac Lab task environment
- Integrating an operational SO-101 motion controller
- Implementing a complete LeRobot dataset exporter
- Reproducing ACT training with accessible datasets
- Improving robustness across object placements
- Expanding physical evaluation trials
- Adding reproducible simulation-to-real benchmarks

These are proposed improvements, not completed project features.

---

## Team

### Team Vayu Astra

**Don Bosco Institute of Technology, Bengaluru**

Developed for the NWaves Physical AI Buildathon 2026.

---

## Acknowledgements

We acknowledge the technologies and platforms used during the project:

- NWaves Physical AI Buildathon
- NVIDIA Isaac Sim
- NVIDIA Isaac Lab
- Hugging Face LeRobot
- SO-101 robotics ecosystem

---

## Disclaimer

This repository is a technical documentation and reconstructed reference-code showcase of the team's hackathon project.

Original competition results are documented from the project presentation. The complete competition workspace, original source code, datasets, and trained policy checkpoints are not included.

---

### AstraX

**Learning in Simulation. Acting in Reality.**

*Developed by Team Vayu Astra.*
