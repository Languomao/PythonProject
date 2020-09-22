import urllib.request

url = 'https://www.ip138.com/'
proxy_support = urllib.request.ProxyHandler({'http': '110.243.31.195:9999'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')]
urllib.request.install_opener(opener)

res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
print(html)


