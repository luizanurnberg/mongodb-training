from datetime import datetime
from book_data import books

def insert(collection):
    for element in books:
        try:
            collection.insert_one(element)
            print("Success")
        except Exception as ex: 
            print("Insert failed", ex)