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
        self.durata=0
        self.casella=casella
        self.presa=False

    def sceglirettangolo(self,pacman, bool=False):
            if self.durata==0 or bool:
                self.presa=False
                n=random.randint(0,len(self.labirinto.tile_liberi)-1)
                self.rect=self.labirinto.tile_liberi[n]
                while self.rect.colliderect(pacman):
                    f=random.randint(0,len(self.labirinto.tile_liberi)-1)
                    self.rect=self.labirinto.tile_liberi[f]
                self.durata=60
    game_over=pygame.image.load("./immaginimenu/immagine_gameover1.png")
    def gameover(screen, game_over=pygame.image.load("./immaginimenu/immagine_gameover1.png")):
        screen.blit(game_over, (0,0))
        pygame.display.update()
        clock=pygame.time.Clock()
        ricomincia=False
        while not ricomincia:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    ricomincia=True
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit
    def draw(self, pacman):
        if self.durata>0:
            self.display.blit(self.image,(self.rect.x,self.rect.y))
            self.durata-=1
            if self.rect.colliderect(pacman.rect):
                self.sceglirettangolo(pacman, True)
        else:
            if not self.presa:
                self.gameover(self.screen)