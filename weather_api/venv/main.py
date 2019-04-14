#pip install weather-api
# or add via pycharm interpreter preferences
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(560743)
condition = lookup.condition

print(condition.text)

#lookup via location name
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('dublin')
condition = location.condition
print(condition.text)

#get weather forecasts for upcoming days
weather = Weather(unit=Unit.CELSIUS)

forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)

#lookup via longitude and latitude
weather = Weather(Unit.CELSIUS)
lookup = weather.lookup_by_latlng(53.3494, -6.2601)
condition = lookup.condition
print(condition.text)

#also supports CL usage
#https://pypi.org/project/weather-api/