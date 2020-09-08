def hello():
    print('hello world')
    return
    print('hello world2.')


def power(x, y):
    """求x**y"""
    result = x ** y
    return result


def gcdtest(x, y):
    """
    利用欧几里得算法求最大公约数
    :param x:参数一
    :param y:参数二
    :return:返回值为最大公约数
    """
    while 1:
        temp = x % y
        if temp == 0:
            return y
        else:
            x, y = y, temp
            continue


def Dec2Bin(x):
    """
    对2求余法将十进制数转换成二进制数
    :param x:
    :return:
    """
    list1 = []
    while x:
        y = x // 2
        list1.append(str(x % 2))
        x = y
    list1.reverse()
    result = ''.join(list1)
    return result


# print(gcdtest(65, 26))
print(Dec2Bin(789))
