from flask import Flask, request
from datetime import date, datetime
import pyowm
import json
app = Flask(__name__)


@app.route("/create-order")
def create_order():
    owm_key = '89e686ad98777cffe46b97744199eab0'

    data = json.loads(request.data)
    start_date, end_date = data['start_date'], data['end_date']

    format_string = '%m %d %Y'

    start_date = datetime.strptime(start_date, format_string).date()
    end_date = datetime.strptime(end_date, format_string).date()



    while start_date != end_date:
        average_temp = 70
        day_of_week = start_date.weekday()

        pass

    pass

    fake_data = {
        'sales': {
            'burger': 15,
            'fries': 25,
            'shakes': 10
        },
        'ingredients': {
            'ground beef': '25 lbs',
            'potatoes': '15 lbs',
            'lettuce': '2 heads',
            'buns': '15 buns'
        }
    }
    return json.dumps(fake_data)


@app.route("/")
def hello():
    return "noice"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
