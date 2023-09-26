from geometry.surface import Surface
from geometry.wing import Wing

s1 = Surface(b_half=5, c_root=2, c_tip=1, le_sweep=1)
s2 = Surface(b_half=5, c_root=1, c_tip=0.5, le_sweep=1)
trapezoidWing = Wing()
trapezoidWing.add_surface(s1)
trapezoidWing.add_surface(s2)

trapezoidWing.plot()
