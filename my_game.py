import pygame
import random
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEGIHT = 650,500
SCREEN = pygame.display.set_mode((WIDTH,HEGIHT))

GREEN = (0,255,0)
RED = (255,0,0)

snake_head = 25
Clock = pygame.time.Clock()
sx = 200
sy = 200

velosity_x = 10
velosity_y = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
               sy = sy-velosity_y
               
               
    pygame.draw.rect(SCREEN,GREEN,[sx+velosity_x, sy, snake_head, snake_head])
            
    Clock.tick(30)
    pygame.display.update()
        