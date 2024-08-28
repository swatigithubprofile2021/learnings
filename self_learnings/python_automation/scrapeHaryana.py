

#importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#creating empty lists
district_list = []
branch_list = []
pin_list = []
state_list = []

#url of the website
url = "http://www.postalpincode.in/Search-By-Location"

#sending request to the website
response = requests.get(url)

#parsing the response
soup = BeautifulSoup(response.text, 'html.parser')

#extracting the district list
districts = soup.find_all('a', class_="district")

#looping through the districts
for district in districts:
    #storing the district name
    district_name = district.text
    district_list.append(district_name)
    print(district_list)
    
    #storing the district url
    district_url = url + district['href']
    
    #sending request to the district page
    district_response = requests.get(district_url)
    
    #parsing the response
    district_soup = BeautifulSoup(district_response.text, 'html.parser')
    
    #extracting the branch list
    branches = district_soup.find_all('a', class_="branch")
    
    #looping through the branches
    for branch in branches:
        #storing the branch name
        branch_name = branch.text
        branch_list.append(branch_name)
        print(branch_list)
        
        #storing the branch url
        branch_url = url + branch['href']
        
        #sending request to the branch page
        branch_response = requests.get(branch_url)
        
        #parsing the response
        branch_soup = BeautifulSoup(branch_response.text, 'html.parser')
        
        #extracting the pin code
        pin_code = branch_soup.find('div', class_="pin").text
        pin_list.append(pin_code)
        
        #storing the state name
        state_name = branch_soup.find('div', class_="state").text
        state_list.append(state_name)

#creating a dataframe
df = pd.DataFrame({'District': district_list, 'Branch': branch_list, 'Pin Code': pin_list, 'State': state_list})

#saving the dataframe to excel
df.to_excel('haryana_district_details.xlsx', index=False)