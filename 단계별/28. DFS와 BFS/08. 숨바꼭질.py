"""
                시작
        /        |         \
    x-1         x+1         x*2
  /  |  \     /  |  \     /  |  \
x-1 x+1 x*2 x-1 x+1 x*2 x-1 x+1 x*2

.....
이런식으로 같을때까지 반복
OMG memory

3제곱으로 늘어나니까 너무 많이 먹는건가?

import sys, collections

N, K = map(int, sys.stdin.readline().split())

queue = collections.deque()
queue.append([N, 0])

while (True):
    x, count = queue.popleft()
    if (x == K):
        print(count)
        break

    queue.append([x - 1, count + 1])
    queue.append([x + 1, count + 1])
    queue.append([x * 2, count + 1])

                                             5
                                        ( 4  6 10)
          ( 3  5  8)                    ( 5  7 12)                    ( 9 11 20)
( 2  4  6)( 4  6 10)( 7  9 16)( 4  6 10)( 6  8 14)(11 13 24)
범위제한, 중복방지

모든수는 0 ~ K + 1까지
순간이동 후 뒤로 두칸을 가게되면 뒤로 한칸 간후 순간이동하는것이 더 나음

import sys, collections

N, K = map(int, sys.stdin.readline().split())

queue = collections.deque()
queue.append([N, 0])

visited = [0 for i in range(K + 5)]

while (True):
    x, count = queue.popleft()
    if (x == K):
        print(count)
        break

    print(queue)
    print(visited)
    print(x, count)

    if (0 <= x - 1 <= K + 1 and not visited[x - 1]):
        queue.append([x - 1, count + 1])
        visited[x - 1] = 1
    if (0 <= x + 1 <= K + 1 and not visited[x + 1]):
        queue.append([x + 1, count + 1])
        visited[x + 1] = 1
    if (0 <= x * 2 <= K + 1 and not visited[x * 2]):
        queue.append([x * 2, count + 1])
        visited[x * 2] = 1

동생이 더 뒤에있을수도있네 ㄷ
"""

import sys, collections

N, K = map(int, sys.stdin.readline().split())

queue = collections.deque()
queue.append([N, 0])

max_x = max(N, K)
visited = [0 for i in range(max_x + 2)]

while (True):
    x, count = queue.popleft()
    if (x == K):
        print(count)
        break

    # print(queue)
    # print(visited)
    # print(x, count)

    if (0 <= x - 1 <= max_x + 1 and not visited[x - 1]):
        queue.append([x - 1, count + 1])
        visited[x - 1] = 1
    if (0 <= x + 1 <= max_x + 1 and not visited[x + 1]):
        queue.append([x + 1, count + 1])
        visited[x + 1] = 1
    if (0 <= x * 2 <= max_x + 1 and not visited[x * 2]):
        queue.append([x * 2, count + 1])
        visited[x * 2] = 1