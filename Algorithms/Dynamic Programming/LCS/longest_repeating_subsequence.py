# Longest Repeating Subsequence
# Given a string, print the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
# Example:
# Input: str = "aab"
# Output: "a"
# The two subsequence are 'a'(first) and 'a'
# (second). Note that 'b' cannot be considered
# as part of subsequence as it would be at same
# index in both.


def lrsubsequence_top_down(x, n):
    y = x
    t = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1] and i != j:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    return t[n][n]


if __name__ == "__main__":
    x = "aabbcddeffg"
    n = len(x)
    print(lrsubsequence_top_down(x, n))
