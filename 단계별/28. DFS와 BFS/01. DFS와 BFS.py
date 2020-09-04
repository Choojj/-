"""
import sys

N, M, V = map(int, sys.stdin.readline().split())

gragh = [[False for _ in range(N)] for _ in range(N)]

line_list = []
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    gragh[x - 1][y - 1] = gragh[y - 1][x - 1] = True

#dfs

curr_num = V - 1
visited = [curr_num]
for _ in range(N):
    for i in range(len(gragh[curr_num])):
        # print(curr_num, i, visited)
        if (i not in visited):
            if (gragh[curr_num][i]):
                curr_num = i
                visited.append(curr_num)
                break

for i in visited:
    print(i + 1, end = " ")

끝까지만 가는게 아니라 다 돌아야되는거네 ㄷ


ex) 
dfs -> 깊이 (스택 2개)

   3
 /  \
1    4
|    |
2 ㅡ 5
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0]
[0, 1, 0, 0, 0, 1]
[0, 1, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 1]
[0, 0, 1, 0, 1, 0]

stack = 3
stack에 3추가
stack pop하면서 pop한 3 = upper
upper의 lower 거꾸로 찾아서 stack에 추가
추가하는 lower는 visited에 없을것
끝난 후 upper visited에 추가

stack = 4, 1
stack pop하면서 pop한 1 = upper
upper의 lower 거꾸로 찾아서 stack에 추가
추가하는 lower는 visited에 없을것
끝난 후 upper visited에 추가

stack = 4

다시

# /숫자 -> 스택에서 pop된 숫자
          1 2 5
          4/1/2/5
stack   3/3 4 4 4/4
        ㅡㅡㅡㅡㅡㅡ
visited   3 3 3 3 3
            1 1 1 1
              2 2 2
                5 5
                  4


bfs -> 너비 (큐 1개 스택 1개)
??? 그냥 그래프 보고 돌리면 되는거 아닌가?

   3
 /  \
1    4
|    |
2 ㅡ 5
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0]
[0, 1, 0, 0, 0, 1]
[0, 1, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 1]
[0, 0, 1, 0, 1, 0]

3
3 1 4
1 4
1 4 2
4 2
4 2 5
2 5
5

큐는 답이없네

간선이 이어지지 않은 정점이있는경우
1 ㅡ 2
|  /
 3   4



인접행렬이 인접리스트보다 별로인가?

class Gragh():
    def __init__(self, size, line_size):
        self.size = size + 1
        self.line_size = line_size
        self.gragh = [[0 for i in range(self.size)] for i in range(self.size)]

    def add_line(self, dot1, dot2, one_way = False):
        if (one_way):
            self.gragh[dot1][dot2] = 1
        else:
            self.gragh[dot1][dot2] = self.gragh[dot2][dot1] = 1

    def dfs(self, start):
        stack = [start]
        visited = []
        while (stack):
            upper = stack.pop()
            visited.append(upper)
            print(upper)
            print(stack)
            print(visited)
            for i in range(len(self.gragh[upper]) - 1, -1, -1):
                if (i not in visited and i not in stack and self.gragh[upper][i]):
                    stack.append(i)
            
        return visited # 자기 크기까지만 맞음 뒤에 잘라야함
    
    def bfs(self, start):
        que = queue.Queue()
        que.put(start)
        visited = [start]
        while(que.qsize()):
            upper = que.get()
            for i in range(len(self.gragh[upper])):
                if (i not in visited and self.gragh[upper][i]):
                    visited.append(i)
                    que.put(i)
        
        return visited


import sys, queue

N, M, V = map(int, sys.stdin.readline().split())

dfs_bfs = Gragh(N, M)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    dfs_bfs.add_line(x, y)

# for i in dfs_bfs.gragh:
#     print(i)

dfs, bfs = dfs_bfs.dfs(V), dfs_bfs.bfs(V)
for i in dfs:
    print(i, end = " ")
# print()
# for i in bfs:
#     print(i, end = " ")

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

   3
 /  \
1    4
|    |
2 ㅡ 5
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0]
[0, 1, 0, 0, 0, 1]
[0, 1, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 1]
[0, 0, 1, 0, 1, 0]

dfs
    [3]
    []

    stack.pop and visited.append
    []
    [3]

    인접노드 추가
    [4, 1]
    [3]

    stack.pop and visited.append
    [4]
    [3, 1]

    인접노드 추가
    [4, 2]
    [3, 1]

    stack.pop and visited.append
    [4]
    [3, 1, 2]

    인접노드 추가
    [4, 5]
    [3, 1, 2]

    stack.pop and visited.append
    [4]
    [3, 1, 2, 5]

    stack.pop and visited.append
    []
    [3, 1, 2, 5, 4]
    
    visited로 방문조건 체크를 하면 안됨 체크할게 필요
    **dfs는 스택에 한번에 다넣으면 안됨**
    ex 451 / 12 / 13 / 14 / 24 / 34
    하나씩 넣을것 and 가지친 곳 위치도 기억해야함
    재귀로만 되나?

bfs


인접행렬이 직관적이지만 비효율적 -> 1번노드의 리스트를 모두 뒤져야함


import sys, queue

N, M, V = map(int, sys.stdin.readline().split())

gragh = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    gragh[x].append(y)
    gragh[y].append(x)

# print(*gragh, sep = "\n")

def DFS(gragh, start):
    for i in gragh:
        i.sort(reverse = True)

    stack = []
    visited = []

    stack.append(start)
    while (stack):
        upper = stack.pop()
        if (upper not in visited):
            visited.append(upper)
            stack.extend(gragh[upper])

    return visited

def BFS(gragh, start):
    for i in gragh:
        i.sort()

    que = queue.Queue()
    visited = []

    que.put(start)
    while (que.qsize()):
        upper = que.get()
        if (upper not in visited):
            visited.append(upper)
            for i in gragh[upper]:
                que.put(i)
    
    return visited

# print()
print(DFS(gragh, V))
print(BFS(gragh, V))


하 queue가 멀티쓰레드용이라 너무 늦어서 collections.deque를 사용해야 된단다 위에꺼가 맞았는지 틀렸는지도 모르겠다


import sys, collections

N, M, V = map(int, sys.stdin.readline().split())

gragh = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    gragh[x].append(y)
    gragh[y].append(x)

for i in gragh:
    i.sort()
        
# print(*gragh, sep = "\n")

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
print(DFS(gragh, V))
print(BFS(gragh, V))

모르겟다
"""

def dfs(start):
    if not start in graph :
        print(start, end = ' ')
        return
    visited.append(start)
    print(start, end = ' ')
    for v in graph[start]:
        if v not in visited:
            dfs(v)
    return

def bfs(start):
    if not start in graph :
        print(start)
        return
    visited = [start]
    queue = [start]
    while queue :
        print(queue[0], end = ' ')
        for v in graph[queue.pop(0)]:
            if v not in visited :
                visited.append(v)
                queue.append(v)
    return

n, number_edge, start = map(int, input().split())
graph = {}
for _ in range(number_edge):
    v,w = map(int, input().split())
    if v == w :
        next
    if v in graph :
        graph[v].add(w)
    else :
        graph[v] = {w}
    if w in graph :
        graph[w].add(v)
    else :
        graph[w] = {v}

for u in graph.keys():
    graph[u] = sorted(graph[u])
    
visited = []
dfs(start)
print()
bfs(start)