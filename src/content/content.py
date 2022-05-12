class Content:
    def __init__(self, name):
        self.name = name

    def load(self):
        print("loading", type(self), self.name)
