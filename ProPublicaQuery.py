import requests

eid = ''

url = r'https://projects.propublica.org/nonprofits/api/v2/organizations/'
response = requests.get(url+eid+'.json')
print(response.text)

list = []
for item in list:
  response = requests.get(url+item)
  print(response.text)
