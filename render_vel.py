from datatypes import FontType, SurfaceType, Cord
from colors import FPS_COLOR


def render_vel(surface: SurfaceType, font: FontType, vel: float, dest: Cord) -> None:
    render: SurfaceType = font.render(f"vel = {vel:.2f}", True, FPS_COLOR)
    surface.blit(source=render, dest=dest, area=None)
    return None