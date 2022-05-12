# this is a library i have worked on myself over 2 other projects as a nice wrapper for most of pygames drawing methods
# mostly because i dont like looking at the same lines over and over again to draw a square a few times

import pygame
import pygame.freetype
pygame.freetype.init()

screen = None
debugfont = pygame.freetype.SysFont("Consolas", 16)

class Screen:
    # class responsible for keeping track of the screen
    
    def __init__(self, fps):
        # get display info (width, height)
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        self.size = str(self.width) + "x" + str(self.height)
        self.fps = fps # target fps
        self.framec = 0 # frame counter
        self.time = 0 # total screen time
        self.ltime = 0 # last frames screen time
        self.deltat = 0 # time between frames
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # the fullscreen display
        self.clock = pygame.time.Clock() # pygame time keeping object
        pygame.display.set_caption("pyDUSTRY")
        pygame.display.set_icon(pygame.image.load("assets/icon.png"))
        print("found a monitor of size " + self.size)

    def preFrame(self):
        # runs before each frame
        self.framec += 1 # increment frame counter
        self.time = pygame.time.get_ticks() / 1000 # get the time
        self.deltat = (self.time - self.ltime) # get the time compared to what it was last frame
        self.display.fill((200, 200, 200)) # refill the screen

    def postFrame(self):
        # runs after each frame
        pygame.display.flip() # flip the display buffers
        self.ltime = self.time # note down the time for next frame
        self.clock.tick(self.fps) # tell the clock to halt execution until next frame

class Region:
    # class responsible for holding small slices of images to draw them to the screen

    def __init__(self, surface):
        self.surface = surface # surfaces are images in pygame
    
    def draw(self, position, alpha = 1, size = None, dest = None):
        # routine to draw this image to the screen
        if dest == None:
            # no specified destination means we probably want to draw this to the screen and not some other surface
            dest = screen.display
        if size == None:
            # no specified size means we probably want to draw this at 100% scale
            rect = self.surface.get_rect()
            rect.topleft = position[0], position[1]
            if alpha == 1:
                # ignorable alpha value, blit it immediately
                dest.blit(self.surface, rect)
            else:
                # alpha value is not one, so we make a new surface and set its alpha value and blit that instead
                tempsurface = self.surface.copy()
                tempsurface.set_alpha(alpha * 255)
                dest.blit(tempsurface, rect)
        else:
            # a specified size, we have to apply some transformations to the surface before doing anything else
            size = (abs(size[0]), abs(size[1]))
            rect = self.surface.get_rect()
            rect.topleft = position[0], position[1]
            tempsurface = pygame.transform.flip(self.surface, size[0] < 0, size[1] < 0)
            tempsurface = pygame.transform.scale(tempsurface, size)
            if alpha != 1:
                tempsurface.set_alpha(alpha * 255)
            dest.blit(tempsurface, rect)

    def drawRect(self, rectangle, alpha = 1, dest = None):
        # shorthand for drawing a region onto a rectangle defined by one tuple
        self.draw((rectangle[0], rectangle[1]), size = (rectangle[2], rectangle[3]), alpha = alpha, dest = dest)


#############
# abc # 012 #
# def # 345 #
# ghi # 678 #
#############

class Slice9:
    # a slice9 is a collection of 9 regions
    # they are stitched together to form a continous border that look good without stretching artifacts around the corners

    def __init__(self, a, b, c, d, e, f, g, h, i, border):
        self.slices = (a, b, c, d, e, f, g, h, i)
        self.border = border

    def draw(self, rectangle):
        # each slice has specific sizes that are calculated through some equations i formed
        # they did not work first try, however it was easy with a test gamestate (since removed) that let me visualise the different slices
        b = self.border
        rx = rectangle[0]
        ry = rectangle[1]
        xs = rectangle[2]
        ys = rectangle[3]
        self.slices[0].draw((rx, ry))
        self.slices[1].draw((rx + b, ry), size = (xs - b * 2, b))
        self.slices[2].draw((rx + xs - b, ry))
        self.slices[3].draw((rx, ry + b), size = (b, ys - b * 2))
        self.slices[4].draw((rx + b, ry + b), size = (xs - b * 2, ys - b * 2))
        self.slices[5].draw((rx + xs - b, ry + b), size = (b, ys - b * 2))
        self.slices[6].draw((rx, ry + ys - b))
        self.slices[7].draw((rx + b, ry + ys - b), size = (xs - b * 2, b))
        self.slices[8].draw((rx + xs - b, ry + ys - b))

