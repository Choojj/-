"""
2개의 정점(A, B)을 경유하는 최단경로
시작 -> A -> B -> 마지막
시작 -> B -> A -> 마지막

시작 -> A 최단 = 시작기준 다익스트라 distance[A]
A -> B 최단 = A기준 다익스트라 distance[B]
B -> 마지막 최단 = B기준 다익스트라 distance[마지막]
"""

import sys, heapq

N, E = map(int, sys.stdin.readline().split())

adjacency_list = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())

    adjacency_list[a].append([b, c])
    adjacency_list[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())
point_list = [1, v1, v2, N]
# print(point_list)

distance_list = []
for i in range(3):
    distance = [float("inf") for _ in range(N + 1)]
    distance[point_list[i]] = 0
    heap = []
    heapq.heappush(heap, [0, point_list[i]])

    while (heap):
        curr_dist, curr_point = heapq.heappop(heap)

        for i in adjacency_list[curr_point]:
            if (distance[i[0]] > curr_dist + i[1]):
                distance[i[0]] = curr_dist + i[1]
                heapq.heappush(heap, [distance[i[0]], i[0]])

    distance_list.append(distance[1:])

# print(distance_list)

answer1 = distance_list[0][v1 - 1] + distance_list[1][v2 - 1] + distance_list[2][N - 1]
answer2 = distance_list[0][v2 - 1] + distance_list[2][v1 - 1] + distance_list[1][N - 1]

if (answer1 == answer2 == float("inf")):
    print(-1)
else:
    print(min(answer1, answer2))