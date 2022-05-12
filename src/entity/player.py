from src.entity.entitytype import EntityType
import src.graphics.core as gcore
import src.graphics.camera as camera

class Player(EntityType):
    def update(self, entity):
        pass
    
    def draw(self, entity):
        rect = camera.projectRect(entity.pos[0] * 64, entity.pos[1] * 64, self.rwidth, self.rheight)
        self.regions[0].drawRect(rect)
    
