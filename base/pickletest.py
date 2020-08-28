import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

stringdata = "teststring"

output = open("C:\\Users\\LanKorment\\Desktop\\data.pkl", "wb")

pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
pickle.dump(stringdata, output)

output.close()


pkl_file = open("C:\\Users\\LanKorment\\Desktop\\data.pkl", "rb")

# load每次只取出一个对象
data1 = pickle.load(pkl_file)
print(data1)

data2 = pickle.load(pkl_file)
print(data2)

data3 = pickle.load(pkl_file)
print(data3)
