import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup

snums = list()
inums = list()

tag = input("enter tag:")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup(tag)
'''
for tag in tags :
    snums.append(tag.contents)
    print(tag.contents)'''

for tag in tags :
    print(tag.append)
