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

num_list = [False,False] + [True] * (246911)

prime_list = []

for i in range(2, 246913):
    if num_list[i]:
        prime_list.append(i)

        for j in range(2 * i, 246913, i):
            num_list[j] = False

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    trig = False

    for i in range(len(prime_list)):
        if (trig == True):
            break

        if (prime_list[i] > N / 2):
            j = i - 1

            while (True):
                part1 = prime_list[j]
                
                if (Prime_Check(N - part1) == True):
                    print(part1, N - part1)
                    trig = True
                    break

                j -= 1