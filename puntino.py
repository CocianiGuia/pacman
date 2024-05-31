
import pygame
class Puntino:
    def __init__(self, pos) -> None:
        self.preso=False
        self.pos=pos
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'yellow', self.pos, 3)

    def collision(self, pacman):
        if pacman.rect.collidepoint(self.pos):
            self.preso=True
    