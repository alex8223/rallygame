import pygame
import random

pygame.init()

win = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("Rally")
clock = pygame.time.Clock()

class GameBoard(object):
    def __init__(self, board):
        self.rect = pygame.Rect(700, 0, 900, 1200)
        self.base = pygame.Surface((self.rect.width, self.rect.height))
        self.tiles = pygame.image.load("../assets/tiles.png")
        self.tiles = pygame.transform.smoothscale(self.tiles, (7*75, 13*75))
        for x in range(12):
            for y in range(16):
                self.base.blit(self.tiles, ((75*x, 75*y), (75*x+75, 75*y+75)), area=(75*random.randint(0,6), 75*random.randint(0,12), 75, 75))
        self.canvas = win.subsurface(self.rect)
        self.floor = pygame.image.load("../assets/floor.png")

    def Draw(self):
        self.canvas.blit(self.base, (0,0))


class Game(object):
    def __init__(self):
        self.stop = False
        self.boards = []

    def Loop(self):
        while not self.stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True
            win.fill((0, 0, 0))
            for board in self.boards:
                board.Draw()

            pygame.display.update()
            clock.tick(60)


#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_LEFT]:
#        x -= vel

game = Game()
game.boards.append(GameBoard(None))
game.Loop()

pygame.quit()
