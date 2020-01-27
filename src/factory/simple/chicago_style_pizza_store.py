from factory.simple.chicago_style_cheese_pizza import ChicagoStyleCheesePizza
from factory.simple.pizza_store import PizzaStore


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, type:str):
        return ChicagoStyleCheesePizza()