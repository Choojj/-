"""
??????

벽을 하나씩 길로 만들어서 돌리면 안될테고

1. 벽 안뚫어도 최단거리로 갈수있는경우
0 1 0
0 1 0
0 0 0
2. 벽 안뚫어도 갈수는있지만 뚫으면 최단거리인 경우
0 1 0 0 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 0 0 1 0
3. 벽을 뚫어야만 갈수 있는경우
0 1 0
1 1 0
0 0 0
4. 갈 수 없는 경우
0 1 1 
1 1 1
1 1 0

벽을 언제뚫어야하는지를 알수가없는데 bfs에 벽을 뚫은 경우까지 넣으면되나?

                                   0,0,F
                                   0 1 0 0
                                   1 1 1 0
                                   1 0 0 0
                                   0 0 0 0
                                   0 1 1 1
                                   0 0 0 0

                              1,0,T     0,1,T
                              1 1 0 0   1 1 0 0
                              1 1 1 0   1 1 1 0
                              1 0 0 0   1 0 0 0
                              0 0 0 0   0 0 0 0
                              0 1 1 1   0 1 1 1
                              0 0 0 0   0 0 0 0

                                END     0,2,T  
                                        1 1 1 0
                                        1 1 1 0
                                        1 0 0 0
                                        0 0 0 0
                                        0 1 1 1
                                        0 0 0 0

                                        0,3,T  
                                        1 1 1 1
                                        1 1 1 0
                                        1 0 0 0
                                        0 0 0 0
                                        0 1 1 1
                                        0 0 0 0

                                        1,3,T  
                                        1 1 1 1
                                        1 1 1 1
                                        1 0 0 0
                                        0 0 0 0
                                        0 1 1 1
                                        0 0 0 0

                                        2,3,T  
                                        1 1 1 1
                                        1 1 1 1
                                        1 0 0 1
                                        0 0 0 0
                                        0 1 1 1
                                        0 0 0 0

                  2,2,T                                       3,3,T  
                  1 1 1 1                                     1 1 1 1
                  1 1 1 1                                     1 1 1 1
                  1 0 1 1                                     1 0 0 1
                  0 0 0 0                                     0 0 0 1
                  0 1 1 1                                     0 1 1 1
                  0 0 0 0                                     0 0 0 0

     2,1,T                      3,2,T                         3,2,T  
     1 1 1 1                    1 1 1 1                       1 1 1 1
     1 1 1 1                    1 1 1 1                       1 1 1 1
     1 1 1 1                    1 0 1 1                       1 0 0 1
     0 0 0 0                    0 0 1 0                       0 0 1 1
     0 1 1 1                    0 1 1 1                       0 1 1 1
     0 0 0 0                    0 0 0 0                       0 0 0 0

     3,1,T               3,1,T          3,3,T          3,1,T          2,2,T  
     1 1 1 1             1 1 1 1        1 1 1 1        1 1 1 1        1 1 1 1
     1 1 1 1             1 1 1 1        1 1 1 1        1 1 1 1        1 1 1 1
     1 1 1 1             1 0 1 1        1 0 1 1        1 0 0 1        1 0 1 1
     0 1 0 0             0 1 1 0        0 0 1 1        0 1 1 1        0 0 1 1
     0 1 1 1             0 1 1 1        0 1 1 1        0 1 1 1        0 1 1 1
     0 0 0 0             0 0 0 0        0 0 0 0        0 0 0 0        0 0 0 0

3,0,T     3,2,T     2,1,T     3,0,T       END     2,1,T     3,0,T     2,1,T  
1 1 1 1   1 1 1 1   1 1 1 1   1 1 1 1             1 1 1 1   1 1 1 1   1 1 1 1
1 1 1 1   1 1 1 1   1 1 1 1   1 1 1 1             1 1 1 1   1 1 1 1   1 1 1 1
1 1 1 1   1 1 1 1   1 1 1 1   1 0 1 1             1 1 0 1   1 0 0 1   1 1 1 1
1 1 0 0   0 1 1 0   0 1 1 0   1 1 1 0             0 1 1 1   1 1 1 1   0 0 1 1
0 1 1 1   0 1 1 1   0 1 1 1   0 1 1 1             0 1 1 1   0 1 1 1   0 1 1 1
0 0 0 0   0 0 0 0   0 0 0 0   0 0 0 0             0 0 0 0   0 0 0 0   0 0 0 0

4,0,T     3,3,T       END     4,0,T                 2,2,T     4,0,T          3,1,T  
1 1 1 1   1 1 1 1             1 1 1 1               1 1 1 1   1 1 1 1        1 1 1 1
1 1 1 1   1 1 1 1             1 1 1 1               1 1 1 1   1 1 1 1        1 1 1 1
1 1 1 1   1 1 1 1             1 0 1 1               1 1 1 1   1 0 0 1        1 1 1 1
1 1 0 0   0 1 1 1             1 1 1 0               0 1 1 1   1 1 1 1        0 1 1 1
1 1 1 1   0 1 1 1             1 1 1 1               0 1 1 1   1 1 1 1        0 1 1 1
0 0 0 0   0 0 0 0             0 0 0 0               0 0 0 0   0 0 0 0        0 0 0 0

5,0,T       END               5,0,T                   END     5,0,T          3,0,T  
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 0 1 1                         1 0 0 1        1 1 1 1
1 1 0 0                       1 1 1 0                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        0 1 1 1
1 0 0 0                       1 0 0 0                         1 0 0 0        0 0 0 0

5,1,T                         5,1,T                           5,1,T          4,0,T  
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 0 1 1                         1 0 0 1        1 1 1 1
1 1 0 0                       1 1 1 0                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 0 0                       1 1 0 0                         1 1 0 0        0 0 0 0

5,2,T                         5,2,T                           5,2,T          5,0,T  
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 0 1 1                         1 0 0 1        1 1 1 1
1 1 0 0                       1 1 1 0                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 0                       1 1 1 0                         1 1 1 0        1 0 0 0

5,3,T                         5,3,T                           5,3,T          5,1,T  
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 0 1 1                         1 0 0 1        1 1 1 1
1 1 0 0                       1 1 1 0                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 1 1
1 1 1 1                       1 1 1 1                         1 1 1 1        1 1 0 0

  END                           END                             END          5,2,T  
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 0
  
                                                                             5,3,T  
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
                                                                             1 1 1 1
  
                                                                               END

범위가 리스트내 / 리스트내용이 0이면 = 한번도 간적이 없으면 / break_wall이 Faslse면 벽통과 -> 방문과 벽 구분해야함


import sys, collections

N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# print(*maze, sep = "\n")

queue = collections.deque()

maze[0][0] = 2
queue.append([0, 0, 1, False])
while (queue):
    x, y, count, break_wall = queue.popleft()

    if (x == N - 1 and y == M - 1):
        break

    print(x, y, count, break_wall)
    print(queue)
    print(*maze, sep = "\n")
    print()

    if (0 <= x + 1 < N):
        if (not break_wall and maze[x + 1][y] == 1):
            queue.append([x + 1, y, count + 1, not break_wall])
        if (maze[x + 1][y] == 0):
            queue.append([x + 1, y, count + 1, break_wall])

        maze[x + 1][y] = 2
    if (0 <= y + 1 < M):
        if (not break_wall and maze[x][y + 1] == 1):
            queue.append([x, y + 1, count + 1, not break_wall])
        if (maze[x][y + 1] == 0):
            queue.append([x, y + 1, count + 1, break_wall])

        maze[x][y + 1] = 2
    if (0 <= x - 1 < N):
        if (not break_wall and maze[x - 1][y] == 1):
            queue.append([x - 1, y, count + 1, not break_wall])
        if (maze[x - 1][y] == 0):
            queue.append([x - 1, y, count + 1, break_wall])

        maze[x - 1][y] = 2
    if (0 <= y - 1 < M):
        if (not break_wall and maze[x][y - 1] == 1):
            queue.append([x, y - 1, count + 1, not break_wall])
        if (maze[x][y - 1] == 0):
            queue.append([x, y - 1, count + 1, break_wall])

        maze[x][y - 1] = 2

if (maze[N - 1][M - 1] != 2):
    count = -1

print(count)

6 4
0000
1110
1000
0000
0111
0100

미로 하나를 쓰니까 서로 뚫은 벽이 곂쳐서 틀린 답이 나오는듯
맵을 여러개로 나누어야하느?

맵을 바꾸지말고 리스트하나를 만들어서 쭉 저장해야하는게 나은가?
"""

