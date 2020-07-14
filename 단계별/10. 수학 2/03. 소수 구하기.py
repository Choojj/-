import sys
import math

M, N = map(int, sys.stdin.readline().rstrip().split())

num_list = [False,False] + [True]*(N-1)

prime_list=[]

for i in range(2, N + 1):
    if num_list[i]:
        prime_list.append(i)

        for j in range(2 * i, N + 1, i):
            num_list[j] = False

for i in prime_list:
    if (M <= i <= N):
        print(i)