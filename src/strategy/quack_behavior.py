from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass