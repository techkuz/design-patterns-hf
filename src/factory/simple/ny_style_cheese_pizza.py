from factory.simple.pizza import Pizza


class NyStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Ny Style Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings.append("grated reggiano cheese")


    def cut(self):
        print("Cutting the pizza into slices")