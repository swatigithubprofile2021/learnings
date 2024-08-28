import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["test_database"]
    inventory = db["inventory"]


#     db.inventory.insert_many([{
#             "item": "canvas",
#             "qty": 100,
#             "size": {"h": 28, "w": 35.5, "uom": "cm"},
#             "status": "A",
#         },
# {
#             "item": "mat",
#             "qty": 85,
#             "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
#             "status": "A",
#         },

#         {
#             "item": "mousepad",
#             "qty": 25,
#             "size": {"h": 19, "w": 22.85, "uom": "cm"},
#             "status": "P",
#         },

#         {
#             "item": "sketchbook",
#             "qty": 80,
#             "size": {"h": 14, "w": 21, "uom": "cm"},
#             "status": "A",
#         },
        
#         {
#             "item": "sketch pad",
#             "qty": 95,
#             "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
#             "status": "A",
#         }
#         ])


## For updating  one data
    # db.inventory.update_one(
    #     {"item":"paper"},
    #     {"$set":{"size.ucom":"cm","status":"P"},
    #     "$currentDate":{"lastmodified":True}
    #     })


    ## For updating multiple data
    # db.inventory.update_many(
        
    #     {"qty":{"$lt":50}},
    #     {"$set":{"size.ucom":"in","status":"P"},
    #     "$currentDate":{"lastmodified":True}
    #     }
    #     )
    ## For replacing

    db.inventory.replace_one(
        {"item":"paper"},
        {
            "item":"paper",
            "instock":[{"warehouse":"A","qty":60},{"warehouse":"B","qty":40}]

        }
        )

