from factory.simple.ny_style_cheese_pizza import NyStyleCheesePizza
from factory.simple.pizza_store import PizzaStore


class NyStylePizzaStore(PizzaStore):
    def create_pizza(self, type:str):
        return NyStyleCheesePizza()