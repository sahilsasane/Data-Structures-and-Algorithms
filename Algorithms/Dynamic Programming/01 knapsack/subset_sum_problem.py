import numpy as np


def subsetsum(arr, sum, n):
    t = np.array([[False for i in range(sum + 1)] for j in range(n + 1)])
    for i in range(n + 1):
        for j in range(sum + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            elif arr[i - 1] > j:
                t[i][j] = t[i - 1][j]
    return t[n, sum], t


if __name__ == "__main__":
    arr = [2, 3, 7, 8, 10]
    sum = 15
    n = len(arr)
    print(subsetsum(arr, sum, n)[0])
