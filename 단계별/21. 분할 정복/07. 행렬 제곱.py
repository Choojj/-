import sys

mod = 1000
N, B = map(int, sys.stdin.readline().split())

A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

# print(N, B, A)

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
                # print(j, k ,"=", j, i,"*",i, k)
                answer[j][k] += matrix1[j][i] * matrix2[i][k]

    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] %= mod
    return answer

for result in Div_Con(A, B):
    for res in result:
        print(res % 1000, end = " ")
    print()