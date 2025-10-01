import os 
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_credentials = os.getenv("MONGO_DB_CREDENTIALS")
db_name = os.getenv("DB_NAME")
db_collection = os.getenv("DB_COLLECTION")

if not mongo_credentials or not db_name or not db_collection:
    raise ValueError("Environment variables are note available")

connection = MongoClient(mongo_credentials)
data_base = connection[db_name]
collection = data_base[db_collection]

try: 
    connection.admin.command("ping")
    print("Connected on Mongo")
    
    # seed data on db
    insert(connection)
    
    # update
except Exception as ex:
    print("Connection failed:", ex)