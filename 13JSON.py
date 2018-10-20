# Extracting data from JSON
# The program will prompt for a URL, read the JSON data from
# that URL using urllib and then parse and extract the comment
# counts from the JSON data, compute the sum of the numbers in the
# file and enter the sum below:
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_119934.json (Sum ends with 21)
import urllib.request, urllib.parse, urllib.error
import json
counts = list()
url = 'http://py4e-data.dr-chuck.net/comments_119934.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
comments = js['comments']
for item in comments:
    counts.append(item['count'])
print('Count', len(counts))
print('Sum',sum(counts))
