import sys
import math

num_list = [False,False] + [True] * (246911)

prime_list = []

for i in range(2, 246913):
    if num_list[i]:
        prime_list.append(i)

        for j in range(2 * i, 246913, i):
            num_list[j] = False

while (True):
    count = 0
    
    N = int(sys.stdin.readline().rstrip())

    if (N == 0):
        break

    for i in prime_list:
        if (N < i <= 2 * N):
            count += 1

    print(count)