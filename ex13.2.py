import json
import twurl
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen

data = input('Enter url- ')
fhand = urlopen(data)

info = json.loads(fhand.read())

snums = list()
inums = list()

for item in info['comments']:
    n = int(item['count'])
    inums.append(n)


#for num in snums:
#    n = int(num)
#    inums.append(n)

print(sum(inums))
