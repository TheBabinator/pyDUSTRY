from src.world.tile import Tile

class Chunk:
    def __init__(self, world, coords):
        self.world = world
        self.coords = coords
        self.tiles = {}
        for x in range(world.chunksize):
            for y in range(world.chunksize):
                pos = (x, y)
                self.tiles[pos] = Tile(self, pos)

    def update(self):
        pass

    def draw(self):
        for coords in self.tiles:
            self.tiles[coords].draw()
