# Matrix Chain Multiplication using Recursion
#  Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to  perform the multiplications, but merely to decide in which order to perform the multiplications.


def solve(arr):
    def mcm_recursive(arr, i, j):
        if i >= j:
            return 0
        min_cost = float("inf")
        for k in range(i, j):
            temp = (
                mcm_recursive(arr, i, k)
                + mcm_recursive(arr, k + 1, j)
                + (arr[i - 1] * arr[k] * arr[j])
            )
            min_cost = min(min_cost, temp)
        return min_cost

    def mcm_memoize(arr, i, j):
        t = [[float("inf") for i in range(len(arr) + 1)] for j in range(len(arr) + 1)]
        if i >= j:
            return 0
        if t[i][j] != float("inf"):
            return t[i][j]
        for k in range(i, j):
            temp = (
                mcm_recursive(arr, i, k)
                + mcm_recursive(arr, k + 1, j)
                + (arr[i - 1] * arr[k] * arr[j])
            )
            t[i][j] = min(t[i][j], temp)
        return t[i][j]

    return mcm_memoize(arr, 1, len(arr) - 1)


if __name__ == "__main__":
    arr = [40, 20, 30, 10, 30]

    min_cost = solve(arr)
    print(min_cost)
