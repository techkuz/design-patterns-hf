from src.decorator.beverage import Beverage
from src.decorator.condiment_decorator import CondimentDecorator


class Soy(CondimentDecorator):
    beverage: Beverage

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + .20