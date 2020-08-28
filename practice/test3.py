def daoxu(arr):
    for i in range(1, len(arr)):

        value = arr[i]
        j = i - 1

        while j >= 0 and value > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value


arr = [1, 2, 3, 4, 5, 6, 7, 8]
daoxu(arr)
print(arr)
