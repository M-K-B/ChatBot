import requests

url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/id/157351"

querystring = {"timezone":"Europe/London"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

def fixt(fix,inp):
    # create a formatted string of the Python JSON object
    # text = json.dumps(obj, sort_keys=True, indent=4)
    i = 0

    for fixtures in fix["api"]["fixtures"]:
        if fixtures["league_id"].lower() == inp.lower():

            break
        i = i + 1
    try:
        print(fix["api"]["fixtures"][i]["event_date"]+ " \n" + fix["api"]["fixtures"][i]["event_timestamp"] + "\n" + fix["api"]["teams"][i]["firstHalfStart"]+ "\n" + fix["api"]["teams"][i]["secondHalfStart"]+ "\n" + fix["api"]["teams"][i]["status"])
    except:
        print("Could not find a team")

if __name__ == "__main__":
    entry = input("***discord entry***: ")
    fixt(response.json(), entry)
print("done")
