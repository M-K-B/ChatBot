import requests,json
import googlemaps
import pprint
import json
api_key = 'AIzaSyACL7b30pHsYzSAsL6Md2rK2CANS1OGako'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


try:
    ans= input('Search Pubs in Location: ') 
except EOFError:
    print ("Error: EOF or empty input!")
    ans = ""
    
print (ans)  




r = requests.get(url + 'query=' + ans +
                        '&key=' + api_key)
x = r.json()
y = x['results']
print(x)
for i in range(len(y)):
    
    print(y[i]['name']) 







gmaps = googlemaps.Client(key = api_key)


places_result  = x





stored_results = []

    
for place in places_result['results']:

    my_place_id = place['place_id']


    my_fields = ['name','formatted_phone_number','website']

    
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)

    
    pprint.pprint(places_details['result'])

    
    stored_results.append(places_details['result'])






