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

N = int(sys.stdin.readline().rstrip())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0

for i in num_list:
    if (Prime_Check(i) == True):
        count += 1

print(count)