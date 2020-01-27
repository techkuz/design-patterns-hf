from abc import abstractmethod, ABC


class Beverage(ABC):
    description: str = "Unknown beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass