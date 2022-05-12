import src.content.blocks
import src.content.entitytypes
import random

class Registry:
    def __init__(self, base):
        self.content = {}
        self.size = 0
        self.loadqueue = []
        base.registerContent(self)

    def __getattr__(self, name):
        return self.content[name]

    def register(self, *allContent):
        for content in allContent:
            self.content[content.name] = content
            self.loadqueue.append(content)
            self.size += 1

    def loadLoop(self):
        if len(self.loadqueue) == 0:
            return 0
        else:
            # artificial loading time to test the loading screen
            if random.randint(1, 10) == 1:
                content = self.loadqueue.pop()
                content.load()
            return len(self.loadqueue)

print("REGISTERING BLOCKS")
blocks = Registry(src.content.blocks)
print("REGISTERING ENTITIES")
entities = Registry(src.content.entitytypes)

