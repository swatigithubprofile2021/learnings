import pandas as pd
import requests
import json
import numpy as np


#df = pd.read_csv("DB_Sheet1_lat_long2.csv")
#df = pd.read_csv("SD_Lat_Lan.csv")
# df = pd.read_csv("Wrong _Address_validation_lat_long.csv")
df = pd.read_csv("CLEANED_B&C_UPDATED_lat_long.csv")

pd.set_option('display.max_rows', None)

for i, row in df.iterrows():
    apiAddress = str(df.at[i,'DB_Latitude'])+','+str(df.at[i,'DB_Longitude'])
    
    parameters = {
        "key": "Y0kld1uS8LKKo18P3ZiLEqHFTRbCBIqw",
        #"location": "3/119,VIKAS NAGAR, LUCKNOW,BARABANKI,225305,UTTAR PRADESH"
        # "location" : "NEAR SANT NIRANKARI SATSANG BHAWAN,ZIRAKPUR,140603,PUNJAB"
        "location": apiAddress}
    

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse", params=parameters)
    print("response---->", response)
    data = response.text
    # print(data)

    dataJ = json.loads(data)['results']
    # print(dataJ)
    postalCode = (dataJ[0]['locations'][0]['postalCode'])
    print("postalCode -------->",postalCode)
    df.at[i,'check_pincode'] = postalCode
        
    df.to_csv('CLEANED_B&C_UPDATED_lat_long.csv')
# df = pd.read_csv('DB_lat_long3.csv') 

for i, row in df.iterrows():
    # print(row)
    df.at[i,"Remarks"] = np.where(df.at[i,"DB Pincode"] == df.at[i,"check_pincode"],"Correct","Need to Check")
# df["Remarks"] = np.where((df["DB Pincode"]) == (df["check_pincode"]),"Correct","Need to Check")
    df.to_csv('CLEANED_B&C_UPDATED_lat_long.csv')    

# df['New_Remarks'] = df.apply(lambda x: x['Pincode matching with lat/long'] if x['DB Pincode'] == x['check_pincode'] else "need to check", axis=1)

# df.to_csv('DB_lat_long3_remarks.csv')

# df.head()




# print(df.head())        








# parameters = {
#         "key": "AlrdUHC2oGQexZigGIiqnvokUWGY8MFr",
#         #"location": "3/119,VIKAS NAGAR, LUCKNOW,BARABANKI,225305,UTTAR PRADESH"
#         # "location" : "NEAR SANT NIRANKARI SATSANG BHAWAN,ZIRAKPUR,140603,PUNJAB"
#         # "location": "363, MAIN ROAD, FATEHPUR BERI , MEHSANA,110074,NEW DELHI"
#         "location" : "28.09692,75.8363"}


# #      }

# response = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse", params=parameters)
# print("response---->", response)
# data = response.text
# print(data)

# dataJ = json.loads(data)['results']
# print(dataJ)
# postalCode = (dataJ[0]['locations'][0]['postalCode'])
# print("postalCode -------->",postalCode)



