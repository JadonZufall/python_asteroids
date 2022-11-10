from colors import CMD_COLOR, CMD_BACK
from datatypes import SurfaceType, FontType, RectType
from const import WINDOW_SIZE


def render_cmd(surface: SurfaceType, font: FontType, cmd_message: str) -> None:
    txt: SurfaceType = font.render(f"~{cmd_message}", True, CMD_COLOR, CMD_BACK)
    dest = (25, WINDOW_SIZE.height - 25)
    surface.blit(source=txt, dest=dest, area=None)