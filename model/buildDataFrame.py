'''
average_temp is a list containing the average temperature for each day in the range of dates
first_day_of_week is an int of the first day of order (Monday = 1, Tuesday = 2 ... Sunday = 7)
first_week_number is an int of the first week of order (First week of January = 1, ... Last week of December = 52)
last_day_week and last_week_number are analogous
weather is a list containing the weather conditions in order (Ex: ["Sun", "Rain", "Snow", "Rain", "Sun"])
'''
def build_new_data(average_temp, first_day_of_week, first_week_number, last_day_of_week, last_week_number, weather):

    new_data = {}
    new_data["Average Temperature"] = average_temp
    new_data["Day of Week"] = []
    new_data["Week Number"] = []
    new_data["Sun"] = [1 if w == "Sun" else 0 for w in weather]
    new_data["Rain"] = [1 if w == "Rain" else 0 for w in weather]
    new_data["Snow"] = [1 if w == "Snow" else 0 for w in weather]
    new_data["Cheese Burger"] = []
    new_data["Chicken Caesar Salad"] = []
    new_data["Chicken Sandwich"] = []
    new_data["Burger"] = []
    new_data["Vanilla Shake"] = []
    new_data["Fries"] = []
    new_data["Lemonade"] = []
    new_data["Coffee"] = []
    new_data["Ice Cream Sundae"] = []
    print(new_data)

    return pd.DataFrame.from_dict(new_data)
