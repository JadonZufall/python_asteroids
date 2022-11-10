from pygame import Surface, Rect
SurfaceType = Surface
RectType = Rect

from pygame.time import Clock
ClockType = Clock

from pygame.font import Font
FontType = Font

from collections import namedtuple
RGBValue = namedtuple("RGBValue", ["r", "g", "b", "alpha"])
Size = namedtuple("Size", ["width", "height"])
Cord = namedtuple("Cord", ["x", "y"])

from typing import List
Polygon = List[Cord]