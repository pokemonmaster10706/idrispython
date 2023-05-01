import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

nums = list()
sums = list()
f = 1

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

cle = '0'

tags = soup('a')
for tag in tags:
    url = tag.get('href', None)
    try:
        he = url.split('/')
    except:
        continue
    #print(he)
    if len(he) > 1:
        cle = he[1]
    if cle == 'wiki':
        nums.append(url)
for n in nums :
    print('link #', f , ':' , n)
    f += 1
print('number of links :',len(nums))
