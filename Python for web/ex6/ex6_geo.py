import json
import urllib.request, urllib.parse

serviceurl = "http://py4e-data.dr-chuck.net/json?"
api_key = 42

params = dict()
params['key'] = api_key
params['address'] = 'Bharthidasan University'
url = serviceurl + urllib.parse.urlencode(params)
data = urllib.request.urlopen(url).read()
info = json.loads(data)
print(info['results'][0]['place_id'])


