"""
10 11 12

제곱
    10 ^ 11 = 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 * 10 -> 10번

분할정복

    반으로가르기(홀수면 -1)
    10 ^ 11 = ((10 * 10) * (10 * 10) * 10) * ((10 * 10) * (10 * 10) * 10) * 10
    10 ^ 11 = 10^4 * 10 * 10^4 * 10 * 10 -> 2번 + 2번 + 4번 -> 8번

    2거듭제곱으로 가르기
    10 ^ 11 = 10^8 * 10^2 * 10 -> 3번 + 1번 + 2번 = 6번
    B 이진수변환


??????????????


import sys

A, B, C, = map(int, sys.stdin.readline().split())

def Div_Con(x, num):
    if (num == 1):
        return x

    if (num % 2 != 0):
        return Div_Con(x, (num - 1) // 2) * Div_Con(x, (num - 1) // 2) * x
    else:
        return Div_Con(x, num // 2) * Div_Con(x, num // 2)

print(Div_Con(A, B))

시간 초과
변수에 넣지않아서 재귀가 반복

숫자가 크면 계산시간도 오래걸려서 중간에 모듈러 해줘야함
"""

import sys

A, B, C, = map(int, sys.stdin.readline().split())

def Div_Con(x, num):
    if (num == 1):
        return x

    result = Div_Con(x, num // 2) % C
    if (num % 2 != 0):
        return result * result * x % C
    else:
        return result * result % C

print(Div_Con(A, B) % C)