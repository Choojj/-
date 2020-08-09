"""
2, 1 -> 6 - 1
(0, 0)
1, 0
2, 0
0, 1
1, 1
2, 1

3 -> 4 - 1
(0)
1
2
3

2, 3, 4 -> 60 - 1
0개 1
1개 2 + 3 + 4
2개 2 * 3 + 3 * 4 + 4 * 2
3개 2 * 3 * 4

a, b, c
0개 1
1개 a + b + c
2개 a * b + b * c + c * a
3개 a * b * c
-> a + b + c + a * b + b + c * c * a + a * b * c + 1
= (a + 1) * (b + 1) * (c + 1)

"""

import sys

N = int(sys.stdin.readline())

for i in range(N):
    costume_num = int(sys.stdin.readline())

    costume_list = []
    for j in range(costume_num):
        _, costume_type = sys.stdin.readline().rstrip().split(" ")

        trig = True
        for k in range(len(costume_list)):
            if(costume_type == costume_list[k][1]):
                costume_list[k][0] += 1
                trig = False

        if (trig == True):
            costume_list.append([1, costume_type])

    result = 1
    for i in range(len(costume_list)):
        result *= costume_list[i][0] + 1

    print(result - 1)