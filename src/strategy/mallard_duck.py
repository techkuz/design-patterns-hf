from src.strategy.duck import Duck
from src.strategy.fly_with_wings import FlyWithWings
from src.strategy.quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")