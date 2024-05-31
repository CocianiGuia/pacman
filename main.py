import pygame, sys
from pygame.locals import *
from punteggio import Punti
from labirinto import Labirinto
from pacman import PacMan
from punteggio import Punti
# from ciliegia import Ciliegia

WHITE=(255,255,255)
BLACK=(0,0,0)
window_width=600
window_height=700
window_size=(window_width,window_height)
pygame.init() #modifica
screen=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=15 #non velocizzare il gioco se no non funziona bene (non prende gli incroci)

labirinto=Labirinto(screen)
labirinto.draw()
# ciliegia=Ciliegia(screen,labirinto,1)



pacman=PacMan(screen,labirinto)
pacman.draw()
punti_h = 60
punti = Punti(screen, [0,0], [window_width, punti_h])


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
#     screen.blit(home(0,0))
#     screen.blit(icona,155,240)
    

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
        punti.draw()
        # ciliegia.sceglirettangolo(pacman.rect)
        pacman.draw(pygame.time.get_ticks())
        # ciliegia.draw()
        pygame.display.flip()

    pygame.quit()

gioca()
# sincr
# while True:
    #mettere la stampa della pagina del mio menu di avvio e le funzioni(es bottoni esci e gioca)
    #quando premi il bottone gioca richiama la funzione gioca
# if __name__ == "__main__":
#     menu_iniziale()
#     gioca()


# def schermogameover(screengameover):
#     while True:
#         screengameover.fill()