from src.observer.display_element import DisplayElement
from src.observer.observer import Observer
from src.observer.subject import Subject


class ForecastDisplay(Observer, DisplayElement):
    temperature: float
    humidity: float
    weather_data: Subject

    def __init__(self, weather_data: Subject):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity")