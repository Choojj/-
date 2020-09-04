"""
import sys

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if (x == 0):
        if (heap):
            # delete
            print(heap[0])
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()

            i = lower  = count = 0
            while (len(heap) >= 2 ** (count + 1)):
                trig = False
                if (i * 2 + 1 <= len(heap) - 1 and abs(heap[i]) >= abs(heap[i * 2 + 1])):
                    lower = i * 2 + 1
                if (i * 2 + 2 <= len(heap) - 1 and abs(heap[i]) >= abs(heap[i * 2 + 2])):
                    lower = i * 2 + 2
                    trig = True
                
                if (trig and abs(heap[i * 2 + 1]) < abs(heap[i * 2 + 2])):
                    lower = i * 2 + 1
                elif (trig and abs(heap[i * 2 + 1]) > abs(heap[i * 2 + 2])):
                    lower = i * 2 + 2
                elif (trig and abs(heap[i * 2 + 1]) == abs(heap[i * 2 + 2])):
                    if (heap[i * 2 + 1] <= heap[i * 2 + 2]):
                        lower = i * 2 + 1
                    else:
                        lower = i * 2 + 2

                heap[i], heap[lower] = heap[lower], heap[i]
                # print(i, lower, heap, count)

                i = lower
                count += 1
            pass
        else:
            print(0)
    else:
        # insert

        heap.append(x)
        i = len(heap) - 1
        while (0 <= i):
            upper_i = (i - 1) // 2
            if (0 <= upper_i and abs(heap[upper_i]) > abs(heap[i])):
                heap[i], heap[upper_i] = heap[upper_i], heap[i]
                i = upper_i
            elif (0 <= upper_i and abs(heap[upper_i]) == abs(heap[i]) and heap[upper_i] > heap[i]):
                heap[i], heap[upper_i] = heap[upper_i], heap[i]
                i = upper_i
            else:
                break

        pass

    # print(heap, "----")

대충 바꿨는데 안되네 ㄷ
abs가 시간을 오래잡아먹나?
2차원 리스트로??
"""

import sys

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if (x == 0):
        if (heap):
            # delete

            print(heap[0][1])
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()

            i = lower = count = 0
            while(len(heap) >= 2 ** (count + 1)):
                left, right = i * 2 + 1, i * 2 + 2
                # 하위 노드 값이 리스트 내에 있음 + 현재 값이 하위 노드 값보다 큼
                # 비교값이 절대값이므로 하위노드 값 == 현재값 -> 실제값 비교 필요
                if (left <= len(heap) - 1 and heap[i][0] >= heap[left][0]):
                    lower = left
                if (right <= len(heap) - 1 and heap[i][0] >= heap[right][0]):
                    lower = right

                if (lower == left and heap[i][1] < heap[left][1]):
                    lower = i

                if (lower == right and heap[left][0] < heap[right][0]):
                    lower = left
                elif (lower == right and heap[left][0] > heap[right][0]):
                    lower = right
                elif (lower == right and heap[left][0] == heap[right][0]):
                    if (heap[left][1] <= heap[right][1]):
                        lower = left
                    else:
                        lower = right

                heap[i], heap[lower] = heap[lower], heap[i]

                i = lower
                count += 1

            # i = lower = count = 0
            # while (len(heap) >= 2 ** (count + 1)):
            #     trig = False
            #     if (i * 2 + 1 <= len(heap) - 1 and heap[i] > heap[i * 2 + 1]):
            #         lower = i * 2 + 1
            #     if (i * 2 + 2 <= len(heap) - 1 and heap[i] > heap[i * 2 + 2]):
            #         lower = i * 2 + 2
            #         trig = True
                
            #     if (trig and heap[i * 2 + 1] <= heap[i * 2 + 2]):
            #         lower = i * 2 + 1
            #     elif (trig and heap[i * 2 + 1] > heap[i * 2 + 2]):
            #         lower = i * 2 + 2

            #     heap[i], heap[lower] = heap[lower], heap[i]
            #     # print(i, lower, heap, count)

            #     i = lower
            #     count += 1
            pass
        else:
            print(0)
    else:
        # insert

        heap.append([abs(x), x])
        i = len(heap) - 1
        while (0 <= i):
            upper_i = (i - 1) // 2
            # i값이 리스트내에 있음 + 상위 노드 값 > 현재값 -> 최소 힙이므로 바꿔 줘야함
            # 비교값이 절대 값이므로 상위노드 값 == 현재값 -> 실제값 비교 필요
            if (0 <= upper_i and (heap[upper_i][0] > heap[i][0] or (heap[upper_i][0] == heap[i][0] and heap[upper_i][1] > heap[i][1]))):
                heap[i], heap[upper_i] = heap[upper_i], heap[i]
                i = upper_i
            else:
                break

    print(heap, "----")