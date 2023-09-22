
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
- b (span)[m]
- c_root (chord @root)[m]
- c_tip (chord @tip)[m]
- le_sweep (leading edge sweep angle) [deg]
- qc_sweep (c/4 sweep angle) [deg]
- mc_sweep (c/2 sweep angle) [deg]
"""

class Surface:
    def __init__(self,b,c_root,c_tip,le_sweep,qc_sweep,mc_sweep) -> None:
        self.b = b
        self.c_root = c_root
        self.c_tip = c_tip
        self.le_sweep = le_sweep
        self.qc_sweep = qc_sweep
        self.mc_sweep = mc_sweep 
