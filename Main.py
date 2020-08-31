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

def draw_window(win, bird, pipes, base):
    win.blit(Terrain.BG_IMG, (0,0))

    for pipe in pipes :
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird.Bird(230,350)
    base = Terrain.Base(730)
    pipes = [Pipe.Pipe(700)]
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run :
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        # bird.move()
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width()<0:
                rem.append(pipe)
            if not pipe.passed and pipe.x<bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
        if add_pipe :
            score += 1
            pipes.append(Pipe.Pipe(600))

        for r in rem :
            pipes.remove(r)

        base.move()
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()

if __name__=='__main__':
    main()
