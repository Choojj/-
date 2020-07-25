import sys

N = int(sys.stdin.readline())

paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

plus = zero = minus = 0
def Div_Con(x, y, num):
    global plus, zero, minus

    break_tirg = False
    for i in range(x, x + num):
        if (break_tirg):
            break

        for j in range(y, y + num):
            if (paper[x][y] != paper[i][j]):
                # x, x + num / y, y + num
                Div_Con(x, y, num // 3) # 0 3, 0 3
                Div_Con(x, y + num // 3, num // 3) # 0 3, 3 6
                Div_Con(x, y + 2 * (num // 3), num // 3) # 0 3, 6 9
                Div_Con(x + num // 3, y, num // 3) # 3 6, 0 3
                Div_Con(x + num // 3, y + num // 3, num // 3) # 3 6, 3 6
                Div_Con(x + num // 3, y + 2 * (num // 3), num // 3) # 3 6, 6 9
                Div_Con(x + 2 * (num // 3), y, num // 3) # 6 9, 0 3
                Div_Con(x + 2 * (num // 3), y + num // 3, num // 3) # 6 9, 3 6
                Div_Con(x + 2 * (num // 3), y + 2 * (num // 3), num // 3) # 6 9, 6 9
                break_tirg = True
                break
    
    if (not break_tirg):
        # print("분할", x, x + num , y, y + num, num)
        # for k in range(x, x + num):
        #     for l in range(y, y + num):
        #         print(paper[k][l], end = " ")
        #     print()

        if (paper[x][y] > 0):
            plus += 1
        elif (paper[x][y] == 0):
            zero += 1
        else:
            minus += 1

Div_Con(0, 0, N)
print(minus)
print(zero)
print(plus)