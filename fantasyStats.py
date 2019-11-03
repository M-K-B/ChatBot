import json
import requests





data = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()
def PlayerPoints(inp):
    (data['elements']) # name of the list
    place = 0
    for player in data['elements']:
        if player['second_name'] == inp:
            break
        place = place + 1
        # print(player['first_name'] + " " + (player['second_name']) + " " + (str(player['total_points'])))
    print((data['elements'][place]['first_name'] + " " + (data['elements'][place]['second_name']) + " " + " \nTotal Fansatsy points this Season: → "+ (str(data['elements'][place]['total_points'] )))) #Gets players first name & second name & total fantasy points
    print(("Any News → "+ (data['elements'][place]['news'])))
    print((("Goals scored → "+ (str(data['elements'][place]['goals_scored'])))))
    print(("Assists "+(str(data['elements'][place]['assists']))))
    print(("Minutes played this season → "+ (str(data['elements'][place]['minutes']))))
    print(("Yellow Cards → " + (str(data['elements'][place]['yellow_cards']))))
    print(("Red Cards → " + (str(data['elements'][place]['red_cards']))))

PlayerPoints(input("What is the players second name ? "))


