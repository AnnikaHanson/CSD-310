import certifi
import pymongo
ca = certifi.where()

client = pymongo.MongoClient(
"mongodb+srv://admin:admin@cluster0.ltoqhqg.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)