import sys
import collections

num_list = []

N = int(sys.stdin.readline())

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

print(round(sum(num_list) / N))

num_list.sort()
print(num_list[N // 2])

num_counting_list = collections.Counter(num_list).most_common(2)
if (N > 1):
    if (num_counting_list[0][1] == num_counting_list[1][1]):
        print(num_counting_list[1][0])
    else:
        print(num_counting_list[0][0])
else:
    print(num_list[0])

print(num_list[N - 1] - num_list[0])