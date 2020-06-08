import sys

remainder_list = []

for i in range(10):
    N = int(sys.stdin.readline())

    remainder_list.append(N % 42)

remainder_list.sort()
count = 1

for i in range(1, 10):
    if (remainder_list[i - 1] != remainder_list[i]):
        count += 1

print(count)