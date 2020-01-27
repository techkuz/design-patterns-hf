from factory.abstract.veggies import Veggies


class Mushroom(Veggies):
    def to_string(self):
        return "Mushroom"