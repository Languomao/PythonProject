def func1(a):
    def func2(b):
        return a * b
    return func2


result = func1(5)
print(type(result))
print(result(5))
print(func1(4)(5))
