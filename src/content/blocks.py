from src.world.block import Block
from src.world.ground import Ground
from src.world.resource import Resource

def registerContent(registry):
    dirt = Ground("dirt")
    dirt.variants = 8

    grass = Ground("grass")
    grass.variants = 8

    ironore = Resource("ironore")

    copperore = Resource("copperore")


    registry.register(
        dirt, grass,
        ironore, copperore,
    )
    