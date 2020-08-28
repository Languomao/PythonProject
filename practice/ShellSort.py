"""

希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。

"""


def shellsort(arr):

    gap = len(arr) // 2
    n = len(arr)

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j-gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2


arr = [10, 7, 8, 9, 1, 5, 4, 23, 32, 6, 51, 17, 16, 15, 14]
shellsort(arr)
print(arr)
