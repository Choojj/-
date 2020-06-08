import sys

while (True):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if (a < b):
        if (b < c):
            side1, side2, side3 = a, b, c
        else:
            side1, side2, side3 = a, c, b
    else:
        if (a < c):
            side1, side2, side3 = a, b, c
        else:
            side1, side2, side3 = c, b, a


    if (side1 == 0 and side2 == 0 and side3 == 0):
        break

    if (side1 ** 2 + side2 ** 2 == side3 ** 2):
        print("right")
    else:
        print("wrong")