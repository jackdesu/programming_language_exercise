import requests

from bs4 import BeautifulSoup

r = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
soup = BeautifulSoup(r.text, "html.parser")
for heading in soup.find_all(class_="content-section"):
    print heading.text.strip()
