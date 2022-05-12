import sys
import pygame
pygame.init() # start up pygame
pygame.mixer.init(frequency = 44100, channels = 16) # audio setup
pygame.display.set_mode((0, 0), pygame.NOFRAME) # start a dummy display to force some other pygame things to load
import src.graphics.core as gcore
import src.input as uinput
import src.gamestate as gamestate

def close(): # quit everything
    pygame.quit()
    sys.exit()

def launch(): # launch process
    gcore.init() # setup the graphics core scripts
    uinput.init() # setup the user input scripts

    while gamestate.current != gamestate.CLOSING: # main loop
        gcore.screen.preFrame()

        # processing inputs
        uinput.update()
        uinput.mouse.wheel = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()            
            elif event.type == pygame.MOUSEWHEEL:
                uinput.mouse.wheel = event.y

        # processing the game state
        gamestate.update()
        
        gcore.screen.postFrame()

    close() # end
