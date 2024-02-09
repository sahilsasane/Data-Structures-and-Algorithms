def kadane(arr):
    max_so_far = max_end_here = arr[0]

    for i in range(1, len(arr)):
        max_end_here = max(arr[i], max_end_here + arr[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(arr))
