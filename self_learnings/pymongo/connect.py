


import pymongo


if __name__ =="__main__":
    print("Welcome to PyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['my_first_database']
    # # collection = db['mySamplecollectionforswati']
    # # dictionary = {'Name':'Swati','Marks':100}
    # # collection.insert_one(dictionary)
    