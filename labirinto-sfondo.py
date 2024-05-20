import pygame, sys
from pygame.locals import *
from math import ceil

class Labirinto():
    def __init__(self, display, filematrice= './mappa/mappalabirinto.txt') -> None:
        self.display=display
        with open (filematrice) as f:
            self.gamemap=[list(map(int, riga.strip().split())) for riga in f]
        
    def draw(self):
        for y in enumerate(self.gamemap):
