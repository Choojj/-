"""
??
박스를 돌다가 1이면 queue저장
queue 주변에 0이 있으면 queue에 저장
-1이 있으면 X

박스 다 돌고 

토마토는 동시에 익음
박스를 돌면서 확인하는게아니라 익은 토마토를 모두 찾은 후 bfs를 해야함

박스크기를 한개 크게 잡아서 마지막 익은토마토가 한번더 익히는 과정이 있음 count - 1

import sys, collections

N, M = map(int, sys.stdin.readline().split())

box = [[0] * (N + 2)]
for i in range(M):
    box.append([0] + list(map(int, sys.stdin.readline().split())) + [0])
box.append([0] * (N + 2))

# print(*box, sep = "\n")
# print()

queue = collections.deque()

for i in range(len(box)):
    for j in range(len(box[i])):
        if (box[i][j] == 1):
            queue.append([i, j, 0])


while (queue):
    x, y, count = queue.popleft()
    # print(x, y, count)

    if (0 < x <= M and 0 < y <= N):
        if (not box[x + 1][y]):
            queue.append([x + 1, y, count + 1])
            box[x + 1][y] = 1
        if (not box[x][y + 1]):
            queue.append([x, y + 1, count + 1])
            box[x][y + 1] = 1
        if (not box[x - 1][y]):
            queue.append([x - 1, y, count + 1])
            box[x - 1][y] = 1
        if (not box[x][y - 1]):
            queue.append([x, y - 1, count + 1])
            box[x][y - 1] = 1
        
        # print(*box, sep = "\n")
        # print()

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if (box[i][j] == 0):
            count = 0
            break

print(count - 1)

# for i in box:
#     for j in i:
#         print("%2d" % j, end = " ")
#     print()

4 7
1 0 -1 -1
-1 0 0 1
1 0 1 -1
0 -1 -1 -1
-1 1 -1 1
1 1 0 1
1 1 -1 -1
output: 1
correct answer: 2

7 5
0 0 1 0 -1 -1 -1
1 0 0 0 1 -1 1
1 0 1 0 0 -1 0
0 -1 -1 1 -1 0 0
-1 -1 1 1 1 -1 -1
output: 2
correct answer: 3

4 5          0            1            2            3
1 -1 1 0     1 -1  1  0   1 -1  1  1   1 -1  1  1   1 -1  1  1
-1 -1 0 -1  -1 -1  0 -1  -1 -1  1 -1  -1 -1  1 -1  -1 -1  1 -1
0 0 -1 1     0  0 -1  1   0  0 -1  1   1  0 -1  1   1  1 -1  1
0 0 -1 1     0  0 -1  1   1  0 -1  1   1  1 -1  1   1  1 -1  1
1 -1 0 0     1 -1  0  0   1 -1  0  1   1 -1  1  1   1 -1  1  1
output: 2
correct answer: 3
안되네 ㄷ

6 4            0                  1                  2                  3                  4                  5                  6
1 -1 0 0 0 0   1 -1  0  0  0  0   1 -1  0  0  0  0   1 -1  0  0  0  0   1 -1  0  0  0  1   1 -1  0  0  1  1   1 -1  0  1  1  1   1 -1  1  1  1  1
0 -1 0 0 0 0   0 -1  0  0  0  0   1 -1  0  0  0  0   1 -1  0  0  0  1   1 -1  0  0  1  1   1 -1  0  1  1  1   1 -1  1  1  1  1   1 -1  1  1  1  1
0 0 0 0 -1 0   0  0  0  0 -1  0   0  0  0  0 -1  1   1  0  0  0 -1  1   1  1  0  0 -1  1   1  1  1  0 -1  1   1  1  1  1 -1  1   1  1  1  1 -1  1
0 0 0 0 -1 1   0  0  0  0 -1  1   0  0  0  0 -1  1   0  0  0  0 -1  1   1  0  0  0 -1  1   1  1  0  0 -1  1   1  1  1  0 -1  1   1  1  1  1 -1  1

주변에늘린것때문에 더복잡한거같다
"""

import sys, collections

N, M = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# print(*box, sep = "\n")
# print()

queue = collections.deque()

for i in range(len(box)):
    for j in range(len(box[i])):
        if (box[i][j] == 1):
            queue.append([i, j, 0])


while (queue):
    x, y, count = queue.popleft()
    # print(x, y, count)

    if (0 <= x < M and 0 <= y < N):
        if (0 <= x + 1 < M and not box[x + 1][y]):
            queue.append([x + 1, y, count + 1])
            box[x + 1][y] = 1
        if (0 <= y + 1 < N and not box[x][y + 1]):
            queue.append([x, y + 1, count + 1])
            box[x][y + 1] = 1
        if (0 <= x - 1 < M and not box[x - 1][y]):
            queue.append([x - 1, y, count + 1])
            box[x - 1][y] = 1
        if (0 <= y - 1 < N and not box[x][y - 1]):
            queue.append([x, y - 1, count + 1])
            box[x][y - 1] = 1
        
    # print(x, y, count)
    # for i in box:
    #     for j in i:
    #         print("%2d" % j, end = " ")
    #     print()
    # print()

for i in box:
    for j in i:
        if (j == 0):
            count = -1
            break

print(count)