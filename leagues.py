
import json
import requests

## this is the code to get the leagues in england for exmaple the premier league and championship etc.
## the thing i need is the input i need, when the user types premier league, it only comes with the info for the premier league and vice versa.
## right now when you run it it comes up with all the all the info and when i get the input, i can implement it on the other codes ive done.

import requests

import requests

import requests
import json
import requests

url = "https://api-football-v1.p.rapidapi.com/v2/leagues/country/england/2019"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)



def Eleagues(standing):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    k = 0
    for sta in standing["api"]["leagues"]:
        if sta["name"] == "Premier League":
            i = k
            break
        k = k + 1

    print(standing["api"]["leagues"][i]["name"]+ " \n" + standing["api"]["leagues"][i]["type"]+ " \n" + standing["api"]["leagues"][i]["country"]+ " \n" + standing["api"]["leagues"][i]["logo"] )

Eleagues(response.json())


def Cleagues(Clea):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    k = 0
    for cle in Clea["api"]["leagues"]:
        if cle["name"] == "Championship":
            i = k
            break
        k = k + 1

    print(Clea["api"]["leagues"][i]["name"]+ " \n" + Clea["api"]["leagues"][i]["type"]+ " \n" + Clea["api"]["leagues"][i]["country"]+ " \n" + Clea["api"]["leagues"][i]["logo"] )

Cleagues(response.json())
