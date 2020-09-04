"""
다똑같은데 bfs의 동심원 크기를 파악해야함
"""

import sys, collections

N, M = map(int, sys.stdin.readline().split())

maze = [[0 * N] + list(map(int, sys.stdin.readline().rstrip())) + [0 * M] for _ in range(N)]
maze.insert(0, [0] * (M + 2))
maze.append([0] * (M + 2))

# print(*maze, sep = "\n")

queue = collections.deque()

maze[1][1] = 0
queue.append([1, 1, 0])
while (True):
    x, y, count= queue.popleft()
    # print(x, y, count)
    if (x == N and y == M):
        print(count + 1)
        break

    if (maze[x + 1][y]):
        queue.append([x + 1, y, count + 1])
        maze[x + 1][y] = 0
    if (maze[x][y + 1]):
        queue.append([x, y + 1, count + 1])
        maze[x][y + 1] = 0
    if (maze[x - 1][y]):
        queue.append([x - 1, y, count + 1])
        maze[x - 1][y] = 0
    if (maze[x][y - 1]):
        queue.append([x, y - 1, count + 1])
        maze[x][y - 1] = 0