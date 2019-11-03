import requests

url = "https://api-football-v1.p.rapidapi.com/v2/countries"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)

def coun(co,inp):
    i = 0

    for cot in co["api"]["countries"]:
        if cot["country"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(co["api"]["countries"][i]["country"] + " \n" + co["api"]["countries"][i]["code"] + "\n" + co["api"]["countries"][i]["flag"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    coun(response.json(), entry)
print("....")







def coun(co,inp):
    i = 0

    for cot in co["api"]["countries"]:
        if cot["country"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(co["api"]["countries"][i]["country"] + " \n" + co["api"]["countries"][i]["code"] + "\n" + co["api"]["countries"][i]["flag"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    coun(response.json(), entry)
print("....")

def coun(co,inp):
    i = 0

    for cot in co["api"]["countries"]:
        if cot["country"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(co["api"]["countries"][i]["country"] + " \n" + co["api"]["countries"][i]["code"] + "\n" + co["api"]["countries"][i]["flag"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    coun(response.json(), entry)
print("....")

def coun(co,inp):
    i = 0

    for cot in co["api"]["countries"]:
        if cot["country"].lower() == inp.lower():
            break
        i = i + 1
    try:
        print(co["api"]["countries"][i]["country"] + " \n" + co["api"]["countries"][i]["code"] + "\n" + co["api"]["countries"][i]["flag"])
    except:
        print("Could not find a team")


if __name__ == "__main__":
    entry = input("***discord entry***: ")
    coun(response.json(), entry)
print("....")

