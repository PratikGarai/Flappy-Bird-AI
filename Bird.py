import pygame
import neat
import time
import os
import random

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird1.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird2.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird3.png")))]
