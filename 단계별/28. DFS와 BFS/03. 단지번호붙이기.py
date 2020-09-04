"""
주변 찾아봐야되니까 map 주변 0으로 감싸기
map 돌면서 1이면 0으로 바꾸고 주변 1 스택이나 q에 넣기
dfs or bfs
스택이나 큐비면 다시 돌면서 1찾기
다돌면 종료
"""

import sys, collections

def DFS(gragh, start):
    stack = []
    visited = []

    stack.append(start)
    while (stack):
        upper = stack.pop()
        if (upper not in visited):
            visited.append(upper)
            stack.extend(reversed(gragh[upper]))

    return visited

def BFS(gragh, start):
    queue = collections.deque()
    visited = []

    queue.append(start)
    while (queue):
        upper = queue.popleft()
        if (upper not in visited):
            visited.append(upper)
            queue.extend(gragh[upper])
    
    return visited


N = int(sys.stdin.readline())

map = [[0 * N] + list(map(int, sys.stdin.readline().rstrip())) + [0 * N] for _ in range(N)]
map.insert(0, [0] * (N + 2))
map.append([0] * (N + 2))

# print(*map, sep = "\n")

apartment_complexes = []
for i in range(1, len(map) - 1):
    for j in range(1, len(map[i]) - 1):
        if (map[i][j]):
            # print(i, j)
            queue = collections.deque()
            count = 0

            map[i][j] = 0
            queue.append([i, j])
            while (queue):
                x, y = queue.popleft()
                if (map[x + 1][y]):
                    queue.append([x + 1, y])
                    map[x + 1][y] = 0
                if (map[x][y + 1]):
                    queue.append([x, y + 1])
                    map[x][y + 1] = 0
                if (map[x - 1][y]):
                    queue.append([x - 1, y])
                    map[x - 1][y] = 0
                if (map[x][y - 1]):
                    queue.append([x, y - 1])
                    map[x][y - 1] = 0
                
                count += 1
            
            apartment_complexes.append(count)

apartment_complexes.sort()

print(len(apartment_complexes))
print(*apartment_complexes, sep = "\n")