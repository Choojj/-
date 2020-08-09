"""
4 30
800
700
600
500

max = 800에서 이분 탐색 시작

400 200 100 50 75 87 81 84 82 83 --->
  5  12  26 52 32 28 30 29 30 83
적으면 last 갱신
많으면 first 갱신
"""

import sys

K, N = map(int, sys.stdin.readline().split())
cable_list = []
for _ in range(K):
    cable_list.append(int(sys.stdin.readline()))

cable_list.sort()

first = 1 # 1,1 / 1 입력시 mid = 0 가능성
last = cable_list[-1]
while (True):
    if (first > last):
        break

    mid = (first + last) // 2
    cable_num = 0
    for cable in cable_list:
        cable_num += cable // mid

    if (N > cable_num):
        last = mid - 1
    if (N <= cable_num):
        first = mid + 1
        answer = mid
    
    # print(mid, cable_num)

print(answer)