data = '1000,小甲鱼,男'
MyDict = {}
(MyDict['id'],MyDict['name'],MyDict['sex']) = data.split(',')

print("ID:   " + MyDict['id'])
print("Name: " + MyDict['name'])
print("Sex   " + MyDict['sex'])
