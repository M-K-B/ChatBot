import json
import requests
import operator

def dictionaryToString(title, dictInput):
    output = title
    for key, value in dictInput:
        if len(key) < 8:
            output += "\n" + key + "\t\t" + str(value)
        else:
            output += "\n" + key + "\t" + str(value)
    return output
def main(input):
    i, arrNom = 0, -1
    for game in odds_json['data']:
        if input.lower().find(game['teams'][0].lower()) or input.lower().find(game['teams'][1].lower()):
            arrNom = i
            break
        i += 1
    if arrNom == -1:
        return "Invalid input"
    winDict = {}
    drawDict = {}
    losDict = {}
    for site in odds_json['data'][arrNom]['sites']:
        winDict[site['site_nice']] = site['odds']['h2h'][0]
        drawDict[site['site_nice']] = site['odds']['h2h'][1]
        losDict[site['site_nice']] = site['odds']['h2h'][2]
    winDictSorted = sorted(winDict.items(), key=operator.itemgetter(1), reverse = True)
    drawDictSorted = sorted(drawDict.items(), key=operator.itemgetter(1), reverse = True)
    losDictSorted = sorted(losDict.items(), key=operator.itemgetter(1), reverse = True)
    output = dictionaryToString("WINS ODDS:", winDictSorted)
    output += dictionaryToString("\n\nDRAW ODDS:", drawDictSorted)
    output += dictionaryToString("\n\nLOSE ODDS:", losDictSorted)
    return output
def usageCheck():
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
# An api key is emailed to you when you sign up to a plan
api_key = 'bad3ddea34371000da26af057af03eb4'
# First get a list of in-season sports
sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
    'api_key': api_key
})

sports_json = json.loads(sports_response.text)

sport_key = 'soccer_epl'

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': api_key,
    'sport': sport_key,
    'region': 'uk', # uk | us | au
    'mkt': 'h2h' # h2h | spreads | totals
})
odds_json = json.loads(odds_response.text)
if not odds_json['success']:
    print(
        'There was a problem with the odds request:',
        odds_json['msg']
    )
else:
    # odds_json['data'] contains a list of live and 
    #   upcoming events and odds for different bookmakers.
    # Events are ordered by start time (live events are first)
    print()
    print(
        'Successfully got {} events'.format(len(odds_json['data'])),
        'Here\'s the first event:'
    )
if not sports_json['success']:
    print(
        'There was a problem with the sports request:',
        sports_json['msg']
    )

else:
    print()
    print(
        'Successfully got {} sports'.format(len(sports_json['data'])),
        'Here\'s the first sport:'
    )
    print(sports_json['data'][0])

# To get odds for a sepcific sport, use the sport key from the last request
#   or set sport to "upcoming" to see live and upcoming across all sports
if __name__ == "__main__":
    print(main(input("Input: ")))