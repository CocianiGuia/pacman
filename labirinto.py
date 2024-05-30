import pygame
pygame.init()
from math import ceil

class Labirinto():
    def __init__(self, display, filematrice='./mappa/mappalabirinto.txt', image_path='./immagini/labirinto1.png') -> None:
        self.display = display
        self.width = display.get_width()
        self.height = display.get_height()
        with open(filematrice) as f:
            self.game_map = [list(map(int, riga.strip().split())) for riga in f]
        self.num_rows = len(self.game_map)
        self.num_cols = len(self.game_map[0])
        self.tile_width = ceil(display.get_width() / self.num_cols)
        self.tile_height = ceil(display.get_height() / self.num_rows)
        
        self.casella = pygame.Surface((self.tile_width, self.tile_height))
        
        # Carica l'immagine del labirinto
        labirinto_img = pygame.image.load(image_path)
        self.labirinto_img = pygame.transform.scale(labirinto_img, (display.get_width(), display.get_height()))

    def draw(self):
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == 0:
                    self.casella.fill("BLACK")
                    self.display.blit(self.casella, (x * self.tile_width, y * self.tile_height))
                elif tile == 1:
                    self.casella.fill("BLUE")
                    self.display.blit(self.casella, (x * self.tile_width, y * self.tile_height))
        
        # Disegna l'immagine del labirinto sopra il disegno a blocchi
        self.display.blit(self.labirinto_img, (0, 0))
