import sys
import math

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if (dist == 0 and r1 == r2):
        print(-1)
    elif (abs(r1 + r2) < dist):
        print(0)
    elif (abs(r1 + r2) == dist):
        print(1)
    elif (abs(r1 - r2) < dist < abs(r1 + r2)):
        print(2)
    elif (abs(r1 - r2) == dist):
        print(1)
    elif (abs(r1 - r2) > dist):
        print(0)