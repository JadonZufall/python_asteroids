from collections import namedtuple
from datatypes import RGBValue

BLACK = RGBValue(0, 0, 0, 255)
WHITE = RGBValue(255, 255, 255, 255)
GREEN = RGBValue(0, 255, 0, 255)


FPS_COLOR: RGBValue = GREEN
PLAYER_COLOR: RGBValue = GREEN
TARGET_COLOR: RGBValue = GREEN
PAUSE_COLOR: RGBValue = WHITE
CMD_COLOR: RGBValue = GREEN
CMD_BACK: RGBValue = BLACK