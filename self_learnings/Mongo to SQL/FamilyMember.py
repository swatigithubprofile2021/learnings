import pymongo
import pyodbc
import pandas as pd
import bson
from bson import ObjectId
import datetime
import numpy as np
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
                              'SERVER=10.18.11.25;' \
                              'DATABASE=Anganwadi_tables;' \
                              'UID=sa;' \
                              'PWD=Bharu@123456$#$'  # Replace with your SQL Server connection details
sql_server_conn = pyodbc.connect(sql_server_connection_string)
sql_server_cursor = sql_server_conn.cursor()

#Create a dictionary to store primary key and foreign key mappings
# key_mapping = {}

#Fetch data from MongoDB
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


    field4 = doc.get('dob', None)
    print("field4----->",field4)

    
    field5 = doc.get('fatherName', None)
    if len(str(field5))<3:
       field5 = 'Not found'
    else:
       field5 = str(doc.get('fatherName', None))
    print("field5----->",field5)
    
    field6 = int(doc.get('gender', None))
    print("field6----->",field6)

    
    field7 = str(doc.get('idType', None))
    if len(str(field7))!=1:
       field7 = 'Not Available'
    else:
       field7 = str(doc.get('idType', None))
    print("field7----->",field7)

    field8 = doc.get('maritalStatus', None)
    if len(str(field8))!=1:
       field8 = 0
    else:
       field8 = int(doc.get('maritalStatus', None))
    print("field8----->",field8)

    field9 = str(doc.get('beneficiary_id', None))
    field9 = "NUll"
    print("field9----->",field9)
    field10 = str(doc.get('mobileNumber', None))
    print("field10----->",field10)
    field11 = str(doc.get('motherName', None))
    print("field11----->",field11)
    field12 = str(doc.get('name', None))
    print("field12----->",field12)
    field13 = str(doc.get('photo', None))
    if len(str(field13))<5:
       field13 = 'Not available'
    else:
       field13 = str(doc.get('photo', None))
    print("field13----->",field13)

    field14 = int(doc.get('recordForMonth', None))
    print("field14----->",field14)

    field15 = doc.get('relationWithOwner', None)
    if len(str(field15))!=1:
       field15 = -1
    else:
       field15 = int(doc.get('relationWithOwner', None))
    print("field15----->",field15)

    
    field16 = str(doc.get('familyId', None))
    print("field16----->",field16)
    
    field17 = str(doc.get('residentArea', None))
    if len(str(field17))!=1:
       field17 = 'Not Available'
    else:
       field17 = str(doc.get('residentArea', None))
    print("field17----->",field17)


    field18 = str(doc.get('idNumber', None))
    if len(str(field18))<5:
       field18 = 'Not Available'
    else:
       field18 = str(doc.get('idNumber', None))
    print("field18----->",field18)

    field19 = doc.get('handicap', None)
    if len(str(field19))!=1:
       field19 = 0
    else:
       field19 = int(doc.get('handicap', None))
    print("field19----->",field19)
     
    field20 = doc.get('dateOfArrival', None)
    if len(str(field20))<2:
       field20 = "Not Available"
    else:
       field20 = str(field20)
    print("field20----->",field20)


    field21 = doc.get('dateOfLeaving', None)
    if len(str(field21))<2:
       field21 = "Not Available"
    else:
        field21 = str(field21)
    print("field21----->",field21)
    
    
    field22 = doc.get('dateOfMortality', None)
    if len(str(field22))<2:
       field22 = "Not Available"
    else:
       field22 = str(field22)
    print("field22----->",field22)
    print("-----------------")
    print("index----->",ix)
    print("-----------------")
    # field7 = doc.get('motherName', None)
    # print("field7----->",field7)
    # field8 = doc.get('profilePic', None)
    # print("field8----->",field8)



    # field4 = doc.get('village_id', None)
    # print(field4)

    #Insert_query = '''INSERT INTO Anganwadi_Centers(id, center_name, uniqueCode,) VALUES (?, ?, ?);'''


    
    # Insert data into SQL Server
    # sql_server_cursor.execute("INSERT INTO Anganwadi_Centers (id, category_id, center_id, family_id, house_no, icds_service_id, is_minority, relgion_id, unique_id_type, unique_id_details) "
    #                           "VALUES (?, ?, ?, ?)", field1, field2, field3, field4)  # Replace with your SQL Server table name
    
    
    # if field6 is not None:

    #     sql_server_cursor.execute("INSERT INTO Attendance (id, center_id, family_id, birth_place, birth_type_id, first_weight, gender_id, height, mother_member_id, child_name) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field4,field5,field5,field6)
    # else:
    # sql_server_cursor.execute("INSERT INTO FamilyMembers (id, category_id, center_id,father_name,gender_id, member_name, record_for_month,handicap_id) VALUES (?,?,?,?,?,?,?,?)",field1,field2,field3,field5,field6,field12,field14,field19)
    sql_server_cursor.execute("INSERT INTO FamilyMembers (id, category_id, center_id, dob, father_name, gender_id, unique_id_number, marital_status ,beneficiary_id,mobile_no, mother_name, member_name, photo_url, record_for_month, relation_with_owner_id, family_id, resident_area, unique_id, handicap_id, date_of_arrival, date_of_leaving, date_of_mortality) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", field1,field2,field3,field4,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18,field19,field20,field21,field22)

    # sql_server_cursor.execute("SELECT @@IDENTITY AS id")  # Replace with your primary key column name
    # row = sql_server_cursor.fetchone()
    # primary_key = row.id
    
    # # Store the primary key mapping for future reference
    # key_mapping[doc['_id']] = primary_key  # Assuming '_id' is the primary key in MongoDB
    
    # # Insert foreign key data into related table in SQL Server
    # # Replace the following lines with your foreign key table and column names
    # # and update the 'foreign_key_value' variable with the appropriate value from the MongoDB document
    # foreign_key_table_name = 'Anganwadi_Centers'
    # foreign_key_column_name = 'village_id'
    # foreign_key_value = doc.get('village_id', None)  # Replace with your field name
    # if foreign_key_value is not None:
    #     sql_server_cursor.execute("INSERT INTO {} ({}, {}) "
    #                               "VALUES (?, ?)".format(foreign_key_table_name, foreign_key_column_name, 'village_id'),
    #                               primary_key, foreign_key_value)  # Replace with your value column name


# Commit and close SQL Server connection
sql_server_conn.commit()
sql_server_conn.close()

print("Data transfer completed successfully!")
