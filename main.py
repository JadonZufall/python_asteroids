from typing import Sequence
import pygame
pygame.init()

from datatypes import *
from colors import *
from fonts import *
from render_fps import render_fps
from render_rot import render_rot
from render_vel import render_vel
from render_dt import render_dt
from draw_scan_lines import draw_scan_lines
from render_pause import render_pause
from draw_scan_tint import draw_tint
from render_player import render_player
from render_pos import render_pos
from render_cmd import render_cmd
from update_player import update_player_rot, update_player_pos, update_player_vel
from const import WINDOW_SIZE

# General declarations
window: SurfaceType = pygame.display.set_mode(WINDOW_SIZE, True)
hud_layer: SurfaceType = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
clock: ClockType = pygame.time.Clock()
window_center: Cord = Cord(WINDOW_SIZE.width // 2, WINDOW_SIZE.height // 2)

# Game variable declarations
is_running: bool = True
game_state: int = "playing"
game_ticks: int = 0
player_pos: Cord = Cord(x=0, y=0)
player_vel: float = 0.0
player_rot: float = 0.0
targeting: any = "player"

# Debug variables should all be False for production
debug_mode: bool = True
display_player_vars: bool = True
display_cmd: bool = False
cmd_message: str = ""

# Game loop
while is_running:
    # Clear layers
    window.fill(BLACK)
    hud_layer.fill(pygame.SRCALPHA)

    # Timing
    ms: int = clock.tick(60)
    dt: float = ms / 1000.0
    fps: float = clock.get_fps()
    game_ticks += 1

    # Get player inputs
    keys: Sequence[bool] = pygame.key.get_pressed()
    key_mods: int = pygame.key.get_mods()

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        # Debug tools
        if event.type == pygame.KEYDOWN and debug_mode:
            if event.key == pygame.K_r and game_state == "playing":
                player_pos: Cord = Cord(x=0, y=0)
                player_rot: float = 0.0
                player_vel: float = 0.0
            elif event.key == pygame.K_SEMICOLON:
                if key_mods == 1 and game_state == "playing":
                    display_cmd: bool = True
                    game_state: str = "command_input"
                elif key_mods == 1 and game_state == "command_input":
                    display_cmd: bool = False
                    game_state: str = "playing"
            elif event.key and game_state == "command_input":
                if event.key == pygame.K_BACKSPACE:
                    cmd_message = cmd_message[:-1]
                elif event.key == pygame.K_RETURN:
                    if cmd_message.startswith("set_rot "):
                        try:
                            player_rot = float(cmd_message[len("set_rot "):])
                        except ValueError:
                            pass
                    elif cmd_message.startswith("set_x "):
                        try:
                            x = float(cmd_message[len("set_x "):])
                            player_pos = Cord(x=x, y=player_pos.y)
                        except ValueError:
                            pass
                    elif cmd_message.startswith("set_y "):
                        try:
                            y = float(cmd_message[len("set_y "):])
                            player_pos = Cord(x=player_pos.x, y=y)
                        except ValueError:
                            pass
                    elif cmd_message == "quit":
                        is_running: bool = False
                    elif cmd_message == "reset":
                        player_pos: Cord = Cord(x=0, y=0)
                        player_rot: float = 0.0
                        player_vel: float = 0.0
                    cmd_message = ""
                else:
                    cmd_message += event.unicode
    
    # Game updates
    if game_state == "playing":
        player_rot: float = update_player_rot(current_rot=player_rot, delta_time=dt, keys=keys)
        player_vel: float = update_player_vel(current_vel=player_vel, delta_time=dt, keys=keys)
        player_pos: Cord = update_player_pos(
            current_pos=player_pos, 
            current_vel=player_vel, 
            player_rot=player_rot, 
            delta_time=dt, 
            keys=keys
        )
    else:
        render_pause(surface=hud_layer)
    
    if game_state == "command_input":
        render_cmd(surface=hud_layer, font=sys_font, cmd_message=cmd_message)

    # Render targeting things
    if targeting == "player":
        render_player(surface=window, pos=window_center, rot=player_rot, targeted=True)
    else:
        render_player(surface=window, pos=window_center, rot=player_rot, targeted=False)

    # Render game objects
    

    # Render hud objects
    if debug_mode:
        render_fps(surface=hud_layer, font=debug_font, fps=clock.get_fps(), dest=Cord(x=25, y=25))
        render_dt(surface=hud_layer, font=debug_font, dt=ms, dest=Cord(x=25, y=45))
        render_rot(surface=hud_layer, font=debug_font, rot=player_rot, dest=Cord(x=25, y=65))
        render_pos(surface=hud_layer, font=debug_font, pos=player_pos, dest=Cord(x=25, y=85))
        render_vel(surface=hud_layer, font=debug_font, vel=player_vel, dest=Cord(x=25, y=105))

    # Merge hud layer
    window.blit(source=hud_layer, dest=Cord(x=0, y=0), area=None)

    # Post effects
    draw_scan_lines(surface=window, game_tick=game_ticks)
    draw_tint(surface=window)

    # Update the display
    pygame.display.flip()