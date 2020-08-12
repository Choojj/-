"""
3
7
A = [1, 2, 3
     2, 4, 6
     3, 6, 9]

B = [1, 2, 2, 3, 3, 4, 6, 6, 9]
100000 * 100000 + log100000 + 1000000000 ㄷㄷ

import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

a = []
for i in range(N):
    for j in range(N):
        a.append((i + 1) * (j + 1))

a.sort()
print(a[k])

시간초과 

 1  2  3  4
 2  4  6  8
 3  6  9 12
 4  8 12 16

 1 16 mid = 8  1  8 mid = 4  4  8 mid = 6  4  6 mid = 5 
 1time  = 4    1time  = 3    1time  = 4    1time  = 4   
 2times = 3    2times = 1    2times = 2    2times = 2   
 3times = 2    3times = 1    3times = 1    3times = 1   
 4times = 1    4times = 0    4times = 1    4times = 1   
 sum = 10      sum = 5      sum = 8      sum = 8     

import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

first = 1
last = N ** 2
while (True):
    if (first > last):
        break

    mid = (first + last) // 2
    count = 0
    for i in range(N):
        for j in range(N):
            if ((i + 1) * (j + 1) < mid):
                count += 1
    
    if (k <= count):
        last = mid - 1
    else:
        first = mid + 1
        answer = mid
    
    # print(mid, count)

print(answer)

N = 1000이되면 느려지기 시작 -> 이중 for문때문인듯
풀면 1000000 까지 ㄱㅊ


"""

import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

first = 1
last = N ** 2
while (True):
    if (first > last):
        break

    mid = (first + last) // 2
    count = 0
    for i in range(N):
        a = mid // (i + 1)
        if (mid % (i + 1) == 0 and (i + 1) * N >= mid):
            a -= 1
        # print(a, N)
        count += min(a, N)
        
    
    if (k <= count):
        last = mid - 1
    else:
        first = mid + 1
        answer = mid
    
    # print(mid, count, "------")

print(answer)