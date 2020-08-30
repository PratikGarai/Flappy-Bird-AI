import pygame
import neat
import time
import os
import random

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images","base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images","bg.png")))
