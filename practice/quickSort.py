"""

快速排序：将比基准值小的元素全放到左边（再将当前位置的值与元素下一个位置的值交换）

"""


def partition(arr, low, high):

    # 元素最小下标
    i = low - 1

    pivot = arr[high]

    # 先找出所有比基准值小的值
    for x in range(low, high):
        if arr[x] <= pivot:
            # 从下标为0开始，不断在前面填入弊基准值小的值
            i += 1
            arr[i], arr[x] = arr[x], arr[i]

    # 将所有比基准值小的值找出后，再把第一个比基准值大的值设置为arr[high],然后开始新一轮的分区
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # 最后返回数组的分界点，i+1
    return i + 1


def quicksort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


arr1 = [2, 4, 0, 14, 44, 20, 6, 66, 19, 28]
quicksort(arr1, 0, len(arr1) - 1)
print(arr1)
