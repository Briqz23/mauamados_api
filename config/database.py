from pymongo import MongoClient
import os

db_username = os.getenv("USERNAME")
db_password = os.getenv("PASSWORD")
connection = f'mongodb+srv://{db_username}:{db_password}cluster0.gmc47vx.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(connection)

db = client.todo_app

collection_name = db["todos_app"]

