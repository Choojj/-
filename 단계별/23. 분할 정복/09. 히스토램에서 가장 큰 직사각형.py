"""
while True:
    N, *l=list(map(int, input().split()))
    l.append(0)
    if N == 0: break
    s=[]
    a=0
    for i,h in enumerate(l):
        while s and l[s[-1]]>h:
            ih=l[s.pop()]
            # s의 높이!
            w=i-s[-1]-1 if s else i
            # i에서부터 s의 top까지의 거리를 가로길이로 한다.
            # w = i일때는 마지막일 때
            if a<w*ih: a=w*ih
        s.append(i)
    print(a)
https://joosjuliet.github.io/6549/
찾다가 봤는데 신기해서 저장


분할정복이나 스택으로 풀기
높이 기준으로 왼쪽 기준으로

"""

import sys

while(True):
    N, *H = list(map(int, sys.stdin.readline().split()))
    # *(asterisk) 여기서는 알수없는 복수의 인자를 입력 받을때 사용

    print(N, H)

    if (N == 0):
        break

    while(True):
        pass