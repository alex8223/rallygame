import pygame

pygame.init()

win = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("Rally")

class GameBoard(object):
    def __init__(self):
        self.rect = (700, 0, 900, 1200)
        self.floor = pygame.image.load('../assets/floor.png')

    def Draw(self):
        pygame.draw.rect(win, (20,20,20), self.rect)
        for x in range (self.rect[0], self.rect[0] + self.rect[2], 75):
            for y in range(self.rect[1], self.rect[1] + self.rect[3], 75):
                win.blit(self.floor, (x+1, y+1))


class Game(object):
    def __init__(self):
        self.stop = False
        self.boards = []

    def Loop(self):
        while not self.stop:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True
            win.fill((0, 0, 0))
            for board in self.boards:
                board.Draw()

            pygame.display.update()


#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_LEFT]:
#        x -= vel

game = Game()
game.boards.append(GameBoard())
game.Loop()

pygame.quit()