import sys

N = int(sys.stdin.readline())

paint_cost = []

for i in range(N):
    paint_cost.append(list(map(int, sys.stdin.readline().split())))

# list1 = [[0] * 3 for _ in range(N)]
# list2 = [[0] * 3] * N
# list1[0][0] = 1
# list2[0][0] = 1
# print(list1)
# print(sys.getsizeof(list1))
# print(list2)
# print(sys.getsizeof(list2)) ???? 왜이렇게 되냐

all_cost = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    for j in range(3):
        if (i == 0):
            all_cost[i][j] = paint_cost[i][j]

        else:
            all_cost[i][j] = min(all_cost[i - 1][(j + 1) % 3], all_cost[i - 1][(j + 2) % 3]) + paint_cost[i][j]
        
print(min(all_cost[-1]))