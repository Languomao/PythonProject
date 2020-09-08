a = 10
def funcA(a):
    print(id(a))
    a += a**2
    print(id(a))
    return a
funcA(a)
print(id(a))
