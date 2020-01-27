from abc import ABC, abstractmethod

from factory.simple.pizza import Pizza


class PizzaStore(ABC):
    def order_pizza(self, type: str):
        pizza: Pizza

        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, typ:str):
        pass