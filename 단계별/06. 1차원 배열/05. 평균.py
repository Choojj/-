import sys

N = int(sys.stdin.readline())

score_list = list(map(int, sys.stdin.readline().split()))

max_score = max(score_list)
sum_score = 0

for i in range(N):
    max_score = max(score_list)

    sum_score += score_list[i] / max_score * 100

print(sum_score / N)