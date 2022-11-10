from datatypes import Size
import pygame.constants as pgConst

WINDOW_SIZE = Size(width=500, height=500)

MAX_SPEED = 100.0
MIN_SPEED = 0.0


KEY_BINDS: dict[str, list[int]] = {
    "move_up": [pgConst.K_w, pgConst.K_UP],
    "move_down": [pgConst.K_s, pgConst.K_DOWN],
    "move_left": [pgConst.K_a, pgConst.K_LEFT],
    "move_right": [pgConst.K_d, pgConst.K_RIGHT]
}