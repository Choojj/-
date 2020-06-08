import sys

N = int(sys.stdin.readline())

check_list = [0] * 3

all_cost = [0] * 3

for i in range(N):
    paint_cost = list(map(int, sys.stdin.readline().split()))

    if (i == 0):
        for j in range(3):
            all_cost[j] += paint_cost[j]
            check_list[j] = j

    else:
        for j in range(3):
            min_cost = float("inf")
            
            for k in range(3):
                if (check_list[j] == k):
                    continue

                if (min_cost > paint_cost[k]):
                    min_cost = paint_cost[k]
                    temp = k

            check_list[j] = temp
            all_cost[j] += min_cost

print(min(all_cost))