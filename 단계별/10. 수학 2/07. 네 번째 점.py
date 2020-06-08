import sys

point_list = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    point_list.append([x, y])

if (point_list[0][0] != point_list[1][0]):
    if (point_list[0][0] != point_list[2][0]):
        x_4 = point_list[0][0]
    else:
        x_4 = point_list[1][0]
else:
    x_4 = point_list[2][0]

if (point_list[0][1] != point_list[1][1]):
    if (point_list[0][1] != point_list[2][1]):
        y_4 = point_list[0][1]
    else:
        y_4 = point_list[1][1]
else:
    y_4 = point_list[2][1]

print(x_4, y_4)