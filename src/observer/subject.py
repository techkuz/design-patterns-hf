from abc import ABC, abstractmethod

from src.observer.observer import Observer


class Subject(ABC):
    @abstractmethod
    def register_observer(self, o: Observer):
        pass

    @abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass