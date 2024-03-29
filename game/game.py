import pygame
from game_panel import GamePanel
from board import Board

pygame.init()

win = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("Rally")
clock = pygame.time.Clock()


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
game.board = Board()
game.board.Preset0()
game.game_panel = GamePanel(win, game.board)
game.boards.append(game.game_panel)
game.Loop()

pygame.quit()
