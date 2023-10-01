from pymongo import MongoClient
import os
from dotenv import load_dotenv


db_username = os.getenv("USERNAME")
db_password = os.getenv("PASSWORD")

connection = 'mongodb://localhost:27017/'
client = MongoClient(connection)

db = client.mauamados_app

collection_name = db["mauamados_app"]