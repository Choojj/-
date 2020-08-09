"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

for num in B:
    if (A[0] <= num <= A[-1]):
        print(1)
    else:
        print(0)

????????

범위 비교가 아니였네 ㄷㄷ
정수 비교를 해야해서 이분 탐색을 해야하는 것이였음


"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

for num in B:
    first = 0
    last = len(A) - 1

    while (True):
        mid = (first + last) // 2

        if (first > last):
            print(0)
            break

        if (A[mid] > num):
            last = mid - 1
        elif (A[mid] < num):
            first = mid + 1
        else:
            print(1)
            break