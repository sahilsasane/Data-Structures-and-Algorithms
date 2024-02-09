for i in range(n + 1):
        for j in range(sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            elif arr[i - 1] > j:
                t[i][j] = t[i - 1][j]