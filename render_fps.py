from datatypes import FontType, SurfaceType, Cord
from colors import FPS_COLOR


def render_fps(surface: SurfaceType, font: FontType, fps: float, dest: Cord) -> None:
    render: SurfaceType = font.render(f"fps = {str(int(fps))}", True, FPS_COLOR)
    surface.blit(source=render, dest=dest, area=None)
    return None

