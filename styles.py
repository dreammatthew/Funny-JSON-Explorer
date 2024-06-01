from abc import ABC, abstractmethod

class Style(ABC):
    def get_style(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class TreeStyle(Style):
    def get_style(self):
        return "tree"

class RectangleStyle(Style):
    def get_style(self):
        return "rectangle"
# 抽象工厂
class StyleFactory(ABC):
    @abstractmethod
    def create_style(self) -> Style:
        pass

# 具体工厂：树形风格工厂
class TreeStyleFactory(StyleFactory):
    def create_style(self) -> Style:
        return TreeStyle()

# 具体工厂：矩形风格工厂
class RectangleStyleFactory(StyleFactory):
    def create_style(self) -> Style:
        return RectangleStyle()