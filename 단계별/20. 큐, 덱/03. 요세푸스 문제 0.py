"""
1 2 3 4 5 6 7

1 2 3 4 5 6 7 8 9 10
"""

import sys

N, K = map(int, sys.stdin.readline().split())

num_list = [i for i in range(1, N + 1)]

i = 0
answer_list = []
while (len(num_list) > 1):
    if (K == 1):
        break

    for num in num_list:
        i += 1

        if (i % K == 0):
            if (num != num_list[-1]):
                i += 1

            num_list.remove(num)
            answer_list.append(num)

answer_list += num_list

print("<", end = "")
for i in range(N):
    if (i == N - 1):
        print(answer_list[i], end = ">")
    else:
        print(answer_list[i], end = ", ")