"""
다익스트라, 벨만, 플로이드 , SPFA??

다익스트라

시작정점을 기준으로 각 정점의 최소비용을 저장
미방문정점 중 최소비용 정점 선택
선택한 정점을 기준으로 최소비용 갱신
반복

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

adjacency_list = [[]
                  [[2, 2], [3, 3]]
                  [[3, 4], [4, 5]]
                  [[4, 6]]
                  []
                  [[1, 1]]]
distance = [inf, 0, inf, inf, inf, inf]
visited = [0, 0, 0, 0, 0, 0]

시작정점 = 1
adjacency_list[1] = [2, 2], [3, 3] / 1 -> 2로 비용 2, 1 -> 3으로 비용 3
distance = [inf, 0, 2, 3, inf, inf]
visited = [0, 1, 0, 0, 0, 0]
미방문정점 중 최소 비용을 가진 정점을 다음시작정점으로 지정

시작정점 = 2
adjacency_list[2] = [3, 4], [4, 5] / 2 -> 3으로 비용 4, 2 -> 4로 비용 5
1 -> 2 -> 3 = 2 + 4 = 6 원래 비용인 3과 2를 거친 6을 비교 min(3, 6)
1 -> 2 -> 4 = 2 + 5 = 7 원래 비용인 inf와 2를 거친 7을 비교 min(inf, 7)
distance = [inf, 0, 2, 3, 7, inf]
visited = [0, 1, 1, 0, 0, 0]
미방문정점 중 최소 비용을 가진 정점을 다음시작정점으로 지정

시작정점 = 3
adjacency_list[3] = [4, 6] / 3 -> 4로 비용 6
1 -> 3 -> 4 = 3 + 6 = 9 원래 비용인 7과 2를 거친 9를 비교 min(7, 9)
distance = [inf, 0, 2, 3, 7, inf]
visited = [0, 1, 1, 1, 0, 0]
미방문정점 중 최소 비용을 가진 정점을 다음시작정점으로 지정

시작정점 = 4
adjacency_list[4] = []
distance = [inf, 0, 2, 3, 7, inf]
visited = [0, 1, 1, 1, 1, 0]
미방문정점 중 최소 비용을 가진 정점을 다음시작정점으로 지정

시작정점 = 5
adjacency_list[5] = [1, 1] / 5 -> 1로 비용 1
...

import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

adjacency_list = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    adjacency_list[u].append([v, w])

distance = [float("INF") for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]
distance[K] = 0
# print(*adjacency_list, sep = "\n")
# print(distance)
# print(visited)
# print()

curr_point = K
for _ in range(V):
    for i in adjacency_list[curr_point]:
        point_num, cost = i[0], i[1]

        # print(distance[point_num], cost)
        distance[point_num] = min(distance[point_num], cost + distance[curr_point])

    # print(curr_point)
    # print(*adjacency_list, sep = "\n")
    # print(distance)
    
    visited[curr_point] = 1

    curr_point = float("inf")
    for i in range(1, V + 1):
        if (not visited[i] and distance[i] <= curr_point):
            curr_point = i

    # print(visited)
    # print()

print(*distance[1:], sep = "\n")

시간 초과
for문 두번돌려서 그런가보다
큐나 힙써서 해야할듯
근데 맞는데 시간초과인지 틀린데 시간초과인지...

최소힙에 distance 넣어두고
while (heap)
curr_point를 heap[0]으로 초기화
"""

import sys, heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

adjacency_list = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    adjacency_list[u].append([v, w])

distance = [float("inf") for _ in range(V + 1)]
distance[K] = 0

# print(*adjacency_list, sep = "\n")
# print(distance)
# print()

heap = []
heapq.heappush(heap, [0, K])

while (heap):
    # print(heap)
    curr_dist, curr_point = heapq.heappop(heap)
    # print(curr_dist, curr_point)
    # print()

    for i in adjacency_list[curr_point]:
        if (distance[i[0]] > curr_dist + i[1]):
            distance[i[0]] = curr_dist + i[1]
            heapq.heappush(heap, [distance[i[0]], i[0]])

# print(*distance[1:], sep = "\n")

for i in distance[1:]:
    if (i == float("inf")):
        print("INF")
    else:
        print(i)