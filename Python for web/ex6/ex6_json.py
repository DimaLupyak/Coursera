import json
from urllib.request import urlopen

url = "http://py4e-data.dr-chuck.net/comments_442669.json"
data = urlopen(url).read()

info = json.loads(data)
print('User count:', len(info))

sum = 0
for comment in info['comments']:
    sum += int(comment['count'])
print(sum)
