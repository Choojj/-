# import sys

# N = int(sys.stdin.readline().rstrip())

# num_list = []

# for i in range(N):
#     num_list.append(int(sys.stdin.readline().rstrip()))

# max_num = -float("inf")

# for i in num_list:
#     if (max_num < i):
#         max_num = i

# num_counting_list = [0] * (max_num + 1)

# for i in num_list:
#     num_counting_list[i] += 1

# cumulative_sum = 0

# for i in range(len(num_counting_list)):
#     cumulative_sum += num_counting_list[i]
#     num_counting_list[i] = cumulative_sum

# sort_list = [0] * N

# for i in range(len(num_list)):
#     sort_list[num_counting_list[num_list[i]] - 1] = num_list[i]
#     num_counting_list[num_list[i]] -= 1

# num_counting_list만 사용해서 풀어야함

import sys

N = int(sys.stdin.readline())

num_counting_list = [0] * 10001

max_num = 0

for i in range(N):
    num = int(sys.stdin.readline())

    if (max_num < num):
        max_num = num

    num_counting_list[num] += 1

for i in range(max_num + 1):
    while(num_counting_list[i] != 0):
        sys.stdout.write(str(i)+"\n")
        num_counting_list[i] -= 1