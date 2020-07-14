"""
import sys

N, K = map(int, sys.stdin.readline().split())

A = []
for i in range(N):
    A.append(int(sys.stdin.readline()))
A.reverse()

count = 0
for i in range(N):
    if (K >= A[i]):
        while(K >= A[i]):
            K -= A[i]
            count += 1

print(count)
??? 시간초과 ㄷㄷ
"""

import sys

N, K = map(int, sys.stdin.readline().split())

A = []
for i in range(N):
    A.append(int(sys.stdin.readline()))
A.reverse()

count = 0
for i in range(N):
    if (K == 0):
        break

    if (K >= A[i]):
        count += K // A[i]
        K %= A[i]
        
print(count)