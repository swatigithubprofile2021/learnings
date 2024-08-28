import pymongo
import pyodbc
import pandas as pd
import bson
from bson import ObjectId
import datetime
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Connect to MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
mongo_db = mongo_client['anganwadi']  # Replace with your MongoDB database name
mongo_collection = mongo_db['Family']  # Replace with your MongoDB collection name
# bson_file = open(r'   .bson', 'rb')
# b = bson.loads(bson_file)
# print(b)

# import bson
# with open("anganwadi/WeightTracking.bson", "rb") as bson_file:
#     bson_data = bson.decode_all(bson_file.read())
# mongo_db["WeightTracking"].insert_many(pd.DataFrame(bson_data).to_dict('record'))

#Connect to SQL Server
sql_server_connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};' \
                              'SERVER=(localdb)\MSSQLLocalDB;' \
                              'DATABASE=Anganwadi_tables;' \
                                # Replace with your SQL Server connection details
sql_server_conn = pyodbc.connect(sql_server_connection_string)
sql_server_cursor = sql_server_conn.cursor()



@app.get('/',tags=["Welcome_to_Mongo_To_SQL"])
def home():
    return "Welcome.....Type /docs in front of URL to get started"

@app.post("/transfer_data")
async def transfer_data():
    mongo_data = list(mongo_collection.find())



# print(mongo_data)
# vid = mongo_data[0]["_id"]
# vindex = mongo_data[0]["indexes"]
#Loop through MongoDB data and insert into SQL Server

    for doc in mongo_data:
    # Extract data from MongoDB document
        field1 = str(doc.get('_id', None)) # Replace with your field names
        print("field1----->",field1)

        field2 = doc.get('category', None)
        print("field2----->",field2)

        field3 = doc.get('centerId', None)
        print("field3----->",field3)

        field4 = doc.get('familyId', None)
        print("field4----->",field4)

        field5 = str(doc.get('houseNo', None))
        print("field5----->",field5)
    
    # date_object = datetime.datetime.strptime(field5, '%d-%m-%Y').date()
    # field4 = date_object
        field6 = doc.get('icdsService', None)
        print("field6----->",field6)

        field7 = str(doc.get('isMinority', None))
        print("field7----->",field7)

        field8 = str(doc.get('religion', None))
        print("field8----->",field8)

        field9 = str(doc.get('uniqueIdType', None))
        print("field9----->",field9)
    
        field10 = str(doc.get('uniqueId', None))
        print("field10----->",field10)
    
    

        sql_server_cursor.execute("INSERT INTO Family (id, category_id, center_id, family_id, house_no, icds_service_id, is_minority, relgion_id, unique_id_type, unique_id_details) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10)

    

# Commit and close SQL Server connection
    sql_server_conn.commit()
    sql_server_conn.close()
    return {"message": "Data transfer completed successfully!"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

