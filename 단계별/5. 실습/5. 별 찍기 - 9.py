import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N * 2 - i):
        if (i <= j < N * 2 - i - 1):
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")

for i in range(N - 2, -1, -1):
    for j in range(N * 2 - i):
        if (i <= j < N * 2 - i - 1):
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")