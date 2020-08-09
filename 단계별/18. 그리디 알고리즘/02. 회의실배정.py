import sys

N = int(sys.stdin.readline())

meeting_time = []
for i in range(N):
    meeting_time.append(list(map(int, sys.stdin.readline().split())))

meeting_time.sort(key = lambda x: [x[1], x[0]])

count = 1
end = meeting_time[0][1]
for i in range(1, N):
    if (meeting_time[i][0] >= end):
        count += 1
        end = meeting_time[i][1]

print(count)