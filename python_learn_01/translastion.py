import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/?aldtype=16047'
data = {}

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode()
print(html)
