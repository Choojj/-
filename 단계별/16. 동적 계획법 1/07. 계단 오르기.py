import sys

N = int(sys.stdin.readline())

stair_score = []
for i in range(N):
    stair_score.append(int(sys.stdin.readline()))

stair_sum = [[0, 0] for _ in range(N)]

for i in range(N):
    
print(stair_score)
print(stair_sum)