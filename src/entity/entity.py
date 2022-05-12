class Entity:
    def __init__(self, etype, world):
        self.world = world
        self.pos = (0, 0)
        self.health = etype.health
        self.type = etype

    def update(self):
        self.type.update(self)

    def draw(self):
        self.type.draw(self)
