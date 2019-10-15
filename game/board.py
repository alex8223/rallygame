class Tile(object):
    def __init__(self, speed=None, direction=None):
        self.image = (0, 4)
        if speed is None:
            self.speed = 0
        else:
            self.speed = speed
        if direction is None:
            self.direction = 0
        else:
            self.direction = direction
        self.rotation = (0, 0, 0, 0)


def Floor():
    return Tile()


def Belt(direction: int, rotation: int) -> Tile:
    tile = Tile(speed=1, direction=direction)
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
            tile.image = (5, 2)
            tile.rotation = (0, 0, 0, 1)
        elif direction == 1:
            tile.image = (4, 2)
            tile.rotation = (1, 0, 0, 0)
        elif direction == 2:
            tile.image = (4, 3)
            tile.rotation = (0, 1, 0, 0)
        elif direction == 3:
            tile.image = (5, 3)
            tile.rotation = (0, 0, 1, 0)
    if rotation == -1:
        if direction == 0:
            tile.image = (5, 1)
            tile.rotation = (0, -1, 0, 0)
        elif direction == 1:
            tile.image = (5, 0)
            tile.rotation = (0, 0, -1, 0)
        elif direction == 2:
            tile.image = (4, 0)
            tile.rotation = (0, 0, 0, -1)
        elif direction == 3:
            tile.image = (4, 1)
            tile.rotation = (-1, 0, 0, 0)
    return tile


def FastBelt(direction: int, rotation: int) -> Tile:
    tile = Tile(speed=2, direction=direction)
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
            tile.image = (3, 2)
            tile.rotation = (0, 0, 0, 1)
        elif direction == 1:
            tile.image = (2, 2)
            tile.rotation = (1, 0, 0, 0)
        elif direction == 2:
            tile.image = (2, 3)
            tile.rotation = (0, 1, 0, 0)
        elif direction == 3:
            tile.image = (3, 3)
            tile.rotation = (0, 0, 1, 0)
    if rotation == -1:
        if direction == 0:
            tile.image = (3, 1)
            tile.rotation = (0, -1, 0, 0)
        elif direction == 1:
            tile.image = (3, 0)
            tile.rotation = (0, 0, -1, 0)
        elif direction == 2:
            tile.image = (2, 0)
            tile.rotation = (0, 0, 0, -1)
        elif direction == 3:
            tile.image = (2, 1)
            tile.rotation = (-1, 0, 0, 0)
    return tile


def MergeBelt(direction: int, cuff: int) -> Tile:
    tile = Tile(speed=1, direction=direction)
    if direction == 0 and cuff == 1:
        tile.image = (8, 0)
        tile.rotation = (0, 0, 0, 1)
    if direction == 0 and cuff == 0:
        tile.image = (8, 4)
        tile.rotation = (0, -1, 0, 1)
    if direction == 0 and cuff == -1:
        tile.image = (7, 0)
        tile.rotation = (-1, 0, 0, 0)
    if direction == 1 and cuff == 1:
        tile.image = (8, 1)
        tile.rotation = (1, 0, 0, 0)
    if direction == 1 and cuff == 0:
        tile.image = (7, 4)
        tile.rotation = (1, 0, -1, 0)
    if direction == 1 and cuff == -1:
        tile.image = (7, 1)
        tile.rotation = (0, 0, -1, 0)
    if direction == 2 and cuff == 1:
        tile.image = (8, 2)
        tile.rotation = (0, 1, 0, 0)
    if direction == 2 and cuff == 0:
        tile.image = (7, 5)
        tile.rotation = (0, 1, 0, -1)
    if direction == 2 and cuff == -1:
        tile.image = (7, 2)
        tile.rotation = (0, 0, 0, -1)
    if direction == 3 and cuff == 1:
        tile.image = (8, 3)
        tile.rotation = (0, 0, 1, 0)
    if direction == 3 and cuff == 0:
        tile.image = (8, 5)
        tile.rotation = (-1, 0, 1, 0)
    if direction == 3 and cuff == -1:
        tile.image = (7, 3)
        tile.rotation = (-1, 0, 0, 0)
    return tile


