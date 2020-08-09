import sys
import math

N = int(sys.stdin.readline())

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

while(True):
    if (N == 1):
        break

    else:
        if (Prime_Check(N)):
            print(N)
            break

        for i in range(2, N):
            if (N % i == 0):
                N //= i
                print(i)
                break