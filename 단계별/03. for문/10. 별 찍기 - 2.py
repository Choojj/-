import sys

num = int(sys.stdin.readline())

for i in range(num):
    for j in range(num):
        # print(i, j, end = " ")
        if (num - j > i + 1):
            print(" ", end = "")
        else:
            print("*", end = "")
    print("")