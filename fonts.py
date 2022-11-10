import pygame.font as pyfont
if not pyfont.get_init():
    pyfont.init()

from datatypes import FontType

sys_font: FontType = pyfont.SysFont(name="arial", size=25, bold=False, italic=False)
debug_font: FontType = pyfont.SysFont(name="arial", size=12, bold=False, italic=False)

