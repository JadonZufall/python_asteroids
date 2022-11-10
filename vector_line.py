from pygame.draw import line as draw_line

from datatypes import Cord, SurfaceType, RGBValue

def render_line(surface: SurfaceType, rot: int) -> None:
    draw_line(
        surface=surface, 
        color=RGBValue(r=255, g=255, b=255, alpha=255), 
        start_pos=Cord(x=0, y=0), 
        end_pos=Cord(x=0, y=0),
        width=2
    )
