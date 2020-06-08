import sys
import math

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dist = y - x

    p = int(math.sqrt(dist))

    remain = math.ceil((dist - (p * p)) / p)

    print(p * 2 - 1 + remain)