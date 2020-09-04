"""
시작점 -> 경유점1 -> 경유점2 -> 목적지 후보
시작점 -> 경유점2 -> 경유점1 -> 목적지 후보
가
시작점 -> 목적지 후보 보다 짧으면 추가

????????

한케이스당 다익스트라 3번

2출발 / 5 or 6 도착 / 1-3 필수경유

3ㅡㅡㅡㅡ6
| \   / |
|   4ㅡㅡ5
|     \ |
1ㅡㅡㅡㅡ2

2출발 다익스트라 / 1 0 4 4 5 6
5최소 = 5, 6최소 = 6

1출발 다익스트라 / 0 1 3 5 6 5
3출발 다익스트라 / 3 4 0 3 7 2

2 -> 1 -> 3 -> 5, 6
  1    3       7  2 11, 6

2 -> 3 -> 1 -> 5, 6
  4    3       6  5 13, 12

-> 5는 11, 13으로 모두 최소인 5보다 크므로 X
   6은 6, 12로 최소인 6과 같거나 크므로 O
   
"""

import sys, heapq

for _ in range(int(sys.stdin.readline())):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    adjacency_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())

        adjacency_list[a].append([b, d])
        adjacency_list[b].append([a, d])

    destination_list = []
    for _ in range(t):
        destination_list.append(sys.stdin.readline())


    distance = [float("inf") for _ in range(n + 1)]
    distance[s] = 0

    heap = []
    heapq.heappush(heap, [0, s])

    while (heap):
        curr_dist, curr_point = heapq.heappop(heap)

        for i in adjacency_list[curr_point]:
            if (distance[i[0]] > curr_dist + i[1]):
                distance[i[0]] = curr_dist + i[1]
                heapq.heappush(heap, [distance[i[0]], i[0]])
    
    print(*distance[1:])
