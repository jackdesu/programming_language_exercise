import requests

from bs4 import BeautifulSoup

r = requests.get('http://www.nytimes.com/?WT.z_jog=1&hF=t&vS=vis')
soup = BeautifulSoup(r.text, "html.parser")
for heading in soup.find_all("h2", {"class": "story-heading"}):
    if heading.findAll("a"):
        print(heading.a.text.strip())
