class Tile(object):
    def __init__(self):
        self.image = (0, 4)


def Floor():
    return Tile()


def Belt(direction: int, rotation: int) -> Tile:
    tile = Tile()
    if rotation == 0:
        if direction == 0:
            tile.image = (6, 0)
        elif direction == 1:
            tile.image = (6, 3)
        elif direction == 2:
            tile.image = (6, 1)
        elif direction == 3:
            tile.image = (6, 2)
    if rotation == 1:
        if direction == 0:
            tile.image = (4, 2)
        elif direction == 1:
            tile.image = (4, 3)
        elif direction == 2:
            tile.image = (5, 3)
        elif direction == 3:
            tile.image = (5, 2)
    if rotation == -1:
        if direction == 0:
            tile.image = (4, 1)
        elif direction == 1:
            tile.image = (5, 1)
        elif direction == 2:
            tile.image = (5, 0)
        elif direction == 3:
            tile.image = (4, 0)
    return tile

def FastBelt(direction: int, rotation: int) -> Tile:
    tile = Tile()
    if rotation == 0:
        if direction == 0:
            tile.image = (1, 4)
        elif direction == 1:
            tile.image = (1, 5)
        elif direction == 2:
            tile.image = (2, 4)
        elif direction == 3:
            tile.image = (2, 5)
    if rotation == 1:
        if direction == 0:
            tile.image = (2, 2)
        elif direction == 1:
            tile.image = (2, 3)
        elif direction == 2:
            tile.image = (3, 3)
        elif direction == 3:
            tile.image = (3, 2)
    if rotation == -1:
        if direction == 0:
            tile.image = (2, 1)
        elif direction == 1:
            tile.image = (3, 1)
        elif direction == 2:
            tile.image = (3, 0)
        elif direction == 3:
            tile.image = (2, 0)
    return tile

def MergeBelt(direction: int, cuff: int) -> Tile:
    tile = Tile()
    if direction == 0 and cuff == 1:
        tile.image = (8, 0)
    if direction == 0 and cuff == 0:
        tile.image = (8, 4)
    if direction == 0 and cuff == -1:
        tile.image = (7, 0)
    if direction == 1 and cuff == 1:
        tile.image = (8, 1)
    if direction == 1 and cuff == 0:
        tile.image = (7, 4)
    if direction == 1 and cuff == -1:
        tile.image = (7, 1)
    if direction == 2 and cuff == 1:
        tile.image = (8, 2)
    if direction == 2 and cuff == 0:
        tile.image = (7, 5)
    if direction == 2 and cuff == -1:
        tile.image = (7, 2)
    if direction == 3 and cuff == 1:
        tile.image = (8, 3)
    if direction == 3 and cuff == 0:
        tile.image = (8, 5)
    if direction == 3 and cuff == -1:
        tile.image = (7, 3)
    return tile

def MergeFastBelt(direction: int, cuff: int) -> Tile:
    tile = Tile()
    if direction == 0 and cuff == 1:
        tile.image = (9, 4)
    if direction == 0 and cuff == 0:
        tile.image = (10, 3)
    if direction == 0 and cuff == -1:
        tile.image = (9, 0)
    if direction == 1 and cuff == 1:
        tile.image = (9, 5)
    if direction == 1 and cuff == 0:
        tile.image = (10, 0)
    if direction == 1 and cuff == -1:
        tile.image = (9, 1)
    if direction == 2 and cuff == 1:
        tile.image = (10, 5)
    if direction == 2 and cuff == 0:
        tile.image = (10, 1)
    if direction == 2 and cuff == -1:
        tile.image = (9, 2)
    if direction == 3 and cuff == 1:
        tile.image = (10, 4)
    if direction == 3 and cuff == 0:
        tile.image = (10, 2)
    if direction == 3 and cuff == -1:
        tile.image = (9, 3)
    return tile

def Pit() -> Tile:
    tile = Tile()
    tile.image = (0, 5)
    return tile

def Cog(rotation: int) -> Tile:
    tile = Tile()
    if rotation == 1:
        tile.image = (6, 5)
    if rotation == -1:
        tile.image = (6, 4)
    return tile

class Board(object):
    def __init__(self):
        self.tiles = [[Floor() for i in range(12)] for j in range(16)]

    def Preset0(self):
        self.tiles[5][0] = Belt(3, 0)
        self.tiles[5][1] = Belt(3, 0)
        self.tiles[6][0] = Belt(1, 0)
        self.tiles[6][1] = Belt(1, 1)
        self.tiles[7][1] = Belt(2, 0)
        self.tiles[8][1] = Belt(2, 0)
        self.tiles[9][1] = Belt(2, 0)
        self.tiles[11][1] = Belt(2, 0)
        self.tiles[11][3] = Belt(0, 0)
        self.tiles[10][3] = Belt(0, 0)
        self.tiles[9][3] = Belt(0, 0)
        self.tiles[7][3] = FastBelt(0, 0)
        self.tiles[6][3] = FastBelt(0, 0)
        self.tiles[5][3] = FastBelt(0, 0)
        self.tiles[4][3] = FastBelt(0, 0)
        self.tiles[3][3] = FastBelt(0, 0)
        self.tiles[2][3] = MergeFastBelt(0, 1)
        self.tiles[1][3] = FastBelt(0, 0)
        self.tiles[0][3] = FastBelt(0, 0)
        self.tiles[0][5] = FastBelt(2, 0)
        self.tiles[1][5] = FastBelt(2, 0)
        self.tiles[2][5] = FastBelt(2, 1)
        self.tiles[2][4] = FastBelt(3, 0)
        self.tiles[4][5] = Belt(1, 0)
        self.tiles[0][6] = Belt(0, 0)
        self.tiles[1][6] = Belt(0, 0)
        self.tiles[2][6] = Belt(0, 0)
        self.tiles[3][6] = Belt(0, 0)
        self.tiles[0][8] = Belt(2, 0)
        self.tiles[1][8] = Belt(2, 0)
        self.tiles[2][8] = Belt(2, 0)
        self.tiles[1][11] = Belt(3, 0)
        self.tiles[1][10] = Belt(3, 0)
        self.tiles[1][9] = Belt(3, -1)
        self.tiles[2][9] = Belt(2, 0)
        self.tiles[5][11] = Belt(3, 0)
        self.tiles[5][10] = Belt(3, 0)
        self.tiles[5][9] = Belt(3, 0)
        self.tiles[5][7] = Belt(3, 0)
        self.tiles[5][6] = Belt(3, -1)
        self.tiles[6][6] = Belt(2, 0)
        self.tiles[7][6] = Belt(2, 0)
        self.tiles[8][11] = Belt(3, 0)
        self.tiles[8][10] = Belt(3, 0)
        self.tiles[8][9] = Belt(3, 0)
        self.tiles[9][8] = Belt(2, 0)
        self.tiles[10][8] = Belt(2, 0)
        self.tiles[11][8] = Belt(2, 0)
        self.tiles[1][1] = Pit()
        self.tiles[3][9] = Pit()
        self.tiles[6][7] = Pit()
        self.tiles[9][5] = Pit()
        self.tiles[9][9] = Pit()
        self.tiles[4][6] = Cog(-1)
        self.tiles[5][2] = Cog(1)
        self.tiles[5][8] = Cog(1)
        self.tiles[6][2] = Cog(-1)
        self.tiles[8][4] = Cog(1)
        self.tiles[8][5] = Cog(-1)
        self.tiles[8][8] = Cog(-1)
