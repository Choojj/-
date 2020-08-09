"""
1 2 3 4 5 6
2 3 4 5 6
3 4 5 6 2
4 5 6 2
5 6 2 4
6 2 4
2 4 6
4 6
6 4
4

1 2 3 4 5
2 3 4 5
3 4 5 2
4 5 2
5 2 4
2 4
4 2
2
"""
import sys

N = int(sys.stdin.readline())

card_list = [i for i in range(1, N + 1)]

curr_num = 0
while (len(card_list) - curr_num > 1):
    curr_num += 1

    card_list.append(card_list[curr_num])
    curr_num += 1

print(card_list[-1])