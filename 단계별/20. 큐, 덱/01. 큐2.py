"""
import sys

N = int(sys.stdin.readline())

queue = []
for _ in range(N):
    command = sys.stdin.readline().split()

    if (command[0] == "push"):
        queue.append(command[1])
    elif (command[0] == "pop"):
        if (queue):
            print(queue.pop(0))
        else:
            print(-1)
    elif (command[0] == "size"):
        print(len(queue))
    elif (command[0] == "empty"):
        if (queue):
            print(0)
        else:
            print(1)
    elif (command[0] == "front"):
        if (queue):
            print(queue[0])
        else:
            print(-1)
    elif (command[0] == "back"):
        if (queue):
            print(queue[-1])
        else:
            print(-1)


pop은 리스트 리빌딩해야되서 오래걸림 -> 디큐사용할것

그냥 삭제하지 않고 리스트 시작점을 변수로 줘서 팝할때마다 1씩 추가함
1 2 3       ->      (1) 2 3
^                       ^
1번째부터 시작 / 두번째부터 시작
"""

import sys

N = int(sys.stdin.readline())

queue = []
starting_point = 0
for _ in range(N):
    command = sys.stdin.readline().split()

    if (command[0] == "push"):
        queue.append(command[1])
    elif (command[0] == "pop"):
        if (len(queue) > starting_point):
            print(queue[starting_point])
            starting_point += 1
        else:
            print(-1)
    elif (command[0] == "size"):
        print(len(queue) - starting_point)
    elif (command[0] == "empty"):
        if (len(queue) > starting_point):
            print(0)
        else:
            print(1)
    elif (command[0] == "front"):
        if (len(queue) > starting_point):
            print(queue[starting_point])
        else:
            print(-1)
    elif (command[0] == "back"):
        if (len(queue) > starting_point):
            print(queue[-1])
        else:
            print(-1)