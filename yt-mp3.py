import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from selenium import webdriver
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

yt = input('enter yt link: ')

s = yt.split('=')
f =  'https://ytmp3x.com/' + s[1]


mp = f
'''
url = f
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')'''

driver = webdriver.Chrome()
driver.get(mp)
button = driver.find_element_by_id('div class="file"')
button.click()
