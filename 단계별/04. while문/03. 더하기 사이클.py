import sys

count = 0

N = N1 = int(sys.stdin.readline())

while (True):
    count += 1

    first = N1 % 10
    N1 = N1 // 10 + N1 % 10

    second = N1 % 10
    N1 = first * 10 + second

    if (N1 == N):
        break

print(count)