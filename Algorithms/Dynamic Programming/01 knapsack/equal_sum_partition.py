import numpy as np
from subset_sum_problem import subsetsum


def equal_sum_partition(arr, n):
    s = sum(arr)
    if s % 2 != 0:
        return False
    else:
        s = s // 2
        return subsetsum(arr, s, n)


if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    n = len(arr)
    print(equal_sum_partition(arr, n))
