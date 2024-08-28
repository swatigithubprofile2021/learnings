import pymongo
import pyodbc
import pandas as pd
import bson
from bson import ObjectId
import datetime
# Connect to MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
mongo_db = mongo_client['anganwadi']  # Replace with your MongoDB database name
mongo_collection = mongo_db['BabiesBirth']  # Replace with your MongoDB collection name
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
    
    
    # field11 = doc.get('mobileNumber', None)
    # print("field11----->",field11)
    # field12 = doc.get('motherName', None)
    # print("field12----->",field12)
    # field13 = doc.get('profilePic', None)
    # print("field13----->",field13)



    # field4 = doc.get('village_id', None)
    # print(field4)

    #Insert_query = '''INSERT INTO Anganwadi_Centers(id, center_name, uniqueCode,) VALUES (?, ?, ?);'''


    
    # Insert data into SQL Server
    # sql_server_cursor.execute("INSERT INTO Anganwadi_Centers (id, category_id, center_id, family_id, house_no, icds_service_id, is_minority, relgion_id, unique_id_type, unique_id_details) "
    #                           "VALUES (?, ?, ?, ?)", field1, field2, field3, field4)  # Replace with your SQL Server table name
    
    
    # if field10 is not None:

    #     sql_server_cursor.execute("INSERT INTO Attendance (id, center_id, family_id, birth_place, birth_type_id, first_weight, gender_id, height, mother_member_id, child_name) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10)
    # else:
    sql_server_cursor.execute("INSERT INTO BabiesBirth (id, center_id, family_id, birth_place, birth_type_id, first_weight, gender_id, height, mother_member_id, child_name) VALUES (?,?,?,?,?,?,?,?,?,?)",  field1,field2,field3,field4,field5,field6,field7,field8,field9,field10)

    

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
