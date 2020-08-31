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

pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans",50)

def draw_window(win, bird, pipes, base, score):
    win.blit(Terrain.BG_IMG, (0,0))

    for pipe in pipes :
        pipe.draw(win)
    
    text = STAT_FONT.render("Score: "+str(score),1,(255,255,255))
    win.blit(text, (WINDOW_WIDTH-10-text.get_width(),10))

    base.draw(win)
    bird.draw(win)
    pygame.display.update()

def main(genomes, config):
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

        if bird.y + bird.img.get_height() >= 730 :
            pass

        base.move()
        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, \
            neat.DefaultReproduction, \
            neat.DefaultSpeciesSet, \
            neat.DefaultStagnation, \
            config_path )
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)

if __name__=='__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
