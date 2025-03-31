import sys
from os import path


def get_int():
    if path.exists("input.txt"):
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")

    input = int(sys.stdin.readline())
    return input


w = get_int() if (path.exists("input.txt")) else int(sys.stdin.readline())
