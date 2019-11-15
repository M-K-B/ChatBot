import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/squad/85/2018-2019"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)


def play45(inp):
    i = 0
    pla300 = response.json()
    for pll in pla300["api"]["players"]:
        if pll["firstname"].lower() == inp.lower():
            break
        i = i + 1
    try:
        return pla300["api"]["players"][i]["player_name"] + " \n" + pla300["api"]["players"][i]["firstname"] + "\n" + pla300["api"]["players"][i]["lastname"] + "\n" + pla300["api"]["players"][i]["nationality"] + "\n" + pla300["api"]["players"][i]["position"] + "\n" + pla300["api"]["players"][i]["birth_country"]
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    play45(response.json(), entry)
print("....")


