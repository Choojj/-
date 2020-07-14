import sys
import math

def Prime_Check(num):
    i = 2

    if (num < 2):
        return False
    else:
        while (True):
            if (i <= int(math.sqrt(num))):
                if (num % i == 0):
                    return False
            else:
                return True
            
            i += 1

prime_list = []

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

for i in range(M, N + 1):
    if (Prime_Check(i) == True):
        prime_list.append(i)

if (len(prime_list) == 0):
    print(-1)
else:
    print(sum(prime_list), min(prime_list))