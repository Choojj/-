import sys

N = int(sys.stdin.readline())

image = []
for _ in range(N):
    image.append(list(map(int, sys.stdin.readline().rstrip())))


def Div_Con(x, y, num):
    break_tirg = False
    for i in range(x, x + num):
        if (break_tirg):
            break

        for j in range(y, y + num):
            if (image[x][y] != image[i][j]):
                # x, x + num / y, y + num
                print("(", end = "")
                Div_Con(x, y, num // 2) # 0 4, 0 4
                Div_Con(x, y + num // 2, num // 2) # 0 4, 4 8
                Div_Con(x + num // 2, y, num // 2) # 4 8, 0 4
                Div_Con(x + num // 2, y + num // 2, num // 2) # 4 8, 4 8
                print(")", end = "")
                break_tirg = True
                break
    
    if (not break_tirg):
        # print("분할", x, x + num , y, y + num, num)
        # for k in range(x, x + num):
        #     for l in range(y, y + num):
        #         print(image[k][l], end = " ")
        #     print()
        print(image[x][y], end = "")

Div_Con(0, 0, N)