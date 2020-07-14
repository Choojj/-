import sys

N = int(sys.stdin.readline().rstrip())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()

for i in num_list:
    print(i)