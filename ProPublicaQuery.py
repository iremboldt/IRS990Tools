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
