import pygame
from config import *
from raycasting import ray_casting
from map import *
class Drawing:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont("Arial", 30)
    def background(self):
        pygame.draw.rect(self.screen, "skyblue", (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, "green", (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    def world(self, position, angle):
        ray_casting(self.screen, position, angle)
    def fps(self, clock):
        display_fps = "Fps: "+str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, "white")
        self.screen.blit(render, (WIDTH - 100, 50))
    def mini_map(self, player):
        self.screen_map.fill("blue")
        map_x , map_y = player.x // MAP_SCALE , player.y // MAP_SCALE
        pygame.draw.circle(self.screen_map, "red", (int(map_x), int(map_y)), 5)
        for x,y in mini_map:
            pygame.draw.rect(self.screen_map, "darkgray", (x,y, MAP_TILE, MAP_TILE))
        self.screen.blit(self.screen_map, MAP_POS)