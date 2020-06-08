import sys

for line in sys.stdin:
    a, b = map(int, line.split())

    print(a+b)

# 원래는 while문인데 EOF는 이게 더 깔끔해서 이거로