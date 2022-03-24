
from parapy.core import *
from casing import Casing
from floor import Floor

class World(Base):

    gravity = 9.80665 # [m/s2]
    depth = Input() # [m] positive is below sea level.

    @Part
    def casing(self):
        return Casing()

    @Part
    def floor(self):
        return Floor()

if __name__ == '__main__':
    from parapy.gui import display
    obj = World(label="world")
    display(obj)
