from abc import ABC, abstractmethod


class Clams(ABC):
    @abstractmethod
    def to_string(self):
        pass