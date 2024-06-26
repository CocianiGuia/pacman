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

    def update(self, punti_ciliegia, listapuntini):
        l=[el for el in listapuntini if el.preso]
        self.punti=len(l)*5+punti_ciliegia

    def draw(self):
        self.image.fill(WHITE)

        font = pygame.font.Font(None, 65)
        text = font.render(f'SCORE:{str(self.punti)}', 1, BLACK)
        self.image.blit(text, (350, 10))

        self.screen.blit(self.image, self.rect)
