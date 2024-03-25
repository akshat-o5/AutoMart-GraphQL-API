from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

if client is not None:
    print("DATABASE CONNECTED SUCCESSFULLY!!")

db = client["graphql"]
collection = db["vehicalInfo"]