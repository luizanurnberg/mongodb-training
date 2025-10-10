from pymongo import ReturnDocument
from db_operations.book_data import books

def insert(collection):
    if not books: 
        raise ValueError("All parameters for insert are not available")
    for element in books:
        try:
            collection.insert_one(element)
            print("Success")
        except Exception as ex: 
            print("Insert failed", ex)

def update(property, book_identifier, new_data, collection):
    if not property or not new_data or not book_identifier: 
        raise ValueError("All parameters for update are not available")
    try:
        updated_book = collection.find_one_and_update({ "title": book_identifier}, {"$set": { property: new_data }},  return_document=ReturnDocument.AFTER)
        if updated_book:
            print(f"Success! New {property} was set with the value: {new_data}")
        else:
            print("Update was not completed")
    except Exception as ex:
        print("Update failed", ex)
        
def find_aggregate(title, collection):
    if not title: 
        raise ValueError("All parameters for find are not available")
    try:
        book_found = collection.aggregate([{
            "$match": {
                "title": {"$regex": title, "$options": "i"}
            }
        },{
            "$project": {
                "price": 1
            }
        }])
        
        if book_found:
            for element in book_found:
                print(f"The book {title} is costing {element['price']} dollars")          
        else:
            print("Book was not found")
    except Exception as ex: 
        print("Find failed", ex)

def group_price(collection, db_name, final_collection):
    try:
        total = collection.aggregate([{
            "$group": {
            "_id": 0,
            "total": {
                "$sum": "$price"
            }
            }
        }, {
            "$out": {
                "db": db_name,
                "coll": final_collection
            }
        }])
        
        if total:
            for element in total:
                print(f"The total value of the books is {element['total']} dolars")          
    except Exception as ex:
        print("Fail to sum total book value", ex)