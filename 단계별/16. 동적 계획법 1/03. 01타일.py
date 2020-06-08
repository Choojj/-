import sys

N = int(sys.stdin.readline())

memo = [0] * (N)

for i in range(N):
    if (i == 0):
        memo[i] = 1
    elif (i == 1):
        memo[i] = 2
    else:
        memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

print(memo[N - 1])