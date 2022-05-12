import src.graphics.camera
import src.graphics.ui as ui

class Tile:
    def __init__(self, chunk, cpos):
        self.chunk = chunk
        self.cpos = cpos
        self.wpos = (cpos[0] + chunk.coords[0] * chunk.world.chunksize, cpos[1] + chunk.coords[1] * chunk.world.chunksize)
        self.dtext = ""
        self.ground = None
        self.resource = None
        chunk.world.generateTile(self)

    def update(self):
        pass

    def draw(self):
        if self.ground:
            self.ground.draw(self)
        if self.dtext != "":
            ui.textWhite(self.dtext, src.graphics.camera.projectRect((self.wpos[0] * 64, self.wpos[1] * 64, 0, 0)), 1)