def MergeFastBelt(direction: int, cuff: int) -> Tile:
    tile = Tile(speed=2, direction=direction)
    if direction == 0 and cuff == 1:
        tile.image = (9, 4)
        tile.rotation = (0, 0, 0, 1)
    if direction == 0 and cuff == 0:
        tile.image = (10, 3)
        tile.rotation = (0, -1, 0, 1)
    if direction == 0 and cuff == -1:
        tile.image = (9, 0)
        tile.rotation = (-1, 0, 0, 0)
    if direction == 1 and cuff == 1:
        tile.image = (9, 5)
        tile.rotation = (1, 0, 0, 0)
    if direction == 1 and cuff == 0:
        tile.image = (10, 0)
        tile.rotation = (1, 0, -1, 0)
    if direction == 1 and cuff == -1:
        tile.image = (9, 1)
        tile.rotation = (0, 0, -1, 0)
    if direction == 2 and cuff == 1:
        tile.image = (10, 5)
        tile.rotation = (0, 1, 0, 0)
    if direction == 2 and cuff == 0:
        tile.image = (10, 1)
        tile.rotation = (0, 1, 0, -1)
    if direction == 2 and cuff == -1:
        tile.image = (9, 2)
        tile.rotation = (0, 0, 0, -1)
    if direction == 3 and cuff == 1:
        tile.image = (10, 4)
        tile.rotation = (0, 0, 1, 0)
    if direction == 3 and cuff == 0:
        tile.image = (10, 2)
        tile.rotation = (-1, 0, 1, 0)
    if direction == 3 and cuff == -1:
        tile.image = (9, 3)
        tile.rotation = (-1, 0, 0, 0)
    return tile


def Pit() -> Tile:
    tile = Tile()
    tile.image = (0, 5)
    return tile


def Cog(rotation: int) -> Tile:
    tile = Tile()
    tile.rotation = (rotation, rotation, rotation, rotation)
    if rotation == 1:
        tile.image = (6, 5)
    if rotation == -1:
        tile.image = (6, 4)
    return tile


class Board(object):
    def __init__(self):
        self.tiles = [[Floor() for i in range(12)] for j in range(16)]
        self.vwalls = [[False for i in range(13)] for j in range(16)]
        self.hwalls = [[False for i in range(12)] for j in range(17)]

    def Preset0(self):
        self.tiles[5][0] = Belt(3, 0)
        self.tiles[5][1] = Belt(3, 0)
        self.tiles[6][0] = Belt(1, 0)
        self.tiles[6][1] = Belt(2, 1)
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
        self.tiles[2][5] = FastBelt(3, 1)
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
        self.tiles[1][9] = Belt(2, -1)
        self.tiles[2][9] = Belt(2, 0)
        self.tiles[5][11] = Belt(3, 0)
        self.tiles[5][10] = Belt(3, 0)
        self.tiles[5][9] = Belt(3, 0)
        self.tiles[5][7] = Belt(3, 0)
        self.tiles[5][6] = Belt(2, -1)
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

        for i in [2, 4, 7, 9]:
            self.hwalls[0][i] = True
            self.hwalls[12][i] = True
            self.vwalls[i][0] = True
            self.vwalls[i][12] = True
        self.vwalls[1][3] = True
        self.vwalls[1][6] = True
        self.hwalls[2][2] = True
        self.vwalls[3][5] = True
        self.hwalls[4][5] = True
        self.hwalls[4][8] = True
        self.vwalls[5][6] = True
        self.hwalls[7][8] = True
        self.hwalls[7][10] = True
        self.hwalls[8][2] = True
        self.vwalls[8][3] = True
        self.vwalls[8][7] = True
        self.vwalls[10][1] = True
        self.vwalls[10][2] = True
        self.vwalls[10][7] = True
        self.vwalls[10][10] = True
