import pygame
from player import *
from config import *
from map import *
from drawing import Drawing
from raycasting import ray_casting

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ray casting")

clock = pygame.time.Clock()

screen_map = pygame.Surface((110, 80), pygame.SRCALPHA)
screen_map.fill("blue")


player = Player()
worls = Drawing(screen, screen_map)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  
    screen.fill("black")
    ray_casting(screen, player.position, player.angle)
    player.move()
    # pygame.draw.line(screen, "red", player.position,(player.x + WIDTH * math.cos(player.angle), player.y + WIDTH * math.sin(player.angle)))
    worls.background()
    worls.world(player.position, player.angle)
    worls.fps(clock)
    worls.mini_map(player)
    # for x, y in map_of_game:
    #     pygame.draw.rect(screen, "white", (x , y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(60)