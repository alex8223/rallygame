import pygame
import random

class GamePanel(object):
    def __init__(self, win, board):
        self.rect = pygame.Rect(700, 0, 900, 1200)
        self.base = pygame.Surface((self.rect.width, self.rect.height))
        self.tiles = pygame.image.load("../assets/tiles.png")
        self.tiles = pygame.transform.smoothscale(self.tiles, (7*75, 13*75))
        for x in range(12):
            for y in range(16):
                self.base.blit(self.tiles, ((75*x, 75*y)), area=(75*random.randint(0,6), 75*random.randint(0,12), 75, 75))
        self.canvas = win.subsurface(self.rect)
        self.floor = pygame.image.load("../assets/floor.png")

    def Draw(self):
        self.canvas.blit(self.base, (0,0))

