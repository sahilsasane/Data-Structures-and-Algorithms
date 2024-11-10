# Evaluate Expression To True-Boolean Parenthesization Recursion
# Given a boolean expression with following symbols.
# Symbols
#     'T' --- true
#     'F' --- false
# And following operators filled between symbols
# Operators
#     &   ---boolean AND
#     |   --- boolean OR
#     ^   --- boolean XOR
# Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
# Example:
# Input: symbol[]    = {T, F, T}
#        operator[]  = {^, &}
# Output: 2
# The given expression is "T ^ F & T", it evaluates true
# in two ways "((T ^ F) & T)" and "(T ^ (F & T))"


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


if __name__ == "__main__":
    s = "ababbbabbababa"

    min_cost = solve(s)
    print(min_cost)
