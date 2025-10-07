import os 
from pymongo import MongoClient
from dotenv import load_dotenv
from db_operations.utils import insert, update, find_aggregate

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
    # insert(collection)
    
    # update based on console info
    # property = input("Type the property you want to update:")
    # identifier = input("Type the book title you want to update:")
    # new_data = input("Type the new value you want to set in the new property:")
    # update(str(property), str(identifier), str(new_data), collection)
    
    # find price by book title
    # title = input("Type the book you want to know the price:")
    # find_aggregate(title, collection)
    
    # get the total value of the books
    
except Exception as ex:
    print("Connection failed:", ex)