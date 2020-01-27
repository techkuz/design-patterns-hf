from abc import ABC, abstractmethod


class Pepperoni(ABC):
    @abstractmethod
    def to_string(self):
        pass