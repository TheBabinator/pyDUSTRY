# launcher for pydustry
print("PYDUSTRY DEBUG WINDOW")

# ensure pygame is installed
try:
    import pygame
except:
    print("PYGAME NOT FOUND")
    exit()


# this bit imports the main game
print("LOADING MODULES")
import src.game

print("LAUNCHING")
src.game.launch() # tell the game to launch
