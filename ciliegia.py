import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
import random

class Ciliegia():

    def __init__(self, display, labirinto, casella, difficolta):
        self.display=display
        self.labirinto=labirinto
        self.size=[labirinto.tile_width, labirinto.tile_height]
        self.image=pygame.Surface((self.size[0], self.size[1]))
        self.image=pygame.image.load('./immagini/ciliegia.png')
        self.image=pygame.transform.scale(self.image,self.size)
        self.difficolta=difficolta
        # self.rect=self.image.get_rect()
        self.durata=0
        self.casella=casella
        self.presa=False

    def sceglirettangolo(self,pacman):
            if self.durata==0:
                self.presa=False
                n=random.randint(0,len(self.labirinto.tile_liberi)-1)
                self.rect=self.labirinto.tile_liberi[n]
                while self.rect.colliderect(pacman):
                    f=random.randint(0,len(self.labirinto.tile_liberi)-1)
                    self.rect=self.labirinto.tile_liberi[f]
                self.durata=150

    def draw(self):
        if self.durata>0:
            self.display.blit(self.image,(self.rect.x,self.rect.y))
            self.durata-=1
        else:
            if not self.presa:
                pass
                #gameover
        


# class Ciliegia():

#     def __init__(self, display, labirinto, difficolta):
#         self.display=display
#         self.labirinto=labirinto
#         self.size=labirinto.tile_width, labirinto.tile_height
#         self.image=pygame.image.load('./immaginimenù/pacman_lady.png')
#         self.image=pygame.transform.scale(self.image,self.size)
#         self.difficolta=difficolta
#         self.rect=[]
#         self.durata=0

#     def sceglirettangolo(self,pacman):
#         for i in range(0,self.difficolta):
#             if self.durata==0:
#                 n=random.randint(0,len(self.labirinto.tile_liberi)-1)
#                 self.rect[i]=self.labirinto.tile_liberi[n]
#                 while self.rect.colliderect(pacman):
#                     n=random.randint(0,len(self.labirinto.tile_liberi)-1)
#                     self.rect[i]=self.labirinto.tile_liberi[n]
#                 self.durata=70

#     def draw(self):
#         if self.durata>0:
#             self.display.blit(self.image,(self.rect.x,self.rect.y))
#             self.durata-=1
            