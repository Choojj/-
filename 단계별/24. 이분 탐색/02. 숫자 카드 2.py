"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()
# print(A)
for num in B:
    first = 0
    last = len(A) - 1
    count = 0

    while (True):
        mid = (first + last) // 2

        if (first > last):
            sys.stdout.write(str(0) + " ")
            break

        if (A[mid] > num):
            last = mid - 1
        elif (A[mid] < num):
            first = mid + 1
        else:
            i = mid
            while(i <= len(A) - 1 and num == A[i]):
                # print("+", count, num, A[i], i, i <= len(A) - 1, num == A[i])
                count += 1
                i += 1
            i = mid - 1
            while(i >= 0 and num == A[i]):
                # print("-", count, num, A[i], i, i <= len(A) - 1, num == A[i])
                count += 1
                i -= 1

            sys.stdout.write(str(count) + " ")
            break

2차원 리스트에 정렬해야하나
"""

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()
sorted_list = []
prev_a = float("inf")
sorted_list_count = -1
for i in range(len(A)):
    if (A[i] != prev_a):
        sorted_list.append([A[i], 1])

        prev_a = A[i]
        sorted_list_count += 1
    else:
        sorted_list[sorted_list_count][1] += 1

# print(sorted_list)

for num in B:
    first = 0
    last = len(sorted_list) - 1

    while (True):
        mid = (first + last) // 2

        if (first > last):
            sys.stdout.write(str(0) + " ")
            break

        if (sorted_list[mid][0] > num):
            last = mid - 1
        elif (sorted_list[mid][0] < num):
            first = mid + 1
        else:
            sys.stdout.write(str(sorted_list[mid][1]) + " ")
            break