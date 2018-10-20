# Calling a JSON API
# The program will prompt for a location, contact a web service
# and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON. A place ID
# is a textual identifier that uniquely identifies a place
# as within Google Maps.
# API End Points http://py4e-data.dr-chuck.net/geojson?
# Please run your program to find the place_id for this location: AGH University of Science and Technology
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'sensor':'false', 'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print('Place ID', js["results"][0]["place_id"])
