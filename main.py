import pygame, sys
from pygame.locals import *
from labirinto import Labirinto


window_size=(700,800)
screenmenu=pygame.display.set_mode(window_size,0,32)
screengioco=pygame.display.set_mode(window_size,0,32)

pygame.display.set_caption('Pac-Man')

clock= pygame.time.Clock()
fps=60

labirinto=Labirinto(screengioco)
labirinto.draw()

pacman=PacMan(screengioco,labirinto,(labirinto.width/2,labirinto.height/2.05))
pacman.draw()
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)