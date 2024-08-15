def JobScheduling(arr, t):
    n = len(arr)
    # insertion sort
    for i in range(n):
        k = arr[i]
        j = i - 1
        while j >= 0 and k[2] > arr[j][2]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

    res = [False] * t
    job = ["-1"] * t
    profit = 0
    for i in range(n):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not res[j]:
                res[j] = True
                job[j] = arr[i][0]
                profit += arr[i][2]
                break
    return job, profit


if __name__ == "__main__":
    arr = [
        ["a", 2, 100],
        ["b", 1, 19],
        ["c", 2, 27],
        ["d", 1, 25],
        ["e", 3, 15],
    ]

    j, p = JobScheduling(arr, 3)
    print(j, "\n", p)
