import numpy as np


def lcs_recursive(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        return 1 + lcs_recursive(x, y, m - 1, n - 1)
    else:
        return max(lcs_recursive(x, y, m, n - 1), lcs_recursive(x, y, m - 1, n))


def lcs_memoize(x, y, m, n):
    t = np.array([[-1 for i in range(m + 1)] for j in range(n + 1)])
    if m == 0 or n == 0:
        return 0
    if t[n, m] != -1:
        return t[n, m]
    if x[m - 1] == y[n - 1]:
        t[n, m] = 1 + lcs_recursive(x, y, m - 1, n - 1)
    else:
        t[n, m] = max(lcs_recursive(x, y, m, n - 1), lcs_recursive(x, y, m - 1, n))
    return t[n, m]


def lcs_top_down(x, y, m, n):
    t = np.array([[-1 for i in range(n + 1)] for j in range(m + 1)])
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i, j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                t[i, j] = 1 + t[i - 1, j - 1]
            else:
                t[i, j] = max(t[i, j - 1], t[i - 1, j])
    return t[m, n]


if __name__ == "__main__":
    x = "abcdefg"
    y = "abcdefgasdf"
    m = len(x)
    n = len(y)
    print(lcs_recursive(x, y, m, n))
    print(lcs_memoize(x, y, m, n))
    print(lcs_top_down(x, y, m, n))
