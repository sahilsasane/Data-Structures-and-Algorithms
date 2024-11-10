# Minimum number of insertions to make a string palindrome
# Given a string, find the minimum number of characters to be inserted to form Palindrome string out of given string


# Examples:
# ab: Number of insertions required is 1. bab
# aa: Number of insertions required is 0. aa
def lps_top_down(x, y, m, n):
    t = [[-1 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    return len(x) - t[m][n]


if __name__ == "__main__":
    x = "abaaa"
    y = x[::-1]
    m = len(x)
    n = len(y)
    print(lps_top_down(x, y, m, n))
