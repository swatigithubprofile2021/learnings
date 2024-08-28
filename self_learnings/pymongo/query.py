import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = client["my_first_database"]
    my_collection = mydb["Customers"]

    ## find document with address park lane 38
    # my_query = {"address":"Park Lane 38"}

    # mydoc = my_collection.find(my_query)
    # for i in mydoc:
    #      print(i)
## Advance query :
## find address field where address starts with letter S or higher
    my_query = {"address":{"$gt":"S"}}
    mydoc = my_collection.find(my_query)
    for i in mydoc:
        print(i)
