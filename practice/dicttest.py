# dictionary中的解析

params = {"name": "languomao", "age": 25, "sex": "man", "birthday": "0602"}

print(params.keys())

print(params.values())

print(params.items())

print(["%s = %s" % (k, v) for k, v in params.items()])


