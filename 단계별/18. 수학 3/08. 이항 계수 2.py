"""
이항계수
(n)        n!
| | = ----------
(r)   r!(n - r)!
정수제한 ㄷㄷ
"""

import sys, math

N, K = map(int, sys.stdin.readline().split())

print((math.factorial(N) // (math.factorial(K) * math.factorial(N - K))) % 10007)