from factory.abstract.chicago_pizza_store import ChicagoPizzaStore
from factory.abstract.ny_pizza_store import NyPizzaStore
from factory.abstract.pizza_store import PizzaStore


class PizzaTestDrive:
    if __name__ == '__main__':
        ny_store: PizzaStore = NyPizzaStore()
        chicago_store: PizzaStore = ChicagoPizzaStore()

        pizza = ny_store.order_pizza("cheese")
        print('Ethan ordered a ' + str(pizza) + "\n")

        pizza = chicago_store.order_pizza("cheese")
        print('Joel ordered a ' + str(pizza) + "\n")

        pizza = ny_store.order_pizza("clam")
        print('Ethan ordered a ' + str(pizza) + "\n")

        pizza = chicago_store.order_pizza("clam")
        print('Joel ordered a ' + str(pizza) + "\n")

        pizza = ny_store.order_pizza("pepperoni")
        print('Ethan ordered a ' + str(pizza) + "\n")

        pizza = chicago_store.order_pizza("pepperoni")
        print('Joel ordered a ' + str(pizza) + "\n")

        pizza = ny_store.order_pizza("veggie")
        print('Ethan ordered a ' + str(pizza) + "\n")

        pizza = chicago_store.order_pizza("veggie")
        print('Joel ordered a ' + str(pizza) + "\n")

