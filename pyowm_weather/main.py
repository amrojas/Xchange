from pyowm import OWM

#owm object
API_key = '3bc0054509fd1ae200b0f12e20c974c6'
owm = OWM(API_key)

#Getting currently observed weather for a specific location
obs = owm.weather_at_place('London,GB')                    # Toponym
obs = owm.weather_at_id(2643741)                           # City ID
obs = owm.weather_at_coords(-0.107331,51.503614)           # lat/lon

#Retrieving city ID for a location
reg = owm.city_id_registry()
reg.ids_for('London')        # [ (123, 'London', 'GB'), (456, 'London', 'MA'), (789, 'London', 'WY')]
reg.locations_for("London")  # gives a list of Location instances
reg.geopoints_for("London")  # gives a list of pyowm.utils.geo.Point objects

london = reg.ids_for('London', country='GB')                 # [ (123, 'London, GB') ]
london_loc = reg.locations_for('London', country='GB')       # [ <Location obj> ]
london_geopoint = reg.geopoints_for('London', country='GB')  # [ <Point obj> ]

reg.ids_for("london", matching='exact')  # literal matching
reg.ids_for("london", matching='nocase') # case-insensitive
reg.ids_for("london", matching='like')   # substring search

list_of_geopoints = reg.geopoints_for('London', country='GB')

#Currently observed weather extended search
# Find observed weather in all the "London"s in the world
obs_list = owm.weather_at_places('London', 'accurate')
# As above but limit result items to 3
obs_list = owm.weather_at_places('London',searchtype='accurate',limit=3)
# Find observed weather for all the places whose name contains the word "London"
obs_list = owm.weather_at_places('London', 'like')
# Find observed weather for all the places in the surroundings of lon=-2.15,lat=57
obs_list = owm.weather_around_coords(-2.15, 57)
# As above but limit result items to 8
obs_list = owm.weather_around_coords(-2.15, 57, limit=8)

#Getting data from Observation objects
obs.get_reception_time()                           # UNIX GMT time
obs.get_reception_time(timeformat='iso')           # ISO8601
obs.get_reception_time(timeformat='date')          # datetime.datetime instance

w = obs.get_weather()

w.get_reference_time()                             # get time of observation in GMT UNIXtime

w.get_reference_time(timeformat='iso')             # ...or in ISO8601

w.get_reference_time(timeformat='date')            # ...or as a datetime.datetime object

w.get_clouds()                                     # Get cloud coverage

w.get_rain()                                       # Get rain volume

w.get_snow()                                       # Get snow volume

w.get_wind()                                       # Get wind degree and speed

w.get_humidity()                                   # Get humidity percentage

w.get_pressure()                                   # Get atmospheric pressure

w.get_temperature()                                # Get temperature in Kelvin

w.get_temperature(unit='celsius')                  # ... or in Celsius degs
w.get_temperature('fahrenheit')                    # ... or in Fahrenheit degs

w.get_status()                                     # Get weather short status

w.get_detailed_status()                           # Get detailed weather status

w.get_weather_code()                               # Get OWM weather condition code

w.get_weather_icon_name()                          # Get weather-related icon name

w.get_weather_icon_url()                          # Get weather-related icon URL=

w.get_sunrise_time()                               # Sunrise time (GMT UNIXtime or ISO 8601)

w.get_sunset_time('iso')                           # Sunset time (GMT UNIXtime or ISO 8601)

l = obs.get_location()

l.get_name()

l.get_lon()

l.get_lat()

l.get_ID()

#Getting weather forecasts
fc = owm.three_hours_forecast('London,uk')

#fc = owm.daily_forecast('London,uk')

#fc = owm.daily_forecast('London,uk', limit=6)

f = fc.get_forecast()

f.get_reception_time()

f.get_reception_time('iso')

f.get_reception_time('date')

f.get_interval()

len(f)

f.get_location()

lst = f.get_weathers()

for weather in f:
      print (weather.get_reference_time('iso'),weather.get_status())

fc.when_starts()

