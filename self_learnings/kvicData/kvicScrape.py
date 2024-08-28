import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re
from selenium.webdriver.support.ui import Select
import os

if not os.path.exists("kvicData"):
    os.makedirs("kvicData")
driver = webdriver.Chrome()
driver.get("https://www.kviconline.gov.in/khinstprofile/regdInstnsOfficewise.jsp?OFF_CD=5&TARGETRANGE=&cat=A")
baseElement = driver.find_element(By.CSS_SELECTOR,"body")
# print("baseElement---------",baseElement)
baseElements = driver.find_elements(By.CSS_SELECTOR,"tbody tr")
# print("baseElements----------",baseElements)
baseTable = pd.read_html(str(bs(baseElement.get_attribute('innerHTML'), 'html.parser').find('table')))[0]
# print(" type of baseTable----------------",type(baseTable))
# print("length of baseTable-----------",len(baseTable))
inst = []
link = []
for sn,baseLink in enumerate(baseElements):
    # print(str(bs(baseLink.get_attribute('innerHTML').split('/td')[-4]).text.replace(">\n","")))
    inst.append(str(bs(baseLink.get_attribute('innerHTML').split('/td')[-4]).text.replace(">\n","")))
    # print(str(baseLink.get_attribute('innerHTML').split('/td')[-3].split('href="')[1].split('"')))
    lk = str(baseLink.get_attribute('innerHTML').split('/td')[-3].split('href="')[1].split('"')[0])
    link.append(f'https://www.kviconline.gov.in/khinstprofile/{lk}')
