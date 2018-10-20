# Extracting Data from XML
# The program will prompt for a URL, read the XML data from
# that URL using urllib and then parse and extract the comment
# counts from the XML data, compute the sum of the numbers in the file.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_119933.xml (Sum ends with 66)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_119933.xml?'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
number = 0
for item in lst:
    number = number + int(item.find('count').text)
print("Total counts:",number)
