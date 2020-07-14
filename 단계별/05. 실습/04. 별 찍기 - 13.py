import sys

N = int(sys.stdin.readline())

for i in range(1, N):
    for j in range(0, i):
        print("*", end = "")
    print()

for i in range(N, 0, -1):
    for j in range(0, i):
        print("*", end = "")
    print()