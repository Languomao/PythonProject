li = ["adc", 2321, "lanlanlan", 7823, "KDJFK"]
# 按索引查找
print(li[2])
# 索引查找最后一个元素
print(li[-1])
# 添加元素
li.append("add element")
print(li)
print(li.index(2321))
print("languomao" in li)
# 删除元素
print(li.remove(7823))
# 运算符
print(li + ["new list", "odajsod", 46])

params = {"name":"languomao", "age":25, "sex":"man"}
str1 = ";"

s = ["%s = %s" % (k, v) for k, v in params.items()]
# join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
print(s)
print(str1.join(s))

# split将一个字符串分割成多个ist,split第二个参数可选，为分割的次数
print(str1.join(s).split(";"))



