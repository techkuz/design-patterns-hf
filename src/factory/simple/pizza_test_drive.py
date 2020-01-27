from factory.simple.chicago_style_pizza_store import ChicagoStylePizzaStore
from factory.simple.ny_style_pizza_store import NyStylePizzaStore
from factory.simple.pizza import Pizza
from factory.simple.pizza_store import PizzaStore


class PizzaTestDrive:
    if __name__ == '__main__':
        ny_store: PizzaStore = NyStylePizzaStore()
        chicago_store: PizzaStore = ChicagoStylePizzaStore()

        pizza: Pizza = ny_store.order_pizza("cheese")
        print("Ethan ordered a " + pizza.get_name() + "\n")

        pizza: Pizza = chicago_store.order_pizza("cheese")
        print("Joel ordered a " + pizza.get_name() + "\n")



