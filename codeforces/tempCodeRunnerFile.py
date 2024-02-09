import sys
from os import path

if path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def get_int():
    input = sys.stdin.readline()
    return input


w = get_int()
n = int(w[0])
m = int(w[2])
scores = get_int().split(" ")
count = 0
for i in range(n):
    if int(scores[i]) > m:
        count += 1
print(count)
