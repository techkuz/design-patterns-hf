from abc import ABC, abstractmethod


class Cheese(ABC):
    @abstractmethod
    def to_string(self):
        pass