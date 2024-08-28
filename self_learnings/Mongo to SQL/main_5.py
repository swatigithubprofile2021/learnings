from pymongo import MongoClient
import pyodbc

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['my_mongo_db']
mongo_collection = mongo_db['my_mongo_collection']

# Connect to SQL Server
sql_server = 'my_sql_server'
sql_database = 'my_sql_database'
sql_username = 'my_sql_username'
sql_password = 'my_sql_password'
sql_driver = '{ODBC Driver 17 for SQL Server}'
cnxn_str = f"DRIVER={sql_driver};SERVER={sql_server};DATABASE={sql_database};UID={sql_username};PWD={sql_password}"
cnxn = pyodbc.connect(cnxn_str)

# Define SQL query to insert new records into existing table
sql_query = "INSERT INTO my_sql_table (field_1, field_2, field_3) VALUES (?, ?, ?)"

# Define function to append new data from MongoDB to SQL Server
def append_data():
    cursor = cnxn.cursor()
    for doc in mongo_collection.find():
        # Check if record already exists in SQL table
        existing_record_query = f"SELECT COUNT(*) FROM my_sql_table WHERE field_1='{doc['field_1']}' AND field_2='{doc['field_2']}'"
        cursor.execute(existing_record_query)
        if cursor.fetchone()[0] == 0:
            # Insert new record into SQL table
            cursor.execute(sql_query, (doc['field_1'], doc['field_2'], doc['field_3']))
    cnxn.commit()
    cursor.close()

# Call function to append new data to SQL table
append_data()
