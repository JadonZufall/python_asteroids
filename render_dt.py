from datatypes import FontType, SurfaceType, Cord
from colors import FPS_COLOR


def render_dt(surface: SurfaceType, font: FontType, dt: float, dest: Cord) -> None:
    render: SurfaceType = font.render(f"dt = {dt:.2f}", True, FPS_COLOR)
    surface.blit(source=render, dest=dest, area=None)
    return None