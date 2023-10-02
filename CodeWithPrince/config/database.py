from pymongo import MongoClient

client = MongoClient("mongodb+srv://kusko:portuguesa1@cluster0.i4xp1jm.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_application

collection_name = db['todo_app']