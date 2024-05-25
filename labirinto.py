import pygame, sys
from pygame.locals import *
from math import ceil

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
        
        
    def draw(self):
        self.colorecorridoi=(0,0,0)
        self.coloremuri=(0,0,255)
        self.colorebordo=(0,0,0)
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile==1:
                    pygame.draw.rect(
                        self.display, 
                        self.colorecorridoi,
                        (x*self.tile_width, y*self.tile_height , self.tile_width, self.tile_height),
                    )
                if tile==0:
                    pygame.draw.rect(
                        self.display, 
                        self.coloremuri,
                        (x*self.tile_width, y*self.tile_height, self.tile_width, self.tile_height),
                    )
                if tile==2:
                    pygame.draw.rect(
                        self.display, 
                        self.colorebordo,
                        (x*self.tile_width, y*self.tile_height, self.tile_width, self.tile_height),
                    )
                
            
