
"""
AstraX - SO-101 Physical AI Buildathon
Shared task constants.

Reconstructed from the project presentation.
Not a copy of the original NWaves source.
"""

# Robot control
CONTROL_HZ = 30
CONTROL_DT = 1.0 / CONTROL_HZ

# Simulated object dimensions (metres)
CUBE_WIDTH_M = 0.025

# Task requirements
POST_RELEASE_HOLD_S = 0.5

# Demonstration motion settings
APPROACH_HEIGHT_M = 0.07
CARRY_CLEARANCE_M = 0.02
RELEASE_GAP_M = 0.003

# Dataset specifications
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# SO-101 observations and actions
NUM_ARM_JOINTS = 5
NUM_GRIPPER_CHANNELS = 1
STATE_DIM = NUM_ARM_JOINTS + NUM_GRIPPER_CHANNELS
ACTION_DIM = STATE_DIM

# Demonstration targets recorded in the presentation
SIM_EPISODES = 20
REAL_EPISODES = 30
