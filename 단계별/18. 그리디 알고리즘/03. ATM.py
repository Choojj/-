import sys

N = int(sys.stdin.readline())

atm_time = list(map(int, sys.stdin.readline().split()))

atm_time.sort()

using_time = 0
sum_time = 0

for i in range(N):
    using_time += atm_time[i]
    sum_time += using_time

print(sum_time)