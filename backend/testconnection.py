from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")
    db = client.test
    print("Connected Successfully!!!")
except:
    print("could not connect to MongoDB")
