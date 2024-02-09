def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_val = i
        for j in range(i, n):
            if arr[j] < arr[min_val]:
                min_val = j
        arr[i], arr[min_val] = arr[min_val], arr[i]
    return arr


array = [64, 25, 12, 22, 11]
print(selection_sort(array))
