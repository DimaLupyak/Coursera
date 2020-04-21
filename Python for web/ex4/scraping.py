from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://py4e-data.dr-chuck.net/comments_442666.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
sum = 0
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])
print(sum)
    