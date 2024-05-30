import pygame
pygame.init()

class PacMan():
    def __init__(self, screen, labirinto):
        self.screen = screen
        self.labirinto = labirinto
        self.x, self.y = 50, 50  # Posizione iniziale di PacMan
        self.direzione = None  # Direzione iniziale
        self.speed = 5  # Velocità di movimento

    def move(self):
        if self.direzione == 'UP':
            self.y -= self.speed
        elif self.direzione == 'DOWN':
            self.y += self.speed
        elif self.direzione == 'LEFT':
            self.x -= self.speed
        elif self.direzione == 'RIGHT':
            self.x += self.speed

    def draw(self, ticks):
        pygame.draw.circle(self.screen, (255, 255, 0), (self.x, self.y), 15)