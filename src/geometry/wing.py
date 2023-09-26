"""
Under the following architecture, a wing represents a collection of
surfaces. Where a surfaces consist of a "section" of the wing.
It allows you to have a wing with different geometries.

"""
import matplotlib.pyplot as plt
from .surface import Surface
class Wing:
    def __init__(self) -> None:
        self.surfaces = [] 
        self.c_root = 0
        self.c_tip = 0
        self.tr = 0
        self.b_half = 0
        
    def add_surface(self,surface):
        # updating wing span
        
        self.surfaces.append(surface)
        surface.build()

        if len(self.surfaces) > 1:
            surface.A.x += self.b_half
            surface.B.x += self.b_half
            surface.C.x += self.b_half
            surface.D.x += self.b_half

        #plt.plot((surface.A.x,surface.C.x),(surface.A.y,surface.C.y),linestyle = "dashed")
        plt.plot((surface.A.x,surface.B.x),(surface.A.y,surface.B.y),linestyle = "dashed")
        plt.plot((surface.C.x,surface.D.x),(surface.C.y,surface.D.y),linestyle = "dashed")
        #plt.plot((surface.B.x,surface.D.x),(surface.B.y,surface.D.y),linestyle = "dashed")
        self.b_half += surface.b_half


    def plot(self):
        # joining first and last section
        if len(self.surfaces)>=1:
            first_surface = self.surfaces[0]
            last_surface = self.surfaces[-1]

            plt.plot((first_surface.A.x,first_surface.C.x),(first_surface.A.y,first_surface.C.y))
            plt.plot((last_surface.B.x,last_surface.D.x),(last_surface.B.y,last_surface.D.y))
        plt.show()
            


