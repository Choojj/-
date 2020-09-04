import sys, collections

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

gragh = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    gragh[x].append(y)
    gragh[y].append(x)

for i in gragh:
    i.sort()

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

# print()
a, b = DFS(gragh, 1), BFS(gragh, 1)
print(len(b) - 1)

#????? dfs와 bfs에서는 틀렸다고 떳는데 여기서는 둘다 맞다고 뜨네 뭐가문제지 ㄷ