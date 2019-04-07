from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")
    db = client.test
    print("Connected Successfully!!!\n")
except Exception as e:
    print(str(e))

