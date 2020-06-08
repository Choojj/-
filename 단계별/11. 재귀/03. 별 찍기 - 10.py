import sys
import math
"""
def get_star_list(star_list):
    matrix = []

    for i in range(3 * len(star_list)):
        if (i // len(star_list) == 1):
            matrix.append(star_list[i % len(star_list)] + " " * len(star_list) + star_list[i % len(star_list)])
        else:
            matrix.append(star_list[i % len(star_list)] * 3)

    return(matrix)


star_list = ["***", "* *", "***"]

N = int(sys.stdin.readline().rstrip())

k = int(round(math.log(N, 3)))

for i in range(k - 1):
    star_list = get_star_list(star_list)
for i in star_list:
    print(i)
"""

def get_star_list(star_list, order):
    if (order == 0):
        return star_list

    else:
        matrix = 1

        matrix += 1

        star_list = matrix

        get_star_list(star_list, order - 1)

    return(star_list)

star_list = 1

get_star_list(star_list, 3)

print(star_list)