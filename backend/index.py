from flask import Flask
import pymongo
import squareconnect
app = Flask(__name__)


@app.route("/")
def hello():
    return "change this up"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
