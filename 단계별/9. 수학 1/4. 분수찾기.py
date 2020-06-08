import sys

X = int(sys.stdin.readline().rstrip())

i = 1
number = 0

while (number < X):
    number += i

    i += 1

if ((i - 1) % 2 != 0):
    print(f"{number - X + 1}/{i - (number - X + 1)}")
else:
    print(f"{i - (number - X + 1)}/{number - X + 1}")