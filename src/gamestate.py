from src.world.map import Map
import src.content.registry as registry
import src.graphics.core as gcore
import src.graphics.ui as ui
import src.loader

CLOSING = -1
LOAD = 0
MENU = 1
GAMETEST = 2

current = LOAD
world = None

def update():
    global current
    global world
    if current == LOAD:
        if src.loader.update():
            current = MENU
    elif current == MENU:
        ui.window(gcore.centerScreen((400, 274)))
        if ui.buttonGreen(gcore.centerRect((0, -81, 384, 60))):
            world = Map(69420)
            for x in range(-2, 2):
                for y in range(-2, 2):
                    world.generateChunk((x, y))
            registry.entities.player.spawn((0, 0))
            current = GAMETEST
        if ui.button(gcore.centerRect((0, -21, 384, 60))):
            print("idk")
        if ui.button(gcore.centerRect((0, 39, 384, 60))):
            print("idk")
        if ui.buttonRed(gcore.centerRect((0, 99, 384, 60))):
            current = CLOSING
        ui.textBlack("pyDUSTRY", gcore.centerPos((0, -300)), 4, ui.CENTER)
        ui.textWhite("Main Menu", gcore.centerPos((-190, -134)))
        ui.textBlack("New Game", gcore.centerPos((0, -103)), 2, ui.CENTER)
        ui.textBlack("Load Game", gcore.centerPos((0, -43)), 2, ui.CENTER)
        ui.textBlack("Online Games", gcore.centerPos((0, 17)), 2, ui.CENTER)
        ui.textBlack("EXIT", gcore.centerPos((0, 77)), 2, ui.CENTER)
    elif current == GAMETEST:
        world.update()
