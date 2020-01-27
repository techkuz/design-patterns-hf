from abc import ABC, abstractmethod

from factory.abstract.cheese import Cheese
from factory.abstract.clams import Clams
from factory.abstract.dough import Dough
from factory.abstract.pepperoni import Pepperoni
from factory.abstract.sauce import Sauce
from factory.abstract.veggies import Veggies


class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    veggies: [Veggies]
    cheese: Cheese
    pepperoni: Pepperoni
    clam: Clams

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("bake for 25 mins at 350")

    def cut(self):
        print("cutting pizza")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def to_string(self):
        return self.name