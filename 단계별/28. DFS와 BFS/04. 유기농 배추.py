import sys, collections

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    field = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        field[x + 1][y + 1] = 1
    # print(*field, sep = "\n")

    count = 0
    for i in range(1, len(field) - 1):
        for j in range(1, len(field[i]) - 1):
            if (field[i][j]):
                queue = collections.deque()

                field[i][j] = 0
                queue.append([i, j])
                while (queue):
                    x, y = queue.popleft()
                    if (field[x + 1][y]):
                        queue.append([x + 1, y])
                        field[x + 1][y] = 0
                    if (field[x][y + 1]):
                        queue.append([x, y + 1])
                        field[x][y + 1] = 0
                    if (field[x - 1][y]):
                        queue.append([x - 1, y])
                        field[x - 1][y] = 0
                    if (field[x][y - 1]):
                        queue.append([x, y - 1])
                        field[x][y - 1] = 0
                    
                count += 1
    print(count)