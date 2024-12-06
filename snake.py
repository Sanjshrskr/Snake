import pygame
import sys
import random

pygame.init()

SW, SH = 800, 800

BLOCK_SIZE = 50
Font = pygame.font.Font("font.tff", BLOCK_SIZE*2)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen,"#9467bd", rect, 1 )

drawGrid()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()
    clock.tick(10)