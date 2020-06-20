"""
아니 정렬을 해줘야 되네 ㅡㅡ
"""
import sys

N = int(sys.stdin.readline())

measure_list = list(map(int, sys.stdin.readline().split()))
measure_list.sort()

if (N % 2 == 0):
    print(measure_list[int(N / 2) - 1] * measure_list[int(N / 2)])
else:
    print(measure_list[int(N / 2)] * measure_list[int(N / 2)])