import matplotlib.pyplot as plt
import numpy as np
from .point import Point

"""
A surface consist of a geometrical section of the wing. As mentioned before,
a Wing is just a surface or a collection of them.

NOTE: make sure to use consistent units

|------------------------------|
|                              |
|     SURFACE1                 |
|                              | 
|                              |
|                              |
|------------------------------|
params:
- b_half (span)[m]
- c_root (chord @root)[m]
- c_tip (chord @tip)[m]
- le_sweep (leading edge sweep angle) [deg]
"""


class Surface:
    def __init__(self, b_half, c_root, c_tip, le_sweep) -> None:
        self.b_half = b_half
        self.c_root = c_root
        self.c_tip = c_tip
        self.le_sweep = le_sweep

    """
    Make the corresponding geometrical computations in order to get
    the coordinates for each point that defines the wing's shape.
    
    """

    def build(self):
        # uppper_section: f(y) [A -> B]
        # lower_section: g(y) [C -> D]
        d = self.b_half * np.tan(self.le_sweep * np.pi / 180)
        self.A = Point(0, 0)
        self.B = Point(self.b_half, -d)
        self.C = Point(0, -self.c_root)
        self.D = Point(self.b_half, -d - self.c_tip)
