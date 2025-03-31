import numpy as np


def lcs_recursive(x, y, m, n, count=0):
    if m == 0 or n == 0:
        return count
    if x[m - 1] == y[n - 1]:
        count = lcs_recursive(x, y, m - 1, n - 1, count + 1)
    return max(
        count,
        max(
            lcs_recursive(x, y, m, n - 1, 0),
            lcs_recursive(x, y, m - 1, n, 0),
        ),
    )


def lcs_memoize(x, y, m, n):
    t = np.array([[0 for i in range(m + 1)] for j in range(n + 1)])
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        t[n, m] = 1 + lcs_recursive(x, y, m - 1, n - 1)
    else:
        t[n, m] = 0
    print(t)
    return t[n, m]


def lcs_top_down(x, y, m, n):
    t = np.array([[0 for i in range(n + 1)] for j in range(m + 1)])
    maxValue = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[i - 1]:
                t[i, j] = 1 + t[i - 1, j - 1]
                maxValue = max(maxValue, t[i, j])
            else:
                t[i, j] = 0
    return maxValue


if __name__ == "__main__":
    x = "abcd"
    y = "abcbd"
    m = len(x)
    n = len(y)
    print(lcs_recursive(x, y, m, n))
    print(lcs_memoize(x, y, m, n))
    print(lcs_top_down(x, y, m, n))
