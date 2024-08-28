import pymongo
from pymongo import ReturnDocument


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017") ## connecting to mongo client
    db = client["test_database"] ## creating database
    inventory = db["items"] ## creating collection in data base
    data = [
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "A",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
    ]

## Inserting data into collection
    #db.inventory.insert_many(data)

## querying  all records(similar to select * from sql)
    # result = db.inventory.find({})
    # for i in result:
    #     print(i)
## Querying with some condition like("Select * from table where condition")
#     #cursor = db.inventory.find_one({"item":"journal"})
    #print(cursor)
    # cursor = db.inventory.find_one_and_update({"item":"journal"},
    #                                        {"$set":{"qty":26}},
    #                                       return_document=ReturnDocument.AFTER)
    # print(cursor)

    # cursor2 = db.inventory.find_one_and_delete({"item":"journal"})
    # for d in db.inventory.find():
    #     print(d)

    ##    
## Specify equality conditions:
## The following query selects from the inventory collection all documents where the status equals "D":



        