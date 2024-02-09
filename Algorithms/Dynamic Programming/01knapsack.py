import numpy as np


def knap_recursive(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] <= W:
        return max(
            val[n - 1] + knap_recursive(wt, val, W - wt[n - 1], n - 1),
            knap_recursive(wt, val, W, n - 1),
        )
    elif wt[n - 1] > W:
        return knap_recursive(wt, val, W, n - 1)


def knap_memoisation(wt, val, W, n):
    t = np.array([[-1 for i in range(W + 1)] for j in range(n + 1)])
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knap_recursive(wt, val, W - wt[n - 1], n - 1),
            knap_recursive(wt, val, W, n - 1),
        )
    if wt[n - 1] > W:
        t[n][W] = knap_recursive(wt, val, W, n - 1)
    return t[n][W]


def knap_top_down(wt, val, W, n):
    t = np.array([[-1 for i in range(W + 1)] for j in range(n + 1)])
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    print(t)
    return t[n][W]


if __name__ == "__main__":
    wt = [1, 2, 3]
    val = [10, 15, 40]
    W = 6
    n = 3
    print(knap_recursive(wt, val, W, n))
    print(knap_memoisation(wt, val, W, n))
    print(knap_top_down(wt, val, W, n))
