import requests

#add a string to the end to return a .json with data for that organization
NameSearchURL = r'https://projects.propublica.org/nonprofits/api/v2/search.json?q='
#add "EIN".json to the end of the url to get 990 info for the org. ex. organizations/123456789.json
OrgSearchURL = r'https://projects.propublica.org/nonprofits/api/v2/organizations/'

eids = []
names = []

def getEIDs(names):
for name in names:
  response = requests.get(NameSearchURL+name)
  #Parse the returned json for the EID and append to eids list
return(eids)

def getTaxInfo(eids):
TaxInfo = []
for eid in eids:
  response = requests.get(OrgSearchURL+eid+'.json')
  #Parse the json and append data to the list, or create a series of csvs
return(TaxInfo)

def writeCSV():
    import csv
  import json
  import requests
  import pandas as pd
  eidlist=[]
  response=requests.get('https://projects.propublica.org/nonprofits/api/v2/search.json?q='+name)
  x=json.loads(response.content)
  #for x in x:
    #https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
    #f.writerow([x["Organizations"]["ein"])
  
  #got this to work!!
  data=pd.read_json(json.dumps(jsonstring))
  if len(data.index)>1:
    i=0
    while i<len(data.index):
      row=data['organizations'].loc[data.index[i]]
      eidlist.append(row['eid'])
      i+=1
  else:
    row=data['organization'].loc[data.index[0]]
    eidlist.append(row['eid'])
    
