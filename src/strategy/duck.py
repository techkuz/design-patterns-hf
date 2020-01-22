from abc import ABC, abstractmethod
from src.strategy.fly_behavior import FlyBehavior
from src.strategy.quack_behavior import QuackBehavior


class Duck(ABC):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def __init__(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behaviour(self, qb: QuackBehavior):
        self.quack_behavior = qb

