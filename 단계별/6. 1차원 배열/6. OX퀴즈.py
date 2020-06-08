import sys

score = point = 0

N = int(sys.stdin.readline())

for i in range(N):
    case = sys.stdin.readline()
    for j in range(len(case)):
        if (case[j] == "O" and case[j - 1] == "O"):
            point += 1
        else:
            point = 1
        
        if (case[j] == "O"):
            score += point

    print(score)
    score = 0