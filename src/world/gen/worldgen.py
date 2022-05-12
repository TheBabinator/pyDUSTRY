import src.content.registry as registry
import src.world.gen.noise as noise

generator = None

def setSeed(seed):
    global generator
    generator = noise.SimplexNoiseOctave3D(seed)
    
def generateTile(world, tile):
    vegitation = generator.noise(tile.wpos[0] * 0.003124, tile.wpos[1] * 0.003124, 53.33873201, 1000)
    if vegitation > 15:
        tile.ground = registry.blocks.grass
    else:
        tile.ground = registry.blocks.dirt
    tile.dtext = str(round(vegitation))
