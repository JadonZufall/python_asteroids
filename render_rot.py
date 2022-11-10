from datatypes import FontType, SurfaceType, Cord
from colors import FPS_COLOR


def render_rot(surface: SurfaceType, font: FontType, rot: float, dest: Cord) -> None:
    render: SurfaceType = font.render(f"rot = {rot:.2f}", True, FPS_COLOR)
    surface.blit(source=render, dest=dest, area=None)
    return None