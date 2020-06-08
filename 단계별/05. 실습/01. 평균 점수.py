import sys

sum = 0

for i in range(5):
    A = int(sys.stdin.readline())

    if (A < 40):
        A = 40

    sum += A

print(int(sum / 5))