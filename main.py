import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
from pacman import PacMan
# from puntini import Puntino

BLACK=(0,0,0)
window_size=(700,800)

screen=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=5 #non velocizzare il gioco se no non funziona bene (non prende gli incroci)

labirinto=Labirinto(screen)
labirinto.draw()

# puntino=Puntino(screen,labirinto,1)

pacman=PacMan(screen,labirinto)
pacman.draw()


def gioca(): 
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]: 
            pacman.move_right()
        if keys[K_LEFT]:
            pacman.move_left()
        if keys[K_UP]:
            pacman.move_up()
        if keys[K_DOWN]:
            pacman.move_down()
        pacman.move()
        clock.tick(fps)   
        # screen.fill("BLACK")# per pulire lo schermo e non fare la scia 
        labirinto.draw()
        # puntino.sceglirettangolo(pacman.rect)
        pacman.draw(pygame.time.get_ticks())
        # puntino.draw()

        pygame.display.flip()
        clock.tick(fps)

gioca()

# while True:
    #mettere la stampa della pagina del mio menu di avvio e le funzioni(es bottoni esci e gioca)
    #quando premi il bottone gioca richiama la funzione gioca

# def schermogameover(screengameover):
#     while True:
#         screengameover.fill()