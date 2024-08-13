import requests 
import csv
import json
import pandas as pd

class Propublica:

  def __init__(self,eins,names)
    #add a string to the end to return a .json with data for that organization
    NameSearchURL = r'https://projects.propublica.org/nonprofits/api/v2/search.json?q='
    #add "EIN".json to the end of the url to get 990 info for the org. ex. organizations/123456789.json
    OrgSearchURL = r'https://projects.propublica.org/nonprofits/api/v2/organizations/'
    #These should be input as python lists, consider using *args to allow multiple inputs, but for now this should work.
    eins = self.eins
    names = self.names
  
'''
  def geteins(self):
    for name in self.names:
      response = requests.get(NameSearchURL+name)
      #Parse the returned json for the ein and append to eins list
    return(eins)
'''
'''  
  def getTaxInfo(self):
      TaxInfo = []
      for ein in self.eins:
        response = requests.get(OrgSearchURL+ein+'.json')
        #Parse the json and append data to the list, or create a series of csvs
        return(TaxInfo)
'''
'''
  def writeCSV():
    #x=json.loads(response.content)
    #for x in x:
    #https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
    #f.writerow([x["Organizations"]["ein"])
    
    #got this to work!!
    #the list i got somewhat differs from name, eg ampersand being spelled out
    data=pd.read_json(json.dumps(jsonstring))
    for name in names:
        response=requests.get('https://projects.propublica.org/nonprofits/api/v2/search.json?q='+name)
        npjson=json.loads(response.content)
        data=pd.read_json(json.dumps(npjspn))
        if len(data.index)>1:
          i=0
          while i<len(data.index):
            row=data['organizations'].loc[data.index[i]]
            try:
                eins.append(row['ein'])
            except:
                print('ein does not exist for '+np)
            i+=1
        elif len(data.index)==1:
          row=data['organization'].loc[data.index[0]]
          try:
              eins.append(row['ein'])
          except:
              print('ein does not exist for '+np)
        else:
          print('data not found for'+np)
'''
