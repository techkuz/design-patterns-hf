from factory.abstract.clams import Clams


class FrozenClams(Clams):
    def to_string(self):
        return "Frozen Clams"