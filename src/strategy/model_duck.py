from src.strategy.duck import Duck
from src.strategy.fly_no_way import FlyNoWay
from src.strategy.quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")