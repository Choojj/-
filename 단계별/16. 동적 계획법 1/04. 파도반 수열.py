import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())

    memo = [0] * (N)

    for i in range(N):
        if (i < 3):
            memo[i] = 1
        elif (i == 3):
            memo[i] = 2
        else:
            memo[i] = memo[i - 1] + memo[i - 5]

    print(memo[N - 1])