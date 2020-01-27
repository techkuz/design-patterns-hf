from factory.abstract.pizza import Pizza
from factory.abstract.pizza_ingredient_factory import PizzaIngredientFactory


class VeggiePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory : PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

