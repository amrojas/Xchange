'''
menu_items is a list of the items on the menu
average_temp is a list containing the average temperature for each day in the range of dates
days_of_week is a list of all the days for the order
week_numbers is a list of all the weeks for the order
last_day_week and last_week_number are analogous
weather is a list containing the weather conditions in order (Ex: ["Sun", "Rain", "Snow", "Rain", "Sun"])
'''
def build_new_data(menu_item, average_temp, days_of_week, week_numbers , weather):

    new_data = {}
    new_data["Average Temperature"] = average_temp
    new_data["Day of Week"] = days_of_week
    new_data["Week Number"] = week_numbers
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
