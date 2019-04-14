class food_sale:

    def __init__(self):
        self.item_id = 0 #Represents food item
        self.week_number = 0 #Based on Calendar week
        self.weather_condition = 0 # 0 = Sun, 1 = Rain, 2 = Snow
        self.average_temperature = 0 # In Farenheit
        self.day_of_week = 0 # 1 = Monday, 7 = Sunday

    def __str__(self):
        return "Item: %s week: %s weather condition: %s average temperature: %s day_of_week: %s" % (self.item_id, self.week_number, self.weather_condition, self.average_temperature, self.day_of_week)

'''    def __init__(self, mitem_id, mweek_number, mweather_condition, maverage_temperature, mday_of_week):
        self.item_id = mitem_id #Represents food item
        self.week_number = mweek_number #Based on Calendar week
        self.weather_condition = mweather_condition # 0 = Sun, 1 = Rain, 2 = Snow
        self.average_temperature = maverage_temperature # In Farenheit
        self.day_of_week = mday_of_week # 1 = Monday, 7 = Sunday
'''
