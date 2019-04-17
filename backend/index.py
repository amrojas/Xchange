from flask import Flask, Response, request
from datetime import datetime, timedelta
import pyowm
import json
app = Flask(__name__)


def fn(day_of_week, week_number, temp, weather):
    return {}


@app.route("/create-order")
def create_order():
    owm_key = '89e686ad98777cffe46b97744199eab0'

    current_day = datetime.strptime(request.args['start_date'], '%Y %m %d')
    end_date = datetime.strptime(request.args['end_date'], '%Y %m %d')

    item_totals = {}
    ingredient_totals = {}
    while current_day <= end_date:
        weather_condition = 'Sun'
        weather_temperature = 70
        week_number = current_day.isocalendar()[1]
        day_of_week = current_day.isoweekday()

        day_total_sales = fn(day_of_week, week_number, weather_temperature, weather_condition)
        # get ingredient totals for the day
        day_total_ingredients = {}

        for key, value in day_total_sales.items():
            if key in item_totals:
                item_totals[key] = value
            else:
                item_totals[key] += value

        for key, value in day_total_ingredients.items():
            if key in ingredient_totals:
                ingredient_totals[key] = value
            else:
                ingredient_totals[key] += value

        current_day + timedelta(1)

    data = {
        'sales': item_totals,
        'ingredients': ingredient_totals
    }

    fake_data = {
        'sales': {
            'burger': 15,
            'friesssssss': 25,
            'shakes': 10
        },
        'ingredients': {
            'ground beef': '25 lbs',
            'potatoes': '15 lbs',
            'lettuce': '2 heads',
            'buns': '15 buns',
            'tomatoes': '4 tomatoes'
        }
    }
    response = Response(json.dumps(fake_data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/")
def hello():
    return "noice"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
