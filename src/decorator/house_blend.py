from src.decorator.beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House blend Coffee;"

    def cost(self):
        return .89