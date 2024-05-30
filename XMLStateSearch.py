import os

directory = os.fsencode(“directory location”)
directorystring = “directory location”

for file in os.listdir(directory):
    filename = os.fsencode(file)
    tree = ET.parse(directorystring+”\\”+filename)
    root = tree.getroot()
    state = root[0][5][4][2].text
    try:
        if state != ‘NE’:
            os.remove(directorystring+”\\”+filename)
        else:
            continue
    except:
        print(‘child index out of range for ‘+filename)