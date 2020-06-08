import sys

def backtraking(N, M, depth):
    if (depth == M):
        for i in range(1, len(answer_list)):
            print(answer_list[i], end = " ")
        print()
        return
    
    for i in range(1, N + 1):
        # if ((not check_list[i])):
            answer_list[depth + 1] = i
            if (answer_list[depth] > answer_list[depth + 1]):
                continue
            # check_list[i] = True
            backtraking(N, M, depth + 1)
            # check_list[i] = False

N, M = map(int, sys.stdin.readline().split())

# check_list = [False] * (N + 1)
answer_list = [0] * (M + 1)

backtraking(N, M, 0)