"""
10 50
59 96 84 160 165 149 131 76 20 125
 0  0  0  20  25   9   0  0  0   0

이분탐색 최대 30번
for문 최대 1000000번
-> 최대 30000000번
"""

import sys

K, N = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

tree_list.sort()

first = 0
last = tree_list[-1]
while (True):
    if (first > last):
        break

    mid = (first + last) // 2
    tree_num = 0
    for tree in tree_list:
        cut_wood = tree - mid
        if (cut_wood > 0):
            tree_num += cut_wood

    if (N > tree_num):
        last = mid - 1
    if (N <= tree_num):
        first = mid + 1
    
    # print(mid, tree_num)

print(last)