import requests

from bs4 import BeautifulSoup

r = requests.get("http://www.practicepython.org/assets/Training_01.txt")

with open("Training_01.txt", "w") as input_file:
    input_file.write(r.text.encode("utf-8"))
input_file.close()

categories = {}
with open("Training_01.txt", "r") as input_file:
    line = input_file.readline()
    while line:
        category = line.split("/")[2]
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

        line = input_file.readline()

input_file.close()

for x in categories.items():
    print x
