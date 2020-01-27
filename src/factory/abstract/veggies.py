from abc import ABC, abstractmethod

class Veggies(ABC):
    @abstractmethod
    def to_string(self):
        pass