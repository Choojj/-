import sys

N = int(sys.stdin.readline().rstrip())

bag_5 = N // 5
bag_3 = 0

indivisible = False

for i in range(bag_5, -1, -1):
    if ((N - 5 * i) % 3 == 0):
        bag_5 = i
        bag_3 = (N - 5 * i) // 3
        indivisible = True
        break

if (indivisible == True):
    print(bag_5 + bag_3)
else:
    print(-1)