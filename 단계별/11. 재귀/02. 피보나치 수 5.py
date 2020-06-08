import sys

def pibonacci(num):
    if (num == 0):
        return 0
    elif (num < 3):
        return 1
    else:
        return pibonacci(num - 1) + pibonacci(num - 2)

N = int(sys.stdin.readline().rstrip())

print(pibonacci(N))