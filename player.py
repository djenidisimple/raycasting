import math
import pygame
from config import pos_player, TILE
class Player:
    def __init__(self):
        self.x , self.y = pos_player
        self.angle = 0
        self.speed = 2
    @property
    def position(self):
        return (self.x, self.y)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
        # if keys[pygame.K_UP]:
        #     self.y -= self.speed 
        # if keys[pygame.K_DOWN]:
        #     self.y += self.speed
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed
        if keys[pygame.K_UP]:
            self.x += dx
            self.y += dy
        if keys[pygame.K_DOWN]:
            self.x -= dx
            self.y -= dy