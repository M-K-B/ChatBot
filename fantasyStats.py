import json
import requests





def PlayerPoints(inp):
    data = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()
    (data['elements']) # name of the list
    place, i = -1, 0
    for player in data['elements']:
        if player['second_name'] == inp:
            place = i
            break
        place = place + 1
        # print(player['first_name'] + " " + (player['second_name']) + " " + (str(player['total_points'])))
    if place == -1:
        return "Invalid input"
    string = (data['elements'][place]['first_name'] + " " + (data['elements'][place]['second_name']) + " " + " \nTotal Fansatsy points this Season: → "+ (str(data['elements'][place]['total_points']) + "\n")) #Gets players first name & second name & total fantasy points
    string += ("Any News → "+ (data['elements'][place]['news'] + "\n"))
    string += (("Goals scored → "+ (str(data['elements'][place]['goals_scored']) + "\n")))
    string += ("Assists "+(str(data['elements'][place]['assists']) + "\n"))
    string += ("Minutes played this season → "+ (str(data['elements'][place]['minutes']) + "\n"))
    string += ("Yellow Cards → " + (str(data['elements'][place]['yellow_cards']) + "\n"))
    string += ("Red Cards → " + (str(data['elements'][place]['red_cards'])))
    return string
    


