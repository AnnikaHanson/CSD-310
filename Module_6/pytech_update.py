import certifi
ca = certifi.where()
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.ltoqhqg.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["pytech"]
collection = db["students"]

update = {"_id": 1007}
print(update)
updatevalue = {"$set": {"Last Name" : "Johnson"}}
print(updatevalue)
collection.update_one(update,updatevalue)


