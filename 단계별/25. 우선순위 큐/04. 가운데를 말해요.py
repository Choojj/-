"""
import sys

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    heap.append(x)
    heap.sort()

    print(heap[(len(heap) - 1) // 2])

시간초과

Running Median Algorithm
[[max_heap][midian][min_heap]]
중앙값을 기준으로 힙을 두개로 나누어 최상위 노드가 중앙값이 되도록 함
1. 기준값보다 작으면 max_heap에 크면 min_heap에 입력
2. 입력 후 max_heap과 min_heap의 차이가 2이상 나면 부족한 쪽의 heap으로 전체 시프트
3. max_heap[0]이 전체의 중앙값 또는 중앙값중 작은 수
4. 1 ~ 3 반복

ex) 1 5 2 10 -99 7 5

      +01
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +01
      +01       +05
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +01
      +02       +05
   +01
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +02
      +02       +05
   +01       +10
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +02
      +02       +05
   +01   -99 +10
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +02
      +02       +05
   +01   -99 +10   +07
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +02
      +05       +05
   +02   -99 +10   +07
+01
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ mid = +05

굳이 리스트 한개로 안해도 되겠지?
차이가 있나?
"""

class Heap():
    def __init__(self, reverse = False):
        self.heap = []
        self.reverse = reverse
    
    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while (0 <= i):
            upper_i = (i - 1) // 2
            if (self.reverse):
                if (upper_i >= 0 and self.heap[upper_i] > self.heap[i]):
                    self.heap[i], self.heap[upper_i] = self.heap[upper_i], self.heap[i]
                    i = upper_i
                else:
                    break
            else:
                if (upper_i >= 0 and self.heap[upper_i] < self.heap[i]):
                    self.heap[i], self.heap[upper_i] = self.heap[upper_i], self.heap[i]
                    i = upper_i
                else:
                    break

    def delete(self):
        deleted_num = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()

        i = lower = count = 0
        while (len(self.heap) >= 2 ** (count + 1)):
            trig = False
            if (self.reverse):
                if (i * 2 + 1 <= len(self.heap) - 1 and self.heap[i] > self.heap[i * 2 + 1]):
                    lower = i * 2 + 1
                if (i * 2 + 2 <= len(self.heap) - 1 and self.heap[i] > self.heap[i * 2 + 2]):
                    lower = i * 2 + 2
                    trig = True
                
                if (trig and self.heap[i * 2 + 1] <= self.heap[i * 2 + 2]):
                    lower = i * 2 + 1
                elif (trig and self.heap[i * 2 + 1] > self.heap[i * 2 + 2]):
                    lower = i * 2 + 2
            else:
                if (i * 2 + 1 <= len(self.heap) - 1 and self.heap[i] < self.heap[i * 2 + 1]):
                    lower = i * 2 + 1
                if (i * 2 + 2 <= len(self.heap) - 1 and self.heap[i] < self.heap[i * 2 + 2]):
                    lower = i * 2 + 2
                    trig = True
                
                if (trig and self.heap[i * 2 + 1] >= self.heap[i * 2 + 2]):
                    lower = i * 2 + 1
                elif (trig and self.heap[i * 2 + 1] < self.heap[i * 2 + 2]):
                    lower = i * 2 + 2

            self.heap[i], self.heap[lower] = self.heap[lower], self.heap[i]

            i = lower
            count += 1

        return deleted_num

import sys

N = int(sys.stdin.readline())

max_heap = Heap()
max_heap.insert(int(sys.stdin.readline()))
print(max_heap.heap[0])
min_heap = Heap(reverse = True)
for _ in range(N - 1):
    mid = max_heap.heap[0]

    x = int(sys.stdin.readline())
    if (mid >= x):
        max_heap.insert(x)
        pass
    else:
        min_heap.insert(x)
        pass

    if (len(max_heap.heap) > len(min_heap.heap) + 1):
        min_heap.insert(max_heap.delete())
    
    if (len(max_heap.heap) < len(min_heap.heap)):
        max_heap.insert(min_heap.delete())

    print(max_heap.heap[0])