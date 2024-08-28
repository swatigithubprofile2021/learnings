import pymongo


if __name__ == '__main__':

    client = pymongo.MongoClient("mongodb://localhost:27017")
    mydatabase = client['Students']  
    collection = mydatabase['studentscores']

    data = [
        {"user":"Swati", "subject":"Database", "score":80}, 
        {"user":"Amit",  "subject":"JavaScript", "score":90}, 
        {"user":"Amit",  "title":"Database", "score":85}, 
        {"user":"Swati",  "title":"JavaScript", "score":75}, 
        {"user":"Amit",  "title":"Data Science", "score":60},
        {"user":"Swati",  "title":"Data Science", "score":95}] 

    #collection.insert_many(data)    

    ## Find total subjects per student
    # agg_result =collection.aggregate([{"$group":{"_id":"$user","Total_subject":{"$sum":1}}}])
    # for i in agg_result:
    #     print(i)
    # my_query = {"user":{}}    

    ## For deleting duplicates

    duplicate = collection.aggregate([{"$group":{
        "_id" :{"title":"$title"}, ## Checking unique ids
        "idsUnicos": {'$addToSet': '$_id'},

        "total" : {"$sum":1}  ## counting occurence of each user id
    }
    },
    {"$match":{"total":{"$gt":1}}}
    ])


    for i in duplicate:
        for j,k in enumerate(i['idsUnicos']):
            if j !=0:
                collection.delete_one({"_id":k})


    ## finding distinct user
    # cursor =  collection.find({}).distinct("user")
    # for i in cursor:
    #     print(i)

    
    #print("deleted")


  


         
