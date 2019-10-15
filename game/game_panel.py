import pygame

class GamePanel(object):
    def __init__(self, win, board):
        self.rect = pygame.Rect(700, 0, 900, 1200)
        self.base = pygame.Surface((self.rect.width, self.rect.height))
        self.tiles = pygame.image.load("../assets/tiles.png")
        self.tiles = pygame.transform.smoothscale(self.tiles, (7*75, 13*75))
        for x in range(12):
            for y in range(16):
                tile = board.tiles[y][x]
                self.base.blit(self.tiles, ((75*x, 75*y)), area=(75*tile.image[1], 75*tile.image[0], 75, 75))
        for x in range(12):
            for y in range(17):
                if board.hwalls[y][x]:
                    yoffset = 0 if y == 0 else -11 if y == 16 else -5
                    self.base.blit(self.tiles, ((75*x, 75*y+yoffset)), area=(300, 289, 75, 11))
        for x in range(13):
            for y in range(16):
                if board.vwalls[y][x]:
                    xoffset = 0 if x == 0 else -11 if x == 12 else -5
                    self.base.blit(self.tiles, ((75*x + xoffset, 75*y)), area=(375, 225, 11, 75))

        self.canvas = win.subsurface(self.rect)
        self.floor = pygame.image.load("../assets/floor.png")

    def Draw(self):
        self.canvas.blit(self.base, (0,0))
