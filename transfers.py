import requests

url = "https://api-football-v1.p.rapidapi.com/v2/transfers/team/33"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7ad59fd663msha96194a35d6ad74p11378djsn8d396b9b4c77"
    }

response = requests.request("GET", url, headers=headers)


def transfer (inp):
    i = 0
    headers = response.json()
    for tr in headers["api"]["transfers"]:
        if tr["player_name"].lower() == inp.lower():
            break
        i = i + 1
    try:



        return ((headers['api']['transfers']['first_name'] + " " + (
        headers['api']['transfers']['second_name']) + " \n" +
        (str(headers['api']['transfers']['transfer_fee']))))
        return (("Team In : " + (headers['api']['transfers']['Team_in'])))
        return ((("Team Out : " + ['api']['transfers']['Team_out'])))
        return (("Transfer date " + (str(headers['api']['transfers']['Transfer_date']))))
        return (("Lastest Update : " + (str(headers['api']['transfer']['Lastest_update']))))
        return (("Player ID : " + (str(headers['api']['transfers']['player_id']))))

    except:
        return ("Couldnt Find a player transfering ")





