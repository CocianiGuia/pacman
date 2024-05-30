import pygame
import sys
from pygame.locals import *
from labirinto import Labirinto
from pacman import PacMan

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = (700, 800)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pac-Man')

clock = pygame.time.Clock()
fps = 15  # Control the game speed

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def menu_iniziale():
    intro = True
    font = pygame.font.SysFont(None, 72)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    intro = False
        
        screen.fill(BLACK)
        draw_text('START', font, WHITE, screen, WIDTH // 2, HEIGHT // 2)
        pygame.draw.rect(screen, WHITE, button_rect, 2)
        pygame.display.flip()
        clock.tick(fps)

def gioca():
    labirinto = Labirinto(screen)
    pacman = PacMan(screen, labirinto)
    run = True
    paused = False

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.direzione = 'UP'
                elif event.key == pygame.K_DOWN:
                    pacman.direzione = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    pacman.direzione = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    pacman.direzione = 'RIGHT'
                elif event.key == pygame.K_p:
                    paused = not paused

        if not paused:
            pacman.move()
            screen.fill(BLACK)
            labirinto.draw()
            pacman.draw(pygame.time.get_ticks())

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    menu_iniziale()
    gioca()

