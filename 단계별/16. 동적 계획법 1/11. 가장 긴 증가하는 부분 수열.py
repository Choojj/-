"""
10 20 10 30 20 50

첫번째수로 부분수열 길이 구하기
두번째수로 부분수열 길이 구하기
세번째수로 부분수열 길이 구하기
...
n번째수로 부분수열 길이 구하기
전에 구한 부분수열의 길이보다 길어야하므로 N - 현재번수 보다 길어야할
가장 긴 부분수열의 길이보다 남은 수열의 길이가 더 길어야 하므로 N - n > 가장 긴 부분수열의 길이 번쨰 까지 구할것

10 20 10 30 20 50
10 20 30 50 4  6 - 1 > 4
20 30 50 3  6 - 2 > 4(X)
????

10 20 10 30 20 50
dp[0] = 10
dp[1] = 10 20 = dp[0] 20
dp[2] = 10 20 = dp[1]
dp[3] = 10 20 30, 20 30, 10 30 = dp[2] 30
dp[4] = 10 20 30, 20 30, 10 30, 10 20 = dp[3]
dp[5] = 10 20 30 50, 20 30 50, 10 30 50 = dp[4] + 50

1 7 6 2 3 4 5
dp[0] = 1
dp[1] = 1 7 = dp[0] 7
dp[2] = 1 7, 1 6 = dp[1]
dp[3] = 1 7, 1 6, 1 2 = dp[1]
dp[4] = 1 7, 1 6, 1 2 3 = 1 2 3
dp[5] = 1 7, 1 6, 1 2 3 4 = dp[4]
dp[6] = 1 7, 1 6, 1 2 3 4 5 = dp[5]

3 2 5 4 5
dp[0] = 3
dp[1] = 3, 2
dp[2] = 3 5, 2 5
dp[3] = 3 5, 3 4, 2 5, 2 4
dp[4] = 3 5, 3 4 5, 2 5, 2 4 5

9
10 20 40 25 20 50 30 70 85
10 20 25 30 70 85
"""

# import sys

# N = int(sys.stdin.readline())

# num_list = list(map(int, sys.stdin.readline().split()))
# num_list.append(0)

# length_subseq = 1

# for i in range(N):
#     if (N - (i + 1) < length_subseq):
#         break
    
#     curr_num = num_list[i]
#     temp_length_subseq = 1
#     for j in range(i + 1, N):
#         print(i, j, curr_num, num_list[j])
#         if (curr_num < num_list[j]):
#             temp_length_subseq += 1
#             curr_num = num_list[j]

#     print(temp_length_subseq)
#     if (length_subseq < temp_length_subseq):
#         length_subseq = temp_length_subseq

# print(length_subseq)

import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

vector = [0]
vector_length = 0
for i in range(N):
    if (i == 0):
        vector.append(num_list[i])
        vector_length += 1
    else:
        if (vector[-1] < num_list[i]):
            vector.append(num_list[i])
            vector_length += 1
        elif (vector[-2] < num_list[i] < num_list[-1]):
            vector[vector_length] = num_list[i]

print(len(vector) - 1)