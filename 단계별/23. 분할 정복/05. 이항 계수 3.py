"""
이항계수 (N, K)
     N!
= ㅡㅡㅡㅡ
  K!(N-K)!

페르마의 소정리 -> 곱셉의 역원
n^p-1 = 1 (mod p)
n * n^p-2 = 1 (mod p)
역원 = n^p-2

????????
"""

import sys
sys.setrecursionlimit(10**7)

N, K = map(int, sys.stdin.readline().split())
mod = 1000000007

factorial = [1]

for i in range(1, N + 1):
    factorial.append(factorial[i - 1] * i % mod)

def Div_Con(x, num):
    if (num == 1):
        return x

    result = Div_Con(x, num // 2) % mod
    if (num % 2 != 0):
        return result * result * x % mod
    else:
        return result * result % mod

print(factorial[N] * Div_Con(factorial[K] * factorial[N - K], mod - 2) % mod)