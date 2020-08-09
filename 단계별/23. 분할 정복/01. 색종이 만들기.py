"""
중앙을 기준으로 4분면으로 쪼갬
쪼갠 분면이 한색으로 이루어져있거나 크기가 1이면 탈출
아니면 반복
"""

import sys

N = int(sys.stdin.readline())

colored_paper = []
for _ in range(N):
    colored_paper.append(list(map(int, sys.stdin.readline().split())))

white = blue = 0
def Div_Con(x, y, num):
    global white, blue

    break_tirg = False
    for i in range(x, x + num):
        if (break_tirg):
            break

        for j in range(y, y + num):
            if (colored_paper[x][y] != colored_paper[i][j]):
                # x, x + num / y, y + num
                Div_Con(x, y, num // 2) # 0 4, 0 4
                Div_Con(x + num // 2, y, num // 2) # 4 8, 0 4
                Div_Con(x, y + num // 2, num // 2) # 0 4, 4 8
                Div_Con(x + num // 2, y + num // 2, num // 2) # 4 8, 4 8
                break_tirg = True
                break
    
    if (not break_tirg):
        # print("분할", x, x + num , y, y + num, num)
        # for k in range(x, x + num):
        #     for l in range(y, y + num):
        #         print(colored_paper[k][l], end = " ")
        #     print()

        if (colored_paper[x][y] == 0):
            white += 1
        else:
            blue += 1

Div_Con(0, 0, N)
print(white)
print(blue)