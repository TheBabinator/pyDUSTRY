from src.world.chunk import Chunk
import src.world.gen.worldgen as worldgen

class Map:
    def __init__(self, seed):
        self.entities = []
        self.chunks = {}
        self.chunksize = 10
        self.seed = seed
        worldgen.setSeed(seed)

    def generateChunk(self, coords):
        self.chunks[coords] = Chunk(self, coords)

    def generateTile(self, tile):
        worldgen.generateTile(self, tile)

    def update(self):
        for coords in self.chunks:
            self.chunks[coords].update()
        for entity in self.entities:
            entity.update()
        for coords in self.chunks:
            self.chunks[coords].draw()
        for entity in self.entities:
            entity.draw()
        
