from pygame import Surface, Rect, SRCALPHA
from pygame.draw import polygon as draw_polygon
from pygame.draw import circle as draw_circle
from pygame.draw import rect as draw_rect
from const import WINDOW_SIZE
from datatypes import Polygon, SurfaceType, Size, Cord, RectType
from colors import PLAYER_COLOR, TARGET_COLOR, PAUSE_COLOR

# Player model drawing
player_size: Size = Size(width=50, height=50)
player_shape: Polygon = [
    Cord(x=player_size.width // 2, y=0),
    Cord(x=player_size.width, y=player_size.height),
    Cord(x=player_size.width // 2, y=(player_size.height - player_size.height // 4)),
    Cord(x=0, y=player_size.height),
    Cord(x=player_size.width // 2, y=0)
]
player_model: SurfaceType = Surface(player_size, SRCALPHA)
draw_polygon(surface=player_model, color=PLAYER_COLOR, points=player_shape, width=0)


# Player targetting circle
player_radius = max(player_size)
player_target_model: SurfaceType = Surface(Size(width=player_size.width*2, height=player_size.height*2), SRCALPHA)
player_rect_target_model: RectType = player_target_model.get_rect()
draw_circle(
    surface=player_target_model, 
    color=TARGET_COLOR, 
    center=player_rect_target_model.center, 
    radius=player_radius, 
    width=1
)

# Pause button
pause_size: Size = Size(width=100, height=100)
pause_button: SurfaceType = Surface(pause_size, SRCALPHA)
# pause_rect_w: int = (pause_size.width // 2) - (pause_size.width * .75)
# pause_rect2_offset: int = pause_size.width + (pause_size.width * .75)
pause_rect1 = Rect((0, 0), (45, 100))
pause_rect2 = Rect((55, 0), (100, 100))
draw_rect(surface=pause_button, color=PAUSE_COLOR, rect=pause_rect1, width=0, border_radius=-1)
draw_rect(surface=pause_button, color=PAUSE_COLOR, rect=pause_rect2, width=0, border_radius=-1)
