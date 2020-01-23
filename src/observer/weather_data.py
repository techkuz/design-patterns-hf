from src.observer.observer import Observer
from src.observer.subject import Subject


class WeatherData(Subject):
    observers: list
    temperature: float
    humidity: float
    pressure: float

    def __init__(self):
        self.observers: [Observer] = []

    def register_observer(self, o: Observer):
        self.observers.append(o)

    def remove_observer(self, o: Observer):
        i: int = self.observers.index(o)

        if i >= 0:
            self.observers.remove(i)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()