import sys, collections

N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# print(*maze, sep = "\n")

queue = collections.deque()

queue.append([0, 0, 1, 0])
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
# print(*visited, sep = "\n")
while (queue):
    x, y, count, break_wall = queue.popleft()

    # print(x, y, count, break_wall)
    # print(queue)
    # print(*visited, sep = "\n")
    # print()

    if (x == N - 1 and y == M - 1):
        break

    # x, y, break_wall -> visited에 동기화
    # 리스트 범위내 and 안부숨 방문 X and 길로감 -> 안부숨 방문에 x, y, count + 1, break_wall
    # 리스트 범위내 and 안부숨 방문 X and 벽으로감 -> 부숨 방문에 x, y, count + 1, break_wall + 1
    # 리스트 범위내 and 부숨 방문 X and 길로감 -> 부숨 방문에 x, y, count + 1, break_wall

    # 돌면서 체크하는데 길이면 가고 벽이면 break_wall = 0이면 부수고 아니면 못가고

    if (0 <= x + 1 < N): # 리스트범위내고
        if (break_wall == 0): # 벽을 부순적이 없고
            if (maze[x + 1][y] == 0): # 길이고
                if (visited[x + 1][y][break_wall] == 0): # 방문한적이 없으면
                    queue.append([x + 1, y, count + 1, break_wall])
                    visited[x + 1][y][break_wall] = 1
            if (maze[x + 1][y] == 1): # 벽이고
                if (visited[x + 1][y][break_wall + 1] == 0): # 방문한적이 없으면
                    queue.append([x + 1, y, count + 1, break_wall + 1])
                    visited[x + 1][y][break_wall + 1] = 1
        if (break_wall == 1): # 벽을 부쉈고
            if (maze[x + 1][y] == 0): # 길이고
                if (visited[x + 1][y][break_wall] == 0): # 방문한적이 없으면
                    queue.append([x + 1, y, count + 1, break_wall])
                    visited[x + 1][y][break_wall] = 1
        
    if (0 <= y + 1 < M):
        if (break_wall == 0):
            if (maze[x][y + 1] == 0):
                if (visited[x][y + 1][break_wall] == 0):
                    queue.append([x, y + 1, count + 1, break_wall])
                    visited[x][y + 1][break_wall] = 1
            if (maze[x][y + 1] == 1):
                if (visited[x][y + 1][break_wall + 1] == 0):
                    queue.append([x, y + 1, count + 1, break_wall + 1])
                    visited[x][y + 1][break_wall + 1] = 1
        if (break_wall == 1):
            if (maze[x][y + 1] == 0):
                if (visited[x][y + 1][break_wall] == 0):
                    queue.append([x, y + 1, count + 1, break_wall])
                    visited[x][y + 1][break_wall] = 1

    if (0 <= x - 1 < N):
        if (break_wall == 0):
            if (maze[x - 1][y] == 0):
                if (visited[x - 1][y][break_wall] == 0):
                    queue.append([x - 1, y, count + 1, break_wall])
                    visited[x - 1][y][break_wall] = 1
            if (maze[x - 1][y] == 1):
                if (visited[x - 1][y][break_wall + 1] == 0):
                    queue.append([x - 1, y, count + 1, break_wall + 1])
                    visited[x - 1][y][break_wall + 1] = 1
        if (break_wall == 1):
            if (maze[x - 1][y] == 0):
                if (visited[x - 1][y][break_wall] == 0):
                    queue.append([x - 1, y, count + 1, break_wall])
                    visited[x - 1][y][break_wall] = 1
        
    if (0 <= y - 1 < M):
        if (break_wall == 0):
            if (maze[x][y - 1] == 0):
                if (visited[x][y - 1][break_wall] == 0):
                    queue.append([x, y - 1, count + 1, break_wall])
                    visited[x][y - 1][break_wall] = 1
            if (maze[x][y - 1] == 1):
                if (visited[x][y - 1][break_wall + 1] == 0):
                    queue.append([x, y - 1, count + 1, break_wall + 1])
                    visited[x][y - 1][break_wall + 1] = 1
        if (break_wall == 1):
            if (maze[x][y - 1] == 0):
                if (visited[x][y - 1][break_wall] == 0):
                    queue.append([x, y - 1, count + 1, break_wall])
                    visited[x][y - 1][break_wall] = 1

if (visited[N - 1][M - 1][0] == 0 and visited[N - 1][M - 1][1] == 0):
    count = -1

print(count)