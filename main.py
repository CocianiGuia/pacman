import pygame, sys
from pygame.locals import *
pygame.init() 
from labirinto import Labirinto
from pacman import PacMan
# from ciliegia import Ciliegia

WHITE=(255,255,255)
BLACK=(0,0,0)
window_size=(700,800)
screen=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=15 #non velocizzare il gioco se no non funziona bene (non prende gli incroci)
home=pygame.image.load('immaginimenù/schermata.png')
home_schermata=screen.blit(home,(0,0))

labirinto=Labirinto(screen)
labirinto.draw()
# ciliegia=Ciliegia(screen,labirinto,1)

pacman=PacMan(screen,labirinto)
pacman.draw()


def schermatainiziale():
    bottone=pygame.draw.rect(home_schermata, BLACK, [350, 400,260,40], 0, 5)
    pygame.draw.rect(home_schermata, WHITE, [350,400,260,40], 5,5)
    text=pygame.font.render('START', 1, WHITE) 
    home_schermata.blit(text, (245, 457))






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
        #screen.fill("BLACK")#per pulire lo schermo e non fare la scia 
        labirinto.draw()
        # ciliegia.sceglirettangolo(pacman.rect)
        pacman.draw(pygame.time.get_ticks())
        # ciliegia.draw()

        pygame.display.flip()
        clock.tick(fps)

schermatainiziale()
                
# gioca()

# while True:
    #mettere la stampa della pagina del mio menu di avvio e le funzioni(es bottoni esci e gioca)
    #quando premi il bottone gioca richiama la funzione gioca

# def schermogameover(screengameover):
#     while True:
#         screengameover.fill()