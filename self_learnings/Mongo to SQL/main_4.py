import pymongo
import pyodbc

# Connect to MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')  # Replace with your MongoDB connection string
mongo_db = mongo_client['anganwadi']  # Replace with your MongoDB database name
mongo_collection = mongo_db['AnganwadiCenter']  # Replace with your MongoDB collection name

# Connect to SQL Server
sql_server_connection_string = 'DRIVER={SQL Server};' \
                              'SERVER=10.18.11.25;' \
                              'DATABASE=Angandwadi_New;' \
                              'UID=sa;' \
                              'PWD=Bharu@123456$#$'  # Replace with your SQL Server connection details
sql_server_conn = pyodbc.connect(sql_server_connection_string)
sql_server_cursor = sql_server_conn.cursor()

# Get MongoDB collection fields and their data types
mongo_collection_fields = mongo_collection.find_one()
field_data_types = {field: type(value).__name__ for field, value in mongo_collection_fields.items()}

# Create SQL Server table with fields as columns
table_name = 'Anganwadi_Center'  # Replace with your desired SQL Server table name
sql_server_cursor.execute(f"CREATE TABLE {table_name} ("
                          f"id INT PRIMARY KEY IDENTITY(1,1),")  # Assuming an IDENTITY column as the primary key

# Add columns to SQL Server table
for field, data_type in field_data_types.items():
    # Map MongoDB field data types to SQL Server data types
    if data_type == 'str':
        sql_data_type = 'VARCHAR(MAX)'
    elif data_type == 'int':
        sql_data_type = 'INT'
    elif data_type == 'float':
        sql_data_type = 'FLOAT'
    elif data_type == 'bool':
        sql_data_type = 'BIT'
    else:
        sql_data_type = 'VARCHAR(MAX)'  # Default to VARCHAR(MAX) if data type is not recognized

    sql_server_cursor.execute(f"ALTER TABLE {table_name} "
                              f"ADD {field} {sql_data_type}")

# Fetch data from MongoDB collection
mongo_data = mongo_collection.find()
print(mongo_data)

# Insert data into SQL Server table
for doc in mongo_data:
    # Insert data into SQL Server table
    values = [doc[field] for field in field_data_types.keys()]
    sql_server_cursor.execute(f"INSERT INTO {table_name} ({','.join(field_data_types.keys())}) "
                              f"VALUES ({','.join(['?'] * len(field_data_types.keys()))})", *values)
    sql_server_conn.commit()  # Commit after every document insertion to improve performance

print("Data transfer completed successfully from MongoDB to SQL Server!")

# Close SQL Server connection
sql_server_conn.close()
