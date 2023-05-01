import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

pos = 1
count = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sp = input("enter position- ")
p = int(sp)
sc = input("enter count- ")
c = int(sc)

demon = True

while demon is True :
    tags = soup('a')
    for tag in tags:
        if pos < p :
            pos = pos + 1
            continue
        elif c == count :
            demon = False
            break
        else :
            print("receiving:" ,tag.get('href', None))
            pos = 1
            url = tag.get('href', None)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            count = count + 1
            break
print("done")
