import pygame, sys
from pygame.locals import *



window_size=(900,600)
screen=pygame.display.set_mode(window_size,0,32)
display=pygame.Surface((900,600))

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=60
