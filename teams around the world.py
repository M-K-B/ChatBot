import requests

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/real_m"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def Real(reall,inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in reall["api"]["teams"]:
        if team["name"].lower() == inp.lower():
            o = i
            break
        o = o + 1

    try:
        print(reall["api"]["teams"][i]["name"] + " \n" + reall["api"]["teams"][i]["venue_name"] + "\n" + reall["api"]["teams"][i]["venue_city"] + "\n" +
              reall["api"]["teams"][i]["logo"] + "\n" + reall["api"]["teams"][i]["venue_address"]+ "\n" + reall["api"]["teams"][i]["venue_city"])
    except:
        print("Could not find a team")

if __name__ == "__main__":
    entry = input("***discord entry***: ")
    Real(response.json(), entry)
print("....")

import requests

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/barc"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def Barc(bar,inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in bar["api"]["teams"]:
        if team["name"].lower() == inp.lower():
            o = i
            break
        o = o + 1

    try:
        print(bar["api"]["teams"][i]["name"] + " \n" + bar["api"]["teams"][i]["venue_name"] + "\n" + bar["api"]["teams"][i]["venue_city"] + "\n" + bar["api"]["teams"][i]["logo"] + "\n" + bar["api"]["teams"][i]["venue_address"]+ "\n" + bar["api"]["teams"][i]["venue_city"])
    except:
        print("Could not find a team")

if __name__ == "__main__":
    entry = input("***discord entry***: ")
    Barc(response.json(), entry)
print("....")

import requests

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/juve"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def Juve(juv,inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in juv["api"]["teams"]:
        if team["name"].lower() == inp.lower():
            o = i
            break
        o = o + 1

    try:
        print(juv["api"]["teams"][i]["name"] + " \n" + juv["api"]["teams"][i]["venue_name"] + "\n" + juv["api"]["teams"][i]["venue_city"] + "\n" + juv["api"]["teams"][i]["logo"] + "\n" + juv["api"]["teams"][i]["venue_address"]+ "\n" + juv["api"]["teams"][i]["venue_city"])
    except:
        print("Could not find a team")

if __name__ == "__main__":
    entry = input("***discord entry***: ")
    Juve(response.json(), entry)
print("....")

import requests

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/paris"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def Paris(par,inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in par["api"]["teams"]:
        if team["name"].lower() == inp.lower():
            o = i
            break
        o = o + 1

    try:
        print(par["api"]["teams"][i]["name"] + " \n" + par["api"]["teams"][i]["venue_name"] + "\n" + par["api"]["teams"][i]["venue_city"] + "\n" + par["api"]["teams"][i]["logo"] + "\n" + par["api"]["teams"][i]["venue_address"]+ "\n" + par["api"]["teams"][i]["venue_city"])
    except:
        print("Could not find a team")

if __name__ == "__main__":
    entry = input("***discord entry***: ")
    Paris(response.json(), entry)
print("....")




import requests

url = "https://api-football-v1.p.rapidapi.com/v2/teams/search/milan"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def Milan(mil,inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in mil["api"]["teams"]:
        if team["name"].lower() == inp.lower():
            o = i
            break
        o = o + 1

    try:
        print(mil["api"]["teams"][i]["name"] + " \n" + mil["api"]["teams"][i]["venue_name"] + "\n" + mil["api"]["teams"][i]["venue_city"] + "\n" + mil["api"]["teams"][i]["logo"] + "\n" + mil["api"]["teams"][i]["venue_address"]+ "\n" + mil["api"]["teams"][i]["venue_city"])
    except:
        print("Could not find a team")

if __name__ == "__main__":
    entry = input("***discord entry***: ")
    Milan(response.json(), entry)
print("....")

