import pygame, sys

class pacman:
    def __init__(self, display, labirinto, pos, vel_orizz=4, vel_vert=4) ->None:
        self.display=display
        self.labirinto=labirinto
