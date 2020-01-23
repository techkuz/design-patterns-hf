from src.observer.current_condition_display import CurrentConditionDisplay
from src.observer.forecast_display import ForecastDisplay
from src.observer.statistics_display import StatisticsDisplay
from src.observer.weather_data import WeatherData


class WeatherStation:
    if __name__ == '__main__':
        weather_data: WeatherData = WeatherData()
        current_conditions_display: CurrentConditionDisplay = CurrentConditionDisplay(weather_data)
        statistics_display: StatisticsDisplay = StatisticsDisplay(weather_data)
        forecast_display: ForecastDisplay = ForecastDisplay(weather_data)

        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)