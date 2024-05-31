import requests

orgname = ''

url = 'https://projects.propublica.org/nonprofits/api/v2'
response = requests.get(url+'/search.json?q='+orgname)
print(response.text)
