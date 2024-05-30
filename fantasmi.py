import pygame, sys
from pygame.locals import *
pygame.init()
import random

class Fantasmi:
    def __init__(self, display,labirinto,pacman)->None:
        self.display=display
        self.labirinto=labirinto
        self.size=labirinto.tile_width, labirinto.tile_height
        self.velocita_x=labirinto.tile_width/1
        self.velocita_y=labirinto.tile_height/1
        self.pos=[0,0]
        self.pos[0]=16*labirinto.tile_width
        self.pos[1]=16*labirinto.tile_height
        self.image=pygame.image.load('./immaginipacman/fantasma1.png')
        self.image=pygame.image.transform.scale(self.image, self.size)
        self.vett_velocita=[6,6]
        self.direzione=2
