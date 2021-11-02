import pygame
import sys
from settings import *
from tiles import Tile

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    pygame.display.update()
    clock.tick(60)
