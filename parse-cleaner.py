import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup
import re

pattern = r'\[.*?\]'

inf = input('enter data to be cleaned : ')

for info in inf :
    info.findall('<')
