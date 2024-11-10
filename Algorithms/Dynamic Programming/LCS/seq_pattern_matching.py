# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true


# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
def seq_pattern_matching(x, y, m, n):
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
    s = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            s += x[i - 1]
            i -= 1
            j -= 1
        else:
            if t[i - 1][j] > t[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return s[::-1] == x


if __name__ == "__main__":
    x = "abcz"
    y = "ahbgdc"
    m = len(x)
    n = len(y)
    print(seq_pattern_matching(x, y, m, n))
