import os
import xml.etree.ElementTree as ET
from zipfile import ZipFile 
#This uses Element Tree, an XML parser library for python

#https://www.irs.gov/charities-non-profits/form-990-series-downloads
#Set the location of the directory the 990s were, or will be, saved in as a string, then create an os object
path = r'directory location'
directory = os.fsencode(path)

def get990s(year)
    monthcodes = ['01A','01B','01C','02A','02B','02C','03A','03B','03C','04A','04B','04C','05A','05B','05C','06A','06B','06C','07A','07B','07C','08A','08B','08C','09A','09B','09C','10A','10B','10C','11A','11B','11C','12A','12B','12C']
    for month in monthcodes:
        #save the .zip for each one, potentially even extract the data as well in this function
        'https://apps.irs.gov/pub/epostcard/990/xml/'+year+'/'+year+'_TEOS_XML_'+month+'.zip'

# input is zip file location, output is desired extract location
def extractzip(input,output)
with ZipFile(input, 'r') as zObject: 
    zObject.extractall(path=output) 

#iterate through files in the directory
for file in os.listdir(directory):
    filename = os.fsencode(file)
    #the next three lines, when run individually, return the state code as a string. When run together, or in a script, it breaks for some reason
    tree = ET.parse(path+'\\'+filename)
    root = tree.getroot()
    state = root[0][5][4][2].text
    #put in a try catch because the previous three strings kept messing up, also the XMLs have slight variations and I wanted a log of which ones to do manually or with an adjusted script
    try:
        if state != ‘NE’:
            os.remove(path+'\\'+filename)
        else:
            continue
    except:
        print('child index out of range for '+filename)
