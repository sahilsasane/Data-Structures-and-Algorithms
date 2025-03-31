import numpy as np
from subset_sum_problem import subsetsum


def min_subset_sum_diff(arr, n):
    s = sum(arr)
    r = subsetsum(arr, s, n)[1][-1]
    i = 0
    s1 = float("inf")
    while i < len(r) // 2 and r[i]:
        s1 = i
        i += 1
    return s - (2 * s1)


if __name__ == "__main__":
    arr = [1, 2, 7]
    n = len(arr)
    print(min_subset_sum_diff(arr, n))
