from src.content.content import Content
import src.graphics.core as gcore
import src.graphics.ui as ui
import src.content.registry as registry

def update():
    contentRemaining = 0
    totalContent = 0
    contentRemaining += registry.blocks.loadLoop()
    totalContent += registry.blocks.size
    contentRemaining += registry.entities.loadLoop()
    totalContent += registry.entities.size
    loadedContent = totalContent - contentRemaining

    gcore.fill((0, 0, 0))
    ui.textWhite("pyDUSTRY", gcore.centerPos((0, -200)), 8, ui.CENTER)
    progressRectOuter = gcore.centerRect((0, 188, 808, 24))
    progressRectInner = gcore.centerRect((0, 188, 804, 20))
    progressRect = gcore.centerRect((0, 188, 800, 16))
    gcore.rect((255, 255, 255), progressRectOuter)    
    gcore.rect((0, 0, 0), progressRectInner)
    progress = (1 - contentRemaining / totalContent)
    if progress > 0:
        gcore.rect((255, 255, 255), (progressRect[0], progressRect[1], progressRect[2] * progress, progressRect[3]))
    ui.textWhite("Loading Content (" + str(loadedContent) + "/" + str(totalContent) + " : " + str(round(loadedContent  / totalContent * 100)) + "%)", (gcore.centerPos((-400, 148))))

    if contentRemaining == 0:
        return True
    else:
        return False
