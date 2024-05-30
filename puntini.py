import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
import random

class Puntino():

    def __init__(self, display, labirinto, difficolta):
        self.display=display
        self.labirinto=labirinto
        self.size=labirinto.tile_width, labirinto.tile_height
        self.image=pygame.image.load('./immagini/ciliegia.png')
        self.image=pygame.transform.scale(self.image,self.size)
        self.difficolta=difficolta
        self.rect=[]
        self.durata=0

    def sceglirettangolo(self,pacman):
        for i in range(0,self.difficolta):
            if self.durata==0:
                n=random.randint(0,len(self.labirinto.tile_liberi)-1)
                self.rect[i]=self.labirinto.tile_liberi[n]
                while self.rect.colliderect(pacman):
                    n=random.randint(0,len(self.labirinto.tile_liberi)-1)
                    self.rect[i]=self.labirinto.tile_liberi[n]
                self.durata=70

    def draw(self):
        if self.durata>0:
            self.display.blit(self.image,(self.rect.x,self.rect.y))
            self.durata-=1
            