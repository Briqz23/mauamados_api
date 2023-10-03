from pymongo import MongoClient
import os
from dotenv import load_dotenv


db_username = os.getenv("USERNAME")
db_password = os.getenv("PASSWORD")

connection = 'mongodb://localhost:27017/'
client = MongoClient(connection)

db = client.mauamados

collection_name_user = db["usuarios"]
collection_name_match = db["matchs_likes"]
collection_name_login = db["login"]
collection_name_conversas = db["conversas"]