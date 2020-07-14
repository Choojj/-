import sys

def backtraking(depth):
    global max_result, min_result

    if (depth == N - 1):
        result = A_list[0]

        for i in range(len(answer_list)):
            if (answer_list[i] == 0):
                result += A_list[i + 1]
            elif (answer_list[i] == 1):
                result -= A_list[i + 1]
            elif (answer_list[i] == 2):
                result *= A_list[i + 1]
            elif (answer_list[i] == 3):
                if (result < 0):
                    result = -(abs(result) // A_list[i + 1])
                else:
                    result //= A_list[i + 1]

        if (max_result < result):
            max_result = result
        if (min_result > result):
            min_result = result
    
    else:
        for i in range(len(operation_list)):
            if (operation_list[i]):
                operation_list[i] -= 1
                answer_list.append(i)
                backtraking(depth + 1)
                operation_list[i] += 1
                answer_list.pop()

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
operation_list = list(map(int, sys.stdin.readline().split()))

answer_list = []

max_result = -float("inf")
min_result = float("inf")

backtraking(0)

print(max_result)
print(min_result)