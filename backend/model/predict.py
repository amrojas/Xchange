from __future__ import absolute_import, division, print_function
from pymongo import MongoClient
from buildDataFrame import build_new_data
import pandas as pd

import tensorflow as tf
from tensorflow import keras

def initialize_model():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = keras.models.model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss='mean_squared_error',
                    optimizer=tf.keras.optimizers.RMSprop(0.001),
                    metrics=['mean_absolute_error', 'mean_squared_error'])

    menu = ["Chicken Caesar Salad",
            "Chicken Sandwich",
            "Cheese Burger",
            "Burger",
            "Vanilla Shake",
            "Fries",
            "Lemonade",
            "Coffee",
            "Ice Cream Sundae"]

    return loaded_model, menu

def norm(x):
    client = MongoClient(
        "mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")

    db2 = client["TrainingStatistics"]

    mean_from_db = db2["mean"].find_one()
    del mean_from_db["_id"]
    mean_from_db_series = pd.Series(mean_from_db)
    mean_from_db_series

    std_from_db = db2["std"].find_one()
    del std_from_db["_id"]
    std_from_db_series = pd.Series(std_from_db)
    std_from_db_series

    return (x - mean_from_db_series) / std_from_db_series

def get_quantity(day_of_week, week_number, temp, weather):
    model, menu = initialize_model()
    df = build_new_data(menu, temp, day_of_week, week_number, weather)
    normalized_data = norm(df)
    nd_array = model.predict(normalized_data)
    quantities = {}

    for i in range(len(menu)):
        quantities[menu[i]] = int(nd_array[i][0])
    return quantities


print(get_quantity(5, 26, 78, "Sun"))