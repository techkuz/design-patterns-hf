from abc import abstractmethod, ABC


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: [str] = []

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce ")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(" " + topping)

    def bake(self):
        print("Baking")

    def cut(self):
        print("Cutting")

    def box(self):
        print("Placing in the box")

    def get_name(self):
        return self.name
