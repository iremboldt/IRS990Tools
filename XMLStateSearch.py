import os
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import pandas as pd
#This uses Element Tree, an XML parser library for python

#https://www.irs.gov/charities-non-profits/form-990-series-downloads
#Set the location of the directory the 990s were, or will be, saved in as a string, then create an os object
path = r'directory location'
directory = os.fsencode(path)

# input is zip file location, output is desired extract location
def extractzip(input,output):
with ZipFile(input, 'r') as zObject: 
    zObject.extractall(path=output) 
    
def get990s(extractYN,directory,*years):
    for year in years:
        monthcodes = ['01A','01B','01C','02A','02B','02C','03A','03B','03C','04A','04B','04C','05A','05B','05C','06A','06B','06C','07A','07B','07C','08A','08B','08C','09A','09B','09C','10A','10B','10C','11A','11B','11C','12A','12B','12C']
        for month in monthcodes:
            #save the .zip for each one, potentially even extract the data as well in this function
            url = 'https://apps.irs.gov/pub/epostcard/990/xml/'+year+'/'+year+'_TEOS_XML_'+month+'.zip'
            file = requests.get(url, stream=True
            dump = file.raw
            location = os.path.abspath(directory)
            filename = 'returns'+month+year+'.zip'
            with open(filename, 'wb') as location:
                shutil.copyfileobj(dump, location)
            del dump
            if extractYN == True:
                extractzip(directory+filename)
            else:
                continue

#iterate through files in the directory and remove non Nebraska States
def removeStates(directory):
    for file in os.listdir(directory):
        temppath = os.fsencode(file)
        filename = os.fsdecode(temppath)
        tree = ET.parse(directory+'\\'+filename)
        root = tree.getroot()
        #the following code replaced trying to search by index, and I just put in the xml path. the part that threw me off was starting with the irs url each time.
        try:
            state = tree.find('.//{http://www.irs.gov/efile}ReturnHeader/{http://www.irs.gov/efile}Filer/{http://www.irs.gov/efile}USAddress/{http://www.irs.gov/efile}StateAbbreviationCd').text
            try:
                if state != 'NE':
                    os.remove(directory+'\\'+filename)
                else:
                    continue
            except:
                 print('child index out of range for '+filename)
        except:
            if tree.find('.//{http://www.irs.gov/efile}ReturnHeader/{http://www.irs.gov/efile}Filer/{http://www.irs.gov/efile}ForeignAddress/{http://www.irs.gov/efile}CountryCd').text != 'US':
                os.remove(directory+'\\'+filename)
            else:
                print('State not found at expected index for '+filename)
        #put in a try catch because the previous three strings kept messing up, also the XMLs have slight variations and I wanted a log of which ones to do manually or with an adjusted script

def removeCity(directory):
        for file in os.listdir(directory):
        temppath = os.fsencode(file)
        filename = os.fsdecode(temppath)
        tree = ET.parse(directory+'\\'+filename)
        root = tree.getroot()
        #the following code replaced trying to search by index, and I just put in the xml path. the part that threw me off was starting with the irs url each time.
        try:
            city = tree.find('.//{http://www.irs.gov/efile}ReturnHeader/{http://www.irs.gov/efile}Filer/{http://www.irs.gov/efile}USAddress/{http://www.irs.gov/efile}CityNm').text
            try:
                if city != 'Lincoln':
                    os.remove(directory+'\\'+filename)
                else:
                    continue
            except:
                 print('child index out of range for '+filename)

#This method is developed from the removeStates function, but it extracts EINs from the expected xml path and adds them to a list
def getEIN(directory):
    eidList=[]
    for file in os.listdir(directory):
        filename = os.fsencode(file)
        tree = ET.parse(path+'\\'+filename)
        root = tree.getroot()
        EIN = tree.find('.//{http://www.irs.gov/efile}ReturnHeader/{http://www.irs.gov/efile}Filer/{http://www.irs.gov/efile}EIN').text
        eidList.append(EIN)

def xmltocsv(directory):        
    cols = ["totalassets", "totalrevenue", "totalexpenses", "liabilities"] 
    rows = [] 
      
    # Parsing the XML file
    for file in os.listdir(directory):
        filename = os.fsencode(file)
        tree = ET.parse(path+'\\'+filename)
        root = tree.getroot()
        # These dumb ass xml paths keep returning "None" instead of a number. Not sure why but I went through and checked everything and it should work. Once I figure that out I can start appending each xml as a row in a csv.
        totalrevenue = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}AnalysisOfRevenueAndExpenses/{{http://www.irs.gov/efile}TotalRevAndExpnssAmt').text 
        totalassets = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}ChgInNetAssetsFundBalancesGrp/{http://www.irs.gov/efile}TotNetAstOrFundBalancesEOYAmt').text
        totalexpenses = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}AnalysisOfRevenueAndExpenses/{http://www.irs.gov/efile}TotalExpensesDsbrsChrtblAmt').text 
        liabilities = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}AnalysisOfRevenueAndExpenses/{http://www.irs.gov/efile}TotalLiabilitiesBOYAmt').text 
            
          
        rows.append({"totalassets": totalassets, 
                     "totalrevenue": totalrevenue, 
                     "totalexpenses": totalexpenses, 
                     "liabilities": liabilities,}) 
        # This will probably need updated, not sure if the syntax is right for a for loop. Might just recreate the data frame instead of appending a row. Probably worth making the dataframe a global variable, or outside the for loop  
        df = pd.DataFrame(rows, columns=cols) 
      
    # Writing dataframe to csv 
    df.to_csv(r'C:\MyFiles\Projects\NonProfits\test.csv')
