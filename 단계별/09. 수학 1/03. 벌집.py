import sys

N = int(sys.stdin.readline().rstrip())

i = 0
room = 1

if (N == 1):
    print(1)

else:
    while (room < N):
        room += i * 6

        i += 1

    print(i)