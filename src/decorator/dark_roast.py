from src.decorator.beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self):
        return .89