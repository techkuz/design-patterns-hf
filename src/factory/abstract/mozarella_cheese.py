from factory.abstract.cheese import Cheese


class MozarellaCheese(Cheese):
    def to_string(self):
        return "Mozarella Cheese"