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

mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  
mongo_db = mongo_client['anganwadi']

sql_server_connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};' \
                              'SERVER=(localdb)\MSSQLLocalDB;' \
                              'DATABASE=Anganwadi_2;' \
                                # Replace with your SQL Server connection details
sql_server_conn = pyodbc.connect(sql_server_connection_string)
sql_server_cursor = sql_server_conn.cursor()

@app.get('/',tags=["Welcome_to_Mongo_To_SQL"])
def home():
    return "Welcome.....Type /docs in front of URL to get started"

@app.post("/AnganwadiCenter")
async def transfer_data():
    

    # Fetch data from MongoDB
    mongo_collection_1 = mongo_db['AnganwadiCenter']
    mongo_data = list(mongo_collection_1.find())
    
    
    # Loop through MongoDB data and insert into SQL Server
    for doc in mongo_data:
        field1 = str(doc.get('_id', None))  # Replace with your field names
        print("field1----->",field1)
        field2 = doc.get('centerName', None)
        print("field2----->",field2)
        field3 = str(doc.get('uniqueCode', None))
        print("field3----->",field3)

    #     Insert data into SQL Server
        if field3 is not None:
            sql_server_cursor.execute("INSERT INTO Anganwadi_Centers (id, center_name, uniqueCode) VALUES (?,?,?)", field1, field2, field3)
        else:
            sql_server_cursor.execute("INSERT INTO Anganwadi_Centers (id, center_name, uniqueCode) VALUES (?,?,?)", field1, field2, '0000000')

    # Commit and close SQL Server connection
    sql_server_conn.commit()
    sql_server_conn.close()

    return {"message": "Data transfer completed successfully!"}




@app.post("/AnganwadiChildren")
async def transfer_data():
    mongo_collection_2 = mongo_db['AnganwadiChildren']
    mongo_data = list(mongo_collection_2.find())

