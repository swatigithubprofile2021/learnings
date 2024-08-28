## Importing necessary libraries

import pandas as pd
import requests
import json

# Reading csv file
# df = pd.read_csv("SD.csv")
#df = pd.read_csv("Sheet2_1001_2158.csv")
# df = pd.read_csv("SD_Lat_Lan.csv")
# df = pd.read_csv("Wrong _Address_validation.csv")
df = pd.read_csv("Mangalam_Distributors.csv")

pd.set_option('display.max_rows', None)


for i, row in df.iterrows():
    # apiAddress = str(df.at[i,'DB Name'])+','+str(df.at[i,'DB Address'])+','+str(df.at[i,'DB District/City'])+','+str(df.at[i,'DB Pincode'])+','+str(df.at[i,'DB STATE'])
    # apiAddress = str(df.at[i,'First_Name'])+','+str(df.at[i,'Store_Address'])+','+str(df.at[i,'Store_City'])+','+str(df.at[i,'Store_State'])+str(df.at[i,'Store_pin_code'])
     # apiAddress = str(df.at[i,'SD_Name'])+','+str(df.at[i,'Village'])+','+str(df.at[i,'Tehsil'])+','+str(df.at[i,'Pin_Code'])+','+str(df.at[i,'District_Name'])+','+str(df.at[i,'State'])
    apiAddress = str(df.at[i,'TEHSIL'])+','+str(df.at[i,'DISTRICT'])+','+str(df.at[i,'PIN CODE'])
 


    parameters = {
        "key": "DKZwCjv4ztt8JmSgxjA1ZVmQBjiKSoI9",
        #"location": "3/119,VIKAS NAGAR, LUCKNOW,BARABANKI,225305,UTTAR PRADESH"
        # "location" : "NEAR SANT NIRANKARI SATSANG BHAWAN,ZIRAKPUR,140603,PUNJAB"
        "location": apiAddress


    }

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    print("response---->", response)
    data = response.text
    dataJ = json.loads(data)['results']
    lat = (dataJ[0]['locations'][0]['latLng']['lat'])
    print("lattitude -------->",lat)
    lng = (dataJ[0]['locations'][0]['latLng']['lng'])
    print("longitude-------->",lng)

    df.at[i,'SD_latitude'] = lat
    # df.at[i,'Store_Latitude'] = lat

    df.at[i,'SD_longitude'] = lng
    # df.at[i,'Store_Longitude'] = lng
    
        
    df.to_csv('Mangalam_Distributors.csv')
# df1 = pd.read_csv('DB_lat_long2.csv')
# df1.head()


# parameters = {
#         "key": "Y0kld1uS8LKKo18P3ZiLEqHFTRbCBIqw",
#         #"location": "3/119,VIKAS NAGAR, LUCKNOW,BARABANKI,225305,UTTAR PRADESH"
#         # "location" : "NEAR SANT NIRANKARI SATSANG BHAWAN,ZIRAKPUR,140603,PUNJAB"
#         # "location": "363, MAIN ROAD, FATEHPUR BERI , MEHSANA,110074,NEW DELHI"
#         "location" : "ASHARAM PRAHLADRAI,NEAR SUBHASH CHOWK,RAIGARH,496001,Chhattisgarh"}


# #      }

# response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
# print("response---->", response)
# data = response.text
# dataJ = json.loads(data)['results']
# lat = (dataJ[0]['locations'][0]['latLng']['lat'])
# print("lattitude -------->",lat)
# lng = (dataJ[0]['locations'][0]['latLng']['lng'])
# print("longitude-------->",lng)








