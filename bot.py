import requests,json
api_key = 'AIzaSyACL7b30pHsYzSAsL6Md2rK2CANS1OGako'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


try:
    query = input('Search query: ') 
except EOFError:
    print ("Error: EOF or empty input!")
    query = ""
print (query)




r = requests.get(url + 'query=' + query +
                        '&key=' + api_key)
x = r.json()
y = x['results']
print(x)
for i in range(len(y)):
    print(y[i]['name']) 



