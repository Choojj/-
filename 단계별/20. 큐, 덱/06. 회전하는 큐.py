"""
왼쪽, 오른쪽 중 적은 쪽으로 회전 결정
"""

import sys

N, M = map(int, sys.stdin.readline().split())
select_list = list(map(int, sys.stdin.readline().split()))
rotary_queue = [i + 1 for i in range(N)]

def rotation_left(queue):
    queue.append(queue[0])
    queue.pop(0)
def rotation_right(queue):
    queue.insert(0, queue[-1])
    queue.pop()
count = 0
for _ in range(M):

    if (rotary_queue.index(select_list[0]) <= len(rotary_queue) // 2):
        while (rotary_queue[0] != select_list[0]):
            rotation_left(rotary_queue)
            count += 1
        select_list.pop(0)
        rotary_queue.pop(0)
    else:
        while (rotary_queue[0] != select_list[0]):
            rotation_right(rotary_queue)
            count += 1
        select_list.pop(0)
        rotary_queue.pop(0)

print(count)