import keyring
import json
import requests
import os


url = "https://api.dusti.co/v1/packages"
#token = keyring.get_password(u":local-database:scs", u"token")

token = os.environ.get('DUSTICO_API_TOKEN')

headers = {
    "Authorization": "token " + token
}

# Opening JSON file
f = open('package.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
scs_data = []

data2 = data['dependencies']

for key in data2:
    
    scs_data.append({"name": key,"type": "npm","version": data2[key]})
    
    pass

# Make the API Request
r = requests.post(url, json=scs_data, headers=headers)
r.raise_for_status()

# Write Results out to a Json File
with open('scs_results.json','w') as outfile:
    json.dump(r.json(),outfile)
    
