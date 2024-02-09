def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr


array = [64, 25, 12, 22, 11]
print(insertion_sort(array))
