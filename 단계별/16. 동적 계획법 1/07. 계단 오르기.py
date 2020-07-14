import sys

N = int(sys.stdin.readline())

stair_score = []
for i in range(N):
    stair_score.append(int(sys.stdin.readline()))

stair_sum = [[0] for _ in range(N)]

for i in range(N):
    if (i == 0):
        stair_sum[i] = stair_score[0]
    elif (i == 1):
        stair_sum[i] = max(stair_score[0] + stair_score[1], stair_score[1])
    elif (i == 2):
        stair_sum[i] = max(stair_score[0] + stair_score[2], stair_score[1] + stair_score[2])

    else:
        stair_sum[i] = max(stair_sum[i - 3] + stair_score[i - 1] + stair_score[i], stair_sum[i - 2] + stair_score[i])

print(stair_sum[-1])