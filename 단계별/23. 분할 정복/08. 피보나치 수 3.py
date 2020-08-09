"""
행렬 곱셈 응용???

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

0 1 3 5  21 34
1 2 8 13 55 89
X
0  1  1  34  55   89 2584
2  3  5 144 233  377
8 13 21 610 987 1597
X

F(1)
F(2)
F(3) = F(2) + F(1)
F(4) = F(3) + F(2)
F(5) = F(4) + F(3) = F(3) + F(2) + F(2) + F(1)
F(6) = F(5) + F(4) = F(4) + F(3) + F(3) + F(2)
F(7) = F(6) + F(5) = F(5) + F(4) + F(4) + F(3)
F(8) = F(7) + F(6) = F(6) + F(5) + F(5) + F(4)

F(n-1) = F(n-2) + F(n-3)
F(n) = F(n-1) + F(n-2)
F(n+1) = F(n) + F(n-1)

F(n) = F(n-1) + F(n-2)
F(n+1) = F(n) + F(n-1)

F(n+2) = F(n+1) + F(n)
F(n+1) = F(n+1) + 0

F(n+2) = (1 1) (F(n+1))
F(n+1) = (1 0) ( F(n) )

(F(n+1)  F(n) ) = (1 0)^n
( F(n)  F(n-1)) = (1 1)
"""

import sys

mod = 1000000
N = int(sys.stdin.readline())

A = [[1, 1], [1, 0]]

def Div_Con(x, num):
    if (num == 1):
        return x

    result = Div_Con(x, num // 2)
    if (num % 2 != 0):
        return matrix_multi(matrix_multi(result, result), x)
    else:
        return matrix_multi(result, result)

def matrix_multi(matrix1, matrix2):
    answer = [[0 for i in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(len(matrix1[0])):
        for j in range(len(matrix1)):
            for k in range(len(matrix2[0])):
                answer[j][k] += matrix1[j][i] * matrix2[i][k]

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] %= mod
    return answer

print(Div_Con(A, N)[0][1])