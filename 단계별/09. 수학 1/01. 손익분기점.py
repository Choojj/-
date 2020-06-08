import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

count = 0


if (B >= C):
    count = -1

else:
    count = A // (C - B) + 1

print(count)