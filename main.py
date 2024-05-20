import pygame, sys
from pygame.locals import *



window_size=(700,800)
screenmenu=pygame.display.set_mode(window_size,0,32)
screengioco=pygame.display.set_mode(window_size,0,32,)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=60
