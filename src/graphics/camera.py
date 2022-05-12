import src.graphics.core as gcore

cameraPosition = (0, 0)
zoom = 1

def projectRect(rectangle):
    return (
        gcore.screen.width / 2 + rectangle[0] * zoom - rectangle[2] * zoom / 2,
        gcore.screen.height / 2 + rectangle[1] * zoom - rectangle[3] * zoom / 2,
        rectangle[2] * zoom, rectangle[3] * zoom
        )
