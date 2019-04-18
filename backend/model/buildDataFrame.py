'''
menu_items is a list of the items on the menu
average_temp is a list containing the average temperature for each day in the range of dates
days_of_week is a list of all the days for the order
week_numbers is a list of all the weeks for the order
last_day_week and last_week_number are analogous
weather is a list containing the weather conditions in order (Ex: ["Sun", "Rain", "Snow", "Rain", "Sun"])
'''
import pandas as pd

def build_new_data(menu, average_temp, days_of_week, week_numbers , weather):

    menu_size = len(menu)
    new_data = {}
    new_data["Average Temperature"] = [average_temp] *  menu_size
    new_data["Day of Week"] = [days_of_week] * menu_size
    new_data["Week Number"] = [week_numbers] * menu_size
    new_data["Sun"] = [1 if weather == "Sun" else 0] * menu_size
    new_data["Rain"] = [1 if weather == "Rain" else 0] * menu_size
    new_data["Snow"] = [1 if weather == "Snow" else 0] * menu_size
    for food in menu:
        new_data[food] = [1 if item == food else 0 for item in menu]

    return pd.DataFrame.from_dict(new_data)
