from flask import Flask, Response
from datetime import date, datetime
import pyowm
import json
app = Flask(__name__)


@app.route("/create-order")
def create_order():
    owm_key = '89e686ad98777cffe46b97744199eab0'

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
            'buns': '15 buns'
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
