from parapy.core import *
from parapy.geom import *


class Stiffener(GeomBase):
    s_len = Input(20e-2)
    s_len_flange = Input(5e-2)
    s_thick = Input(1e-2)


    @Part
    def flangeSection(self):
        crv1 = LineSegment(Point(0, 0, 0), Point(1, 0, 0))
        crv2 = LineSegment(Point(1, 0, 0), Point(1, 1, 0))
        line = Wire([crv1, crv2])
        return line

