import requests
import json
import pandas as pd
import openpyxl


ENDPOINT = 'https://api.postalpincode.in/pincode/'

PINCODE = 201010

response = requests.get(ENDPOINT + str(PINCODE))
# print(type(response.text))

pincode_info = json.loads(response.text)
# print(type(pincode_info[0]['PostOffice']))



# required_info = pincode_info[0]['PostOffice'][0]

# for key,value in required_info.items():
#     x = f"{key} : {value}"
#     print(x)

df = pd.DataFrame(pincode_info[0]['PostOffice'])
df_temp  = pd.DataFrame(pincode_info[0]['PostOffice'])
pd.concat([df,df_temp])
df.to_excel('My_data_2.xlsx', index=False)
