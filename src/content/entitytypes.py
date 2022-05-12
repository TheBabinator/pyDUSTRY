from src.entity.player import Player

def registerContent(registry):
    player = Player("player")
    player.rwidth = 48
    player.rheight = 80
    player.rotations = 8
    player.animations = 1

    registry.register(
        player,
    )
    
