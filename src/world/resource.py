from src.world.block import Block

class Resource(Block):
    def __init__(self, name):
        super().__init__(name)
        self.atlasLocation += "resource/"
