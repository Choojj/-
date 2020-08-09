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
        if (tree - mid > 0):
            tree_num += tree - mid

    if (N > tree_num):
        last = mid - 1
    if (N <= tree_num):
        first = mid + 1
        answer = mid
    
    # print(mid, tree_num)

print(answer)