import sys

num_sum = 0

N = int(sys.stdin.readline().rstrip())
num = sys.stdin.readline().rstrip()

for i in range(N):
    num_sum += int(num[i])

print(num_sum)