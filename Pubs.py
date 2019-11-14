import requests,json
import googlemaps
import json
api_key = 'AIzaSyACL7b30pHsYzSAsL6Md2rK2CANS1OGako'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


query = input('Search query: ') 



r = requests.get(url + 'query=' + query +
                        '&key=' + api_key)
x = r.json()
y = x['results']
print(x)
for i in range (y):
    
    print(y[i]['name']) 



