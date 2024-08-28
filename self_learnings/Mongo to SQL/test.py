import pymongo
import pyodbc

# Connect to MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
mongo_db = mongo_client['anganwadi']  # Replace with your MongoDB database name

# Connect to SQL Server
sql_server_connection_string = 'DRIVER={SQL Server};' \
                              'SERVER=your_sql_server_name;' \
                              'DATABASE=your_sql_server_database_name;' \
                              'UID=your_sql_server_username;' \
                              'PWD=your_sql_server_password'  # Replace with your SQL Server connection details
sql_server_conn = pyodbc.connect(sql_server_connection_string)
sql_server_cursor = sql_server_conn.cursor()

# Loop through MongoDB collections and transfer data to SQL Server
for collection_name in mongo_db.list_collection_names():
    # Fetch data from MongoDB collection
    mongo_collection = mongo_db[collection_name]
    mongo_data = mongo_collection.find()

    # Loop through MongoDB data and insert into SQL Server
    for doc in mongo_data:
        # Extract data from MongoDB document
        # Replace the following lines with your field names
        field1 = doc.get('field1', None)
        field2 = doc.get('field2', None)
        field3 = doc.get('field3', None)
        
        # Insert data into SQL Server
        sql_server_cursor.execute("INSERT INTO {} (field1, field2, field3) "
                                  "VALUES (?, ?, ?)".format(collection_name), field1, field2, field3)
        # Commit after every document insertion to improve performance
        sql_server_conn.commit()

print("Data transfer completed successfully from MongoDB to SQL Server!")

# Close SQL Server connection
sql_server_conn.close()
