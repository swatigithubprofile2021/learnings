import pymongo


if __name__ =="__main__":
    print("Welcome to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    mydb = client['my_first_database']
    ## List name of databases
    #db_list =mydb.list_databases()
    
    my_collection = mydb["Customers"]
    ## In MongoDB, a collection is not created until it gets content!
    # mydict = { "name": "swati", "address": "vasundhara" }
    # x = my_collection.insert_one(mydict)
    ## If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each
    #  document.
    mydict = {"name":"amit","address":"ghaziabad"}
    x = my_collection.insert_one(mydict)
    print(x.inserted_id)




    ## Check list of collections
    collection_list = mydb.list_collection_names()
    print(mydb.list_collection_names())
    ## Specifially check any collection existence by name
    if "swati" in collection_list:
        print("Collection exists")
