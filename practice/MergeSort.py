"""

归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
分治法:
    分割：递归地把当前序列平均分割成两半,最后得到的每个子序列都是有序的。
    集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。递归比较子序列。

"""


def mergesort(li):

    # 分割list，当list全部分割为单个元素时，可把子list看做是有序的
    if len(li) == 1:
        return li

    # 充分调用分割函数，直至每个字序列长度都为1
    mid = len(li) // 2
    left = mergesort(li[:mid])
    right = mergesort(li[mid:])

    return merge(left, right)


def merge(left, right):

    # 临时数组，存放比较的数据
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] >= right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    # 比较取值直至其中一个数组为空，然后将余下的数组添加到临时数组中（子数组已经有序）
    result += left
    result += right

    return result


arr = [10, 7, 8, 9, 1, 5, 4, 23, 32, 6, 51, 17, 16, 15, 14]
print(mergesort(arr))
