from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def to_string(self):
        pass