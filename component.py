class Container:
    def __init__(self, name, level=0):
        self.name = name
        self.level = level
        self.children = []

    def add(self, child):
        self.children.append(child)

class Leaf(Container):
    def __init__(self, name, level=0):
        super().__init__(name, level)