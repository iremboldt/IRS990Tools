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
  eidList=[]
  #populate nplist with values from non profit list, url encoded
  nplist=[]
  
  #x=json.loads(response.content)
  #for x in x:
    #https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
    #f.writerow([x["Organizations"]["ein"])
  
  #got this to work!!
  #the list i got sewhat differs from name, eg ampersand being spelled out
  data=pd.read_json(json.dumps(jsonstring))
  for np in nplist:
      response=requests.get('https://projects.propublica.org/nonprofits/api/v2/search.json?q='+np)
      npjson=json.loads(response.content)
      data=pd.read_json(json.dumps(npjspn))
      if len(data.index)>1:
        i=0
        while i<len(data.index):
          row=data['organizations'].loc[data.index[i]]
          try:
              eidList.append(row['eid'])
          except:
              print('eid does not exist for '+np)
          i+=1
      elif len(data.index)==1:
        row=data['organization'].loc[data.index[0]]
        try:
            eidList.append(row['eid'])
        except:
            print('eid does not exist for '+np)
      else:
        print('data not found for'+np)
    
