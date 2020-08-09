"""
a / b = 몫 + 나머지

a[1] = a[1] / M * M + a[1] % M
a[2] = a[2] / M * M + a[2] % M
a[3] = a[3] / M * M + a[3] % M
a[4] = a[4] / M * M + a[4] % M
나머지로 정리하면

a[1] % M = a[1] - a[1] / M * M
a[2] % M = a[2] - a[2] / M * M
a[3] % M = a[3] - a[3] / M * M
a[4] % M = a[4] - a[4] / M * M
나머지가 모두 같아야하므로

a[1] - a[1] / M * M = a[2] - a[2] / M * M = a[3] - a[3] / M * M = a[4] - a[4] / M * M

a[1] - a[1] / M * M - a[2] + a[2] / M * M = 0

a[1] - a[2] = M * (a[1] / M - a[2] / M)
a[2] - a[3] = M * (a[2] / M - a[3] / M)
a[3] - a[4] = M * (a[3] / M - a[4] / M)
-> 두수의 차는 M이라는 공통 약수를 갖는다

38 - 34 = M (38 / M - 34 / M) = 4
34 -  6 = M (34 / M -  6 / M) = 28 
M은 4, 28의 공통약수 -> 최대공약수의 약수

6
34 28
38 4 4

2 4

2
100
142 42 

2 3 6 7 14 21 42

8
8  
13  5 
23  10 5
43  20 10 5
63  20 20 10 5
83  20 20 20 10 5
93  10 10 10 10 10 5
103 10 10 10 10 10 10 5

5

2
2
5 3 -> 최소값까지 X

3

3
145
652
361 -> 정렬하기

145
361 216
652 291 75

3 5 15 25 75

3

4
38  
56  18
84  28 10
124 40 12 2
38  
56  18
84  28 2
124 40 4 2

2

4
123
159 36
456 297 261
753 297 0

123
159 36
456 297 9
753 297 297 9

3 9

4
156
248 92
378 130 38
642 264 134 96

156
248 4
378 2 2
642 6 2 2

2
차의 최대공약수의 약수
"""

# import sys

# N = int(sys.stdin.readline())

# num_list = []
# for i in range(N):
#     num_list.append(int(sys.stdin.readline()))

# for i in range(2, min(num_list) + 1):
#     remainder = num_list[0] % i

#     trig = True
#     for j in range(1, N):
#         if (trig == False):
#             break

#         if (num_list[j] % i == remainder):
#             trig == True
#         else:
#             trig = False

#     if (trig == True):
#         print(i)

import sys, math

N = int(sys.stdin.readline())

num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort(reverse = True)

num_diff_list = []
for i in range(N - 1):
    for j in range(N - 1 - i):
        if (i == 0):
            num_diff_list.append(num_list[j] - num_list[j + 1])
        else:
            num_diff_list[j] = (math.gcd(num_diff_list[j], num_diff_list[j + 1]))

result = []
for i in range(1, int(math.sqrt(num_diff_list[0])) + 1):
    if (num_diff_list[0] % i == 0):
        result.append(i)
for i in range(len(result) - 1, -1, -1):
    if (result[i] != num_diff_list[0] // result[i]):
        result.append(num_diff_list[0] // result[i])

for i in range(1, len(result)):
    print(result[i], end = " ")