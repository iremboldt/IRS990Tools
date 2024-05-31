import os
import xml.etree.ElementTree as ET
#This uses Element Tree, an XML parser library for python

#Set the location of the directory as a string, then create an os object
path = r'directory location'
directory = os.fsencode(path)

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
