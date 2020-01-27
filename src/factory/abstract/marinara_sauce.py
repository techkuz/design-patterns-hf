from factory.abstract.sauce import Sauce


class MarinaraSauce(Sauce):
    def to_string(self):
        return "Marinara Sauce"