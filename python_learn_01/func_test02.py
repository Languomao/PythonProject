"""
一、
如果通过这种方式来定义函数就会出错，因为在x相当于一个func1内的全局变量，func2想要修改这个变量的时候，x已经被屏蔽
相当于在这个过程会创建一个与x同名的局部变量，但是变量没有初始化，没有定义，所以会报错
def func1():
    x=5
    def func2():
        x *= x
    func2()
    return x
二、
容器的值不存放在栈中，如果使用栈来存放值，则通过索引来使用全局变量的值是可以的
def func1():
    x=[5]
    def func2():
        x[0] *= x[0]
    func2()
    return x[0]

"""
def func1():
    x = 5
    def func2():
        nonlocal x
        x *= x
    func2()
    return x


print(func1())
