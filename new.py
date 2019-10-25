import parameters as parameters
import requests
import json
url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/2"
api_key = "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)




jprint(response.json())