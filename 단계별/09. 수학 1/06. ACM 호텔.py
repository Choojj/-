import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    W, H, N = map(int, sys.stdin.readline().rstrip().split())

    room_num = 0

    if (N % W == 0):
        print(f"%d%02d" % (W, N // W))
    else:
        print(f"%d%02d" % (N % W, N // W + 1))