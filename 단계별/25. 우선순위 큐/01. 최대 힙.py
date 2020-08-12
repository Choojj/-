"""
import sys

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if (x == 0):
        if (heap):
            # delete
            heap[0], heap[-1] = heap[-1], heap[0]
            print(heap[-1])
            heap.pop()

            # 자기가 제일 크면 완성
            # 자식이 더 크면 자리바꾸기
            # 둘 다 크면 큰자식이랑 자리 바꾸기

            i = 0
            while (True):
                lower = i
                trig = False
                if (i * 2 + 1 <= len(heap) - 1 and heap[i] < heap[i * 2 + 1]):
                    lower = i * 2 + 1
                if (i * 2 + 2 <= len(heap) - 1 and heap[i] < heap[i * 2 + 2]):
                    lower = i * 2 + 2
                    trig = True
                
                if (trig and heap[i * 2 + 1] >= heap[i * 2 + 2]):
                    lower = i * 2 + 1
                elif (trig and heap[i * 2 + 1] < heap[i * 2 + 2]):
                    lower = i * 2 + 2

                heap[i], heap[lower] = heap[lower], heap[i]

                print(i, lower, heap)
                if (len(heap) <= 2 ** (lower + 1)):
                    break

                i = lower

        else:
            print(0)
    else:
        # insert

        heap.append(x)
        i = len(heap) - 1
        while (0 <= i):
            upper_i = (i - 1) // 2
            if (0 <= upper_i and heap[upper_i] < heap[i]):
                heap[i], heap[upper_i] = heap[upper_i], heap[i]
                i = upper_i
            else:
                break

    print(heap)

너무 많이 고쳐야 한다 ㄷ
모르겠따


"""
import sys

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if (x == 0):
        if (heap):
            # delete

            # 가장 큰수 출력 + pop쓰려고 뒤로 뺌 + pop
            print(heap[0])
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()

            # 마지막수와 교체 -> 최대힙 X -> 바꿔주기
            # lower 2개와 비교해서 lower가 더 크면 교체 -> 둘다 크면 더 큰쪽과 교체
            # 큰지 작은지 비교하기전에 비교할게 있는지 먼저 검사할것
            # 0부터 시작할때 언제 끝내야 할까?
            # 트리 섹터의 마지막 i는 항상 2의 배수 -> len(heap) <= 2 ** (lower + 1) 이런식

            pass
        else:
            print(0)
    else:
        # insert

        heap.append(x)
        i = len(heap) - 1
        while (0 <= i):
            upper_i = (i - 1) // 2
            if (0 <= upper_i and heap[upper_i] < heap[i]):
                heap[i], heap[upper_i] = heap[upper_i], heap[i]
                i = upper_i
            else:
                break

        pass
