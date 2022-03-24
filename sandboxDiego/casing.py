from parapy.core import *
from parapy.geom import *


class Casing(GeomBase):
    c_length = Input(4)  # [m]
    c_width = Input(4)
    c_depth = Input(1)

    c_thick = Input(1e-1)  # [m]

    @Attribute
    def area(self):
        return self.c_length * self.c_width

    @Attribute
    def volume(self):
        return self.area * self.c_depth

    @Part
    def caseOuterBox(self):
        return Box(self.c_length, self.c_width, self.c_depth)

    @Part
    def caseInnerBox(self):
        return Box(self.c_length - 2*self.c_thick, self.c_width - 2*self.c_thick, self.c_depth - 2*self.c_thick,
                   position = translate(self.position,
                                      'x', self.c_thick,
                                      'y', self.c_thick,
                                      'z', self.c_thick))

    @Part
    def case(self):
        '''
        The actual outer casing object
        :return: Object
        '''
        return SubtractedSolid(self.caseOuterBox,
                               self.caseInnerBox,
                               color="pink")