class Atlas:
    # an atlas is one image that is created to be put into different regions
    # the terminology is technically slightly off but the main idea of cutting up a big image into smaller ones is there

    def __init__(self, filename):
        # fallback for when an image inevitably doesnt exist because i am lazy
        # or if some setup goes wrong and the code and assets are in the wrong place
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except:
            self.sheet = pygame.image.load("assets/sprites/error.png").convert_alpha() # this is an in-joke in the mindustry community
            print("ATLAS WARNING couldnt find", filename)

    def region(self, rectangle):
        # routine for creating a new region
        rect = pygame.Rect(rectangle)
        surface = pygame.Surface(rect.size, pygame.SRCALPHA) # make a new surface
        surface.blit(self.sheet, (0, 0), rect) # render only the relevant part of the image to this new surface
        new = Region(surface.convert_alpha()) # pass this surface on to put it into a new region
        return new

    def slice9(self, rectangle, border):
        # routine for creating a new slice9 which figures out all of the sizes with more equations i figured out myself
        # of course this didnt work first try either
        rx = rectangle[0]
        ry = rectangle[1]
        xs = rectangle[2]
        ys = rectangle[3]
        return Slice9(
            self.region((rx, ry, border, border)),
            self.region((rx + border, ry, xs - border * 2, border)),
            self.region((rx + xs - border, ry, border, border)),
            self.region((rx, ry + border, border, ys - border * 2)),
            self.region((rx + border, ry + border, xs - border * 2, ys - border * 2)),
            self.region((rx + xs - border, ry + border, border, ys - border * 2)),
            self.region((rx, ry + ys - border, border, border)),
            self.region((rx + border, ry + ys - border, xs - border * 2, border)),
            self.region((rx + xs - border, ry + ys - border, border, border)),
            border
        )

def lerp(a, b, alpha):
    # linear interpolation formula
    # doesnt really have to be here but is used a lot
    return a + (b - a) * alpha

def sig(x):
    # truncated sigmoid function
    # this proved helpful in a different project but has not yet been implemented in pyDUSTRY
    if x < -100:
        return 0
    elif x > 100:
        return 1
    else:
        return 1 / (1 + (2.714 ** -x))

def centerScreen(size):
    # takes rectangle coordinates and puts them in the middle of the screen then returns the new coordinates
    return (screen.width / 2 - size[0] / 2, screen.height / 2 - size[1] / 2, size[0], size[1])

def translate(rectangle, translation):
    # takes rectangle coordinates and translates them then returns the new coordinates
    return (rectangle[0] + translation[0], rectangle[1] + translation[1], rectangle[2], rectangle[3])

def centerRect(rectangle):
    # takes rectangle coordinates and centers it around itself rather than the top left then returns the new coordinates
    return (screen.width / 2 - rectangle[2] / 2 + rectangle[0], screen.height / 2 - rectangle[3] / 2 + rectangle[1], rectangle[2], rectangle[3])

def centerPos(position):
    # returns a point that is translated from the centre of the screen rather than the top left
    return (screen.width / 2 + position[0], screen.height / 2 + position[1])

def text(string, position, color):
    # self explanatory
    debugfont.render_to(screen.display, position, string, color)

def fill(color):
    # self explanatory
    screen.display.fill(color)

def rect(color, rectangle, alpha = 1):
    # draw a coloured rectangle
    if alpha == 1:
        rect = pygame.Rect(rectangle)
        surface = pygame.Surface(rect.size)
        surface.fill(color)
        screen.display.blit(surface, rect)
    else:
        rect = pygame.Rect(rectangle)
        surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        surface.fill(color)
        surface.set_alpha(alpha * 255)
        screen.display.blit(surface, rect)

def ellipse(color, rectangle):
    # draw a coloureed ellipse
    pygame.draw.ellipse(screen.display, color, rectangle)

def init():
    # set up some stuff
    global screen
    screen = Screen(60)

