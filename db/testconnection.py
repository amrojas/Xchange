from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://Xchange_admin:R2f3qzOyEkyWZjWd@xchangealpha-qyyva.mongodb.net/test?retryWrites=true")
    db = client.test
    print("Connected Successfully!!!\n")
except Exception as e:
    print(str(e))

mdatabase = client["generatedData"]
mcol = mdatabase[""]

mcol.drop()

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
try:
    x = mcol.insert_many(mylist)
    print("x.inserted_id:", x.inserted_ids)
    print("Database names:", client.list_database_names())
    print("Collection names:", mdatabase.list_collection_names())

except Exception as e:
    print(str(e))
    print(e.details)
