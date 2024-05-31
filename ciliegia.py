import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
import random

def gameover(screen):
    game_over=pygame.image.load("./immaginimenu/immagine_gameover1.png")
    screen.fill((0,0,0))
    screen.blit(game_over, (0,0))
    pygame.display.update()
    ricomincia=False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                ricomincia=True
                # menu(screen)
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()


class Ciliegia():
    def __init__(self, display, labirinto, casella,punti):
        self.display=display
        self.labirinto=labirinto
        self.size=[labirinto.tile_width, labirinto.tile_height]
        self.image=pygame.Surface((self.size[0], self.size[1]))
        self.image=pygame.image.load('./immagini/ciliegia.png')
        self.image=pygame.transform.scale(self.image,self.size)
<<<<<<< HEAD
        self.difficolta=difficolta
        self.durata=0
=======
        self.punti=punti
        self.punti=0
        # self.rect=self.image.get_rect()
        self.durata=1
>>>>>>> 45472f74b7f54ebd101e43c69d4477d461d58e8a
        self.casella=casella
        self.presa=False

    def sceglirettangolo(self,pacman, bool=False):
            if self.durata==0 and self.presa:
                self.presa=False
                n=random.randint(0,len(self.labirinto.tile_liberi)-1)
                self.rect=self.labirinto.tile_liberi[n]
                while self.rect.colliderect(pacman):
                    f=random.randint(0,len(self.labirinto.tile_liberi)-1)
                    self.rect=self.labirinto.tile_liberi[f]
                self.durata=60
            if bool:
                self.presa=False
                n=random.randint(0,len(self.labirinto.tile_liberi)-1)
                self.rect=self.labirinto.tile_liberi[n]
                while self.rect.colliderect(pacman):
                    f=random.randint(0,len(self.labirinto.tile_liberi)-1)
                    self.rect=self.labirinto.tile_liberi[f]
                self.durata=60

         
    def draw(self, pacman, punti):
        if self.durata>0:
            self.display.blit(self.image,(self.rect.x,self.rect.y))
            self.durata-=1
            if self.rect.colliderect(pacman.rect):
                self.presa=True
                self.sceglirettangolo(pacman, True)
<<<<<<< HEAD
        else:
            if not self.presa:
                self.gameover(self.screen)
=======
                self.punti+=50
        elif not self.presa:
            gameover(self.display)
            print('x')
        #         return True
        #     return False
        # # else:
        # #     if not self.presa:
        # #         self.gameover(self.screen)




 # def gameover(self):
    #     self.image=pygame.image.load("./immaginimenu/immagine_gameover1.png")
    #     self.display.blit(self.image, (0,0))
    #     pygame.display.update()
    #     clock=pygame.time.Clock()
    #     ricomincia=False
    #     while not ricomincia:
    #         for event in pygame.event.get():
    #             if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
    #                 ricomincia=True
    #             if event.type==pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit
    #             clock.tick(60)

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
>>>>>>> 45472f74b7f54ebd101e43c69d4477d461d58e8a
