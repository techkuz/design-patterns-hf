from factory.simple.pizza import Pizza


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Pizza"
        self.dough = "Extra thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("shredded mozarella sauce")


    def cut(self):
        print("Cutting the pizza into square slices")