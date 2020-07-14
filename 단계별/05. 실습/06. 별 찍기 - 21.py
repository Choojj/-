import sys

N = int(sys.stdin.readline())

for i in range(N * 2):
    for j in range(N):
        if ((j + i) % 2 == 0):
            print("*", end = "")
        else:
            print(" ", end = "")
    print("")