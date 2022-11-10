from pygame import Surface, SRCALPHA
from datatypes import SurfaceType, Size, Cord, RGBValue

scan_line: SurfaceType = Surface(Size(width=500, height=5), SRCALPHA)
scan_line.fill(RGBValue(r=100, g=100, b=100, alpha=100))


def draw_scan_lines(surface: SurfaceType, game_tick: int) -> None:
    surface_size: Size = Size(width=surface.get_width(), height=surface.get_height())
    target_y = game_tick % surface_size.height
    surface.blit(source=scan_line, dest=Cord(x=0, y=target_y), area=None)
    return None

    
    