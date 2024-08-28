import pymongo
import pandas as pd
import numpy as np
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
database1 = client['database1']
# data = database1.food_inventory.find()
# for i in data:
#     print(i)

data  = database1.food_inventory.find()
first_datalist = list(data)
#print(first_datalist)
df1 = pd.DataFrame(first_datalist)
#print(df1)

second_datalist = list(database1.orders.find())
#print(second_datalist)
df2 = pd.DataFrame(second_datalist)
#print(df2)

## Merging two dataframes

final_df = df1.merge(df2,left_on= 'sku',right_on='item',how='left')
#print(final_df)

## Again converting it into a dictionary
records = json.loads(final_df.to_json(orient='records'))
#print(list(data_dict.items()))

# final_data = list(data_dict.items())

joined_collection = database1["joined_collection"] 
database1.joined_collection.insert_many(final_df.to_dict('records'))


