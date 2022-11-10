from datatypes import SurfaceType
from datatypes import RGBValue


def draw_tint_filter(surface: SurfaceType, color: RGBValue) -> None:
    surface.fill(color)

