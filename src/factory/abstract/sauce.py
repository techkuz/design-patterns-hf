from abc import ABC, abstractmethod

class Sauce(ABC):
    @abstractmethod
    def to_string(self):
        pass