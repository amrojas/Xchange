from flask import Flask
import json, weather
app = Flask(__name__)


@app.route("/create-order")
def create_order():
    # actually grab the predictions from the model

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
