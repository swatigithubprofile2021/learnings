import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["db"]
collection1 = db["collection1"]
collection2 = db["collection2"]

data1 = [{"name":"swati","address":"vasundhara","designation" : "Data SCientist"},
         {"name":"amit","address":"allahabad","designation":"Property Administrator"}
        ]

data2 = [{"company":"BT","address":"gurugram"},
         {"company":"BSPL","address":"noida"} 
         ]        
db.collection1.insert_many(data1)  
db.collection2.insert_many(data2) 