fc.when_starts('iso')

fc.when_starts('date')

fc.when_ends()

fc.when_ends('iso')

fc.when_ends('date')

#Weather in 24 hours
from datetime import datetime
#date_tomorrow = datetime(2013, 9, 19, 12, 0)
#str_tomorrow = "2013-09-19 12:00+00"
#fc.get_weather_at(date_tomorrow)
#fc.get_weather_at(str_tomorrow)

#fc.get_weather_at("1492-10-12 12:00:00+00")

from pyowm import timeutils
timeutils.tomorrow()                              # Tomorrow at this hour
timeutils.yesterday(23, 27)                       # Yesterday at 23:27
timeutils.next_three_hours()                      # 3 hours from now
t = datetime.datetime(2013, 19, 27, 8, 47, 0)
timeutils.next_three_hours(t)                     # 3 hours from a specific datetime

# Will it rain, be sunny, foggy or snow during the covered period?
fc.will_have_rain()

fc.will_have_sun()
fc.will_have_fog()
fc.will_have_clouds()
fc.will_have_snow()

# Will it be rainy, sunny, foggy or snowy at the specified GMT time?
time = "2013-09-19 12:00+00"
fc.will_be_rainy_at(time)
fc.will_be_sunny_at(time)
fc.will_be_foggy_at(time)

fc.will_be_cloudy_at(time)
fc.will_be_snowy_at(time)

#fc.will_be_sunny_at(0L)           # Out of weather forecast coverage
#pyowm.exceptions.not_found_error.NotFoundError: The searched item was not found.
#Reason: Error: the specified time is not included in the weather coverage range

# List the weather elements for which the condition will be:
# rain, sun, fog and snow
fc.when_rain()
fc.when_sun()
fc.when_clouds()
fc.when_fog()
fc.when_snow()                               # It won't snow: empty list

# Get weather for the hottest, coldest, most humid, most rainy, most snowy
# and most windy days in the forecast
fc.most_hot()
fc.most_cold()
fc.most_humid()
fc.most_rainy()
fc.most_snowy()
fc.most_windy()

#Getting weather history on a location
owm.weather_history_at_place('London,uk')
#owm.weather_history_at_place('London,uk', start=1379090800L, end=1379099800L)
owm.weather_history_at_place('London,uk', '2013-09-13 16:46:40+00', '2013-09-13 19:16:40+00')
from datetime import datetime
owm.weather_history_at_place('London,uk', datetime(2013, 9, 13, 16, 46, 40), datetime(2013, 9, 13, 19, 16, 40))

#Getting meteostation measurements history
# Get tick historic data for station 39276, only 4 data items
hist = owm.station_tick_history(39276, limit=4)
# Get hourly historic data for station 39276
hist = owm.station_hour_history(39276)
# Get daily historic data for station 39276, only 10 data items
hist = owm.station_day_history(39276, 10)

sh = hist.get_station_history()

sh.get_station_ID()                   # Meteostation ID
sh.get_interval()                     # Data sampling interval
sh.get_reception_time()               # Timestamp when data was received (GMT UNIXtime, ISO8601
                                          # or datetime.datetime)
sh.get_reception_time("iso")
sh.get_measurements()                 # Get historic data as a dict

# Get the temperature time series (in different units of measure)
hist.temperature_series()

hist.temperature_series(unit="celsius")

hist.temperature_series("fahrenheit")

# Get the humidity time series
hist.humidity_series()

# Get the atmospheric pressure time series
hist.pressure_series()

# Get the rain volume time series
hist.rain_series()

# Get the wind speed time series
hist.wind_series()

# Get the minimum temperature value in the series
hist.min_temperature(unit="celsius")

# Get the maximum rain value in the series
hist.max_rain()

# Get the average wind value in the series
hist.average_wind()

#Dumping objects’ content to JSON and XML
# Dump a Weather object to JSON...
w.to_JSON()

#... and to XML
w.to_XML()

w.to_XML(xml_declaration=True, xmlns=False)

print(w)
print(w.get_location())