# print(mongo_data)
# vid = mongo_data[0]["_id"]
# vindex = mongo_data[0]["indexes"]
#Loop through MongoDB data and insert into SQL Server

    for doc in mongo_data:
    # Extract data from MongoDB document
        field1 = str(doc.get('_id', None))  # Replace with your field names
        print("field1----->",field1)

        field2 = doc.get('category', None)
        print("field2----->",field2)

        field3 = str(doc.get('centerId', None))
        print("field3----->",field3)

        field4 = doc.get('childId', None)
        print("field4----->",field4)

        field5 = doc.get('dob', None)
        date_object = datetime.datetime.strptime(field5, '%d-%m-%Y').date()
        field5 = date_object
        print("field5----->",type(field5))

        field6 = doc.get('familyId', None)
        print("field6----->",field6)

        field7 = doc.get('fatherName', None)
        print("field7----->",field7)

        field8 = doc.get('gender', None)
        print("field8----->",field8)

        field9 = doc.get('handicap', None)
        print("field9----->",field9)

        field10 = doc.get('minority', None)
        print("field10----->",field10)

        field11 = doc.get('mobileNumber', None)
        print("field11----->",field11)

        field12 = doc.get('motherName', None)
        print("field12----->",field12)

        field13 = doc.get('profilePic', None)
        print("field13----->",field13)

        field14 = doc.get('name')
        print("field14----->",field14)
   
    
    # if (field12 and field13) is not None:

    #     sql_server_cursor.execute("INSERT INTO Anganwadi_children (id, category_id, center_id, child_id, dob, family_id, father_name, gender_id, handicap_id, is_minority, mobile_no, mother_name, profile_pic) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10,field11,field12,field13)# Replace with your SQL Server table name
     
    # else:
        sql_server_cursor.execute("INSERT INTO Anganwadi_children (id, category_id, center_id,child_id, dob, family_id, father_name, gender_id, handicap_id, is_minority, mobile_no, mother_name, profile_pic, child_name) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14)

    


    sql_server_conn.commit()
    sql_server_conn.close()
    return {"message": "Data transfer completed successfully!"}



@app.post("/Attendance")
async def transfer_data():
    mongo_collection_3 = mongo_db['Attendance']
    mongo_data = list(mongo_collection_3.find())


#Fetch data from MongoDB


# print(mongo_data)
# vid = mongo_data[0]["_id"]
# vindex = mongo_data[0]["indexes"]
#Loop through MongoDB data and insert into SQL Server

    for doc in mongo_data:
    # Extract data from MongoDB document
        field1 = str(doc.get('_id', None))  # Replace with your field names
        print("field1----->",field1)

        field2 = doc.get('centerId', None)
        print("field2----->",field2)
    
        field3 = doc.get('attendance', None)
        print("field3----->",field3)
    
        field4 = doc.get('childId', None)
        print("field4----->",field4)
    
        field5 = str(doc.get('date', None))
        print("field5----->",field5)
        
        # date_object = datetime.datetime.strptime(field5, '%d-%m-%Y').date()
        # field4 = date_object
        field6 = doc.get('gender', None)
        print("field6----->",field6)
    
        field7 = str(doc.get('latitude', None))
        print("field7----->",field7)
    
        field8 = str(doc.get('longitude', None))
        print("field8----->",field8)
        
        field9 = doc.get('photo', None)
        print("field9----->",field9)
        
        field10 = doc.get('name', None)
        print("field10----->",field10)
        
       
        if field10 is not None:

            sql_server_cursor.execute("INSERT INTO Attendance (id, center_id, attendance, child_id, attendance_date, gender_id, lattitude, longitude, photo_url, child_name ) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10)
        else:
            sql_server_cursor.execute("INSERT INTO Attendance (id, center_id, attendance, child_id, attendance_date, gender_id, lattitude, longitude, photo_url, child_name ) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,'Not found')

    
# Commit and close SQL Server connection
    sql_server_conn.commit()
    sql_server_conn.close()
    return {"message": "Data transfer completed successfully!"}


@app.post("/BabiesBirth")
async def transfer_data():
    mongo_collection_4 = mongo_db['BabiesBirth']
    mongo_data = list(mongo_collection_4.find())
    
    for doc in mongo_data:
    # Extract data from MongoDB document
        field1 = str(doc.get('_id', None))  # Replace with your field names
        print("field1----->",field1)
    
        field2 = doc.get('centerId', None)
        print("field2----->",field2)
    
        field3 = doc.get('familyId', None)
        print("field3----->",field3)
    
        field4 = doc.get('birthPlace', None)
        print("field4----->",field4)
    
        field5 = str(doc.get('birthType', None))
        print("field5----->",field5)
        
        # date_object = datetime.datetime.strptime(field5, '%d-%m-%Y').date()
        # field4 = date_object
        field6 = doc.get('firstWeight', None)
        print("field6----->",field6)
    
        field7 = str(doc.get('gender', None))
        print("field7----->",field7)
    
        field8 = str(doc.get('height', None))
        print("field8----->",field8)
        
        field9 = doc.get('motherMemberId', None)
        print("field9----->",field9)
        
        field10 = doc.get('name', None)
        print("field10----->",field10)
    
    

        sql_server_cursor.execute("INSERT INTO BabiesBirth (id, center_id, family_id, birth_place, birth_type_id, first_weight, gender_id, height, mother_member_id, child_name) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10)


# Commit and close SQL Server connection
    sql_server_conn.commit()
    sql_server_conn.close()
    return {"message": "Data transfer completed successfully!"}


@app.post("/Family")
async def transfer_data():
    mongo_collection_5 = mongo_db['Family']
    mongo_data = list(mongo_collection_5.find())



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

@app.post("/FamilyMember")
async def transfer_data():
    mongo_collection_6 = mongo_db['FamilyMember']
    mongo_data = list(mongo_collection_6.find())
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

