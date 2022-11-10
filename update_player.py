from typing import Sequence
from pygame import K_RIGHT, K_LEFT, K_a, K_d
from const import KEY_BINDS, MIN_SPEED, MAX_SPEED
from math import sin, cos

from datatypes import Cord


def update_player_rot(current_rot: float, delta_time: float, keys: Sequence[bool]) -> float:
    result: float = current_rot
    # Update the rotation based on user key inputs
    for k in KEY_BINDS["move_left"]:
        if keys[k]:
            result += 300.0 * delta_time
            break
    for k in KEY_BINDS["move_right"]:
        if keys[k]:
            result -= 300.0 * delta_time
            break
    # Correct over / under shooting
    if result > 360:
        result -= 360
    elif result < 0:
        result += 360
    return result


def update_player_pos(
    current_pos: Cord, 
    current_vel: float,
    player_rot: float, 
    delta_time: float, 
    keys: Sequence[bool]
) -> Cord:
    delta_distance = current_vel * delta_time
    angle: float = player_rot - 90
    if angle < 0:
        angle += 360
    elif angle > 360:
        angle -= 360
    delta_x = cos(angle) * delta_distance
    delta_y = sin(angle) * delta_distance
    new_pos: Cord = Cord(x=current_pos.x + delta_x, y=current_pos.y + delta_y)
    return new_pos


def update_player_vel(current_vel: float, delta_time: float, keys: Sequence[bool]) -> Cord:
    result: float = current_vel
    speed_up: bool = False
    slow_down: bool = False
    for k in KEY_BINDS["move_up"]:
        if keys[k]:
            speed_up: bool = True
            break
    for k in KEY_BINDS["move_down"]:
        if keys[k]:
            slow_down: bool = True
            break
    
    if speed_up and slow_down:
        return result
    elif speed_up:
        result += 1000 * delta_time
    elif slow_down:
        result -= 1000 * delta_time
    
    if result < MIN_SPEED:
        result = MIN_SPEED
    elif result > MAX_SPEED:
        result = MAX_SPEED
    
    return result