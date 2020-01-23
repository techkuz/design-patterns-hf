from src.decorator.beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso Coffee;"

    def cost(self):
        return .89