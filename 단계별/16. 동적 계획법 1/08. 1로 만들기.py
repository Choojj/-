"""
n -> n-1, n/2, n/3
n-1 -> list[n-1] + 횟수 1 추가
n/2 -> list[n/1] + 횟수 1 추가
n/3 -> list[n/2] + 횟구 1 추가
 1 
 2 1
 3 1
 4 2 1
 5 4 2 1
 6 2 1
 7 6 2 1
 8 4 2 1
 9 3 1
10 9 3 1
"""
import sys

N = int(sys.stdin.readline())

count_making_one = [0] + [-1 for _ in range(N)]

for i in range(1, N + 1):
    if (i < 2):
        count_making_one[i] = 0
    elif (i == 2):
        count_making_one[i] = 1
    elif (i == 3):
        count_making_one[i] = 1
    else:
        if (i % 6 == 0):
            count_making_one[i] = (min(count_making_one[i - 1] + 1, count_making_one[int(i / 2)] + 1, count_making_one[int(i / 3)] + 1))
        elif (i % 3 == 0):
            count_making_one[i] = (min(count_making_one[i - 1] + 1 , count_making_one[int(i / 3)] + 1))
        elif (i % 2 == 0):
            count_making_one[i] = (min(count_making_one[i - 1] + 1 , count_making_one[int(i / 2)] + 1))
        else:
            count_making_one[i] = count_making_one[i - 1] + 1

print(count_making_one[-1])