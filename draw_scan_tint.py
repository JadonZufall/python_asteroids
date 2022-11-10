from pygame import Surface, SRCALPHA

from datatypes import RGBValue, Size, Cord, SurfaceType

tint = Surface(Size(width=500, height=500), SRCALPHA)
tint.fill(RGBValue(r=25, g=150, b=25, alpha=25))


def draw_tint(surface: SurfaceType) -> None:
    surface.blit(source=tint, dest=Cord(x=0, y=0), area=None)
    return None
    