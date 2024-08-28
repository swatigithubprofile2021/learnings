import pymongo
import pyodbc
import pandas as pd
import bson
from bson import ObjectId
import datetime
import numpy as np
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Connect to MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
mongo_db = mongo_client['anganwadi']  # Replace with your MongoDB database name
mongo_collection = mongo_db['FamilyMember']  # Replace with your MongoDB collection name
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

#Create a dictionary to store primary key and foreign key mappings
# key_mapping = {}

#Fetch data from MongoDB
@app.get('/',tags=["Welcome_to_Mongo_To_SQL"])
def home():
    return "Welcome.....Type /docs in front of URL to get started"

@app.post("/transfer_data")
async def transfer_data():
    mongo_data = list(mongo_collection.find())
    mongo_data = pd.DataFrame(mongo_data).fillna(pd.NA).to_dict('record')



# mongo_data = mongo_data[950:]
# print(mongo_data)
# vid = mongo_data[0]["_id"]
# vindex = mongo_data[0]["indexes"]
#Loop through MongoDB data and insert into SQL Server
# mongo_data = pd.DataFrame(list(mongo_collection.find()))

# mongo_data['dateOfArrival'] = mongo_data['dateOfArrival'].astype(np.datetime64())
# mongo_data['dateOfLeaving'] = mongo_data['dateOfLeaving'].astype(np.datetime64())

    for ix,doc in enumerate(mongo_data):
    # Extract data from MongoDB document
        field1 = str(doc.get('_id', None)) # Replace with your field names
        print("field1----->",field1)
    
        field2 = int(doc.get('category', None))
        print("field2----->",field2)
    
        field3 = str(doc.get('centerId', None))
        print("field3----->",field3)
    
        field4 = doc.get('dateOfArrival', None)
        if len(str(field4))<2:
           field4 = "Not Found"
        else:
           field4 = str(field4)
        print("field4----->",field4)

        field5 = doc.get('dateOfLeaving', None)
        if len(str(field5))<2:
           field5 = "Not Found"
        else:
            field5 = str(field5)
        print("field5----->",field5)
        
        field6 = doc.get('dateOfMortality', None)
        if len(str(field6))<2:
           field6 = "Not Found"
        else:
           field6 = str(field6)
        print("field6----->",field6)
        
        field7 = doc.get('dob', None)
        print("field7----->",field7)
    

        field8 = str(doc.get('familyId', None))
        print("field8----->",field8)

        field9 = doc.get('fatherName', None)
        if len(str(field9))<3:
           field9 = 'Not found'
        else:
           field9 = str(doc.get('fatherName', None))
        print("field9----->",field9)
        
        field10 = int(doc.get('gender', None))
        print("field10----->",field10)

        field11 = doc.get('handicap', None)
        if len(str(field11))!=1:
           field11 = 0
        else:
           field11 = int(doc.get('handicap', None))
        print("field11----->",field11)
    
        field12 = str(doc.get('idNumber', None))
        if len(str(field12))<5:
           field12 = 'Not Found'
        else:
           field12 = str(doc.get('idNumber', None))
        print("field12----->",field12)

        field13 = str(doc.get('idType', None))
        if len(str(field13))!=1:
           field13 = 'Not Found'
        else:
           field13 = str(doc.get('idType', None))
        print("field13----->",field13)
    
    
        field14 = doc.get('maritalStatus', None)
        if len(str(field14))!=1:
           field14 = 0
        else:
           field14 = int(doc.get('maritalStatus', None))
        print("field14----->",field14)
    
        field15 = str(doc.get('beneficiary_id', None))
        field15 = "Not Found"
        print("field15----->",field15)

        field16 = str(doc.get('mobileNumber', None))
        print("field16----->",field16)

        field17 = str(doc.get('motherName', None))
        print("field17----->",field17)

        field18 = str(doc.get('name', None))
        print("field18----->",field18)

        field19 = str(doc.get('photo', None))
        if len(str(field19))<5:
           field19 = 'Not Found'
        else:
           field19 = str(doc.get('photo', None))
        print("field19----->",field19)
    
        field20 = int(doc.get('recordForMonth', None))
        print("field20----->",field20)
    
        field21 = doc.get('relationWithOwner', None)
        if len(str(field21))!=1:
           field21 = -1
        else:
           field21 = int(doc.get('relationWithOwner', None))
        print("field21----->",field21)
    
        
        
        field22 = str(doc.get('residentArea', None))
        if len(str(field22))!=1:
           field22 = 'Not Found'
        else:
           field22 = str(doc.get('residentArea', None))
        print("field22----->",field22)
    
    
         
        print("-----------------")
        print("index----->",ix)
        print("-----------------")
      
        sql_server_cursor.execute("INSERT INTO FamilyMembers (id, category_id, center_id, date_of_arrival, date_of_leaving, date_of_mortality, dob, family_id, father_name, gender_id, handicap_id, unique_id_number, unique_id, marital_status, beneficiary_id, mobile_no, mother_name, member_name, photo_url, record_for_month, relation_with_owner_id,  resident_area_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", field1,field2,field3,field4,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18,field19,field20,field21,field22)



# Commit and close SQL Server connection
    sql_server_conn.commit()
    sql_server_conn.close()
    return {"message": "Data transfer completed successfully!"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



