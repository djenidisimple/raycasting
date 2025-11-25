import pygame
from config import *
from map import map_of_game
import math

def mapping(a, b):
    return ( a // TILE ) * TILE , ( b // TILE ) * TILE

def ray_casting(SCREEN, position, angle):
    ox , oy = position
    xm , ym = mapping(ox, oy)
    cur_angle = angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        # vertical lines
        x , dx = (xm + TILE, 1) if cos_a >= 0 else (xm , -1)
        for i in range(0, WIDTH, TILE):
            depth_v = ( x - ox ) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in map_of_game:
                break
            x += dx * TILE
        # horizontal lines
        y , dy = (ym + TILE, 1) if sin_a >= 0 else (ym , -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = ( y - oy ) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in map_of_game:
                break
            y += dy * TILE
        # projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(angle - cur_angle)
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.0001)
        color = (63 + c // 2, 63 + c // 2, 63 + c // 2 )
        pygame.draw.rect(SCREEN, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height ))
                # break
        cur_angle += DELTA_ANGLE
        # for depth in range(MAX_DEPTH):
        #     x = ox + depth * cos_a
        #     y = oy + depth * sin_a
        #     # pygame.draw.line(SCREEN, "red", position, (x,y), 2)
        #     if (x // TILE * TILE, y // TILE * TILE ) in map_of_game:
        # cur_angle %= 2 * math.pi