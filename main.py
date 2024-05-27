import pygame, sys
from pygame.locals import *
from labirinto import Labirinto
from pacman import PacMan

BLACK=(0,0,0)
window_size=(700,800)

screen=pygame.display.set_mode(window_size,0,32)
# tasti_zona = pygame.set_mode(window_size,0,32)
# personaggio_zona=pygame.display.set_mode(window_size,0,32)
# gioco_zona=pygame.display.set_mode(window_size,0,32)
# gameover_zona=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=60

labirinto=Labirinto(screen)
labirinto.draw()

pacman=PacMan(screen,labirinto,(labirinto.width/2,labirinto.height/2.05))
pacman.draw()

# def schermotasti(screentasti):
#     while True:
#         screentasti.fill(BLACK)

        
# def schermopersonaggio(screenpersonaggio):
#     while True:
#         screenpersonaggio.fill()


# def schermatagioco(screengioco,labirinto,pacman):   
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
    pacman.move()# per aggiornare la posizione del pacman   
    screen.fill("BLACK")# per pulire lo schermo e non fare la scia 
    pacman.draw(pygame.time.get_ticks())
    labirinto.draw()
    pacman.draw()
        
    pygame.display.flip()
    clock.tick(fps)

# def schermogameover(screengameover):
#     while True:
#         screengameover.fill()