from abc import ABC, abstractmethod

from factory.abstract.pizza import Pizza


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, item: str):
        pass

    def order_pizza(self, type: str):
        pizza: Pizza = self.create_pizza(type)
        print("--- Making a " + pizza.get_name() + "---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza