"""

冒泡排序：重复走访要排序的元素，一次比较两个元素。如果顺序错误就交换过来。
一次走访就相当于与把找出一个最大值（或最小值）

"""


def bubblesort(arr):

    # 需要重复走访的次数为len(arr) - 2
    for i in range(1, len(arr) - 1):
        for j in range(0, len(arr) - i):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)


arr = [10, 7, 8, 9, 1, 5, 4, 23, 32, 6, 51, 17, 16, 15, 14]
bubblesort(arr)
print(arr)

