import sys
from os import path

if path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def get_int():
    input = sys.stdin.readline()
    return input


n = int(input())
for i in range(n):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print(s[0] + str(len(s) - 2) + s[-1])
