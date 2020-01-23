from src.decorator.beverage import Beverage
from src.decorator.dark_roast import DarkRoast
from src.decorator.espresso import Espresso
from src.decorator.mocha import Mocha
from src.decorator.soy import Soy
from src.decorator.whip import Whip


class StarBuzzCoffee:
    if __name__ == '__main__':
        beverage: Beverage = Espresso()
        print(beverage.get_description() + " $" + str(beverage.cost()))

        beverage2: Beverage = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print(beverage2.get_description() + " $" + str(beverage2.cost()))

        beverage3: Beverage = DarkRoast()
        beverage3 = Soy(beverage3)
        beverage3 = Mocha(beverage3)
        beverage3 = Whip(beverage3)
        print(beverage3.get_description() + " $" + str(beverage3.cost()))

