import pymongo


if __name__ =="__main__":
    print("Welcome to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    mydb = client['my_first_database']
    my_collection = mydb["Customers"]
    ## to find only one record
    x = my_collection.find_one()
    print(x)
    ## To find all record at once
    for x in my_collection.find():
        print(x)
    ## To find specific columns in document:this will not return id field, only return name and address of the documnet
    for x in my_collection.find({},{ "_id": 0, "name": 1, "address": 1 }):
       print(x)
    ## If only want to exclude address field then set address 0
    for x in my_collection.find({},{ "address": 0 }):
      print(x)

       

    

