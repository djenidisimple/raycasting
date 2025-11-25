import pygame
from config import TILE, MAP_TILE
map_game = [
    'WWWWWWWWWWW',
    'W.....WW..W',
    'W..WWWWW..W',
    'W......W..W',
    'W......W..W',
    'W..WW.....W',
    'W.........W',
    'WWWWWWWWWWW'
]

map_of_game = set()
mini_map = set()
for j, row in enumerate(map_game):
    for i, char in enumerate(row):
        if char == 'W':
            map_of_game.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))