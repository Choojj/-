import sys

N = int(sys.stdin.readline())

the_triangle = []
for i in range(N):
    the_triangle.append([0] + list(map(int, sys.stdin.readline().split())) + [0])

triangle_sum = [[0] + [0] * (i + 1) + [0] for i in range(N)]

for i in range(N):
    for j in range(1, i + 2):
        if (i == 0):
            triangle_sum[i][j] = the_triangle[i][j]

        else:
            triangle_sum[i][j] = max(triangle_sum[i - 1][j - 1], triangle_sum[i - 1][j]) + the_triangle[i][j]

print(max(triangle_sum[-1]))