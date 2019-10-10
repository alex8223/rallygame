class Tile(object):
    def __init__(self):
        self.image = (0, 4)

def Floor():
    return Tile()

def Belt(direction, rotation, speed=1):
    tile = Tile()
    if rotation == 0:
        if direction == 0:
            tile.image = (6,0)
        elif direction == 1:
            tile.image = (6,3)
        elif direction == 2:
            tile.image = (6,1)
        elif direction == 3:
            tile.image = (6,2)
    if rotation == 1:
        if direction == 0:
            tile.image = (4,2)
        elif direction == 1:
            tile.image = (4,3)
        elif direction == 2:
            tile.image = (5,3)
        elif direction == 3:
            tile.image = (5,2)
    if rotation == -1:
        if direction == 0:
            tile.image = (4,1)
        elif direction == 1:
            tile.image = (5,1)
        elif direction == 2:
            tile.image = (5,0)
        elif direction == 3:
            tile.image = (4,0)
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

