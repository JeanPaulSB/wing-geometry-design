"""
Under the following architecture, a wing represents a collection of
surfaces. Where a surfaces consist of a "section" of the wing.
It allows you to have a wing with different geometries.

"""

class Wing:
    def __init__(self) -> None:
        self.surfaces = [] 
        self.c_root = None
        self.c_tip = None
        self.tr = None
        self.b = None
        
