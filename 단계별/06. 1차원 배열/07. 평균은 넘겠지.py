import sys

average = count = 0

C = int(sys.stdin.readline())

for i in range(C):
    score_list = list(map(int, sys.stdin.readline().split()))

    for j in range(1, score_list[0] + 1):
        average += score_list[j]
    
    average /= score_list[0]

    for j in range(1, score_list[0] + 1):
        if (score_list[j] > average):
            count += 1
    
    print("%.3f%%" % (count / score_list[0] * 100))
    average = count = 0