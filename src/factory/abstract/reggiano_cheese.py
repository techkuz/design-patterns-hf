from factory.abstract.cheese import Cheese


class ReggianoCheese(Cheese):
    def to_string(self):
        return "reggian cheese"