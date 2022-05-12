from src.content.content import Content
from src.entity.entity import Entity
import src.gamestate as gamestate
import src.graphics.core as gcore
import src.graphics.camera as camera

class EntityType(Content):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.rotations = 0
        self.animations = 0
        self.rwidth = 0
        self.rheight = 0
        self.atlasLocation = "assets/sprites/entity/"
        self.atlas = None
        self.regions = None
    
    def load(self):
        super().load()
        self.atlas = gcore.Atlas(self.atlasLocation + self.name + ".png")
        self.regions = []
        for i in range(self.rotations):
            for a in range(self.animations):
                self.regions.append(self.atlas.region((i * self.rwidth, a * self.rheight, self.rwidth, self.rheight)))

    def spawn(self, position):
        entity = Entity(self, gamestate.world)
        entity.position = position
        return entity
    
    def update(self, entity):
        pass
    
    def draw(self, entity):
        pass
