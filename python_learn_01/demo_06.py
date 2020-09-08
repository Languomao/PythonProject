def min(x):
    least = x[0]
    for each in x:
        if each < least:
            least = each
    return least


def sum(x):
    result = 0
    for each in x:
        if type(each) == int or type(each) == float:
            result += int(each)
        else:
            continue
    return result


# min("languomao")
# print(sum([1, 2.1, 2.3, 'a', '1', True]))
list1 = list("eqfwklf3424523l5")
print(list1)
print(sum(list1))
