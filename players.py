import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/300"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)



def play(pla,inp):
    i = 0

    for pll in pla["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(pla["api"]["players"][i]["player_name"] + " \n" + pla["api"]["players"][i]["firstname"] + "\n" + pla["api"]["players"][i]["lastname"] + "\n" + pla["api"]["players"][i]["team_name"] + "\n" + pla["api"]["players"][i]["position"] + "\n" + pla["api"]["players"][i]["league"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play(response.json(), entry)
print("....")




import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/302"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def play1(pla1,inp):
    i = 0

    for pll in pla1["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(pla1["api"]["players"][i]["player_name"] + " \n" + pla1["api"]["players"][i]["firstname"] + "\n" + pla1["api"]["players"][i]["lastname"] + "\n" + pla1["api"]["players"][i]["team_name"] + "\n" + pla1["api"]["players"][i]["position"] + "\n" + pla1["api"]["players"][i]["league"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play1(response.json(), entry)
print("....")


import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/305"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def play2(pla2,inp):
    i = 0

    for pll in pla2["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(pla2["api"]["players"][i]["player_name"] + " \n" + pla2["api"]["players"][i]["firstname"] + "\n" + pla2["api"]["players"][i]["lastname"] + "\n" + pla2["api"]["players"][i]["team_name"] + "\n" + pla2["api"]["players"][i]["position"] + "\n" + pla2["api"]["players"][i]["league"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play2(response.json(), entry)
print("....")




import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/369"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def play3(pla3,inp):
    i = 0

    for pll in pla3["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(pla3["api"]["players"][i]["player_name"] + " \n" + pla3["api"]["players"][i]["firstname"] + "\n" + pla3["api"]["players"][i]["lastname"] + "\n" + pla3["api"]["players"][i]["team_name"] + "\n" + pla3["api"]["players"][i]["position"] + "\n" + pla3["api"]["players"][i]["league"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play3(response.json(), entry)
print("....")

import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/327"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def play4(pla4,inp):
    i = 0

    for pll in pla4["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(pla4["api"]["players"][i]["player_name"] + " \n" + pla4["api"]["players"][i]["firstname"] + "\n" + pla4["api"]["players"][i]["lastname"] + "\n" + pla4["api"]["players"][i]["team_name"] + "\n" + pla4["api"]["players"][i]["position"] + "\n" + pla4["api"]["players"][i]["league"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play4(response.json(), entry)
print("....")



import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/330"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def play5(pla5,inp):
    i = 0

    for pll in pla5["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(pla5["api"]["players"][i]["player_name"] + " \n" + pla5["api"]["players"][i]["firstname"] + "\n" + pla5["api"]["players"][i]["lastname"] + "\n" + pla5["api"]["players"][i]["team_name"] + "\n" + pla5["api"]["players"][i]["position"] + "\n" + pla5["api"]["players"][i]["league"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play5(response.json(), entry)
print("....")




