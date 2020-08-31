import pygame
import neat
import time
import os
import random

import Bird 
import Pipe
import Terrain

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800

def draw_window(win, bird):
    win.blit(Terrain.BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird.Bird(200,200)
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run :
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()

if __name__=='__main__':
    main()
