from datatypes import FontType, SurfaceType, Cord
from colors import FPS_COLOR


def render_pos(surface: SurfaceType, font: FontType, pos: Cord, dest: Cord) -> None:
    message: str = f"pos = ({pos.x:>5.2f}, {pos.y:>5.2f})"
    render: SurfaceType = font.render(message, True, FPS_COLOR)
    surface.blit(source=render, dest=dest, area=None)
    return None