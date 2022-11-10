from datatypes import RectType, SurfaceType, Cord
from const import WINDOW_SIZE
from models import pause_button


def render_pause(surface: SurfaceType) -> None:
    rect: RectType = pause_button.get_rect()
    dest: Cord = Cord(x=WINDOW_SIZE.width - rect.width - 25, y=25)
    surface.blit(source=pause_button, dest=dest)