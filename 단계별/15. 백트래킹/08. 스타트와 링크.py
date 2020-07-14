import sys

def backtraking(depth):
    global min_value

    if (depth == N // 2):
        start_stat = link_stat = 0

        if (check_list[0]):
            for i in range(N):
                for j in range(N):
                    if (check_list[i] and check_list[j]):
                        start_stat += stat_table[i][j]
                        
                    if (not check_list[i] and not check_list[j]):
                        link_stat += stat_table[i][j]

            if (abs(start_stat - link_stat) < min_value):
                min_value = abs(start_stat - link_stat)

        else:
            print(min_value)
            sys.exit()

        return
    
    for i in range(N):
        if ((not check_list[i])):
            member_list[depth + 1] = i
            if (member_list[depth] > member_list[depth + 1]):
                continue
            check_list[i] = True
            backtraking(depth + 1)
            check_list[i] = False

N = int(sys.stdin.readline())

check_list = [False] * (N)
member_list = [0] * (N // 2 + 1)

stat_table = []
for i in range(N):
    stat_table.append(list(map(int, sys.stdin.readline().split())))

min_value = float("inf")

backtraking(0)