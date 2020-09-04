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
                if (i * 2 + 1 <= len(heap) - 1 and heap[i] > heap[i * 2 + 1]):
                    lower = i * 2 + 1
                if (i * 2 + 2 <= len(heap) - 1 and heap[i] > heap[i * 2 + 2]):
                    lower = i * 2 + 2
                    trig = True
                
                if (trig and heap[i * 2 + 1] <= heap[i * 2 + 2]):
                    lower = i * 2 + 1
                elif (trig and heap[i * 2 + 1] > heap[i * 2 + 2]):
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
            if (0 <= upper_i and heap[upper_i] > heap[i]):
                heap[i], heap[upper_i] = heap[upper_i], heap[i]
                i = upper_i
            else:
                break

        pass

    # print(heap, "----")