from models import player_model, player_target_model
from datatypes import Cord, SurfaceType, RectType

from pygame.transform import rotate as rotate_surface


def render_player(surface: SurfaceType, pos: Cord, rot: float, targeted: bool = False) -> None:
    updated_model: SurfaceType = rotate_surface(surface=player_model, angle=rot)
    rect: RectType = updated_model.get_rect()
    rect.center = pos
    surface.blit(source=updated_model, dest=rect, area=None)
    if targeted:
        rect2: RectType = player_target_model.get_rect()
        rect2.center = pos
        surface.blit(source=player_target_model, dest=rect2, area=None)
    return None
    
    