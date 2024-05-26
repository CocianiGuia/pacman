import pygame, sys
from pygame.locals import *
class Ball():
    circle_color=(255,255,255)
    circle_size=(100,100)
    
    def __init__(self, screen, pos, size, color):
        self.screen = screen
        self.image = pygame.Surface(size)
        pygame.draw.circle(self.image, color, [size[0]/2, size[1]/2], size[0]/2)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def draw(self):
        self.screen.blit(self.image, self.rect) #per visualizzare il disegno ad una certa posizione
        




    
    