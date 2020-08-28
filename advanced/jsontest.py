import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

data_str = json.dumps(data)
print()
print(data_str)
