"""

选择排序（Selection sort）是一种简单直观的排序算法.
它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

"""


def selectsort(arr):

    if len(arr) <= 1:
        return arr
    else:

        for x in range(0, len(arr)):
            for y in range(x + 1, len(arr)):
                # 如果有比自身小的值则置换
                if arr[x] < arr[y]:
                    arr[x], arr[y] = arr[y], arr[x]
            print(arr)
    return arr


arr = [10, 7, 8, 9, 1, 5, 4, 23, 32, 6, 51, 17, 16, 15, 14]
selectsort(arr)
print(arr)
