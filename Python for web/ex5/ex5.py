from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_442668.xml"
data = urlopen(url).read()
tree = ET.fromstring(data)
sum = 0
for count in tree.findall('.//count'):
    sum += int(count.text)
print(sum)