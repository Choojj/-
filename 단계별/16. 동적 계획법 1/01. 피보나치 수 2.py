import sys

n = int(sys.stdin.readline())

memo = [0] * (n + 1)

def Fibonacci(num):
    global memo

    if (num == 0):
        memo[num] = 0
        return memo[num]
    elif (num < 3):
        memo[num] = 1
        return memo[num]
    else:
        if (memo[num] == 0):
            memo[num] = Fibonacci(num - 1) + Fibonacci(num - 2)
        return memo[num]

print(Fibonacci(n))