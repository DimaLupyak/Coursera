from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://py4e-data.dr-chuck.net/known_by_Rosalie.html"

count = 7
position = 18
i = 0
while i < count:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    name = tags[position - 1].contents[0]
    i += 1
print(name)