import os
import xml.etree.ElementTree as ET
from zipfile import ZipFile
import pandas as pd
import requests
import urllib.request

Class IRS990:

    def __init__(self,directory,*years):
        self.directory=directory
        self.years=years

    # input is zip file location, output is desired extract location
    def extractzip(directory):
        for input in os.path(directory):
            with ZipFile(input, 'r') as zObject: 
                zObject.extractall(path=directory+\\+input) 
    
    #This function downloads and saves 990 zip repositories from the irs website using their naming convention
    #Input is the directory you want to save to and a wildcard argument to allow multiple years
    def get990s(directory,*years):
        for year in years:
            monthcodes = ['01A','01B','01C','02A','02B','02C','03A','03B','03C','04A','04B','04C','05A','05B','05C','06A','06B','06C','07A','07B','07C','08A','08B','08C','09A','09B','09C','10A','10B','10C','11A','11B','11C','12A','12B','12C']
            for month in monthcodes:
                #Current IRS 990 website
                url = 'https://apps.irs.gov/pub/epostcard/990/xml/'+year+'/'+year+'_TEOS_XML_'+month+'.zip'
                file = requests.get(url)
                #dump = file.raw
                location = os.path.abspath(directory)
                filename = 'returns'+month+year+'.zip'
                with open(location+filename, 'wb') as filelocation:
                    filelocation.write(file.content)
                #del dump
                #import urllib.request
                #f = open('00000001.jpg','wb')
                #f.write(urllib.request.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read())
                #f.close()
                
    #iterate through files in the directory and remove xmls with business address not in Nebraska (NE)
    def removeStates(directory):
        for file in os.listdir(directory):
            temppath = os.fsencode(file)
            filename = os.fsdecode(temppath)
            tree = ET.parse(directory+'\\'+filename)
            root = tree.getroot()
            #The following code replaced trying to search by index, and I just put in the xml path. the part that threw me off was starting with the irs url each time.
            #The try catch is so that you can see files that did not have the correct file strucure. It also accounts for foreign companny addresses, which use differen tags
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
    
    #This function works the same as removeState, but uses the city tags/location
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
    
    #WIP

    #pathGen creates strings for the fully qualified xml path, reducing the amount of duplicate columns in a PD dataframe. It will still need some editing, such as adding a 2 to the end of actually duplicated paths.
    def pathGen(fn):
        path = []
        it = ET.iterparse(fn, events=('start', 'end'))
        for evt, el in it:
            if evt == 'start':
                path.append(el.tag)
                yield '/'.join(path)
            else:
                path.pop()

    #Runs pathGen and populates a list of paths for later use in xmltocsv as column headers
    def createPathList(list)
        for pth in pathGen(file):
            list.append(pth)
        '''
        list=[]
        i=0
        for pth in pathGen(file):
            k=i+1
            for j in range(k, _size):
            if x[i] == x[j] and x[i] not in list:
                list.append(x[i])
        '''        

    # This will convert multiple 990 xml documents into rows on a csv, which will them be able to imported to excel to be sorted
    def xmltocsv(directory):        
        cols = ["Tag","Value"] 
        rows = [] 
          
        # Parsing the XML file
        for file in os.listdir(directory):
            filename = os.fsencode(file)
            tree = ET.parse(path+'\\'+filename)
            root = tree.getroot()
            if tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF') != None:
                for elem in tree.iter():
                    rows.append(elem.tag+"|"+elem.text)
            elif tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990EZ') != None:
                #Space
            if tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990') != None:
                #Space
            '''
            totalrevenue = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}AnalysisOfRevenueAndExpenses/{{http://www.irs.gov/efile}TotalRevAndExpnssAmt').text 
            totalassets = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}ChgInNetAssetsFundBalancesGrp/{http://www.irs.gov/efile}TotNetAstOrFundBalancesEOYAmt').text
            totalexpenses = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}AnalysisOfRevenueAndExpenses/{http://www.irs.gov/efile}TotalExpensesDsbrsChrtblAmt').text 
            liabilities = tree.find('.//{http://www.irs.gov/efile}ReturnData/{http://www.irs.gov/efile}IRS990PF/{http://www.irs.gov/efile}AnalysisOfRevenueAndExpenses/{http://www.irs.gov/efile}TotalLiabilitiesBOYAmt').text 
                
            rows.append({"totalassets": totalassets, "totalrevenue": totalrevenue, "totalexpenses": totalexpenses, "liabilities": liabilities,})  
            df = pd.DataFrame(rows, columns=cols)
            '''
            df=pd.DataFrame(rows)
        # Writing dataframe to csv 
         df.to_csv(directory+'\990data.csv')
    
