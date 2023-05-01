import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

nums = list()
sums = list()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:
    nums.append(tag.contents[0])
for n in nums :
    s = int(n)
    sums.append(s)
print("Sum",sum(sums))
