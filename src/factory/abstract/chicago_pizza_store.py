from factory.abstract.cheese_pizza import CheesePizza
from factory.abstract.chicago_pizza_ingredient_factor import ChicagoPizzaIngredientFactory
from factory.abstract.clam_pizza import ClamPizza
from factory.abstract.pepperoni_pizza import PepperoniPizza
from factory.abstract.pizza import Pizza
from factory.abstract.pizza_ingredient_factory import PizzaIngredientFactory
from factory.abstract.pizza_store import PizzaStore
from factory.abstract.veggie_pizza import VeggiePizza


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item: str):
        pizza: Pizza = None
        ingredient_factory: PizzaIngredientFactory = ChicagoPizzaIngredientFactory()

        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style veggie pizza")
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam pizzas")
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")

        return pizza
