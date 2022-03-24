from parapy.core import *
from parapy.geom import *

class Floor(GeomBase):

    @Part
    def floor(self):
        return Plane(reference=Point(0, 0, 0), normal=Vector(0, 0, 1), v_dim = 100,
                     display_mode='shaded', color='orange')