from flask import Flask, Response, request
from datetime import datetime, timedelta
from pymongo import MongoClient
import json
from model import predict
app = Flask(__name__)
import sys

@app.route("/create-order")
def create_order():
    owm_key = '89e686ad98777cffe46b97744199eab0'

    current_day = datetime.strptime(request.args['start_date'], '%Y %m %d')
    end_date = datetime.strptime(request.args['end_date'], '%Y %m %d')

    item_totals = {}
    while current_day <= end_date:
        weather_condition = 'Sun'
        weather_temperature = 70
        week_number = current_day.isocalendar()[1]
        day_of_week = current_day.isoweekday()

        day_total_sales = predict.get_quantity(day_of_week, week_number, weather_temperature, weather_condition)
        # get ingredient totals for the day

        for key, value in day_total_sales.items():
            if key in item_totals:
                item_totals[key] += value
            else:
                item_totals[key] = value

        current_day += timedelta(1)

    ingredient_totals = {}
    client = MongoClient(
        "mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")

    ingredients = client["Ingredients"]["List"].find_one()
    for item_name in item_totals.keys():
        ingredients_for_item = ingredients[item_name]
        for ingredient, quantity in ingredients_for_item.items():
            if ingredient in ingredient_totals:
                ingredient_totals[ingredient] += quantity
            else:
                ingredient_totals[ingredient] = quantity

    data = {
        'sales': item_totals,
        'ingredients': ingredient_totals
    }

    response = Response(json.dumps(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/")
def hello():
    return "noice"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
