import pymongo


if __name__ =="__main__":
    print("Welcome to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    mydb = client['my_first_database']
    my_collection = mydb["Customers"]

    ## Insert one document
    # mydict = { "name": "swati", "address": "vasundhara" }
    # x = my_collection.insert_one(mydict)

    ## Insert many document at once
    mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
  ]

    x = my_collection.insert_many(mylist)
    print(x)




