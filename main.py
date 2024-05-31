import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
from pacman import PacMan
from punteggio import Punti
from ciliegia import Ciliegia
from puntino import Puntino
from random import randint

BLACK=(0,0,0)
window_width=700
window_height=800
window_size=(window_width,window_height)
pygame.init() #modifica
screen=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=30 #non velocizzare il gioco se no non funziona bene (non prende gli incroci)



labirinto=Labirinto(screen)
ciliegia=Ciliegia(screen,labirinto,labirinto.casella,1)

pacman=PacMan(screen,labirinto)
pacman.draw()
punti_h = 60
punti = Punti(screen, [0,0], [window_width, punti_h])

icona=pygame.image.load("immaginimenu/icona.png")
menu=pygame.image.load("immaginimenu/menu.png")
listapuntini=[Puntino((x*labirinto.tile_width+10, y*labirinto.tile_height+10)) for y in range(labirinto.num_rows) for x in range(labirinto.num_cols)]

# def main_menu():
#     pygame.display.set_caption("Menu")

#     while True:
#         screen.blit(home,(0,0))

#         menu_mouse_pos=pygame.mouse.get_pos()
#         menu_text=font.render("START", True, WHITE)
#         menu_rect=menu_text.get_rect(center=)

# def draw_game():
#     pass

# def draw_menu():
#     bottone=pygame.draw.rect(screen,WHITE, [230,450, 260, 40],0,5)
#     pygame.draw.rect(screen, WHITE, [230,450,260,40], 5,5)
#     text=pygame.font.Font('START', 1, WHITE) 
#     screen.blit(text, (245, 457))
   
    

# def gioca(): 
# def menu_iniziale():
#     intro=True:
#     while intro:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type==pygame.MOUSEBUTTONDOWN:
#                 if button_rect.collidepoint(event.pos):
#                     print("PACMAN")
        
#         screen.fill(BLACK)

#         draw_text('START', font, BLACK, screen, 1100//2, )


# def gioca(): 
def menu(screen):
        screen.fill("black")
        icona_bottone=icona.get_rect(center=(350, 300))
        font=pygame.font.Font(None, 70)
        gioca=font.render("START", True, "white", None)
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
menu(screen)

# game_over=pygame.image.load("./immaginimenu/immagine_gameover1.png")
# def gameover(screen):
#     screen.blit(game_over, (0,0))
#     pygame.display.update()
#     clock=pygame.time.Clock()
#     ricomincia=False
#     while not ricomincia:
#         for event in pygame.event.get():
#             if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
#                 ricomincia=True
#                 menu(screen)
#             if event.type==pygame.QUIT:
#                 pygame.quit()
#                 sys.exit
#         clock.tick(fps)

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
    #screen.fill("BLACK")#per pulire lo schermo e non fare la scia 
    labirinto.draw(listapuntini)
    punti.draw()
    ciliegia.sceglirettangolo(pacman.rect)
    pacman.draw(pygame.time.get_ticks())
    ciliegia.draw(pacman)
    if pacman.rect.colliderect(ciliegia.rect):
        ciliegia.sceglirettangolo(pacman)
    else:
        ciliegia.gameover(screen)
    for i in range(len(listapuntini)):
        listapuntini[i].collision(pacman)
  
    pygame.display.update()
    clock.tick(fps)


    # gioca()

    # while True:
        #mettere la stampa della pagina del mio menu di avvio e le funzioni(es bottoni esci e gioca)
        #quando premi il bottone gioca richiama la funzione gioca

    # def schermogameover(screengameover):
    #     while True:
    #         screengameover.fill()