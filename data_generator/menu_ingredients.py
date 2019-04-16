from pymongo import MongoClient

#menu = {"Chicken Caesar Salad": 1, "Chicken Sandwich": 2, "Cheese Burger": 3, "Burger": 4, "Vanilla Shake": 5, "Fries": 6, "Lemonade": 7, "Coffee": 8, "Ice Cream Sundae": 9}

ingredients = {}

ingredients["Chicken Caesar Salad"] = {"Lettuce Head": 1, "Chicken Breast": 2, "Caesar Dressing": 0.5, "Cheese": 2}
ingredients["Chicken Sandwich"] = {"Chicken Breast": 1, "Hamburger Buns": 2, "Pickles": 2}
ingredients["Cheese Burger"] = {"Hamburger": 1, "Hamburger Buns": 2, "Cheese": 1, "Pickles": 2}
ingredients["Burger"] = {"Hamburger": 1, "Hamburger Buns": 2, "Pickles": 2}
ingredients["Vanilla Shake"] = {"Vanilla Ice Cream Scoops": 2, "Milk Jug": 1}
ingredients["Fries"] = {"Potatoes": 2}
ingredients["Lemonade"] = {"Lemons": 2, "Water Bottles": 1, "Sugar": 1}
ingredients["Coffee"] = {"Black Coffee Beans": 1, "Sugar": 2}
ingredients["Ice Cream Sundae"] = {"Vanilla Ice Cream Scoops": 2, "Bananas": 1, "Chocolate Syrup Pack": 1}

try:
    client = MongoClient("mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")
    db = client.test
    print("Connected Successfully!!!\n")
    mdatabase = client["Ingredients"]
    mcol = mdatabase["List"]
    print("Got here\n")
    x = mcol.insert(ingredients)
    print("Database names:", client.list_database_names())
    print("Collection names:", mdatabase.list_collection_names())
except Exception as e:
    print(str(e))
