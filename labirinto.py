import pygame, sys
from pygame.locals import *
from math import ceil

BLACK=(0,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

class Labirinto():
    def __init__(self, display, filematrice= './mappa/mappalabirinto.txt') -> None:
        self.display=display
        self.width=display.get_width()
        self.height=display.get_height()
        with open (filematrice) as f:
            self.game_map=[list(map(int, riga.strip().split())) for riga in f]
        self.num_rows = len(self.game_map)
        self.num_cols = len(self.game_map[0])
        self.tile_width = ceil(display.get_width() / self.num_cols)
        self.tile_height = ceil(display.get_height() / self.num_rows)
        
        self.casella=pygame.Surface((self.tile_width,self.tile_height)) #definisco la casella in cui disegno il labirinto(rettangolo)
                                                                        #prima lo disegnavamo volta per volta
        self.tile_rects = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):       #definisco dove pacman non può passare
                if tile != 1:
                    self.tile_rects.append(pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height))

    def draw(self):
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile==1:
                    self.casella.fill(BLACK)
                    self.display.blit(self.casella, (x*self.tile_width, y*self.tile_height))
                    
                if tile==0:
                    self.casella.fill(BLUE)
                    self.display.blit(self.casella, (x*self.tile_width, y*self.tile_height))
                if tile==2:
                    self.casella.fill(WHITE)
                    self.display.blit(self.casella, (x*self.tile_width, y*self.tile_height))