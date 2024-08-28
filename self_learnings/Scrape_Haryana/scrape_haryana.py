from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import os
os.system("cls")
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import warnings
warnings.filterwarnings('ignore')

url = "http://www.postalpincode.in/Search-By-Location?StateId=13"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-webgl")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(r"chromedriver.exe",options=options)

driver.get(url)

driver.maximize_window()

Haryana_district_details = []


while True:   

    

    soup = BeautifulSoup(driver.page_source,'html.parser')


    options = soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlState"}).findAll("option")

    # print(options)

     ## For appending details

    for i in options:
    
        state_value = i.text

        if state_value == 'HARYANA':



            district_list = soup.find('table',class_='DDGridView')

            for i in district_list.find_all('a',href=True):
                link = "http://www.postalpincode.in/"+i.get('href')
                # print(link)

                next_url = requests.get(link)
                next_url_Content = next_url.content
                district_soup = BeautifulSoup(next_url_Content,'html.parser')

                district_details = district_soup.find_all('table',id='ContentPlaceHolder1_fvBranchDetails')
                # print(district_details)
                for i in district_details:
                    table_column = i.find_all('label')
                    for j in table_column:
                        final_detail = j.string
                        
                        Haryana_district_details.append(final_detail)

    try:
        next_button = driver.find_element("xpath","//input[@id='ContentPlaceHolder1_gvBranch_GridViewPaging_imgBtnNext']")

        next_button.click()

        print("next_page clicked" )

        # time.sleep(3)
    except WebDriverException as e:    
        print(e)
        # driver.get(url)
        break

    print("lenth of Haryana_district_detail",len(Haryana_district_details))                    

    if len(Haryana_district_details) == 48402:
        print("in if condition")
        break


driver.close()

    ##### Creating Data Frame  
df = pd.DataFrame({'Post_Office': Haryana_district_details[1::18],
                  'Post_Office_Type': Haryana_district_details[3::18],
                  'Tehsil': Haryana_district_details[5::18],
                  'District' : Haryana_district_details[7::18],
                  'State' : Haryana_district_details[9::18],
                  'Division':Haryana_district_details[11::18],
                  'Delivery_Status' : Haryana_district_details[13::18],
                  'Pin_Code':Haryana_district_details[15::18],
                  'Address':Haryana_district_details[17::18]})
# print(df)


## Converting into excel sheet

df.to_excel('Haryana_Details.xlsx')

               



      
















