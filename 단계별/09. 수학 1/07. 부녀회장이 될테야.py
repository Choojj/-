import sys

memo = []

def get_apt_residents(k, n):
    if (k < 1):
        return n

    if (memo[k][n] != 0):
        return memo[k][n]
    else:
        residents_sum = 0

        for j in range(n + 1):
            residents_sum += get_apt_residents(k - 1, j)

        memo[k][n] = residents_sum
        return memo[k][n]

T = int(sys.stdin.readline().rstrip())

for i in range(15):
    memo.append([])
    for j in range(15):
        memo[i].append(0)

for i in range(T):
    K = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())

    print(get_apt_residents(K, N))