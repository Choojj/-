import sys

N = int(sys.stdin.readline().rstrip())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(N - 1 - i):
        if (num_list[j] > num_list[j + 1]):
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

for i in range(N):
    print(num_list[i])