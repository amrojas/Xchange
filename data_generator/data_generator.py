import random
from pymongo import MongoClient
from food_sale import food_sale

'''
DO NOT RUN THIS! DATA IS ALREADY INSIDE MONGODB CLUSTER
'''
#menu = {"Chicken Caesar Salad": 1, "Chicken Sandwich": 2, "Cheese Burger": 3, "Burger": 4, "Vanilla Shake": 5, "Fries": 6, "Lemonade": 7, "Coffee": 8, "Ice Cream Sundae": 9}
total_items = 0
restaurant_sales = []
for year in range(5):
    for week in range(1, 53):
        for day in range(1, 8):
            # Generate number of goods sold
            mu = 290 if day >= 5 else 275
            sigma = 20 if day >= 5 else 10
            number_sold = round(random.gauss(mu, sigma))
            weather_condition = 'Sun'
            if (week < 13):
                if (random.random() < 0.15):
                    number_sold = number_sold * 0.3
                    weather_condition = 'Snow'
            # Sunny vs rain
            sunny = random.random()
            if (sunny > 0.3 and weather_condition != 'Snow'):
                number_sold = number_sold*1.1
                weather_condition = 'Sun'
            elif (sunny <= 0.3 and weather_condition != 'Snow'):
                number_sold = number_sold*0.9
                weather_condition = 'Rain'
            number_sold = int(number_sold)
            total_items += number_sold
            for _ in range(number_sold):
                item_sold = food_sale()
                item_sold.week_number = week
                item_sold.day_of_week = day
                item_sold.weather_condition = weather_condition

                # Food item or drink
                food = True if random.random() > 0.3 else False

                # Winter
                if (week < 13):
                    item_sold.average_temperature = round(random.gauss(37, 10))
                    # Drink distribution
                    if (not food):
                        if (day <= 5):
                            rand = random.random()
                            if (rand < .1):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .8):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                        else:
                            if (rand < .1):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .7):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                    # Food item distribution
                    else:
                        rand = random.random()
                        if (rand <= .25):
                            item_sold.item_id = 'Chicken Caesar Salad'
                        elif (rand <= .45):
                            item_sold.item_id = 'Chicken Sandwich'
                        elif (rand <= .60):
                            item_sold.item_id = 'Cheese Burger'
                        elif (rand <= .75):
                            item_sold.item_id = 'Burger'
                        elif (rand <= .95):
                            item_sold.item_id = 'Fries'
                        else:
                            item_sold.item_id = 'Ice Cream Sundae'

                # Spring
                elif (week < 26):
                    item_sold.average_temperature = round(random.gauss(60, 10))
                    # Drink distribution
                    if (not food):
                        if (day <= 5):
                            rand = random.random()
                            if (rand < .2):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .6):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                        else:
                            if (rand < .3):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .6):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                    # Food item distribution
                    else:
                        rand = random.random()
                        if (rand <= .20):
                            item_sold.item_id = 'Chicken Caesar Salad'
                        elif (rand <= .40):
                            item_sold.item_id = 'Chicken Sandwich'
                        elif (rand <= .60):
                            item_sold.item_id = 'Cheese Burger'
                        elif (rand <= .80):
                            item_sold.item_id = 'Burger'
                        elif (rand <= .95):
                            item_sold.item_id = 'Fries'
                        else:
                            item_sold.item_id = 'Ice Cream Sundae'

                # Summer
                elif (week < 39):
                    item_sold.average_temperature = round(random.gauss(80, 10))
                    # Drink distribution
                    if (not food):
                        if (day <= 5):
                            rand = random.random()
                            if (rand < .5):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .7):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                        else:
                            if (rand < .6):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .7):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                    # Food item distribution
                    else:
                        rand = random.random()
                        if (rand <= .15):
                            item_sold.item_id = 'Chicken Caesar Salad'
                        elif (rand <= .30):
                            item_sold.item_id = 'Chicken Sandwich'
                        elif (rand <= .50):
                            item_sold.item_id = 'Cheese Burger'
                        elif (rand <= .70):
                            item_sold.item_id = 'Burger'
                        elif (rand <= .85):
                            item_sold.item_id = 'Fries'
                        else:
                            item_sold.item_id = 'Ice Cream Sundae'

                # Fall
                else:
                    item_sold.average_temperature = round(random.gauss(50, 10))
                    # Drink distribution
                    if (not food):
                        if (day <= 5):
                            rand = random.random()
                            if (rand < .2):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .8):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                        else:
                            if (rand < .2):
                                 item_sold.item_id = 'Vanilla Shake'
                            elif (rand < .6):
                                 item_sold.item_id = 'Coffee'
                            else:
                                 item_sold.item_id = 'Lemonade'
                    # Food item distribution
                    else:
                        rand = random.random()
                        if (rand <= .20):
                            item_sold.item_id = 'Chicken Caesar Salad'
                        elif (rand <= .40):
                            item_sold.item_id = 'Chicken Sandwich'
                        elif (rand <= .60):
                            item_sold.item_id = 'Cheese Burger'
                        elif (rand <= .75):
                            item_sold.item_id = 'Burger'
                        elif (rand <= .95):
                            item_sold.item_id = 'Fries'
                        else:
                            item_sold.item_id = 'Ice Cream Sundae'
                #print(item_sold)
                restaurant_sales.append({"Item_id": item_sold.item_id, "Week Number": item_sold.week_number, "Weather Condition": item_sold.weather_condition, "Average Temperature": item_sold.average_temperature, "Day of Week": item_sold.day_of_week})

print(total_items)

try:
    client = MongoClient("mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")
    db = client.test
    print("Connected Successfully!!!\n")
    mdatabase = client["generatedData"]
    mcol = mdatabase["Data"]
    x = mcol.insert_many(restaurant_sales)
    print("Database names:", client.list_database_names())
    print("Collection names:", mdatabase.list_collection_names())
except Exception as e:
    print(str(e))
