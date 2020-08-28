"""

插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

"""


def insertionSort(arr):
    for i in range(1, len(arr)):

        value = arr[i]
        j = i - 1

        # 与前一个元素比较
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            # 下标前移一位
            j -= 1
        arr[j + 1] = value


arr = [10, 9, 8, 7, 6, 5]
insertionSort(arr)
print(arr)
