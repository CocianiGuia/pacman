import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
from pacman import PacMan
from punteggio import Punti
from ciliegia import Ciliegia
from puntino import Puntino
from random import randint

WHITE=(255,255,255)
BLACK=(0,0,0)
window_width=700
window_height=800
window_size=(window_width,window_height)
pygame.init() #modifica
screen=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=30 


labirinto=Labirinto(screen)

pacman=PacMan(screen,labirinto)
pacman.draw()
punti_h = 60
punti = Punti(screen, [0,0], [window_width, punti_h])
ciliegia=Ciliegia(screen,labirinto,labirinto.casella,punti)

icona=pygame.image.load("immaginimenu/icona.png")
menu=pygame.image.load("immaginimenu/menu.png")
listapuntini=[Puntino((x*labirinto.tile_width+10, y*labirinto.tile_height+10)) for y in range(labirinto.num_rows) for x in range(labirinto.num_cols)]



def menu(screen):
        screen.fill(BLACK)
        icona_bottone=icona.get_rect(center=(350, 300))
        font=pygame.font.Font(None, 70)
        gioca=font.render("START", True, WHITE, None)
        rectbot=gioca.get_rect(center=(350,550))
        clock=pygame.time.Clock()
        fps=60
        b=True
        while b==True:
            lista=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN and event.button==1:
                    if rectbot.collidepoint(lista):
                        b=False
            screen.blit(icona, icona_bottone)
            screen.blit(gioca,rectbot)
            clock.tick(fps)
            pygame.display.flip()

bool=True

menu(screen)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                menu(screen)
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
    labirinto.draw(listapuntini)
    punti.update(ciliegia.punti,listapuntini)
    punti.draw()
    
    ciliegia.sceglirettangolo(pacman,bool)
    bool=False
    labirinto.draw(listapuntini)
    punti.draw()
    pacman.draw(pygame.time.get_ticks())
    ciliegia.draw(pacman,punti)

    for i in range(len(listapuntini)):
        listapuntini[i].collision(pacman)
    punti.draw()
    
  
    pygame.display.update()
    clock.tick(fps)