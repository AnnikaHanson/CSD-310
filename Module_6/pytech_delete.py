import certifi
ca = certifi.where()
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.ltoqhqg.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["pytech"]
collection = db["students"]


value = {"_id": 1010}
collection.delete_one(value)

find_one = {"_id": 1010}
print (find_one)
results = collection.find_one({"_id": 1010})
print(results)

