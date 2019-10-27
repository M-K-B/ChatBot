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
# print(response.text)
def jprint(obj, inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    for team in obj["api"]["teams"]:
        if team["name"].lower() == inp.lower():
            break
        i = i + 1

    try:
        print(obj["api"]["teams"][i]["venue_city"]+ " \n" + obj["api"]["teams"][i]["venue_name"] + "\n" + obj["api"]["teams"][i]["venue_city"]+ "\n" + obj["api"]["teams"][i]["logo"]+ "\n" + obj["api"]["teams"][i]["venue_address"])
    except:
        print("Could not find valid team")
    
if __name__ == "__main__":
    entry = input("***discord entry***: ") 
    jprint(response.json(), entry)
print("done")
def ManuPrint(manu):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    j = 0
    o = 0
    for team in manu["api"]["teams"]:
        if team["venue_city"] == "Manchester":
            j = o
            break
        o = o + 1

    print(manu["api"]["teams"][j]["venue_city"] + " \n" + manu["api"]["teams"][j]["venue_name"] + "\n" + manu["api"]["teams"][j]["venue_city"] + "\n" + manu["api"]["teams"][j]["logo"] + "\n" + manu["api"]["teams"][j]["venue_address"])

ManuPrint(response.json())


def Chelsea(chel):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    h = 0
    c = 0
    for team in chel["api"]["teams"]:
        if team["name"] == "Chelsea":
            h = c
            break
        c = c + 1

    print(chel["api"]["teams"][h]["name"] + " \n" + chel["api"]["teams"][h]["venue_name"] + "\n" + chel["api"]["teams"][h]["venue_city"] + "\n" + chel["api"]["teams"][h]["logo"] + "\n" + chel["api"]["teams"][h]["venue_address"]+ "\n" + chel["api"]["teams"][h]["venue_city"])

Chelsea(response.json())


def ManC(manc):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    y = 0
    p = 0
    for team in manc["api"]["teams"]:
        if team["venue_name"] == "Etihad Stadium":
            y = p
            break
        p = p + 1

    print(manc["api"]["teams"][y]["name"] + " \n" + manc["api"]["teams"][y]["venue_name"] + "\n" + manc["api"]["teams"][y]["venue_city"] + "\n" + manc["api"]["teams"][y]["logo"] + "\n" + manc["api"]["teams"][y]["venue_address"]+ "\n" + manc["api"]["teams"][y]["venue_city"])

ManC(response.json())


def Tott(toth):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    z = 0
    q = 0
    for team in toth["api"]["teams"]:
        if team["venue_name"] == "Tottenham Hotspur Stadium":
            z = q
            break
        q = q + 1

    print(toth["api"]["teams"][z]["name"] + " \n" + toth["api"]["teams"][z]["venue_name"] + "\n" + toth["api"]["teams"][z]["venue_city"] + "\n" + toth["api"]["teams"][z]["logo"] + "\n" + toth["api"]["teams"][z]["venue_address"]+ "\n" + toth["api"]["teams"][z]["venue_city"])

Tott(response.json())


def Ares(aress):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    l = 0
    a = 0
    for team in aress["api"]["teams"]:
        if team["venue_name"] == "Emirates Stadium":
            l = a
            break
        a = a + 1

    print(aress["api"]["teams"][l]["name"] + " \n" + aress["api"]["teams"][l]["venue_name"] + "\n" + aress["api"]["teams"][l]["venue_city"] + "\n" + aress["api"]["teams"][l]["logo"] + "\n" + aress["api"]["teams"][l]["venue_address"]+ "\n" + aress["api"]["teams"][l]["venue_city"])

Ares(response.json())

def wolv(wolvv):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    q = 0
    w = 0
    for team in wolvv["api"]["teams"]:
        if team["venue_name"] == "Molineux Stadium":
            q = w
            break
        w = w + 1

    print(wolvv["api"]["teams"][q]["name"] + " \n" + wolvv["api"]["teams"][q]["venue_name"] + "\n" + wolvv["api"]["teams"][q]["venue_city"] + "\n" + wolvv["api"]["teams"][q]["logo"] + "\n" + wolvv["api"]["teams"][q]["venue_address"]+ "\n" + wolvv["api"]["teams"][q]["venue_city"])

wolv(response.json())

def leiss(liesss):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    r = 0
    t = 0
    for team in liesss["api"]["teams"]:
        if team["venue_name"] == "King Power Stadium":
            r = t
            break
        t = t + 1

    print(liesss["api"]["teams"][r]["name"] + " \n" + liesss["api"]["teams"][t]["venue_name"] + "\n" + liesss["api"]["teams"][r]["venue_city"] + "\n" + liesss["api"]["teams"][t]["logo"] + "\n" + liesss["api"]["teams"][t]["venue_address"]+ "\n" + liesss["api"]["teams"][t]["venue_city"])

leiss(response.json())


def sout(south):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    u = 0
    x = 0
    for team in south["api"]["teams"]:
        if team["venue_name"] == "St. Mary's Stadium":
            u = x
            break
        x = x + 1

    print(south["api"]["teams"][u]["name"] + " \n" + south["api"]["teams"][u]["venue_name"] + "\n" + south["api"]["teams"][u]["venue_city"] + "\n" + south["api"]["teams"][u]["logo"] + "\n" + south["api"]["teams"][u]["venue_address"]+ "\n" + south["api"]["teams"][u]["venue_city"])

sout(response.json())

def Bri(britt):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    s = 0
    f = 0
    for team in britt["api"]["teams"]:
        if team["venue_name"] == "The American Express Community Stadium":
            s = f
            break
        f = f + 1

    print(britt["api"]["teams"][s]["name"] + " \n" + britt["api"]["teams"][s]["venue_name"] + "\n" + britt["api"]["teams"][s]["venue_city"] + "\n" + britt["api"]["teams"][s]["logo"] + "\n" + britt["api"]["teams"][s]["venue_address"]+ "\n" + britt["api"]["teams"][s]["venue_city"])

Bri(response.json())


def Eve(ever):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in ever["api"]["teams"]:
        if team["venue_name"] == "Goodison Park":
            i = o
            break
        o = o + 1

    print(ever["api"]["teams"][i]["name"] + " \n" + ever["api"]["teams"][i]["venue_name"] + "\n" + ever["api"]["teams"][i]["venue_city"] + "\n" + ever["api"]["teams"][i]["logo"] + "\n" + ever["api"]["teams"][i]["venue_address"]+ "\n" + ever["api"]["teams"][i]["venue_city"])

Eve(response.json())

def WES(west):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in west["api"]["teams"]:
        if team["venue_name"] == "London Stadium":
            i = o
            break
        o = o + 1

    print(west["api"]["teams"][i]["name"] + " \n" + west["api"]["teams"][i]["venue_name"] + "\n" + west["api"]["teams"][i]["venue_city"] + "\n" + west["api"]["teams"][i]["logo"] + "\n" + west["api"]["teams"][i]["venue_address"]+ "\n" + west["api"]["teams"][i]["venue_city"])

WES(response.json())



def Bur(Burs):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in Burs["api"]["teams"]:
        if team["venue_name"] == "Turf Moor":
            i = o
            break
        o = o + 1

    print(Burs["api"]["teams"][i]["name"] + " \n" + Burs["api"]["teams"][i]["venue_name"] + "\n" + Burs["api"]["teams"][i]["venue_city"] + "\n" + Burs["api"]["teams"][i]["logo"] + "\n" + Burs["api"]["teams"][i]["venue_address"]+ "\n" + Burs["api"]["teams"][i]["venue_city"])

Bur(response.json())


def New(news):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in news["api"]["teams"]:
        if team["venue_name"] == "St. James' Park":
            i = o
            break
        o = o + 1

    print(news["api"]["teams"][i]["name"] + " \n" + news["api"]["teams"][i]["venue_name"] + "\n" + news["api"]["teams"][i]["venue_city"] + "\n" + news["api"]["teams"][i]["logo"] + "\n" + news["api"]["teams"][i]["venue_address"]+ "\n" + news["api"]["teams"][i]["venue_city"])

New(response.json())



def Bour(bours):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in bours["api"]["teams"]:
        if team["venue_name"] == "Vitality Stadium":
            i = o
            break
        o = o + 1

    print(bours["api"]["teams"][i]["name"] + " \n" + bours["api"]["teams"][i]["venue_name"] + "\n" + bours["api"]["teams"][i]["venue_city"] + "\n" + bours["api"]["teams"][i]["logo"] + "\n" + bours["api"]["teams"][i]["venue_address"]+ "\n" + bours["api"]["teams"][i]["venue_city"])

Bour(response.json())


def Car(card):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in card["api"]["teams"]:
        if team["venue_name"] == "Cardiff City Stadium":
            i = o
            break
        o = o + 1

    print(card["api"]["teams"][i]["name"] + " \n" + card["api"]["teams"][i]["venue_name"] + "\n" + card["api"]["teams"][i]["venue_city"] + "\n" +  card["api"]["teams"][i]["logo"] + "\n" + card["api"]["teams"][i]["venue_address"]+ "\n" + card["api"]["teams"][i]["venue_city"])

Car(response.json())



def Ful(fula):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in fula["api"]["teams"]:
        if team["venue_name"] == "Craven Cottage":
            i = o
            break
        o = o + 1

    print(fula["api"]["teams"][i]["name"] + " \n" + fula["api"]["teams"][i]["venue_name"] + "\n" + fula["api"]["teams"][i]["venue_city"] + "\n" + fula["api"]["teams"][i]["logo"] + "\n" + fula["api"]["teams"][i]["venue_address"]+ "\n" + fula["api"]["teams"][i]["venue_city"])

Ful(response.json())


def Cry(crys):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in crys["api"]["teams"]:
        if team["venue_name"] == "Selhurst Park":
            i = o
            break
        o = o + 1

    print(crys["api"]["teams"][i]["name"] + " \n" + crys["api"]["teams"][i]["venue_name"] + "\n" + crys["api"]["teams"][i]["venue_city"] + "\n" + crys["api"]["teams"][i]["logo"] + "\n" + crys["api"]["teams"][i]["venue_address"]+ "\n" + crys["api"]["teams"][i]["venue_city"])

Cry(response.json())

def Hudd(hudde):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in hudde["api"]["teams"]:
        if team["venue_name"] == "John Smith's Stadium":
            i = o
            break
        o = o + 1

    print(hudde["api"]["teams"][i]["name"] + " \n" + hudde["api"]["teams"][i]["venue_name"] + "\n" + hudde["api"]["teams"][i]["venue_city"] + "\n" + hudde["api"]["teams"][i]["logo"] + "\n" + hudde["api"]["teams"][i]["venue_address"]+ "\n" + hudde["api"]["teams"][i]["venue_city"])

Hudd(response.json())


def Wat(wats):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0
    o = 0
    for team in wats["api"]["teams"]:
        if team["venue_name"] == "Vicarage Road":
            i = o
            break
        o = o + 1

    print(wats["api"]["teams"][i]["name"] + " \n" + wats["api"]["teams"][i]["venue_name"] + "\n" + wats["api"]["teams"][i]["venue_city"] + "\n" + wats["api"]["teams"][i]["logo"] + "\n" + wats["api"]["teams"][i]["venue_address"]+ "\n" + wats["api"]["teams"][i]["venue_city"])

Wat(response.json())


