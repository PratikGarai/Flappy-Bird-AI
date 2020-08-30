import pygame
import neat
import time
import os
import random

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird1.png"))),\
                pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird2.png"))),\
                pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird3.png")))]

class Bird :
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        d = self.vel*self.tick_count + 0.5*3*self.tick_count**2  #d = ut + 0.5at^2

        if d>16 :   #terminal velocity
            d = 16
        if d<0 :    #a little boost to a jump
            d -= 2
        self.y = self.y + d
        if d<0 or self.y < self.height+50:
            if self.tilt<self.MAX_ROTATION :
                self.tilt = self.MAX_ROTATION
        else :
            if self.tilt>-90:
                self.tilt -= self.ROT_VEL

