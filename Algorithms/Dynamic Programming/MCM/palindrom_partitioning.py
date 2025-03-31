# Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome.
# Example:
#   “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.


def solve(s):
    def is_palindrome(s, i, j):
        return s[i : j + 1] == s[i : j + 1][::-1]

    def pp_recursive(s, i, j):
        if i >= j:
            return 0
        if is_palindrome(s, i, j):
            return 0
        min_partitions = float("inf")
        for k in range(i, j):
            temp = pp_recursive(s, i, k) + pp_recursive(s, k + 1, j) + 1
            min_partitions = min(min_partitions, temp)
        return min_partitions

    def pp_memoize(s, i, j):
        t = [[float("inf") for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        if i >= j:
            return 0
        if is_palindrome(s, i, j):
            return 0
        if t[i][j] != float("inf"):
            return t[i][j]
        for k in range(i, j):
            temp = pp_recursive(s, i, k) + pp_recursive(s, k + 1, j) + 1
            t[i][j] = min(t[i][j], temp)
        return t[i][j]

    return pp_memoize(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = "ababbbabbababa"

    min_cost = solve(s)
    print(min_cost)
