import pygame
import src.graphics.core as gcore

mouse = None

class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.left = -1
        self.middle = -1
        self.right = -1
        self.wheel = 0

def update():
    global mouse
    delta = gcore.screen.deltat

    mx, my = pygame.mouse.get_pos()
    mouse.x = mx
    mouse.y = my
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        if mouse.left == -1:
            mouse.left = 0
        else:
            mouse.left += delta
    else:
        mouse.left = -1
    if middle:
        if mouse.middle == -1:
            mouse.middle = 0
        else:
            mouse.middle += delta
    else:
        mouse.middle = -1
    if right:
        if mouse.right == -1:
            mouse.right = 0
        else:
            mouse.right += delta
    else:
        mouse.right = -1

    keys = pygame.key.get_pressed()

def init():
    global mouse
    mouse = Mouse()