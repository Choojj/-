import sys

def backtraking(N, depth):
    global count

    if (depth == N):
        count += 1
        return
    
    for i in range(N):
        if (not check_list[i]):
            answer_list[depth] = i
            if (possible(depth, i)):
                continue
            check_list[i] = True
            backtraking(N, depth + 1)
            check_list[i] = False

def possible(x, y):
    for i in range(x):
        if x - i == abs(y - answer_list[i]):
            return True
    return False

N = int(sys.stdin.readline())

check_list = [False] * N
answer_list = [0] * N

count = 0

backtraking(N, 0)

print(count)