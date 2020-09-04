import sys, collections

M, N, H = map(int, sys.stdin.readline().split())

box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

# print()
# for i in box:
#     for j in i:
#         for k in j:
#             print("%2d" % k, end = " ")
#         print()
#     print()

queue = collections.deque()

for i in range(len(box)):
    for j in range(len(box[i])):
        for k in range(len(box[i][j])):
            if (box[i][j][k] == 1):
                queue.append([i, j, k, 0])

# print(queue)

while (queue):
    z, y, x, count = queue.popleft()

    if (0 <= z + 1 < H and not box[z + 1][y][x]):
        queue.append([z + 1, y, x, count + 1])
        box[z + 1][y][x] = 1
    if (0 <= y + 1 < N and not box[z][y + 1][x]):
        queue.append([z, y + 1, x, count + 1])
        box[z][y + 1][x] = 1
    if (0 <= x + 1 < M and not box[z][y][x + 1]):
        queue.append([z, y, x + 1, count + 1])
        box[z][y][x + 1] = 1
    if (0 <= z - 1 < H and not box[z - 1][y][x]):
        queue.append([z - 1, y, x, count + 1])
        box[z - 1][y][x] = 1
    if (0 <= y - 1 < N and not box[z][y - 1][x]):
        queue.append([z, y - 1, x, count + 1])
        box[z][y - 1][x] = 1
    if (0 <= x - 1 < M and not box[z][y][x - 1]):
        queue.append([z, y, x - 1, count + 1])
        box[z][y][x - 1] = 1

    # print(z, y, x, count, queue)
    # for i in box:
    #     for j in i:
    #         for k in j:
    #             print("%2d" % k, end = " ")
    #         print()
    #     print()

for i in box:
    for j in i:
        for k in j:
            if (k == 0):
                count = -1
                break
print(count)