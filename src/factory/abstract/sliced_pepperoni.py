from factory.abstract.pepperoni import Pepperoni


class SlicedPepperoni(Pepperoni):
    def to_string(self):
        return "Sliced pepperoni;"