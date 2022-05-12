from src.content.content import Content
import src.graphics.core as gcore
import src.graphics.camera as camera

class Block(Content):
    def __init__(self, name):
        super().__init__(name)
        self.entity = False
        self.variants = 1
        self.atlasLocation = "assets/sprites/blocks/"
        self.atlas = None
        self.regions = []
        
    def load(self):
        super().load()
        self.atlas = gcore.Atlas(self.atlasLocation + self.name + ".png")
        for i in range(self.variants):
            self.regions.append(self.atlas.region((i * 64, 0, 64, 64)))

    def draw(self, tile):
        i = int((tile.wpos[0] * 3.184418488345422462 + tile.wpos[1] * 2.487356873456786498) % self.variants)
        rect = camera.projectRect((tile.wpos[0] * 64, tile.wpos[1] * 64, 64, 64))
        self.regions[i].drawRect(rect)
        