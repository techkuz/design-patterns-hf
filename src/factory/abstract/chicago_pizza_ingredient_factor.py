from factory.abstract.fresh_clams import FreshClam
from factory.abstract.garlic import Garlic
from factory.abstract.marinara_sauce import MarinaraSauce
from factory.abstract.mushroom import Mushroom
from factory.abstract.onion import Onion
from factory.abstract.pizza_ingredient_factory import PizzaIngredientFactory
from factory.abstract.red_pepper import RedPepper
from factory.abstract.reggiano_cheese import ReggianoCheese
from factory.abstract.sliced_pepperoni import SlicedPepperoni
from factory.abstract.thin_crust_dough import ThinCrustDough


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClam()