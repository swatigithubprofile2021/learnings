import pymongo
import pyodbc
import json
import os



# Connect to MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
mongo_db = mongo_client['anganwadi']  # Replace with your MongoDB database name
mongo_collection = mongo_db['WeightTracking']  # Replace with your MongoDB collection name

# for i in os.listdir(r'anganwadi'):

#     if i.endswith('json'):

#         file_name = open(i)
#         print(file_name)

with open (r'anganwadi/WeightTracking.metadata.json') as file:


           file_data = json.load(file)

if isinstance(file_data, list):
    mongo_collection.insert_many(file_data) 
else:
    mongo_collection.insert_one(file_data)
    




# # Connect to SQL Server
# sql_server_connection_string = 'DRIVER={SQL Server};' \
#                               'SERVER=your_sql_server_name;' \
#                               'DATABASE=your_sql_server_database_name;' \
#                               'UID=your_sql_server_username;' \
#                               'PWD=your_sql_server_password'  # Replace with your SQL Server connection details
# sql_server_conn = pyodbc.connect(sql_server_connection_string)
# sql_server_cursor = sql_server_conn.cursor()

# # Fetch data from MongoDB
# mongo_data = mongo_collection.find()

# # Loop through MongoDB data and insert into SQL Server
# for doc in mongo_data:
#     # Extract data from MongoDB document
#     field1 = doc.get('field1', None)  # Replace with your field names
#     field2 = doc.get('field2', None)
#     field3 = doc.get('field3', None)
    
#     # Insert data into SQL Server
#     sql_server_cursor.execute("INSERT INTO your_sql_server_table_name (field1, field2, field3) "
#                               "VALUES (?, ?, ?)", field1, field2, field3)  # Replace with your SQL Server table name

# # Commit and close SQL Server connection
# sql_server_conn.commit()
# sql_server_conn.close()

# print("Data transfer completed successfully!")
