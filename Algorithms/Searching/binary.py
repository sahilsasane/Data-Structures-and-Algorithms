def binary_search(arr, val, l, r):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == val:
            return True
        elif val < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return False


array = sorted([64, 25, 12, 22, 11])
val = 11
print(binary_search(array, val, 0, len(array) - 1))