baseTable["institute"] = inst
baseTable["link"] = link
instTableMain = pd.DataFrame()
salesOutletTableMain = pd.DataFrame()
infraTableMain = pd.DataFrame()
LBTableMain = pd.DataFrame()
artisanTableMain = pd.DataFrame()
artisanMainTable = pd.DataFrame()
productsTableMain = pd.DataFrame()
catalogueTableMain = pd.DataFrame()
performanceTableMain = pd.DataFrame()
soin,infin = 0,0
for hci,lk in enumerate(link):
    print(hci)
    driver.get(lk)
    instElement = driver.find_element(By.CSS_SELECTOR,"body")
    # print(len(bs(instElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))
    instTableData = bs(instElement.get_attribute('innerHTML'), 'html.parser').find_all('table')[1].find_all('td')
    for mi,mj in enumerate(instTableData):
        if mi == 1:
            instTableMain.at[hci,'Institution Code'] = str(mj.text).strip()
        elif mi == 3:
            instTableMain.at[hci,'KVIC Office Name'] = str(mj.text).strip()
        elif mi == 5:
            instTableMain.at[hci,'Institution Name'] = str(mj.text).strip()
        elif mi == 7:
            instTableMain.at[hci,'Institution Address'] = str(mj.text).strip()    
        elif mi == 9:
            instTableMain.at[hci,'City/Village'] = str(mj.text).strip()     
        elif mi == 11:
            instTableMain.at[hci,'Post'] = str(mj.text).strip()                
        elif mi == 13:
            instTableMain.at[hci,'Pin Code'] = str(mj.text).strip()                
        elif mi == 15:
            instTableMain.at[hci,'District'] = str(mj.text).strip()                
        elif mi == 17:
            instTableMain.at[hci,'Ph. No. with STD Code'] = str(mj.text).strip()                
        elif mi == 19:
            instTableMain.at[hci,'e-Mail ID'] = str(mj.text).strip()                  
        elif mi == 21:
            instTableMain.at[hci,'Aided By'] = str(mj.text).strip()                  
        elif mi == 23:
            instTableMain.at[hci,'Contact Person Name(Chairman)'] = str(mj.text).strip()                  
        elif mi == 24:
            instTableMain.at[hci,'Email ID(Chairman)'] = str(mj.text).strip()                  
        elif mi == 25:
            instTableMain.at[hci,'Mobile No.(Chairman)'] = str(mj.text).strip()     
        elif mi == 27:
            instTableMain.at[hci,'Contact Person Name(Secretary)'] = str(mj.text).strip()                  
        elif mi == 28:
            instTableMain.at[hci,'Email ID(Secretary)'] = str(mj.text).strip()                  
        elif mi == 29:
            instTableMain.at[hci,'Mobile No.(Secretary)'] = str(mj.text).strip()     
        elif mi == 31:
            instTableMain.at[hci,'Contact Person Name(KVIC Nodal Officer)'] = str(mj.text).strip()                  
        elif mi == 32:
            instTableMain.at[hci,'Email ID(KVIC Nodal Officer)'] = str(mj.text).strip()                  
        elif mi == 33:
            instTableMain.at[hci,'Mobile No.(KVIC Nodal Officer)'] = str(mj.text).strip()     
        elif mi == 38:
            instTableMain.at[hci,'Registration Date'] = str(mj.text).strip()                  
        elif mi == 39:
            instTableMain.at[hci,'Registration No.'] = str(mj.text).strip()                  
        elif mi == 40:
            instTableMain.at[hci,'Registration Type'] = str(mj.text).strip()     
        elif mi == 42:
            instTableMain.at[hci,'Khadi Certificate No.'] = str(mj.text).strip()                  
        elif mi == 44:
            instTableMain.at[hci,'Date'] = str(mj.text).strip()                  
        elif mi == 46:
            instTableMain.at[hci,'Khadi Mark No.'] = str(mj.text).strip()         
        elif mi == 48:
            instTableMain.at[hci,'Date of Issue'] = str(mj.text).strip()     
        else:
            pass
    linkTabelData = bs(instElement.get_attribute('innerHTML'), 'html.parser').find_all('table')[0].find_all('td')
    mainPageLinksDetail = {}
    for li,lj in enumerate(linkTabelData):
        mpld = lj.find('a')['href']
        mainPageLinksDetail[lj.find('a').text.strip()] = f'https://www.kviconline.gov.in/khinstprofile/{mpld}'
    for mpldj in mainPageLinksDetail:
        if mpldj == 'Sales Outlet':
            driver.get(mainPageLinksDetail['Sales Outlet'])
            soElement = driver.find_element(By.CSS_SELECTOR,"body")
            soTableData = bs(soElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
            for soif,sojf in enumerate(soTableData[1].find_all('td')):
                if soif == 1:
                    institutionCode = str(sojf.text).strip()
                elif soif == 3:
                    officeName = str(sojf.text).strip()
                elif soif == 5:
                    institutionName = str(sojf.text).strip()
                elif soif == 7:
                    address = str(sojf.text).strip()
                else:
                    pass
            for msois,msojs in enumerate(soTableData[2].find_all('tr')[2:]):
                for sois, sojs in enumerate(msojs.find_all('td')):
                    if sois == 1:
                        salesOutletTableMain.at[soin,'Institution Name'] = institutionName
                        salesOutletTableMain.at[soin,'Institution Code'] = institutionCode
                        salesOutletTableMain.at[soin,'Office Name'] = officeName
                        salesOutletTableMain.at[soin,'Institute Address'] = address
                        salesOutletTableMain.at[soin,'ID(Sales Outlet)'] = sojs.text
                    elif sois == 2:
                        salesOutletTableMain.at[soin,'Type(Sales Outlet)'] = sojs.text
                    elif sois == 3:
                        salesOutletTableMain.at[soin,'Name(Sales Outlet)'] = sojs.text
                    elif sois == 4:
                        salesOutletTableMain.at[soin,'Address(Sales Outlet)'] = sojs.text
                    elif sois == 5:
                        salesOutletTableMain.at[soin,'City(Sales Outlet)'] = sojs.text
                    elif sois == 6:
                        salesOutletTableMain.at[soin,'Pincode(Sales Outlet)'] = sojs.text
                        
                        button = driver.find_elements(By.CLASS_NAME, 'button')[msois]
                        button.click()
                        sodLinkEndPoint = str(soElement.get_attribute('innerHTML')).split(' id="bailwal_overlay_frame" src="')[1].split('"')[0]
                        sodLink = 'https://www.kviconline.gov.in/khinstprofile/'+sodLinkEndPoint
                        salesOutletTableMain.at[soin,'Profile Link(Sales Outlet)'] = sodLink
                        buttonClose = driver.find_element(By.CSS_SELECTOR, '#bailwal_img_overlay_close')
                        buttonClose.click()
                        soin = soin+1
        elif mpldj == 'Infrastructure':
            driver.get(mainPageLinksDetail['Infrastructure'])
            infElement = driver.find_element(By.CSS_SELECTOR,"body")
            infTableData = bs(infElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
            for infif,infjf in enumerate(infTableData[1].find_all('td')):
                if infif == 1:
                    institutionCode = str(infjf.text).strip()
                elif infif == 3:
                    officeName = str(infjf.text).strip()
                elif infif == 5:
                    institutionName = str(infjf.text).strip()
                elif infif == 7:
                    address = str(infjf.text).strip()
                else:
                    pass
            for minfis,minfjs in enumerate(infTableData[2].find_all('tr')[2:]):
                for infis, infjs in enumerate(minfjs.find_all('td')):
                    if infis == 1:
                        infraTableMain.at[infin,'Institution Name'] = institutionName
                        infraTableMain.at[infin,'Institution Code'] = institutionCode
                        infraTableMain.at[infin,'Office Name'] = officeName
                        infraTableMain.at[infin,'Institute Address'] = address
                        infraTableMain.at[infin,'Infrastructure Type'] = infjs.text
                    elif infis == 2:
                        infraTableMain.at[infin,'Description'] = infjs.text
                    elif infis == 3:
                        infraTableMain.at[infin,'in No.'] = infjs.text
                    elif infis == 4:
                        infraTableMain.at[infin,'Remarks'] = infjs.text
                        infin = infin+1
        elif mpldj == 'Land and Building':
            driver.get(mainPageLinksDetail['Land and Building'])
            lbElement = driver.find_element(By.CSS_SELECTOR,"body")
            lbTableData = bs(lbElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
            for lbif,lbjf in enumerate(lbTableData[1].find_all('td')):
                if lbif == 1:
                    institutionCode = str(lbjf.text).strip()
                elif lbif == 3:
                    officeName = str(lbjf.text).strip()
                elif lbif == 5:
                    institutionName = str(lbjf.text).strip()
                elif lbif == 7:
                    address = str(lbjf.text).strip()
                else:
                    pass
            lbDf = pd.read_html(str(bs(lbElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))[2]
            if len(lbDf)>1:
                lbDf.columns = lbDf.iloc[0]
                lbDf = lbDf.iloc[1:].reset_index(drop=True)
                lbDf['Institution Name'] = institutionName
                lbDf['Institution Code'] = institutionCode
                lbDf['Office Name'] = officeName
                lbDf['Institute Address'] = address
                lbDf.drop('Sr No.',inplace=True,axis=1)
                lbDf.fillna("",inplace=True)
                LBTableMain = pd.concat([LBTableMain,lbDf])
            else:
                pass

        elif mpldj == 'Artisan':
            driver.get(mainPageLinksDetail['Artisan'])
            artElement = driver.find_element(By.CSS_SELECTOR,"body")
            artTableData = bs(artElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
            for artif,artjf in enumerate(artTableData[1].find_all('td')):
                if artif == 1:
                    institutionCode = str(artjf.text).strip()
                elif artif == 3:
                    officeName = str(artjf.text).strip()
                elif artif == 5:
                    institutionName = str(artjf.text).strip()
                elif artif == 7:
                    address = str(artjf.text).strip()
                else:
                    pass
            artisanDf = pd.read_html(str(bs(artElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))[2]
            artisanDf.columns = artisanDf.iloc[0]
            artisanDf = artisanDf.iloc[1:-1].reset_index(drop=True)
            artisanDf['Institution Name'] = institutionName
            artisanDf['Institution Code'] = institutionCode
            artisanDf['Office Name'] = officeName
            artisanDf['Institute Address'] = address
            if len(artisanDf)>0:
                artisanTableMain = pd.concat([artisanTableMain,artisanDf])
                artisanLinkEndPoint = bs(artElement.get_attribute('innerHTML'), 'html.parser').find_all('table')[2].find_all('tr')[-1].find('a')['href']
                artisanDescriptionLink=f'https://www.kviconline.gov.in/khinstprofile/{artisanLinkEndPoint}'
                driver.get(artisanDescriptionLink)

                artnElement = driver.find_element(By.CSS_SELECTOR,"body")
                artnTableData = bs(artnElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
                for artnif,artnjf in enumerate(artnTableData[2].find_all('td')):
                    if artnif == 1:
                        institutionCode = str(artnjf.text).strip()
                    elif artnif == 3:
                        officeName = str(artnjf.text).strip()
                    elif artnif == 5:
                        institutionName = str(artnjf.text).strip()
                    elif artnif == 7:
                        address = str(artnjf.text).strip()
                    else:
                        pass
                artisanMainDf = pd.read_html(str(bs(artnElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))[3]
                artisanMainDf.columns = artisanMainDf.iloc[0]
                artisanMainDf = artisanMainDf.iloc[1:].reset_index(drop=True)
                artisanMainDf['Institution Name'] = institutionName
                artisanMainDf['Institution Code'] = institutionCode
                artisanMainDf['Office Name'] = officeName
                artisanMainDf['Institute Address'] = address
                artisanMainDf.drop('Sr no.',inplace=True,axis=1)
                artisanMainDf.fillna("",inplace=True)
                artisanMainTable = pd.concat([artisanMainTable,artisanMainDf])
            else:
                pass

        elif mpldj == 'Products':
            driver.get(mainPageLinksDetail['Products'])
            prdElement = driver.find_element(By.CSS_SELECTOR,"body")
            prdTableData = bs(prdElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
            for prdif,prdjf in enumerate(prdTableData[1].find_all('td')):
                if prdif == 1:
                    institutionCode = str(prdjf.text).strip()
                elif prdif == 3:
                    officeName = str(prdjf.text).strip()
                elif prdif == 5:
                    institutionName = str(prdjf.text).strip()
                elif prdif == 7:
                    address = str(prdjf.text).strip()
                else:
                    pass
            productsDf = pd.read_html(str(bs(prdElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))[2]
            if len(productsDf)>1:
                productsDf.columns = productsDf.iloc[0]
                productsDf = productsDf.iloc[1:].reset_index(drop=True)
                productsDf['Institution Name'] = institutionName
                productsDf['Institution Code'] = institutionCode
                productsDf['Office Name'] = officeName
                productsDf['Institute Address'] = address
                productsDf.fillna("",inplace=True)
                productsTableMain = pd.concat([productsTableMain,productsDf])
            else:
                pass
            #-------------------
            #Catalogue
            #-------------------
        elif mpldj == 'Performance':
            driver.get(mainPageLinksDetail['Performance'])
            perElement = driver.find_element(By.CSS_SELECTOR,"body")
            perTableData = bs(perElement.get_attribute('innerHTML'), 'html.parser').find_all('table')
            for perif,perjf in enumerate(perTableData[1].find_all('td')):
                if perif == 1:
                    institutionCode = str(perjf.text).strip()
                elif perif == 3:
                    officeName = str(perjf.text).strip()
                elif perif == 5:
                    institutionName = str(perjf.text).strip()
                elif perif == 7:
                    address = str(perjf.text).strip()
                else:
                    pass
            performanceDf = pd.read_html(str(bs(perElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))[2]
            performanceDf.columns = performanceDf.iloc[0]
            performanceDf = performanceDf.iloc[1:].reset_index(drop=True)
            performanceDf['Institution Name'] = institutionName
            performanceDf['Institution Code'] = institutionCode
            performanceDf['Office Name'] = officeName
            performanceDf['Institute Address'] = address
            performanceDf.drop('Sr No.',inplace=True,axis=1)
            performanceDf.fillna("",inplace=True)
            performanceTableMain = pd.concat([performanceTableMain,performanceDf])
for soli,solj in enumerate(salesOutletTableMain['Profile Link(Sales Outlet)']):
    driver.get(solj)
    sodElement = driver.find_element(By.CSS_SELECTOR,"body")
    df = pd.read_html(str(bs(sodElement.get_attribute('innerHTML'), 'html.parser').find_all('table')))[0]
    df[0] = df[0].str.replace(":","")
    df[0] = df[0].str.strip()
    df1 = df.iloc[:,0:2][1:]
    df2 = df.iloc[:,2:5][1:].iloc[[7,10]]
    df1 = df1.transpose()
    df1.columns = df1.iloc[0]
    df1.drop(0,inplace=True)
    df1.reset_index(drop=True,inplace=True)
    df1.at[0,'FAX NO'] = str(df2[3][8])
    df1.at[0,'Contract'] = str(df2[4][11])
    df1.fillna("",inplace=True)
    addrs=str(df1.iloc[:,2][0])+", "+str(df1.iloc[:,3][0])
    df1.drop('Address',axis=1,inplace=True)
    df1['Address'] = addrs
    for ci,cj in enumerate(df1.columns):
        salesOutletTableMain.at[soli,cj] = df1[cj][0]


instTableMain.fillna("",inplace=True)
infraTableMain.fillna("",inplace=True)
instTableMain.to_excel('kvicData/mainPageData.xlsx',index=False)
salesOutletTableMain.to_excel('kvicData/salesOutletPageData.xlsx',index=False)
LBTableMain.to_excel('kvicData/land&BuildingPageData.xlsx',index=False)
infraTableMain.to_excel('kvicData/infrastructurePageData.xlsx',index=False)
artisanTableMain.to_excel('kvicData/artisanPageData.xlsx',index=False)
artisanMainTable.to_excel('kvicData/artisanPageEmployeeData.xlsx',index=False)
performanceTableMain.to_excel('kvicData/performancePageData.xlsx',index=False)
