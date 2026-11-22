
"""
AstraX SO-101 - Basic Project Tests

Tests reconstructed reference code.
Does not test Isaac Lab or physical hardware.
"""

import unittest

from nwaves_hackathon import layout as L
from scripts.generate import build_sequence


class TestAstraX(unittest.TestCase):

    def test_control_frequency(self):
        self.assertEqual(L.CONTROL_HZ, 30)

    def test_cube_dimensions(self):
        self.assertAlmostEqual(
            L.CUBE_WIDTH_M, 0.025
        )

    def test_robot_state(self):
        self.assertEqual(L.STATE_DIM, 6)
        self.assertEqual(L.ACTION_DIM, 6)

    def test_demonstration_sequence(self):
        steps = build_sequence()

        phases = [step.phase for step in steps]

        self.assertEqual(
            phases,
            [
                "approach",
                "descend",
                "close",
                "lift",
                "carry",
                "release",
                "settle",
            ],
        )

    def test_release_hold(self):
        steps = build_sequence()

        self.assertAlmostEqual(
            steps[-1].duration_s,
            L.POST_RELEASE_HOLD_S,
        )


if __name__ == "__main__":
    unittest.main()
