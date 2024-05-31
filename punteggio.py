import pygame, sys
from pygame.locals import *
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Punti:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.pos = pos
        self.size = size

        self.punti = 0

        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw(self):
        self.image.fill(WHITE)

        # l'altezza disponibile è 60
        font = pygame.font.Font(None, 65)
        text = font.render('Score:',str(self.punti), 1, BLACK)
        self.image.blit(text, (620, 10)) # surface e pos, quando passo un rect di esso viene comunque presa solo la posizione

        self.screen.blit(self.image, self.rect)
