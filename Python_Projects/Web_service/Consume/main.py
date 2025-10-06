import requests

#url = 'https://api.zippopotam.us/us/90210'
url = ' http://api.zippopotam.us/us/ma/illi'
print (url) # For testing 

# Consume the web service
response = requests.get(url)
if response.status_code == 200:
    print(url + ' is good! ')
    zipJson = response.json()
    #print(zipJson)
else:
    print(url + ' is bad ')
    print('Error code ' + str(response.status_code))
    exit(response.status_code)

    
# Parse json 

country = zipJson['country']
print(country)

# Lets pull one value 
#city = zipJson['places'][0]['place name']
#lat = zipJson['places'][0]['latitude']
#lon = zipJson['places'][0]['longitude']

#print(city + ' (' + str(lat) + ', ' + str(lon) + ')')

places = zipJson['places'] # places now holdss the array from the api
print(str(len(places)) + ' places found with that name')

for place in places:
    city = place['place name']
    lat = place['latitude']
    lon = place['longitude']
    print(city + ' (' + str(lat) + ', ' + str(lon) + ')')

