import pygame
class Puntino:
    def __init__(self) -> None:
        self.preso=False
    
    def draw(self, screen, pos):
        pygame.draw.circle(screen, 'yellow', pos, 3)

        