from flask import Flask
import pymongo
import squareconnect
app = Flask(__name__)


@app.route("/create-order")
def create_order():
    return "this is an order for the modal"


@app.route("/")
def hello():
    return "noice"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
