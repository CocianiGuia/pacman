import pygame, sys
from pygame.locals import *
from collisioni import *
from math import floor

BLACK=(0,0,0)

class PacMan:
    def __init__(self, display, labirinto) ->None:
        self.display=display
        self.labirinto=labirinto
        self.size=labirinto.tile_width, labirinto.tile_height
        self.velocita_x=labirinto.tile_width/1
        self.velocita_y=labirinto.tile_height/1
        self.pos=[0,0]
        self.pos[0]=17*labirinto.tile_width
        self.pos[1]=17*labirinto.tile_height
        self.image=[]
        self.image.append(pygame.image.load('./immaginipacman/pacman1.png'))
        self.image[0]=pygame.transform.scale(self.image[0],self.size)
        self.image.append(pygame.image.load('./immaginipacman/pacman2.png'))
        self.image[1]=pygame.transform.scale(self.image[1],self.size)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.labirinto.tile_width, self.labirinto.tile_height)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.vett_velocita=[0,0]
        self.direzione="UP"  #in cui è rivolto pacman (in base a questo so di quanto girarlo quando si muove)
        self.counter=0 #contatore che dice quanto spesso deve aprire e chiudere la bocca


    def move_right(self):
        self.moving_right=True
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    
    def move_left(self):
        self.moving_left=True
        self.moving_right=False
        self.moving_up=False
        self.moving_down=False

    def move_up(self):
        self.moving_up=True
        self.moving_down=False
        self.moving_left=False
        self.moving_right=False

    def move_down(self):
        self.moving_down=True
        self.moving_left=False
        self.moving_right=False
        self.moving_up=False

    def move(self):
        collision_types= {'top': False, 'bottom':False,'right':False, 'left':False}

        if self.moving_right:
            self.vett_velocita[0] = self.velocita_x
            self.vett_velocita[1]=0  #escludo movimento verticale
            self.direzione="RIGHT"
        elif self.moving_left:
            self.vett_velocita[0]=-self.velocita_x
            self.vett_velocita[1]=0
            self.direzione="LEFT"
        elif self.moving_up:
            self.vett_velocita[1]=-self.velocita_y
            self.vett_velocita[0]=0    #escludo movimento orizzontale
            self.direzione="UP"
        elif self.moving_down:
            self.vett_velocita[1]=self.velocita_y
            self.vett_velocita[0]=0
            self.direzione="DOWN"
        
        self.rect.x +=self.vett_velocita[0]
        self.rect.y +=self.vett_velocita[1]
    
        listacollisioni = collision_test(self.rect, self.labirinto.tile_rects)

        for tile in listacollisioni:
            if self.vett_velocita[0]>0:
                self.rect.right=tile.left
                collision_types['right']=True
            if self.vett_velocita[0]<0:
                self.rect.left=tile.right
                collision_types['left']=True
            if self.vett_velocita[1]>0:
                self.rect.bottom=tile.top
                collision_types['bottom']=True
            if self.vett_velocita[1]<0:
                self.rect.top=tile.bottom
                collision_types['top']=True
                self.vett_velocita[1]=0
        
        if self.rect.x<=3*self.labirinto.tile_width:
            self.rect.right=30*self.labirinto.tile_width
        
        if self.rect.x>=30*self.labirinto.tile_width:
            self.rect.left=3*self.labirinto.tile_width

    def draw(self,tempo=0):
        self.counter=tempo%100
        if self.direzione=="RIGHT": 
            self.display.blit(self.image[floor(self.counter//50)],(self.rect.x,self.rect.y))
        elif self.direzione=="LEFT": 
            self.display.blit(pygame.transform.flip(self.image[floor(self.counter//50)],True,False),(self.rect.x,self.rect.y))
        elif self.direzione=="UP": 
            self.display.blit(pygame.transform.rotate(self.image[floor(self.counter//50)],90),(self.rect.x,self.rect.y))
        elif self.direzione=="DOWN": 
            self.display.blit(pygame.transform.rotate(self.image[floor(self.counter//50)],270),(self.rect.x,self.rect.y))