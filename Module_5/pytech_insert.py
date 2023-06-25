import pymongo
import certifi
from pymongo import MongoClient
connection = "mongodb+srv://admin:admin@cluster0.ltoqhqg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection, ssl=certifi.where())
db = client["pytech"]
collection = db["students"]

post1 = {"_id": 1007, "First Name": "Jake", "Last Name": "Sully"}
post2 = {"_id": 1008, "First Name": "Harry", "Last Name": "Potter"}
post3 = {"_id": 1009, "First Name": "Legolas", "Last Name": "Leaf"}
collection.insert_many([post1, post2, post3])