"""
0 0 = 0 0 * 0 0 + 0 1 * 1 0
0 1 = 0 0 * 0 1 + 0 1 * 1 1
0 2 = 0 0 * 0 2 + 0 1 * 1 2
1 0 = 1 0 * 0 0 + 1 1 * 1 0
1 1 = 1 0 * 0 1 + 1 1 * 1 1
1 2 = 1 0 * 0 2 + 1 1 * 1 2
2 0 = 2 0 * 0 0 + 2 1 * 1 0
2 1 = 2 0 * 0 1 + 2 1 * 1 1
2 2 = 2 0 * 0 2 + 2 1 * 1 2
"""
import sys

A = []
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

# print(A, len(A), len(A[0]))
# print(B, len(B), len(B[0]))

answer = [[0 for i in range(len(B[0]))] for i in range(len(A))]
for i in range(len(A[0])):
    for j in range(len(A)):
        for k in range(len(B[0])):
            # print(j, k ,"=", j, i,"*",i, k)
            answer[j][k] += A[j][i] * B[i][k]

for ans in answer:
    for a in ans:
        print(a, end = " ")
    print()