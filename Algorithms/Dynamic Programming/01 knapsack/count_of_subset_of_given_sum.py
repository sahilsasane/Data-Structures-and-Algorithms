import numpy as np


def count_subset(arr, sum, n):
    t = np.array([[0 for i in range(sum + 1)] for j in range(n + 1)])
    for i in range(n + 1):
        for j in range(sum + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            elif arr[i - 1] > j:
                t[i][j] = t[i - 1][j]
    return t


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    sum = 10
    n = len(arr)
    print(count_subset(arr, sum, n))
