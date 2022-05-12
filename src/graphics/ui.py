import src.graphics.core as gcore
import src.input as uinput

genericAtlas = gcore.Atlas("assets/sprites/ui/generic.png")
windowSlice = genericAtlas.slice9((0, 0, 96, 96), 32)
buttonSlice = genericAtlas.slice9((0, 96, 96, 96), 32)
buttonSlice1 = genericAtlas.slice9((96, 96, 96, 96), 32)
buttonSlice2 = genericAtlas.slice9((192, 96, 96, 96), 32)
buttonGreenSlice = genericAtlas.slice9((0, 192, 96, 96), 32)
buttonGreenSlice1 = genericAtlas.slice9((96, 192, 96, 96), 32)
buttonGreenSlice2 = genericAtlas.slice9((192, 192, 96, 96), 32)
buttonRedSlice = genericAtlas.slice9((0, 288, 96, 96), 32)
buttonRedSlice1 = genericAtlas.slice9((96, 288, 96, 96), 32)
buttonRedSlice2 = genericAtlas.slice9((192, 288, 96, 96), 32)

fontAtlas = gcore.Atlas("assets/sprites/ui/font.png")
fontMap = {}
fontMapBK = {}

LEFT = 0
CENTER = 0.5
RIGHT = 1

def generateFontMap():
    global fontMap
    i = 0
    for c in "abcdefghijklmnopqrstuvwxyz0123456789":
        fontMap[c] = fontAtlas.region((i * 10, 0, 10, 26))
        fontMapBK[c] = fontAtlas.region((i * 10, 52, 10, 26))
        i += 1
    i = 0
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ()/%:.":
        fontMap[c] = fontAtlas.region((i * 10, 26, 10, 26))
        fontMapBK[c] = fontAtlas.region((i * 10, 78, 10, 26))
        i += 1
    i = 0
generateFontMap()

def window(rectangle):
    windowSlice.draw(rectangle)

def button(rectangle):
    if rectangle[0] <= uinput.mouse.x < rectangle[0] + rectangle[2]:
        if rectangle[1] <= uinput.mouse.y < rectangle[1] + rectangle[3]:
            if uinput.mouse.left == -1:
                buttonSlice1.draw(rectangle)
                return False
            elif uinput.mouse.left == 0:
                buttonSlice2.draw(rectangle)
                return True
            else:
                buttonSlice2.draw(rectangle)
                return False
    buttonSlice.draw(rectangle)
    return False

def buttonGreen(rectangle):
    if rectangle[0] <= uinput.mouse.x < rectangle[0] + rectangle[2]:
        if rectangle[1] <= uinput.mouse.y < rectangle[1] + rectangle[3]:
            if uinput.mouse.left == -1:
                buttonGreenSlice1.draw(rectangle)
                return False
            elif uinput.mouse.left == 0:
                buttonGreenSlice2.draw(rectangle)
                return True
            else:
                buttonGreenSlice2.draw(rectangle)
                return False
    buttonGreenSlice.draw(rectangle)
    return False

def buttonRed(rectangle):
    if rectangle[0] <= uinput.mouse.x < rectangle[0] + rectangle[2]:
        if rectangle[1] <= uinput.mouse.y < rectangle[1] + rectangle[3]:
            if uinput.mouse.left == -1:
                buttonRedSlice1.draw(rectangle)
                return False
            elif uinput.mouse.left == 0:
                buttonRedSlice2.draw(rectangle)
                return True
            else:
                buttonRedSlice2.draw(rectangle)
                return False
    buttonRedSlice.draw(rectangle)
    return False

def textWhite(text, position, scale = 1, justify = LEFT):
    i = 0
    unit = 10 * scale
    height = 26 * scale
    x = position[0] - (len(text) * unit * justify)
    y = position[1]
    for c in text:
        if c in fontMap:
            fontMap[c].draw((x + i * unit, y), size = (unit, height))
        i += 1

def textBlack(text, position, scale = 1, justify = LEFT):
    i = 0
    unit = 10 * scale
    height = 26 * scale
    x = position[0] - (len(text) * unit * justify)
    y = position[1]
    for c in text:
        if c in fontMapBK:
            fontMapBK[c].draw((x + i * unit, y), size = (unit, height))
        i += 1
